# Dialogs in WPF DOCX Editor

The Syncfusion WPF DOCX Editor provides built‑in dialogs for performing common document editing and formatting operations through a rich UI.

---

## Font Dialog
```xaml
<Button Content="Font" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowFontDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Paragraph Dialog
```xaml
<Button Content="Paragraph" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowParagraphDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## List Dialog
```xaml
<Button Content="List" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowListDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Insert Table Dialog
```xaml
<Button Content="Insert Table" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowInsertTableDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Insert Hyperlink Dialog
```xaml
<Button Content="Hyperlink" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowHyperlinkDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Find and Replace Dialog
```xaml
<Button Content="Find and Replace" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowFindAndReplaceDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Encrypt / Password Dialog
```xaml
<Button Content="Encrypt Document" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowEncryptDocumentDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Table Properties Dialog
```xaml
<Button Content="Table Properties" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowTableDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Table Options Dialog
```xaml
<Button Content="Table Options" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowTableOptionsDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Cell Options Dialog
```xaml
<Button Content="Cell Options" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowCellOptionsDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Borders and Shading Dialog
```xaml
<Button Content="Borders and Shading" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowBordersAndShadingDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

## Styles Dialogs

### Create Style dialog
```xaml
<Button Content="Create style" Command="Syncfusion:SfRichTextBoxAdv.ShowStyleDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### Modify Style dialog
```xaml
<Button Content="Modify style" Command="Syncfusion:SfRichTextBoxAdv.ShowStylesDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
