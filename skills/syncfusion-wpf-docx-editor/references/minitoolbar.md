# Mini Toolbar in WPF DOCX Editor

The mini toolbar feature in the Syncfusion WPF DOCX Editor provides quick access to common formatting actions for selected content.

---

**Overview**
- The Mini Toolbar is a small context toolbar that appears near the selection and provides quick formatting commands (Bold, Italic, underline, etc.).


## Enable / Disable Mini Toolbar
By default the mini toolbar is enabled. To disable it set `EnableMiniToolBar` to `False` on the control.

### XAML:

```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" EnableMiniToolBar="False" />
```

**Placeholders**
- `EnableMiniToolBar="False"` → Replace with `{enableMiniToolBar}`

### C#:

```csharp
// Disable
richTextBoxAdv.EnableMiniToolBar = false;

// Enable
richTextBoxAdv.EnableMiniToolBar = true;
```

**Placeholders**
- `false` / `true` → Replace with `{enableMiniToolBar}`