# How to determine the editing context type

Identify the current editing context in the Syncfusion UWP DOCX Editor, such as whether the selection is within text, a table, an image, or other document elements.

---

## EditingContext and EditingContextType

The `SfRichTextBoxAdv` exposes an `EditingContext` for the current selection which indicates what kind of content is active for editing. Common `EditingContextType` values are:

- `Text` — the selection/caret is inside editable text.
- `Image` — an image is selected.
- `Table` — table  is selected.

---

## C#

```csharp
EditingContext editingContext = richTextBoxAdv.Selection?.EditingContext;
if (editingContext != null)
{
    switch (editingContext.Type)
    {
        case EditingContextType.Text:
            // Enable text formatting toolbar
            break;
        case EditingContextType.Image:
            // Enable image tools (resize, wrap, alt text)
            break;
        case EditingContextType.Table:
            // Enable table tools (insert/delete row/column)
            break;
    }
}
```

---