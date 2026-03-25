# Hyperlinks in WPF DOCX Editor

Hyperlink support in the Syncfusion WPF DOCX Editor allows inserting and interacting with hyperlinks within documents.

---

## Insert a hyperlink

The low-level representation of a hyperlink is a field composed of `FieldBeginAdv`, a `SpanAdv` containing the HYPERLINK field code, a `FieldSeparatorAdv`, a display `SpanAdv`, and `FieldEndAdv`.

## XAML
```xaml
<RichTextBoxAdv:ParagraphAdv>
	<RichTextBoxAdv:FieldBeginAdv />
	<RichTextBoxAdv:SpanAdv Text=" HYPERLINK &quot;http://www.syncfusion.com&quot; " />
	<RichTextBoxAdv:FieldSeparatorAdv />
	<RichTextBoxAdv:SpanAdv Text="Syncfusion">
		<RichTextBoxAdv:SpanAdv.CharacterFormat>
			<RichTextBoxAdv:CharacterFormat Underline="Single" FontColor="#ff0563c1" />
		</RichTextBoxAdv:SpanAdv.CharacterFormat>
	</RichTextBoxAdv:SpanAdv>
	<RichTextBoxAdv:FieldEndAdv />
</RichTextBoxAdv:ParagraphAdv>
```

**Placeholders**
- `http://www.syncfusion.com` → Replace with `{hyperlinkUrl}`
- `Syncfusion` → Replace with `{displayText}`
- `Underline="Single"` → Replace with `{underlineStyle}`
- `FontColor="#ff0563c1"` → Replace with `{fontColor}`


### C#
```csharp
// Appends the field start.
paragraphAdv.Inlines.Add(new FieldBeginAdv());
// Appends the field code.
SpanAdv fieldCode = new SpanAdv();
string url = "www.syncfusion.com";
fieldCode.Text = " HYPERLINK \"" + url + "\" ";
paragraphAdv.Inlines.Add(fieldCode);
// Appends the field separator
paragraphAdv.Inlines.Add(new FieldSeparatorAdv());
// Appends the field result.
SpanAdv fieldResult = new SpanAdv();
fieldResult.Text = "Syncfusion";
fieldResult.CharacterFormat.Underline = Underline.Single;
fieldResult.CharacterFormat.FontColor = Color.FromArgb(0xff, 0x05, 0x63, 0xc1);
paragraphAdv.Inlines.Add(fieldResult);
// Appends the field end.
paragraphAdv.Inlines.Add(new FieldEndAdv());
```
 
 **Placeholders**
- `"www.syncfusion.com"` → Replace with `{hyperlinkUrl}`
- `" HYPERLINK \"" + url + "\" "` → Replace with `{fieldCode}`
- `"Syncfusion"` → Replace with `{displayText}`
- `Color.FromArgb(0xff, 0x05, 0x63, 0xc1)` → Replace with `{fontColor}`
- `Underline.Single` → Replace with `{underlineStyle}`

---

## Insert hyperlink via UI dialog

### XAML
```xaml
<!-- Insert hyperlink using built-in command -->
<Button Content="Insert Hyperlink" Command="RichTextBoxAdv:SfRichTextBoxAdv.InsertHyperlinkCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" CommandParameter="www.google.com" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

**Placeholders**
- `CommandParameter="www.google.com"` → Replace with `{hyperlinkUrl}`

### C#

```csharp
SfRichTextBoxAdv.InsertHyperlinkCommand.Execute(new string[] { "www.syncfusion.com", "Syncfusion", "Go to Syncfusion" }, richTextBoxAdv);
```

**Placeholders**
- `"www.syncfusion.com"` → Replace with `{hyperlinkUrl}`
- `"Syncfusion"` → Replace with `{displayText}`
- `"Go to Syncfusion"` → Replace with `{screenTip}`

---

## ScreenTip (tooltip) for hyperlinks

- Include a ScreenTip in the hyperlink field code (the `\o` switch). 

- When the mouse hovers over a hyperlink a tooltip shows the navigation link or custom ScreenTip text.

### XAML

```xaml
<RichTextBoxAdv:ParagraphAdv>
	<RichTextBoxAdv:FieldBeginAdv />
	<RichTextBoxAdv:SpanAdv Text=" HYPERLINK \"http://www.syncfusion.com\" \o SfRichTextBox " />
	<RichTextBoxAdv:FieldSeparatorAdv />
	<RichTextBoxAdv:SpanAdv Text="SfRichTextBoxAdv">
		<RichTextBoxAdv:SpanAdv.CharacterFormat>
			<RichTextBoxAdv:CharacterFormat Underline="Single" FontColor="#ff0563c1" />
		</RichTextBoxAdv:SpanAdv.CharacterFormat>
	</RichTextBoxAdv:SpanAdv>
	<RichTextBoxAdv:FieldEndAdv />
</RichTextBoxAdv:ParagraphAdv>
```

**Placeholders**
- `" HYPERLINK \"http://www.syncfusion.com\" \o SfRichTextBox "` → Replace with `{fieldCodeWithScreenTip}` *(parts: `{hyperlinkUrl}`, `{screenTipText}`)*
- `SfRichTextBoxAdv` → Replace with `{displayText}`
- `Underline="Single"` → Replace with `{underlineStyle}`
- `FontColor="#ff0563c1"` → Replace with `{fontColor}`

---

## Show built-in hyperlink dialog

### XAML
```xaml
<Button Content="Hyperlink" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowHyperlinkDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />
```

- The dialog lets users enter display text, link, and ScreenTip and inserts the field when OK is pressed.

---

## Disable hyperlink ScreenTips

- The editor `EditorSettings.DisplayScreenTips` controls whether tooltip text is shown for hyperlinks. Disable it to prevent showing the tooltip.

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv">
	<RichTextBoxAdv:SfRichTextBoxAdv.EditorSettings>
		<RichTextBoxAdv:EditorSettings DisplayScreenTips="False" />
	</RichTextBoxAdv:SfRichTextBoxAdv.EditorSettings>
</RichTextBoxAdv:SfRichTextBoxAdv>
```

**Placeholders**
- `DisplayScreenTips="False"` → Replace with `{displayScreenTips}`

---

## Hyperlink navigation event

- Handle `RequestNavigate` to customize navigation (open links, handle files, block navigation, etc.).

```csharp

// Subscribe
richTextBoxAdv.RequestNavigate += RichTextBoxAdv_RequestNavigate;

private void RichTextBoxAdv_RequestNavigate(object sender, Syncfusion.Windows.Controls.RichTextBoxAdv.RequestNavigateEventArgs args)
{
	// args.Hyperlink contains LinkType and NavigationLink
	if (args.Hyperlink.LinkType == HyperlinkType.Webpage || args.Hyperlink.LinkType == HyperlinkType.Email)
	{
		Process.Start(new ProcessStartInfo(new Uri(args.Hyperlink.NavigationLink).AbsoluteUri) { UseShellExecute = true });
	}
	else if (args.Hyperlink.LinkType == HyperlinkType.File && File.Exists(args.Hyperlink.NavigationLink))
	{
		Process.Start(new ProcessStartInfo(args.Hyperlink.NavigationLink) { UseShellExecute = true });
	}
}

// Unsubscribe when no longer needed
richTextBoxAdv.RequestNavigate -= RichTextBoxAdv_RequestNavigate;
```

**Placeholders**
- `RichTextBoxAdv_RequestNavigate` → Replace with `{requestNavigateHandler}`
- `args.Hyperlink.NavigationLink` → Replace with `{navigationLink}`

---