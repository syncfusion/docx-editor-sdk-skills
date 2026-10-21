# Collaborative Editing

> Core setup for real-time multi-user collaborative editing using Collaboration Client and Server.

---

## Enable Collaborative Editing

Enable collaborative editing in the DOCX Editor component.

```javascript
import { DocumentEditorContainer, DocumentEditor, CollaborativeEditingHandler } from '@syncfusion/ej2-documenteditor';

// Inject collaborative editing module
DocumentEditor.Inject(CollaborativeEditingHandler);
DocumentEditorContainer.Inject(Toolbar);

let container = new DocumentEditorContainer({ enableToolbar: true, height: '590px' });
container.serviceUrl = 'http://localhost:5000/api/documenteditor/';
container.appendTo('#container');

// Enable collaborative editing
container.documentEditor.enableCollaborativeEditing = true;
```

**Placeholders**
- `'http://localhost:5000/api/documenteditor/'` → Replace with `{backendServiceUrl}`

---

## Create Document Editor Adapter

Implement `ICollaborationProvider` to bridge the DOCX Editor and Collaboration Client.

```typescript
import { ICollaborationProvider, ICollaborationActionData } from '@syncfusion/ej2-collaborator';

export class DocumentEditorAdapter implements ICollaborationProvider {
  constructor(
    private container: DocumentEditorContainer,
    private serviceUrl: string
  ) {}

  // The only ICollaborationProvider method — applied for every remote action.
  public applyRemoteAction(action: string, data: ICollaborationActionData): void {
    this.container.documentEditor.collaborativeEditingHandlerModule?.applyRemoteAction(action, data.payload);
  }

  // Fetch the document from the product's REST API and return the room name.
  public async loadFromServer(fileName: string): Promise<string> {
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
  public async open(responseText: string, roomName: string): Promise<void> {
    const data = JSON.parse(responseText);
    this.container?.documentEditor.collaborativeEditingHandlerModule?.updateRoomInfo(
      roomName, data.version, this.serviceUrl + 'api/CollaborativeEditing/'
    );
    this.container.documentEditor.open(data.sfdt);
    this.container.contentChange = (args: any) => {
      this.container.documentEditor.collaborativeEditingHandlerModule?.sendActionToServer(args.operations as Operation[]);
    };
  }

  // Generate unique room name
  private getRoomName(fileName: string): string {
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

## Wire Collaboration Client (WebSocket)

Initialize Collaboration Client with WebSocket transport and join the room. ASP.NET MVC supports WebSocket transport only.

```typescript
import { CollaborationClient, UserInfo } from '@syncfusion/ej2-collaborator';
import { DocumentEditorAdapter } from './DocumentEditorAdapter';

const serviceUrl = 'https://localhost:44387/';
const adapter = new DocumentEditorAdapter(this.container, serviceUrl);

// Create and configure client with WebSocket
const client = new CollaborationClient(adapter, {
  serviceUrl: 'https://localhost:44387/',
  connectionType: 'websocket',
  currentUser: this.currentUser,
  onUserJoined: (user: UserInfo) => {
    if (this.titleBar) { this.titleBar.addUser(user); }
  },
  onUserLeft: (user: UserInfo) => {
    if (this.titleBar) { this.titleBar.removeUser(user); }
  }
});

