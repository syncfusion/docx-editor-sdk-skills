# Collaborative Editing

> Core setup for real-time multi-user collaborative editing using Collaboration Client and Server.

---

## Enable Collaborative Editing

Enable collaborative editing in the DOCX Editor component. All initialization must run inside the component's **`created` event** — NOT during script load. The `created` event fires only after the `DocumentEditorContainer` has fully initialized, so `documentEditor` is guaranteed to be defined.

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.syncfusion.com/ej2/dist/ej2.min.js"></script>
</head>
<body>
    <div id="container" style="height: 590px"></div>

    <script>
        let documentEditor;

        // Create the DocumentEditorContainer
        let container = new ej.documenteditor.DocumentEditorContainer({
            currentUser: 'User Name',
            serviceUrl: 'http://localhost:5212/api/documenteditor',
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
    </script>
</body>
</html>
```

---

## Create Document Editor Adapter

Implement `ICollaborationProvider` to bridge the DOCX Editor and Collaboration Client.

```javascript
class DocumentEditorAdapter {
    constructor(container, serviceUrl) {
        this.container = container;
        this.serviceUrl = serviceUrl;
    }

    // The only ICollaborationProvider method — applied for every remote action.
    applyRemoteAction(action, data) {
        if (this.container.documentEditor.collaborativeEditingHandlerModule) {
            this.container.documentEditor.collaborativeEditingHandlerModule.applyRemoteAction(
                action,
                data.payload
            );
        }
    }

    // Fetch the document from the product's REST API and return the room name.
    async loadFromServer(fileName) {
        const roomName = this.getRoomName(fileName);
        const response = await fetch(
            this.serviceUrl + 'api/CollaborativeEditing/ImportFile',
            {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ fileName, roomName })
            }
        );

        if (!response.ok) {
            throw new Error('Failed to load document');
        }

        const responseText = await response.text();
        await this.open(responseText, roomName);
        return roomName;
    }

    // Seed the editor and bridge local edits to the editor's sender.
    async open(responseText, roomName) {
        const data = JSON.parse(responseText);
        if (this.container.documentEditor.collaborativeEditingHandlerModule) {
            this.container.documentEditor.collaborativeEditingHandlerModule.updateRoomInfo(
                roomName,
                data.version,
                this.serviceUrl + 'api/CollaborativeEditing/'
            );
        }
        this.container.documentEditor.open(data.sfdt);

        // Bridge local edits to server
        this.container.contentChange = (args) => {
            if (this.container.documentEditor.collaborativeEditingHandlerModule) {
                this.container.documentEditor.collaborativeEditingHandlerModule.sendActionToServer(
                    args.operations
                );
            }
        };
    }

    // Generate unique room name
    getRoomName(fileName) {
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        let roomId = urlParams.get('id');

        if (!roomId) {
            roomId = Math.random().toString(32).slice(2);
            window.history.replaceState({}, '', '?id=' + roomId);
        }

        return roomId;
    }
}
```

---

## Wire Collaboration Client with SignalR

Initialize Collaboration Client with SignalR transport and join the room.

```javascript
// This code runs inside the DocumentEditorContainer's `created` event handler
const serviceUrl = 'http://localhost:5212/';
const adapter = new DocumentEditorAdapter(container, serviceUrl);

// Create and configure client with SignalR
const client = new ej.collaborator.CollaborationClient(adapter, {
    serviceUrl: 'http://localhost:5212/',
    connectionType: 'signalr',
    currentUser: 'John',
    onUserJoined: (user) => {
        console.log(`${user.name} joined`);
    },
    onUserLeft: (user) => {
        console.log(`${user.name} left`);
    }
});

// Load document and join room
(async () => {
    const roomName = await adapter.loadFromServer('document.docx');
    await client.joinRoomAsync(roomName);
})();
```

---

## Wire Collaboration Client with WebSocket

Use WebSocket transport instead of SignalR.

```javascript
const client = new ej.collaborator.CollaborationClient(adapter, {
    serviceUrl: 'ws://localhost:5212/',
    connectionType: 'websocket',
    currentUser: 'John'
});

