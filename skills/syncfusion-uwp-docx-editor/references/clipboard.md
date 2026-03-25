# Clipboard Operations in UWP DOCX Editor

Clipboard support in the Syncfusion UWP DOCX Editor allows copying, cutting, and pasting document content using built‑in commands and APIs.

---

## Copy

### XAML
```xaml
<!-- Binds button to the CopyCommand -->
<Button Content="Copy" Command="{Binding ElementName=richTextBoxAdv, Path=CopyCommand, Mode=TwoWay}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
richTextBoxAdv.CopyCommand.Execute(richTextBoxAdv);
```

---

## Cut

### XAML
```xaml
<!-- Binds button to the CutCommand -->
<Button Content="Cut" Command="{Binding ElementName=richTextBoxAdv, Path=CutCommand, Mode=TwoWay}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
richTextBoxAdv.CutCommand.Execute(richTextBoxAdv);
```
---

## Paste
### XAML
```xaml
<!-- Binds button to the PasteCommand -->
<Button Content="Paste" Command="{Binding ElementName=richTextBoxAdv, Path=PasteCommand, Mode=TwoWay}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
richTextBoxAdv.PasteCommand.Execute(richTextBoxAdv);
```
---

## Clipboard supported formats

Typical clipboard formats the editor can work with:

- Plain text
- Rich Text Format (RTF)
- Image

---

## Keyboard shortcuts

- Ctrl+C — Copy
- Ctrl+X — Cut
- Ctrl+V — Paste

---