// Load document and join room
(async () => {
  const roomName = await adapter.loadFromServer('Giant Panda.docx');
  await client.joinRoomAsync(roomName);
})();
```

**Placeholders**
- `'https://localhost:44387/'` → Replace with `{backendServiceUrl}`
- `this.currentUser` → Replace with `{currentUser}`

**Note**
- ASP.NET MVC Collaboration Server supports WebSocket transport only.

---

## Register Collaboration Server (Global.asax.cs)

Register the Collaboration Server and adapter during application startup.

```csharp
namespace WebApplication1
{
    public class MvcApplication : System.Web.HttpApplication
    {
        protected void Application_Start()
        {
            AreaRegistration.RegisterAllAreas();
            GlobalConfiguration.Configure(WebApiConfig.Register);
            FilterConfig.RegisterGlobalFilters(GlobalFilters.Filters);
            RouteConfig.RegisterRoutes(RouteTable.Routes);
            BundleConfig.RegisterBundles(BundleTable.Bundles);

            // Register the control-specific adapter
            ServiceCollectionExtensions.RegisterAdapter(
                new DocumentEditorCollaborationAdapter());

            // Configure Redis + WebSocket transport
            ServiceCollectionExtensions.AddCollaborationServer(options =>
            {
                options.ConnectionString = "Your Redis Connection string";
                options.ConnectionType = CollaborationConnectionType.WebSocket;
            });
        }
    }
}
```

**Placeholders**
- `"Your Redis Connection string"` → Replace with `{redisConnectionString}`

**Settings**
- `ConnectionString` — Redis connection string
- `ConnectionType` — `CollaborationConnectionType.WebSocket` (MVC supports WebSocket only)

---

## Mount WebSocket Endpoint (Startup.cs)

Add an OWIN startup class to expose the Collaboration Server WebSocket endpoint.

```csharp
public class Startup
{
    public void Configuration(IAppBuilder app)
    {
        app.Map("/ws", map =>
        {
            map.Run(context =>
            {
                var httpContext = HttpContext.Current;

                if (httpContext == null)
                {
                    context.Response.StatusCode = 500;
                    return Task.CompletedTask;
                }

                if (!httpContext.IsWebSocketRequest)
                {
                    context.Response.StatusCode = 400;
                    return context.Response.WriteAsync("WebSocket connection required.");
                }

                httpContext.AcceptWebSocketRequest(ServiceCollectionExtensions.MapCollaborationServer());
                return Task.CompletedTask;
            });
        });
    }
}
```

---

## Create Document Editor Collaboration Adapter (Server)

Implement `ICollaborationAdapter` to translate Document Editor actions.

```csharp
using Syncfusion.Collaboration.Core.Interfaces;
using Syncfusion.Collaboration.Core.Models;
using Syncfusion.Collaboration.Core.Services;
using Syncfusion.EJ2.DocumentEditor;
using Newtonsoft.Json;

namespace WebApplication1.Adapter
{
    public class DocumentEditorCollaborationAdapter : ICollaborationAdapter
    {
        public DocumentEditorCollaborationAdapter() { }

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
            var queue = CollaborationServiceContainer.Resolve<IBackgroundTaskQueue>();
            await queue.QueueBackgroundWorkItemAsync(message);
        }

        // Process and persist document
        public async Task ProcessSaveRequestAsync(SaveRequest request, CancellationToken cancellationToken)
        {
            Syncfusion.EJ2.DocumentEditor.WordDocument document = CollaborativeEditingController.GetSourceDocument();
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
                Syncfusion.DocIO.DLS.WordDocument doc =
                    WordDocument.Save(JsonConvert.SerializeObject(handler.Document));
                doc.Save(stream, Syncfusion.DocIO.FormatType.Docx);
                stream.Close();
            }

            document.Dispose();

            var actionService = CollaborationServiceContainer.Resolve<IActionService>();
            await actionService.ClearRecordsAsync(request.RoomName, request.PartialSave);
        }
    }
}
```

---

## Add Collaboration API Controller

Implement three required endpoints for collaborative editing.

```csharp
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Syncfusion.Collaboration.Core.Interfaces;
using Syncfusion.Collaboration.Core.Models;
using Syncfusion.Collaboration.Core.Services;
using Syncfusion.EJ2.DocumentEditor;
using Newtonsoft.Json;

namespace WebApplication1.Controllers
{
    [RoutePrefix("api/CollaborativeEditing")]
    public class CollaborativeEditingController : ApiController
    {
        private static string fileLocation;
        private readonly IActionService actionService;
        private readonly ICollaborationAdapter adapter;
        private readonly IActiveTransport transport;

        public CollaborativeEditingController()
        {
            fileLocation = HostingEnvironment.MapPath("~/App_Data");
            actionService = CollaborationServiceContainer.Resolve<IActionService>();
            adapter = CollaborationServiceContainer.Resolve<ICollaborationAdapter>();
            transport = CollaborationServiceContainer.Resolve<IActiveTransport>();
        }

        // Load document and apply pending operations
        [HttpPost]
        [Route("ImportFile")]
        public async Task<HttpResponseMessage> ImportFile(FileInfo param)
        {
            try
            {
                DocumentContent content = new DocumentContent();
                EJ2WordDocument document = GetSourceDocument();

                List<CollaborationAction> collaborationActions =
                    await actionService.GetPendingOperationsAsync(param.roomName, 0, -1);

                List<ActionInfo> actions = collaborationActions
                    .Select(x => (ActionInfo)adapter.MapGenericToControlAction(x))
                    .ToList();

                if (actions != null && actions.Count > 0)
                {
                    document.UpdateActions(actions);
                }

                string sfdt = JsonConvert.SerializeObject(document);
                content.version = 0;
                content.sfdt = sfdt;
                document.Dispose();

                return Request.CreateResponse(HttpStatusCode.OK, content);
            }
            catch (Exception ex)
            {
                return Request.CreateErrorResponse(HttpStatusCode.InternalServerError, ex);
            }
        }