const roomName = await adapter.loadFromServer('document.docx');
await client.joinRoomAsync(roomName);
```

---

## Complete JavaScript Setup

Full example integrating collaborative editing with SignalR.

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.syncfusion.com/ej2/dist/ej2.min.js"></script>
    <script src="https://cdn.syncfusion.com/ej2/dist/ej2-collaborator.min.js"></script>
</head>
<body>
    <div id="container" style="height: 590px"></div>

    <script>
        class DocumentEditorAdapter {
            constructor(container, serviceUrl) {
                this.container = container;
                this.serviceUrl = serviceUrl;
            }

            applyRemoteAction(action, data) {
                if (this.container.documentEditor.collaborativeEditingHandlerModule) {
                    this.container.documentEditor.collaborativeEditingHandlerModule.applyRemoteAction(
                        action,
                        data.payload
                    );
                }
            }

            async loadFromServer(fileName) {
                const roomName = this.getRoomName(fileName);
                const response = await fetch(
                    this.serviceUrl + 'api/CollaborativeEditing/ImportFile',
                    {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ fileName, roomName })
                    }
                );

                if (!response.ok) {
                    throw new Error('Failed to load document');
                }

                const responseText = await response.text();
                await this.open(responseText, roomName);
                return roomName;
            }

            async open(responseText, roomName) {
                const data = JSON.parse(responseText);
                if (this.container.documentEditor.collaborativeEditingHandlerModule) {
                    this.container.documentEditor.collaborativeEditingHandlerModule.updateRoomInfo(
                        roomName,
                        data.version,
                        this.serviceUrl + 'api/CollaborativeEditing/'
                    );
                }
                this.container.documentEditor.open(data.sfdt);

                this.container.contentChange = (args) => {
                    if (this.container.documentEditor.collaborativeEditingHandlerModule) {
                        this.container.documentEditor.collaborativeEditingHandlerModule.sendActionToServer(
                            args.operations
                        );
                    }
                };
            }

            getRoomName(fileName) {
                const queryString = window.location.search;
                const urlParams = new URLSearchParams(queryString);
                let roomId = urlParams.get('id');

                if (!roomId) {
                    roomId = Math.random().toString(32).slice(2);
                    window.history.replaceState({}, '', '?id=' + roomId);
                }

                return roomId;
            }
        }

        // Create DocumentEditorContainer
        let container = new ej.documenteditor.DocumentEditorContainer({
            currentUser: 'John',
            serviceUrl: 'http://localhost:5212/api/documenteditor',
            created: initializeCollaboration
        });

        async function initializeCollaboration() {
            const serviceUrl = 'http://localhost:5212/';
            const adapter = new DocumentEditorAdapter(container, serviceUrl);

            // Create Collaboration Client with SignalR
            const client = new ej.collaborator.CollaborationClient(adapter, {
                serviceUrl: 'http://localhost:5212/',
                connectionType: 'signalr',
                currentUser: 'John',
                onUserJoined: (user) => {
                    console.log(`${user.name} joined`);
                },
                onUserLeft: (user) => {
                    console.log(`${user.name} left`);
                }
            });

            // Load document and join room
            const roomName = await adapter.loadFromServer('document.docx');
            await client.joinRoomAsync(roomName);
        }

        // Render component
        container.appendTo('#container');
    </script>
</body>
</html>
```

---

## Configure Collaboration Server (ASP.NET Core)

Register and configure the server-side collaboration framework.

```csharp
using Syncfusion.Collaboration.Core.Extensions;

var builder = WebApplication.CreateBuilder(args);

// Configure Redis connection for distributed cache
builder.Services.AddCollaborationServer(options =>
{
    options.ConnectionString = 
        builder.Configuration.GetConnectionString("Redis") ?? "localhost:6379";
    // options.SaveThreshold = 100; // default
});

// Register the control-specific adapter
builder.Services.AddSingleton<ICollaborationAdapter, DocumentEditorCollaborationAdapter>();

builder.Services.AddControllers();

var app = builder.Build();

app.UseStaticFiles();
app.UseRouting();
app.MapControllers();

// Map collaboration hub
app.MapCollaborationServer(); // maps /collaborationhub

app.Run();
```

**Settings**
- `ConnectionString` — Redis connection (localhost:6379)
- `SaveThreshold` — Operations before auto-save (default: 100)
- `ConnectionType` — SignalR or WebSocket

---

## Configure WebSocket Transport (ASP.NET Core)

Use WebSocket instead of SignalR for communication.

```csharp
builder.Services.AddCollaborationServer(options =>
{
    options.ConnectionString = builder.Configuration.GetConnectionString("Redis");
    options.ConnectionType = CollaborationConnectionType.WebSocket;
});

var app = builder.Build();

app.UseWebSockets(); // Enable WebSocket support
app.MapCollaborationServer();

app.Run();
```

