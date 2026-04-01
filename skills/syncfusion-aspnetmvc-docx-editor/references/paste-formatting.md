# Paste with Formatting

Enable system clipboard paste with formatting preservation using the Document Editor.

## Enable Paste Formatting
Set up Document Editor to support formatted clipboard paste by connecting to a backend service running the Syncfusion clipboard formatting library.


```cshtml

@Html.EJS().DocumentEditorContainer("container").Height("590px").EnableToolbar(true).Render()

<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor = document.getElementById("container").ej2_instances[0];
        documenteditor.serviceUrl = "/api/DocumentEditor/"
        documenteditor.enableLocalPaste = false;
    });
</script>

```

**Explanation:** Setting `enableLocalPaste` to `false` disables the internal clipboard and instead enables the system clipboard with formatting support through the backend service.


## Paste Options
Three formatting options appear in the context menu when pasting from system clipboard.

### Keep Source Formatting
Retains all character styles and direct formatting from the copied text, including font size, italics, and other direct styling not in paragraph styles. Use this when you want to preserve the original document's visual appearance.

### Match Destination Formatting
Discards most direct formatting but preserves emphasis styles (bold, italic). Text adopts the destination paragraph style and direct formatting of surrounding text. Use this to integrate copied content into the target document's style while maintaining semantic emphasis.

### Text Only
Removes all formatting and non-text elements. Pictures are discarded, tables are converted to paragraphs. Text adopts destination paragraph style and surrounding text formatting. Use this for plain text insertion without any visual styling.

## Configuration Notes

**Context Menu Behavior**
Formatting paste options appear automatically in the context menu when paste formatting is enabled. Keyboard shortcuts (Ctrl + V) work with these options available.

**Browser Compatibility**
System clipboard access requires appropriate browser permissions. Most modern browsers support this; ensure the application runs in a secure context (HTTPS).

**Prerequisites for Setup**
- `enableLocalPaste` set to `false` on DocumentEditorComponent
- Web API service running and accessible from the frontend application
