# Collaborative Editing (Java)

> Core setup for real-time multi-user collaborative editing using SockJS, STOMP, and Redis in a Java (Spring Boot) backend.

---

## Enable Collaborative Editing

All initialization that touches `documentEditor` must run inside the component's **`created` event** — NOT inside `mounted()`.

```vue
<template>
  <ejs-documenteditorcontainer
    ref="containerRef"
    id="container"
    :currentUser="currentUser"
    :serviceUrl="serviceUrl + 'api/wordeditor'"
    :enableToolbar="true"
    @created="onCreated"
  ></ejs-documenteditorcontainer>
</template>

<script>
import { ref } from 'vue';
import { DocumentEditorContainerComponent, Toolbar, DocumentEditor } from '@syncfusion/ej2-vue-documenteditor';
import { CollaborativeEditingHandler } from '@syncfusion/ej2-documenteditor';

export default {
  components: {
    'ejs-documenteditorcontainer': DocumentEditorContainerComponent
  },
  setup() {
    const containerRef = ref(null);
    const currentUser = 'user@syncfusion.com';
    const serviceUrl = 'http://localhost:5212/';

    const onCreated = () => {
      DocumentEditor.Inject(CollaborativeEditingHandler);
      if (containerRef.value?.documentEditor) {
        containerRef.value.documentEditor.enableCollaborativeEditing = true;
      }
    };

    return {
      containerRef,
      currentUser,
      serviceUrl,
      onCreated
    };
  }
};
</script>
```

**main.js (register plugin)**

```javascript
import { DocumentEditorContainerPlugin } from '@syncfusion/ej2-vue-documenteditor';

app.use(DocumentEditorContainerPlugin);
```

---

## Configure SockJS Client

Initialize SockJS + STOMP to broadcast and receive remote editing actions.

```javascript
import * as SockJS from 'sockjs-client';
import { Stomp, CompatClient } from '@stomp/stompjs';

const webSocketEndPoint = 'http://localhost:8024/ws';
const stompClient = Stomp.over(new SockJS(webSocketEndPoint));
const currentRoomName = '';

// Initialize SockJS connection
const initializeSockJs = () => {
  stompClient.connect({}, () => {
    onConnected();
  });
}

// Subscribe to the room topic
const onConnected = () => {
  if (stompClient.connected) {
    stompClient.subscribe(
      '/topic/public/' + currentRoomName,
      onDataReceived
    );
    connectToRoom(currentRoomName);
  }
}

// Apply received remote action to the editor
const onDataReceived = (data) => {
  const content = JSON.parse(data.body);
  const action = content.headers['action'];
  if (content.payload.operations != null) {
    containerRef.value.documentEditor.collaborativeEditingHandlerModule
      .applyRemoteAction('action', content.payload);
  }
}
```

---

## Open Document and Join Room

Open the document, update room info, and join the SockJS room.

```javascript
const openDocument = (responseText, roomName) => {
  const data = JSON.parse(responseText);
  const container = containerRef.value;
  if (container) {
    // Update room and version info
    container.documentEditor.collaborativeEditingHandlerModule.updateRoomInfo(
      roomName,
      data.version,
      serviceUrl + 'api/collaborativeediting/'
    );
    // Open the document
    container.documentEditor.open(data.sfdt);

    setTimeout(() => {
      connectToRoom({
        action: 'connect',
        roomName: roomName,
        currentUser: container.currentUser
      });
    });
  }
}

// Send user info to the server to join the room
const connectToRoom = (data) => {
  const userInfo = {
    currentUser: currentUser,
    clientVersion: 0,
    roomName: currentRoomName,
    connectionId: ''
  };
  stompClient.send(
    '/app/join/' + currentRoomName,
    {},
    JSON.stringify(userInfo)
  );
}
```

---

## Broadcast Local Edits to Server

Send local editing operations to the server using the `contentChange` event.

```javascript
containerRef.value.contentChange = (args) => {
  containerRef.value.documentEditor.collaborativeEditingHandlerModule
    .sendActionToServer(args.operations);
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
    String channel = "collaborativeediting";
    new Thread(() -> {
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        poolConfig.setMaxTotal(100);
        poolConfig.setMaxIdle(20);
        poolConfig.setMinIdle(10);
        poolConfig.setTestWhileIdle(true);
        jedisPool = new JedisPool(poolConfig, REDIS_HOST, REDIS_PORT, 50000, REDIS_PASSWORD, REDISSSL);
        try (Jedis jedis = jedisPool.getResource()) {
            jedis.subscribe(new JedisPubSub() {
                @Override
                public void onMessage(String channel, String message) {
                    // Broadcast to all users connected to the room via SockJS
                    DocumentEditorHub.broadcastToRoom(action.getRoomName(), action, updateActionHeaders);
                }

                @Override
                public void onSubscribe(String channel, int subscribedChannels) {
                    System.out.println("Subscribed to channel: " + channel);
                }
            }, channel);
        } catch (JedisConnectionException e) {
            System.out.println("Connection failed. Retrying ...");
        }
    }).start();
}
```

---

## Install Required Packages

### Client side (npm)

```bash
npm install @syncfusion/ej2-vue-documenteditor
npm install sockjs-client
npm install @stomp/stompjs
```

---

## Run the Application

1. Start Redis server
2. Start the Spring Boot Java backend
3. Run the Vue client: `npm run dev`
4. Open the app in multiple browser tabs/windows
5. Changes made in one tab sync to all tabs in real-time

---

## Reference Example

Full version of the code discussed above can be found in the following GitHub location:

[Collaborative editing examples](https://github.com/SyncfusionExamples/EJ2-Document-Editor-Collaborative-Editing)