---

## Configure Redis Connection

Add your Redis connection string in `appsettings.json`. Replace the placeholder with your actual Redis connection string (e.g. `localhost:6379` for local development, or your production Redis host:port with auth).

```json
{
  "ConnectionStrings": {
    "Redis": "<Your redis connection string>"
  }
}
```

**Note**
- Minimum 400 KB cache per document
- Redis stores up to 2× SaveThreshold operations

---

## Create Document Editor Collaboration Adapter (Server)

Implement `ICollaborationAdapter` to translate Document Editor actions.

```csharp
using Syncfusion.Collaboration.Core.Interfaces;
using Syncfusion.Collaboration.Core.Models;
using Syncfusion.EJ2.DocumentEditor;
using Newtonsoft.Json;

public class DocumentEditorCollaborationAdapter : ICollaborationAdapter
{
    private readonly IBackgroundTaskQueue saveTaskQueue;
    private readonly IWebHostEnvironment _hostingEnvironment;
    static string fileLocation;

    public DocumentEditorCollaborationAdapter(
        IWebHostEnvironment hostingEnvironment,
        IBackgroundTaskQueue saveTaskQueue)
    {
        _hostingEnvironment = hostingEnvironment;
        fileLocation = _hostingEnvironment.WebRootPath;
        this.saveTaskQueue = saveTaskQueue;
    }

    // Convert Document Editor action to collaboration action
    public CollaborationAction MapControlToGenericAction(object controlAction)
    {
        var action = (Syncfusion.EJ2.DocumentEditor.ActionInfo)controlAction;
        return new CollaborationAction
        {
            RoomName = action.RoomName,
            ConnectionId = action.ConnectionId,
            CurrentUser = action.CurrentUser,
            Version = action.Version,
            ClientVersion = action.ClientVersion,
            IsTransformed = action.IsTransformed,
            Data = JsonConvert.SerializeObject(action.Operations)
        };
    }

    // Convert collaboration action back to Document Editor action
    public object MapGenericToControlAction(CollaborationAction action)
    {
        return new Syncfusion.EJ2.DocumentEditor.ActionInfo
        {
            RoomName = action.RoomName,
            ConnectionId = action.ConnectionId,
            CurrentUser = action.CurrentUser,
            Version = action.Version,
            ClientVersion = action.ClientVersion,
            IsTransformed = action.IsTransformed,
            Operations = JsonConvert.DeserializeObject<List<DocumentOperation>>(action.Data)
        };
    }

    // Transform operations before applying
    public void TransformOperations(List<CollaborationAction> actions)
    {
        var documentActions = actions
            .Select(x => (Syncfusion.EJ2.DocumentEditor.ActionInfo)MapGenericToControlAction(x))
            .ToList();
        documentActions
            .Where(x => !x.IsTransformed).ToList()
            .ForEach(x => CollaborativeEditingHandler.TransformOperation(x, documentActions));
    }

    // Queue save request
    public async Task SaveOperationsAsync(List<CollaborationAction> actions, string roomName, bool partialSave)
    {
        var message = new SaveRequest
        {
            Actions = actions,
            PartialSave = partialSave,
            RoomName = roomName
        };
        await saveTaskQueue.QueueBackgroundWorkItemAsync(message);
    }

    // Process and persist document
    public async Task ProcessSaveRequestAsync(SaveRequest request, CancellationToken ct)
    {
        Syncfusion.EJ2.DocumentEditor.WordDocument document = GetSourceDocument();
        CollaborativeEditingHandler handler = new CollaborativeEditingHandler(document);

        var actions = request.Actions
            .Select(x => (Syncfusion.EJ2.DocumentEditor.ActionInfo)MapGenericToControlAction(x))
            .ToList();

        if (actions.Count > 0)
        {
            foreach (var action in actions)
            {
                if (!action.IsTransformed)
                {
                    CollaborativeEditingHandler.TransformOperation(action, actions);
                }
            }
            foreach (var action in actions)
            {
                handler.UpdateAction(action);
            }

            MemoryStream stream = new MemoryStream();
            var doc = WordDocument.Save(JsonConvert.SerializeObject(handler.Document));
            doc.Save(stream, Syncfusion.DocIO.FormatType.Docx);
            SaveDocument(stream, "document.docx");
            stream.Close();
        }

        document.Dispose();
    }

    private void SaveDocument(Stream document, string fileName)
    {
        string filePath = Path.IsPathRooted(fileName) ? fileName : Path.Combine(fileLocation, fileName);
        using (FileStream file = new FileStream(filePath, FileMode.Create, FileAccess.Write))
        {
            document.Position = 0;
            document.CopyTo(file);
        }
    }

    internal static Syncfusion.EJ2.DocumentEditor.WordDocument GetSourceDocument()
    {
        string path = Path.Combine(fileLocation, "document.docx");
        Stream stream = System.IO.File.Open(path, FileMode.Open, FileAccess.Read, FileShare.Read);
        var document = Syncfusion.EJ2.DocumentEditor.WordDocument.Load(stream, FormatType.Docx);
        stream.Dispose();
        return document;
    }
}
```

