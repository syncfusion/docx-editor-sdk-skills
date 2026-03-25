# Printing in WPF DOCX Editor

Printing support in the Syncfusion WPF DOCX Editor allows printing document contents directly from the editor using built‑in APIs and commands.

---

## Print document

### XAML
```xaml
<!-- Binds button to the PrintDocumentCommand -->
<Button Content="Print" Command="RichTextBoxAdv:SfRichTextBoxAdv.PrintDocumentCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
// Displays the Print Dialog and prints the document as pages.
richTextBoxAdv.PrintDocument();
```

## Shortcut
Keyboard shortcut: `Ctrl+P` also invokes printing.

## Print completed event
- `SfRichTextBoxAdv` exposes `PrintCompleted` to notify when printing finishes. Hook and unhook the event as shown below:

```csharp
// Hook the event
richTextBoxAdv.PrintCompleted += RichTextBoxAdv_PrintCompleted;

private void RichTextBoxAdv_PrintCompleted(object sender, PrintCompletedEventArgs args)
{
    // Printing finished — inspect args for status or show notification
}

// Unhook when no longer needed
richTextBoxAdv.PrintCompleted -= RichTextBoxAdv_PrintCompleted;
```

## Hide comments during printing
- By default comments are printed. To prevent comments from appearing in the printed output, set `EditorSettings.PrintComments` to `False` on the control.

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv">
    <RichTextBoxAdv:SfRichTextBoxAdv.EditorSettings>
        <RichTextBoxAdv:EditorSettings PrintComments="False" />
    </RichTextBoxAdv:SfRichTextBoxAdv.EditorSettings>
</RichTextBoxAdv:SfRichTextBoxAdv>
```
**Placeholders**
- `PrintComments="False"` → Replace with `{printComments}`

### C#
```csharp
richTextBoxAdv.EditorSettings.PrintComments = false;
```

**Placeholders**
- `false` → Replace with `{printComments}`
