# Clipboard Operations in WPF DOCX Editor

Clipboard support in the Syncfusion WPF DOCX Editor allows copying, cutting, and pasting document content using built‑in commands and APIs.

---

## Copy

### XAML
```xaml
<!-- Binds button to the CopyCommand -->
<Button Content="Copy" Command="RichTextBoxAdv:SfRichTextBoxAdv.CopyCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
SfRichTextBoxAdv.CopyCommand.Execute(null, richTextBoxAdv);
```

---

## Cut

### XAML
```xaml
<!-- Binds button to the CutCommand -->
<Button Content="Cut" Command="RichTextBoxAdv:SfRichTextBoxAdv.CutCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
SfRichTextBoxAdv.CutCommand.Execute(null, richTextBoxAdv);
```
---

## Paste
### XAML
```xaml
<!-- Binds button to the PasteCommand -->
<Button Content="Paste" Command="RichTextBoxAdv:SfRichTextBoxAdv.PasteCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
SfRichTextBoxAdv.PasteCommand.Execute(null, richTextBoxAdv);
```
---

## Clipboard supported formats

Typical clipboard formats the editor can work with:

- Plain text
- Rich Text Format (RTF)
- Image
- HTML

---

## Keyboard shortcuts

- Ctrl+C — Copy
- Ctrl+X — Cut
- Ctrl+V — Paste

---