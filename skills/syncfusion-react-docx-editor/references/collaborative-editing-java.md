# Collaborative Editing (Java)

> Core setup for real-time multi-user collaborative editing using SockJS, STOMP, and Redis in a Java (Spring Boot) backend.

---

## Enable Collaborative Editing

```tsx
import { DocumentEditorContainerComponent, Toolbar, CollaborativeEditingHandler, Inject } from '@syncfusion/ej2-react-documenteditor';

DocumentEditorComponent.Inject(CollaborativeEditingHandler);

componentDidMount(): void {
  if (this.container) {
    this.container.documentEditor.enableCollaborativeEditing = true;
  }
}

render() {
  return (
    <DocumentEditorContainerComponent
      id="container"
      ref={(scope) => { this.container = scope; }}
      currentUser={this.currentUser}
      serviceUrl={this.serviceUrl + 'api/wordeditor'}
      enableToolbar={true}
    >
      <Inject services={[Toolbar]} />
    </DocumentEditorContainerComponent>
  );
}
```

---

## Configure SockJS Client

Initialize SockJS + STOMP to broadcast and receive remote editing actions.

```tsx
import * as SockJS from 'sockjs-client';
import { Stomp, CompatClient } from '@stomp/stompjs';

webSocketEndPoint: string = 'http://localhost:8024/ws';
public stompClient!: CompatClient;
public currentRoomName: string = '';

// Initialize SockJS connection
public initializeSockJs = (): void => {
  const ws = new SockJS(this.webSocketEndPoint);
  this.stompClient = Stomp.over(ws);
  this.stompClient.connect({}, () => {
    this.onConnected();
  });
}

// Subscribe to the room topic
public onConnected(): void {
  if (this.stompClient.connected) {
    this.stompClient.subscribe(
      '/topic/public/' + this.currentRoomName,
      this.onDataReceived.bind(this)
    );
    this.connectToRoom(this.currentRoomName);
  }
}

// Apply received remote action to the editor
public onDataReceived(data: any): void {
  const content = JSON.parse(data.body);
  const action = content.headers['action'];
  if (content.payload.operations != null) {
    this.container.documentEditor.collaborativeEditingHandlerModule.applyRemoteAction('action', content.payload);
  }
}
```

---

## Open Document and Join Room

Open the document, update room info, and join the SockJS room.

```tsx
public openDocument(responseText: string, roomName: string): void {
  const data = JSON.parse(responseText);
  if (this.container) {
    // Update room and version info
    this.container.documentEditor.collaborativeEditingHandlerModule.updateRoomInfo(
      roomName,
      data.version,
      this.serviceUrl + 'api/collaborativeediting/'
    );
    // Open the document
    this.container.documentEditor.open(data.sfdt);

    setTimeout(() => {
      this.connectToRoom({
        action: 'connect',
        roomName: roomName,
        currentUser: this.container.currentUser
      });
    });
  }
}

// Send user info to the server to join the room
public connectToRoom(data: any): void {
  const userInfo = {
    currentUser: this.currentUser,
    clientVersion: 0,
    roomName: this.currentRoomName,
    connectionId: ''
  };
  this.stompClient.send(
    '/app/join/' + this.currentRoomName,
    {},
    JSON.stringify(userInfo)
  );
}
```

---

## Broadcast Local Edits to Server

Send local editing operations to the server using the `contentChange` event.

```tsx
this.container.contentChange = (args: ContainerContentChangeEventArgs) => {
  if (this.collaborativeEditingHandler) {
    this.collaborativeEditingHandler.sendActionToServer(args.operations as Operation[]);
  }
}
```

---

## Configure Redis Connection (application.properties)

```properties
spring.datasource.redishost=<Redis host string>
spring.datasource.redisport=<Redis port>
spring.datasource.redispassword=<Redis password>
spring.datasource.redisssl=<boolean>
```

**Placeholders**
- `<Redis host string>` → Replace with `{redisHost}`
- `<Redis port>` → Replace with `{redisPort}`
- `<Redis password>` → Replace with `{redisPassword}`
- `<boolean>` → Replace with `true` or `false`

---

## Create SockJS Hub (Java)

Manage groups per document using SockJS room names via the `@MessageMapping` approach.

```java
@MessageMapping("/join/{documentName}")
public void joinGroup(ActionInfo info, SimpMessageHeaderAccessor headerAccessor,
        @DestinationVariable String documentName) throws JsonProcessingException {
    // Get the connection ID
    String connectionId = headerAccessor.getSessionId();
    info.setConnectionId(connectionId);
    String docName = info.getRoomName();

    HashMap<String, Object> additionalHeaders = new HashMap<>();
    additionalHeaders.put("action", "connectionId");
    MessageHeaders headers = new MessageHeaders(additionalHeaders);

    // Send the connection ID to the client
    broadcastToRoom(docName, info, headers);
}

public static void broadcastToRoom(String roomName, Object payload, MessageHeaders headers) {
    messagingTemplate.convertAndSend(
        "/topic/public/" + roomName,
        MessageBuilder.createMessage(payload, headers)
    );
}
```

