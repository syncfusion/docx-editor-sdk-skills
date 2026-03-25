# Layout Types in WPF DOCX Editor

Layout type support in the Syncfusion WPF DOCX Editor controls how document content is rendered and displayed within the editor.


---

## Pages

- When using Pages layout type, the rich text document content is rendered sequentially in several pages, similar to the Print layout view of Microsoft Word. 

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" LayoutType="Pages"/>
```

**Placeholders**
- `LayoutType="Pages"` → Replace with `{layoutType}`

### C#
```csharp
// Initializes a new instance of RichTextBoxAdv.
SfRichTextBoxAdv richTextBoxAdv = new SfRichTextBoxAdv();

// Defines the layout type as Pages
richTextBoxAdv.LayoutType = LayoutType.Pages;
```

**Placeholders**
- `LayoutType.Pages` → Replace with `{layoutType}`

---

## Continuous

- When using Continuous layout type, the entire rich text document content is rendered continuously in a single page, similar to the Web layout view of Microsoft Word. 

- This layout looks like a simple text box with rich-text content and can be used for applications such as forums and blogs.

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" LayoutType="Continuous"/>
```

**Placeholders**
- `LayoutType="Continuous"` → Replace with `{layoutType}`

### C#
```csharp
// Initializes a new instance of RichTextBoxAdv.
SfRichTextBoxAdv richTextBoxAdv = new SfRichTextBoxAdv();

// Defines the layout type as Continuous.
richTextBoxAdv.LayoutType = LayoutType.Continuous;
```

**Placeholders**
- `LayoutType.Continuous` → Replace with `{layoutType}`

---

## Block

- When using Block layout type, the rich text content is rendered continuously in a single page as read only. 

- This layout looks like a simple text block with rich text content such as texts, images, and tables. 

- Block Layout also supports copying contents to the clipboard. This can be used for applications such as forums and blogs in order to display the rich-text contents with same look and feel as in the continuous layout type.

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" LayoutType="Block"/>
```

**Placeholders**
- `LayoutType="Block"` → Replace with `{layoutType}`

### C#
```csharp
// Initializes a new instance of RichTextBoxAdv.
SfRichTextBoxAdv richTextBoxAdv = new SfRichTextBoxAdv();

// Defines the layout type as Block.
richTextBoxAdv.LayoutType = LayoutType.Block;
```

**Placeholders**
- `LayoutType.Block` → Replace with `{layoutType}`

---