---

## Add Collaboration API Controller

Implement three required endpoints for collaborative editing.

```csharp
using Microsoft.AspNetCore.Mvc;
using Syncfusion.Collaboration.Core.Interfaces;
using Syncfusion.Collaboration.Core.Models;
using Syncfusion.EJ2.DocumentEditor;

[Route("api/[controller]")]
[ApiController]
public class CollaborativeEditingController : ControllerBase
{
    private readonly IActionService actionService;
    private readonly ICollaborationAdapter adapter;
    private readonly IActiveTransport _transport;

    public CollaborativeEditingController(
        IActionService actionService,
        ICollaborationAdapter adapter,
        IActiveTransport transport)
    {
        this.actionService = actionService;
        this.adapter = adapter;
        this._transport = transport;
    }

    // Load document and apply pending operations
    [HttpPost]
    [Route("ImportFile")]
    public async Task<string> ImportFile([FromBody] FileInfo param)
    {
        try
        {
            var document = GetSourceDocument();
            var collaborationActions = await actionService.GetPendingOperationsAsync(param.roomName, 0, -1);
            var actions = collaborationActions
                .Select(x => (Syncfusion.EJ2.DocumentEditor.ActionInfo)adapter.MapGenericToControlAction(x))
                .ToList();

            if (actions != null && actions.Count > 0)
            {
                document.UpdateActions(actions);
            }

            string sfdt = JsonConvert.SerializeObject(document);
            var content = new { version = 0, sfdt };
            document.Dispose();
            return JsonConvert.SerializeObject(content);
        }
        catch { return null; }
    }

    // Receive, transform, and broadcast edit
    [HttpPost]
    [Route("UpdateAction")]
    public async Task<Syncfusion.EJ2.DocumentEditor.ActionInfo> UpdateAction(
        Syncfusion.EJ2.DocumentEditor.ActionInfo param)
    {
        var collaborationAction = (CollaborationAction)adapter.MapControlToGenericAction(param);
        var modifiedAction = await actionService.AddOperationAsync(collaborationAction, adapter);
        var documentAction = (Syncfusion.EJ2.DocumentEditor.ActionInfo)adapter.MapGenericToControlAction(modifiedAction);

        await _transport.SendToGroupAsync(param.RoomName, "action", documentAction);
        return documentAction;
    }

    // Get unsynchronized actions
    [HttpPost]
    [Route("GetActionsFromServer")]
    public async Task<string> GetActionsFromServer(Syncfusion.EJ2.DocumentEditor.ActionInfo param)
    {
        try
        {
            var collaborationActions = await actionService.GetEffectivePendingVersionAsync(param.RoomName, param.Version);
            var actions = collaborationActions
                .Select(x => (Syncfusion.EJ2.DocumentEditor.ActionInfo)adapter.MapGenericToControlAction(x))
                .ToList();

            int clientVersion = param.Version;
            actions.ForEach(action => action.Version = ++clientVersion);
            actions = actions.Where(action => action.Version > param.Version).ToList();

            return JsonConvert.SerializeObject(actions);
        }
        catch { return "{}"; }
    }

    public class FileInfo
    {
        public string fileName { get; set; }
        public string roomName { get; set; }
    }
}
```

---

## Install Required Packages

### Client side (npm/CDN)

**Via npm:**
```bash
npm install @syncfusion/ej2-documenteditor
npm install @syncfusion/ej2-collaborator
```
### Server side (NuGet)

```bash
dotnet add package Syncfusion.Collaborator.Server.AspNet.Core
dotnet add package Syncfusion.EJ2.WordEditor.AspNet.Core
```

---

## Run the Application

1. Start the ASP.NET Core backend: `dotnet run`
2. Open the HTML file in multiple browser tabs/windows
3. Changes made in one tab sync to all tabs in real-time

---