        // Receive, transform, and broadcast edit
        [HttpPost]
        [Route("UpdateAction")]
        public async Task<Syncfusion.EJ2.DocumentEditor.ActionInfo> UpdateAction(
            Syncfusion.EJ2.DocumentEditor.ActionInfo param)
        {
            CollaborationAction collaborationAction =
                (CollaborationAction)adapter.MapControlToGenericAction(param);
            CollaborationAction modifiedAction =
                await actionService.AddOperationAsync(collaborationAction, adapter);
            var documentAction =
                (Syncfusion.EJ2.DocumentEditor.ActionInfo)adapter.MapGenericToControlAction(modifiedAction);

            await transport.SendToGroupAsync(param.RoomName, "action", documentAction);
            return documentAction;
        }

        // Get unsynchronized actions
        [HttpPost]
        [Route("GetActionsFromServer")]
        public async Task<string> GetActionsFromServer(Syncfusion.EJ2.DocumentEditor.ActionInfo param)
        {
            try
            {
                string roomName = param.RoomName;
                int lastSyncedVersion = param.Version;
                int clientVersion = param.Version;

                List<CollaborationAction> collaborationActions =
                    await actionService.GetEffectivePendingVersionAsync(roomName, lastSyncedVersion);

                List<Syncfusion.EJ2.DocumentEditor.ActionInfo> actions = collaborationActions
                    .Select(x => (Syncfusion.EJ2.DocumentEditor.ActionInfo)adapter.MapGenericToControlAction(x))
                    .ToList();

                actions.ForEach(action => action.Version = ++clientVersion);
                actions = actions.Where(action => action.Version > lastSyncedVersion).ToList();

                actions.Where(action => !action.IsTransformed).ToList()
                    .ForEach(action => CollaborativeEditingHandler.TransformOperation(action, actions));

                return JsonConvert.SerializeObject(actions);
            }
            catch
            {
                return "{}";
            }
        }

        public class DocumentContent
        {
            public int version { get; set; }
            public string sfdt { get; set; }
        }

        public class FileInfo
        {
            public string fileName { get; set; }
            public string roomName { get; set; }
        }

        internal static EJ2WordDocument GetSourceDocument()
        {
            string path = HostingEnvironment.MapPath("~/App_Data/Giant Panda.docx");
            string extension = Path.GetExtension(path);

            Stream stream = File.Open(path, FileMode.Open, FileAccess.Read, FileShare.Read);
            EJ2WordDocument document = EJ2WordDocument.Load(stream, GetFormatType(extension));
            stream.Dispose();

            return document;
        }

        internal static Syncfusion.EJ2.DocumentEditor.FormatType GetFormatType(string format)
        {
            if (string.IsNullOrEmpty(format))
                throw new NotSupportedException("EJ2 DocumentEditor does not support this file format.");

            switch (format.ToLower())
            {
                case ".dotx":
                case ".docx":
                case ".docm":
                case ".dotm":
                    return Syncfusion.EJ2.DocumentEditor.FormatType.Docx;
                case ".dot":
                case ".doc":
                    return Syncfusion.EJ2.DocumentEditor.FormatType.Doc;
                case ".rtf":
                    return Syncfusion.EJ2.DocumentEditor.FormatType.Rtf;
                case ".txt":
                    return Syncfusion.EJ2.DocumentEditor.FormatType.Txt;
                case ".xml":
                    return Syncfusion.EJ2.DocumentEditor.FormatType.WordML;
                case ".html":
                    return Syncfusion.EJ2.DocumentEditor.FormatType.Html;
                default:
                    throw new NotSupportedException("EJ2 DocumentEditor does not support this file format.");
            }
        }
    }
}
```

---

## Install Required NuGet Packages

```bash
Install-Package Syncfusion.Collaborator.Server.AspNet.Mvc
Install-Package Syncfusion.EJ2.WordEditor.AspNet.Mvc5
```

---

## Install Collaboration Client (npm)

```bash
npm install @syncfusion/ej2-collaborator
```

---

## Run the Application

1. Start Redis server
2. Run the ASP.NET MVC application
3. Open the app in multiple browser tabs/windows
4. Changes made in one tab sync to all tabs in real-time

---
