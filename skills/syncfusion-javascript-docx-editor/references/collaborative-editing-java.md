# Collaborative Editing (Java)

> Core setup for real-time multi-user collaborative editing using SockJS, STOMP, and Redis in a Java (Spring Boot) backend.

---

## Enable Collaborative Editing

All initialization must run inside the component's **`created` event** — NOT during script load.

> **Note:** The collaborative editing examples referenced in this skill use ES5 script-based code. When generating ES6 module-based implementations, always import and inject the required modules before initializing collaborative editing.

```ts
import {
    DocumentEditorContainer,
    Toolbar,
    DocumentEditor,
    CollaborativeEditingHandler
} from '@syncfusion/ej2-documenteditor';
import { CollaborationClient } from '@syncfusion/ej2-collaborator';

DocumentEditorContainer.Inject(Toolbar);
DocumentEditor.Inject(CollaborativeEditingHandler);
```

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.syncfusion.com/ej2/dist/ej2.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/sockjs-client/1.5.0/sockjs.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/stomp.js/2.3.3/stomp.min.js"></script>
</head>
<body>
    <div id="container" style="height: 590px"></div>

    <script>
        let documentEditor;
        let container;

        // Create the DocumentEditorContainer
        function loadDocumentEditor() {
            container = new ej.documenteditor.DocumentEditorContainer({
                currentUser: 'user@syncfusion.com',
                serviceUrl: 'http://localhost:5212/api/wordeditor',
                enableToolbar: true,
                created: onCreated
            });

            // Enable collaborative editing inside created event
            function onCreated() {
                documentEditor = container.documentEditor;
                if (documentEditor) {
                    documentEditor.enableCollaborativeEditing = true;
                }
            }

            // Render the component
            container.appendTo('#container');
        }
    </script>
</body>
</html>
```

---

## Configure SockJS Client

Initialize SockJS + STOMP to broadcast and receive remote editing actions.

```javascript
const webSocketEndPoint = 'http://localhost:8024/ws';
let stompClient;
let currentRoomName = '';

// Initialize SockJS connection
function initializeSockJs() {
    const ws = new SockJS(webSocketEndPoint);
    stompClient = Stomp.over(ws);
    stompClient.connect({}, onConnected);
}

// Subscribe to the room topic
function onConnected() {
    if (stompClient.connected) {
        stompClient.subscribe(
            '/topic/public/' + currentRoomName,
            onDataReceived
        );
        connectToRoom(currentRoomName);
    }
}

// Apply received remote action to the editor
function onDataReceived(data) {
    const content = JSON.parse(data.body);
    const action = content.headers['action'];
    if (content.payload.operations != null) {
        documentEditor.collaborativeEditingHandlerModule.applyRemoteAction('action', content.payload);
    }
}
```

---

## Open Document and Join Room

Open the document, update room info, and join the SockJS room.

```javascript
function openDocument(responseText, roomName) {
    const data = JSON.parse(responseText);
    if (container) {
        // Update room and version info
        documentEditor.collaborativeEditingHandlerModule.updateRoomInfo(
            roomName,
            data.version,
            'http://localhost:5212/api/collaborativeediting/'
        );
        // Open the document
        documentEditor.open(data.sfdt);

        setTimeout(function () {
            connectToRoom({
                action: 'connect',
                roomName: roomName,
                currentUser: container.currentUser
            });
        });
    }
}

// Send user info to the server to join the room
function connectToRoom(data) {
    const userInfo = {
        currentUser: container.currentUser,
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
container.contentChange = function (args) {
    documentEditor.collaborativeEditingHandlerModule.sendActionToServer(args.operations);
};
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

### Client side (CDN)

```html
<script src="https://cdn.syncfusion.com/ej2/dist/ej2.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/sockjs-client/1.5.0/sockjs.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/stomp.js/2.3.3/stomp.min.js"></script>
```

---

## Run the Application

1. Start Redis server
2. Start the Spring Boot Java backend
3. Open the HTML file in multiple browser tabs/windows
4. Changes made in one tab sync to all tabs in real-time

---

## Reference Example

Full version of the code discussed above can be found in the following GitHub location:

[Collaborative editing examples](https://github.com/SyncfusionExamples/EJ2-Document-Editor-Collaborative-Editing)
