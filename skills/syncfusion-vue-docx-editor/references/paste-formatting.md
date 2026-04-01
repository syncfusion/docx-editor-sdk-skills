# Paste Formatting

Paste system clipboard content into the Document Editor while preserving formatting using a server-side processor.

## Enable server paste
Use this when you need to paste clipboard content with rich formatting that the browser cannot preserve client-side.

```html
<ejs-documenteditor
  ref="documenteditor"
  :enableLocalPaste="false"
  :enableEditor="true"
  style="width:100%;height:100%">
</ejs-documenteditor>
```

## Server-side processing
Process the system clipboard data on the server using Syncfusion's WordEditor library so the paste options (Keep Source Formatting, Match Destination Formatting, Text Only) can be applied before returning content to the client.

```text
// Install NuGet package in your ASP.NET project
// Package: Syncfusion.EJ2.WordEditor.AspNet.Core
```

```csharp
// Minimal Web API controller skeleton (adapt to your server app)
[ApiController]
[Route("api/[controller]")]
public class WordEditorController : ControllerBase
{
    [HttpPost("paste")]
    public IActionResult Paste([FromBody] PasteRequest req)
    {
        // Use Syncfusion.EJ2.WordEditor.AspNet.Core services here to
        // convert/process the incoming clipboard payload (HTML/plain text)
        // applying the desired paste mode, then return processed content.
        // Return type should be the HTML or document content the client will insert.
        return Ok(new { content = processedHtml });
    }
}

public class PasteRequest
{
    public string ClipboardHtml { get; set; }
    public string PasteMode { get; set; } // e.g. "KeepSource", "MatchDestination", "TextOnly"
}
```

**Placeholders**
- 'Syncfusion.EJ2.WordEditor.AspNet.Core' → Replace with {nugetPackage}
- 'https://api.example.com/api/wordeditor/paste' → Replace with {pasteServiceUrl}
- 'KeepSource' → Replace with {pasteModeKeepSource}
- 'MatchDestination' → Replace with {pasteModeMatchDestination}
- 'TextOnly' → Replace with {pasteModeTextOnly}

## Client wiring (minimal)
Send the clipboard payload to the server paste endpoint and apply the returned content into the editor (server implementation details determine exact payload/response shapes).

```javascript
// Example client-side fetch (adapt to your app and clipboard capture)
fetch('{pasteServiceUrl}', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ ClipboardHtml: clipboardHtml, PasteMode: 'KeepSource' })
})
.then(r => r.json())
.then(data => {
  // Insert data.content into the Document Editor using the appropriate API
  // (use your app's editor instance methods to insert HTML or open document)
});
```

## File changes
- Add NuGet package: `Syncfusion.EJ2.WordEditor.AspNet.Core` to the server project
- Add server controller: `WordEditorController.cs` → paste handling endpoint
- Update client config: replace `{pasteServiceUrl}` with your real endpoint

## Paste options
Use the server-side paste handler to implement three paste modes:
- Keep Source Formatting: preserve original formatting
- Match Destination Formatting: adapt formatting to target paragraph
- Text Only: discard formatting and non-text elements

#### Notes
- Set `:enableLocalPaste="false"` so the editor defers formatted paste handling to your server pipeline.
- Browser security limits direct programmatic access to the system clipboard; server processing requires the client to supply the clipboard HTML (e.g., via a paste event or user action).
