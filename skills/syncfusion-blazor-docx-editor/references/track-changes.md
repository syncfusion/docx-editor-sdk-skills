# Track Changes

Monitor and manage document edits with revision tracking, allowing you to accept or reject changes and enforce document protection modes.

## Enable tracking

```csharp
<SfDocumentEditorContainer EnableTrackChanges="true" EnableToolbar="true">
</SfDocumentEditorContainer>
```

To enable tracking for all documents on load:

```csharp
<SfDocumentEditorContainer @ref="container" EnableToolbar="true">
    <DocumentEditorContainerEvents DocumentChanged="OnDocumentChange" />
</SfDocumentEditorContainer>

@code {
    SfDocumentEditorContainer container;
    
    public void OnDocumentChange()
    {
        if(container != null){
            container.EnableTrackChanges = true;
        }
    }
}
```

> Track changes are document-level settings. When opening a document, `EnableTrackChanges` reflects the document's existing state unless explicitly set during the `DocumentChanged` event.

## Toggle revisions pane

Show or hide the revisions pane to manage tracked changes visibility.

```csharp
@using Syncfusion.Blazor.DocumentEditor
<SfDocumentEditorContainer @ref="container" EnableToolbar=true EnableTrackChanges=true>
    <DocumentEditorContainerEvents Created="OnLoad"></DocumentEditorContainerEvents>
</SfDocumentEditorContainer>

@code {
    SfDocumentEditorContainer container;
    
    public async void OnLoad(object args)
    {
        container.DocumentEditor.ShowRevisions = true;   // Show pane
        container.DocumentEditor.ShowRevisions = false;  // Hide pane
    }
}
```

## Navigate revisions

Move between tracked changes programmatically.

```csharp
// Move to next change
await container.DocumentEditor.Selection.NavigateNextRevisionAsync();

// Move to previous change
await container.DocumentEditor.Selection.NavigatePreviousRevisionAsync();
```

## Add custom metadata to revisions

Attach additional metadata (roles, tags, identifiers) to tracked changes and display it alongside the author name.

```csharp
<SfDocumentEditorContainer @ref="container" 
    DocumentEditorSettings="@settings" 
    EnableTrackChanges="true">
</SfDocumentEditorContainer>

@code {
    DocumentEditorSettingsModel settings = new DocumentEditorSettingsModel() 
    { 
        RevisionSettings = new RevisionSettingsModel 
        { 
            CustomData = "Developer",
            ShowCustomDataWithAuthor = true
        }
    };
}
```

**Placeholders**
- `"Developer"` → Replace with `{roleOrTag}`

> **Note:** Custom metadata is preserved when exporting as SFDT. For other formats (DOCX, etc.), custom data is not retained as it is specific to Document Editor.

## Set colors for revision types

Override the default author-based color for specific revision types.

```csharp
<SfDocumentEditorContainer EnableToolbar=true Height="890px" EnableTrackChanges="true" DocumentEditorSettings="@Settings"></SfDocumentEditorContainer>

@code {
    private DocumentEditorSettingsModel Settings = new DocumentEditorSettingsModel
    {
        RevisionSettings = new RevisionSettingsModel()
        {
            InsertRevisionColor = "#22C55E",
            DeleteRevisionColor = "#EF4444",
            InsertedRowColor = "#f6fa06",
            DeletedRowColor = "#3a02bb"
        }
    };
}
```

**Placeholders**
- `"#22C55E"` → Replace with `{insertRevisionColor}`
- `"#EF4444"` → Replace with `{deleteRevisionColor}`
- `"#f6fa06"` → Replace with `{insertedRowColor}`
- `"#3a02bb"` → Replace with `{deletedRowColor}`

> **Note:** These settings only affect how revisions are displayed in the DOCX Editor and are not stored in the document. By default, all revision types use author-specific colors (`'byAuthor'`).

## Custom colors for track changes

Assign a color per author from a custom array, applied in order.

```csharp
@using Syncfusion.Blazor.DocumentEditor

<SfDocumentEditorContainer @ref="container" EnableToolbar="true" DocumentEditorSettings="settings">
</SfDocumentEditorContainer>

@code {
    SfDocumentEditorContainer container;
    private DocumentEditorSettingsModel settings = new DocumentEditorSettingsModel()
    {
        RevisionSettings = new RevisionSettingsModel()
        {
            RevisionColors = new string[]
            {
                "#0000ff",
                "#bb00ff",
                "#c14f16"
            }
        }
    };
}
```

**Placeholders**
- `"#0000ff"`, `"#bb00ff"`, `"#c14f16"` → Replace with `{authorColors}` (an array of hex color strings applied to authors in order)

> **Note:** The first author gets the first color, the second gets the next, and so on. If there are more authors than colors, the assignment starts again from the beginning of the array.

## Protect document (revisions-only mode)

Restrict users to view and edit with tracked changes only—they cannot accept or reject revisions without a password.

```csharp
<button @onclick="ProtectDocument">Protect</button>
<SfDocumentEditorContainer @ref="container" EnableToolbar="true"></SfDocumentEditorContainer>

@code {
    SfDocumentEditorContainer container;
    
    protected async void ProtectDocument(object args)
    {
        // Enforce revisions-only protection
        await container.DocumentEditor.Editor.EnforceProtectionAsync("password", ProtectionType.RevisionsOnly);
        
        // Remove protection
        await container.DocumentEditor.Editor.StopProtectionAsync("password");
    }
}
```

**Placeholders**
- `"password"` → Replace with `{documentPassword}`

> **Protection types:** `NoProtection | ReadOnly | FormFieldsOnly | CommentsOnly | RevisionsOnly`
