# Background in WPF DOCX Editor

Background customization in the Syncfusion WPF DOCX Editor allows controlling the visual appearance of the editor control and document pages.


---

## Control background

- Set the `Background` property on the control to change its overall background color.

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" Background="#6699cc" />
```

**Placeholders**
- `Background="#6699cc"` → Replace with `{controlBackgroundColor}`

## C#

```csharp
richTextBoxAdv.Background = new SolidColorBrush(Color.FromRgb(102, 153, 204));
```

**Placeholders**
- `new SolidColorBrush(Color.FromRgb(102, 153, 204))` → Replace with `{backgroundBrush}`
- `Color.FromRgb(102, 153, 204)` → Replace with `{backgroundColor}`

---

## Override document background in Continuous layout

- By default document background properties are applied for `Continuous` layout. 

- To force the control background to be used instead, set `OverridesDocumentBackground` to `true` (only valid when `LayoutType` is `Continuous`).

## XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" LayoutType="Continuous" Background="#6699cc" OverridesDocumentBackground="True" />
```

**Placeholders**
- `Background="#6699cc"` → Replace with `{controlBackgroundColor}`
- `OverridesDocumentBackground="True"` → Replace with `{overridesDocumentBackground}`

---

## Page/document background

- To change the background color of document pages (the `DocumentAdv` background):

### C#
```csharp
// Sets the document background color
richTextBoxAdv.Document.Background.Color = Color.FromRgb(102, 153, 204);
```

**Placeholders**
- `Color.FromRgb(102, 153, 204)` → Replace with `{documentBackgroundColor}`
---