---

## Handle User Disconnection

```java
@EventListener
public void handleWebSocketDisconnectListener(SessionDisconnectEvent event) throws Exception {
    String sessionId = event.getSessionId();
    try (Jedis jedis = RedisSubscriber.getJedis()) {
        // Get the document the user was editing
        String docName = jedis.hget("documentMap", sessionId);
        // Publish a message indicating the user's departure
        jedis.publish(docName, "LEAVE|" + sessionId);
    } catch (JedisConnectionException e) {
        System.out.println(e);
    }
}
```

---

## Import File (Java)

Load the source document, apply pending Redis operations, and return SFDT.

```java
@PostMapping("/api/collaborativeediting/ImportFile")
public String importFile(@RequestBody FilesPathInfo file) throws Exception {
    try {
        // Get the source document
        WordProcessorHelper document = getDocumentFromBucketS3(
            file.getFileName(),
            datasourceAccessKey,
            datasourceSecretKey,
            datasourceBucketName
        );

        // Get the list of pending operations
        List<ActionInfo> actions = getPendingOperations(file.getFileName(), 0, -1);
        if (actions != null && actions.size() > 0) {
            document.updateActions(actions);
        }

        // Serialize to SFDT and return
        return WordProcessorHelper.serialize(document);
    } catch (Exception e) {
        e.printStackTrace();
        return "{\"sections\":[{\"blocks\":[{\"inlines\":[{\"text\":" + e.getMessage() + "}]}]}]}";
    }
}
```

---

## Update Action (Java)

Add the operation to Redis, transform, and broadcast to all room users.

```java
@PostMapping("/api/collaborativeediting/UpdateAction")
public ActionInfo updateAction(@RequestBody ActionInfo param) throws Exception {
    String roomName = param.getRoomName();
    ActionInfo transformedAction = addOperationsToCache(param);

    HashMap<String, Object> action = new HashMap<>();
    action.put("action", "updateAction");

    // Publish to Redis (scaling) and broadcast to room (SockJS)
    DocumentEditorHub.publishToRedis(roomName, transformedAction);
    DocumentEditorHub.broadcastToRoom(
        roomName,
        transformedAction,
        new MessageHeaders(action)
    );

    return transformedAction;
}

private ActionInfo addOperationsToCache(ActionInfo action) throws Exception {
		int clientVersion = action.getVersion();
		// Serialize the action
		String serializedAction = gson.toJson(action);
		String roomName = action.getRoomName();

		// Define the keys for Redis operations based on the action's room name
		String[] keys = { roomName + CollaborativeEditingHelper.versionInfoSuffix, roomName,
				roomName + CollaborativeEditingHelper.revisionInfoSuffix,
				roomName + CollaborativeEditingHelper.actionsToRemoveSuffix };
		// Prepare values for the Redis script
		String[] values = { serializedAction, String.valueOf(clientVersion),
				String.valueOf(CollaborativeEditingHelper.saveThreshold) };

		try (Jedis jedis = RedisSubscriber.getJedis()) {
			try {
				// Execute the Lua script in Redis and store the results
				Object response = jedis.eval(CollaborativeEditingHelper.insertScript, keys.length, keys[0], keys[1],
						keys[2], keys[3], values[0], values[1], values[2]);
				List<Object> results = (List<Object>) response;
				// Parse the version number from the script results
				int version = Integer.parseInt(results.get(0).toString());
				// Deserialize the list of previous operations from the script results
				ArrayList<ActionInfo> previousOperations = new ArrayList();
				Object data = results.get(1);
				if (data instanceof List) {
					for (Object result : (List<?>) data) {
						if (result instanceof String) {
							previousOperations.add(gson.fromJson((String) result, ActionInfo.class));
						}
					}
				}
				// Increment the version for each previous operation
				previousOperations.forEach(op -> op.setVersion(op.getVersion() + 1));
				// Check if there are multiple previous operations to determine if
				// transformation is needed
				if (previousOperations.size() > 1) {
					// Set the current action to the last operation in the list
					action = previousOperations.get(previousOperations.size() - 1);
					for (ActionInfo op : previousOperations) {
						// Transform operations that have not been transformed yet
						List<DocumentOperation> operation = op.getOperations();
						if (operation != null && !op.isTransformed()) {
							CollaborativeEditingHandler.transformOperation(op, previousOperations);
						}
					}
				}
				// Update the action's version and mark it as transformed
				action.setVersion(version);
				action.setTransformed(true);
				// Update the record in the cache with the new version
				updateRecordToCache(version, action, jedis);
				// Check if there are cleared operations to be saved
				if (results.size() > 2 && results.get(2) != null) {
					autoSaveChangesToSourceDocument((List<Object>) results.get(2), action);
				}

			} catch (Exception e) {
				e.printStackTrace();
			}
		} catch (JedisException e) {
			e.printStackTrace();
		}
		// Return the updated action
		return action;
	}
```

