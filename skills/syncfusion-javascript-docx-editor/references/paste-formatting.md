# Paste with Formatting

Enable formatted clipboard paste by disabling local paste and using the Syncfusion web API service library for rich text formatting retention.

## Configuration

Set `enableLocalPaste` to false to allow pasting formatted content from system clipboard with the web API service support.

```ts
//Initialize the Document Editor.
let editor: DocumentEditor = new DocumentEditor({ enableEditor: true, isReadOnly: false, enableSelection: true });
//Enable the local paste.
editor.enableLocalPaste = true;
```

**Requirement:** Deploy the `Syncfusion.EJ2.WordEditor.AspNet.Core` library on your web API service. This library processes clipboard data and preserves formatting during paste operations.

## Keep Source Formatting

Retains character styles and direct formatting (font size, italics, bold) from the copied text exactly as it appeared in the source.

## Match Destination Formatting

Applies the paragraph style and formatting of the paste destination, preserving only emphasis formatting (bold, italic) if applied to partial selections.

## Text Only

Strips all formatting and non-text elements (images, tables); tables convert to paragraphs and the text inherits the destination paragraph style.

**Note:** Keyboard shortcut Ctrl + V works across all paste modes. Copying from Document Editor and pasting externally works regardless of the `enableLocalPaste` setting.