---

## Get Actions From Server (Java)

Retrieve actions newer than the client's last synced version as a backup for missed messages.

```java
@PostMapping("/api/collaborativeediting/GetActionsFromServer")
public String getActionsFromServer(@RequestBody ActionInfo param) throws ClassNotFoundException {
    try (Jedis jedis = RedisSubscriber.getJedis()) {
        String roomName = param.getRoomName();
        int lastSyncedVersion = param.getVersion();
        int clientVersion = param.getVersion();

        // Fetch actions pending after lastSyncedVersion
        List<ActionInfo> actions = GetEffectivePendingVersion(roomName, lastSyncedVersion, jedis);
        List<ActionInfo> currentAction = new ArrayList<>();

        for (ActionInfo action : actions) {
            action.setVersion(++clientVersion);

            if (action.getVersion() > lastSyncedVersion) {
                if (!action.isTransformed()) {
                    CollaborativeEditingHandler.transformOperation(action, new ArrayList<>(actions));
                }
                currentAction.add(action);
            }
        }

        return gson.toJson(currentAction);
    } catch (Exception ex) {
        ex.printStackTrace();
        return "{}";
    }
}
```

---

## Configure Redis Pub/Sub for Scaling

Publish each editing operation to Redis and subscribe via `onMessage` to broadcast across server instances.

### Publish to Redis channel

```java
try (Jedis jedis = RedisSubscriber.jedisPool.getResource()) {
    jedis.publish("collaborativeediting",
        new com.fasterxml.jackson.databind.ObjectMapper().writeValueAsString(payload));
    break;
} catch (JedisConnectionException e) {
}
```

### Subscribe to Redis channel

```java
@PostConstruct
public void subscribeToInstanceChannel() {
		String channel = "collaborativedtiting";
		new Thread(() -> {
			JedisPoolConfig poolConfig = new JedisPoolConfig();
			poolConfig.setMaxTotal(100);
			poolConfig.setMaxIdle(20);
			poolConfig.setMinIdle(10);
			poolConfig.setTestWhileIdle(true);
			jedisPool = new JedisPool(poolConfig, REDIS_HOST, REDIS_PORT,50000,REDIS_PASSWORD,REDISSSL);
			try (Jedis jedis = RedisSubscriber.getJedis()) {				
				jedis.subscribe(new JedisPubSub() {
					@Override
					public void onMessage(String channel, String message) {						
						System.out.println("Received message from channel " + channel + ": " + message);
						ObjectMapper objectMapper = new ObjectMapper();
						try {
							ActionInfo action = objectMapper.readValue(message, ActionInfo.class);
							HashMap<String, Object> updateAction = new HashMap<>();
							updateAction.put("action", "updateAction");
							MessageHeaders updateActionheaders = new MessageHeaders(updateAction);
							DocumentEditorHub.broadcastToRoom(action.getRoomName(), action, updateActionheaders);
						} catch (JsonProcessingException e) {
							e.printStackTrace();
						}
					}
					@Override
					public void onSubscribe(String channel, int subscribedChannels) {
						System.out.println("Subscribed to channel: " + channel);
					}
					
				}, channel);
				
			} catch (JedisConnectionException e) {
				// Handle the connection exception
				System.out.println("Connection failed. Retrying .....");
				e.printStackTrace();
			}
			 finally {
		            if (jedisPool != null) {
		                jedisPool.close(); // Ensure pool is closed when done
		            }
		        }
		}).start();
	}
```

---

## Install Required Packages

### Client side (npm)

```bash
npm install @syncfusion/ej2-react-documenteditor
npm install sockjs-client
npm install @stomp/stompjs
```

---

## Run the Application

1. Start Redis server
2. Start the Spring Boot Java backend
3. Run the React client: `npm start`
4. Open the app in multiple browser tabs/windows
5. Changes made in one tab sync to all tabs in real-time

---

## Reference Example

Full version of the code discussed above can be found in the following GitHub location:

[Collaborative editing examples](https://github.com/SyncfusionExamples/EJ2-Document-Editor-Collaborative-Editing)
