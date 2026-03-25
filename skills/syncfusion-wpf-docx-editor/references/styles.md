# Styles in WPF DOCX Editor

Styles support in the Syncfusion WPF DOCX Editor allows creating and managing reusable formatting styles within documents.

---

## Create Character Style

```csharp
CharacterStyle newCharStyle = new CharacterStyle();
newCharStyle.Name = "NewChar";
newCharStyle.CharacterFormat.FontSize = 16d;
newCharStyle.CharacterFormat.FontFamily = new FontFamily("Calibri Light");
newCharStyle.CharacterFormat.FontColor = Color.FromRgb(47, 84, 150);
newCharStyle.CharacterFormat.Bold = true;
newCharStyle.CharacterFormat.Italic = true;
newCharStyle.CharacterFormat.Underline = Underline.Single;
richTextBoxAdv.Document.Styles.Add(newCharStyle);
```

**Placeholders**
- `NewChar` → Replace with `{styleName}`
- `Calibri Light` → Replace with `{fontFamily}`
- `16d` → Replace with `{fontSize}`
- `Color.FromRgb(47, 84, 150)` → Replace with `{fontColor}`
- `true` (Bold / Italic) → Replace with `{bold}` / `{italic}`
- `Underline.Single` → Replace with `{underline}`
---

## Create Paragraph Style

```csharp
ParagraphStyle newParaStyle = new ParagraphStyle();
newParaStyle.Name = "NewPara";
newParaStyle.CharacterFormat.FontSize = 16d;
newParaStyle.CharacterFormat.FontFamily = new FontFamily("Calibri Light");
 newParaStyle.CharacterFormat.FontColor = Color.FromRgb(47, 84, 150);

newParaStyle.ParagraphFormat.BeforeSpacing = 12d;
newParaStyle.ParagraphFormat.LineSpacing = 1.07d;
newParaStyle.ParagraphFormat.LineSpacingType = LineSpacingType.Multiple;
richTextBoxAdv.Document.Styles.Add(newParaStyle);
```

**Placeholders**
- `NewPara` → Replace with `{styleName}`
- `Calibri Light` → Replace with `{fontFamily}`
- `16d` → Replace with `{fontSize}` 
- `1.07d` → Replace with `{lineSpacing}`
- `Color.FromRgb(47, 84, 150)` → Replace with `{fontColor}`
- `12d` → Replace with `{beforeSpacing}`
- `LineSpacingType.Multiple` → Replace with `{lineSpacingType}`
---

## Create Table Style

```csharp
TableStyle tableGridStyle = new TableStyle();
tableGridStyle.Name = "Table Grid";

tableGridStyle.TableFormat.LeftIndent = 0;
tableGridStyle.TableFormat.TopMargin = 0;
tableGridStyle.TableFormat.LeftMargin = 7.2;
tableGridStyle.TableFormat.RightMargin = 7.2;
tableGridStyle.TableFormat.BottomMargin = 0;

tableGridStyle.ParagraphFormat.AfterSpacing = 0;
tableGridStyle.ParagraphFormat.LineSpacing = 1;
tableGridStyle.ParagraphFormat.LineSpacingType = LineSpacingType.Multiple;
tableGridStyle.TableFormat.LeftIndent = 0;

tableGridStyle.TableFormat.Borders.Left.LineStyle = LineStyle.Single;
tableGridStyle.TableFormat.Borders.Left.LineWidth = 0.5;
tableGridStyle.TableFormat.Borders.Left.Color = Colors.Black;

tableGridStyle.TableFormat.Borders.Top.LineStyle = LineStyle.Single;
tableGridStyle.TableFormat.Borders.Top.LineWidth = 0.5;
tableGridStyle.TableFormat.Borders.Top.Color = Colors.Black;

tableGridStyle.TableFormat.Borders.Right.LineStyle = LineStyle.Single;
tableGridStyle.TableFormat.Borders.Right.LineWidth = 0.5;
tableGridStyle.TableFormat.Borders.Right.Color = Colors.Black;

tableGridStyle.TableFormat.Borders.Bottom.LineStyle = LineStyle.Single;
tableGridStyle.TableFormat.Borders.Bottom.LineWidth = 0.5;
tableGridStyle.TableFormat.Borders.Bottom.Color = Colors.Black;

tableGridStyle.TableFormat.Borders.Horizontal.LineStyle = LineStyle.Single;
tableGridStyle.TableFormat.Borders.Horizontal.LineWidth = 0.5;

tableGridStyle.TableFormat.Borders.Vertical.LineStyle = LineStyle.Single;
tableGridStyle.TableFormat.Borders.Vertical.LineWidth = 0.5;
richTextBoxAdv.Document.Styles.Add(tableGridStyle);
```

**Placeholders**
- `Table Grid` → Replace with `{styleName}`
- `0 (LeftIndent)` → Replace with `{leftIndent}`
- `TopMargin = 0` / `LeftMargin = 7.2` / `RightMargin = 7.2` / `BottomMargin = 0` → Replace with `{topMargin}` / `{leftMargin}` / `{rightMargin}` / `{bottomMargin}`
- `0 (AfterSpacing)` → Replace with `{afterSpacing}`
- `1` → Replace with `{lineSpacing}`
- `LineSpacingType.Multiple` → Replace with `{lineSpacingType}`
- `LineStyle.Single` → Replace with `{borderLineStyle}`
- `0.5` → Replace with `{borderLineWidth}`
- `Colors.Black` → Replace with `{borderColor}`

---

## Create Linked Style

```csharp
ParagraphStyle linkedParaStyle = new ParagraphStyle();
linkedParaStyle.Name = "NewPara";
linkedParaStyle.BaseStyleName = "Normal";
linkedParaStyle.LinkStyleName = "NewLinkedChar";
linkedParaStyle.CharacterFormat.FontSize = 16d;
linkedParaStyle.CharacterFormat.FontFamily = new FontFamily("Calibri Light");
linkedParaStyle.CharacterFormat.FontColor = Color.FromRgb(47, 84, 150);

linkedParaStyle.ParagraphFormat.BeforeSpacing = 12d;
linkedParaStyle.ParagraphFormat.LineSpacing = 1.07d;
linkedParaStyle.ParagraphFormat.LineSpacingType = LineSpacingType.Multiple;
richTextBoxAdv.Document.Styles.Add(linkedParaStyle);
```

**Placeholders**
- `NewPara` → Replace with `{styleName}`
- `Normal` → Replace with `{baseStyleName}`
- `NewLinkedChar` → Replace with `{linkStyleName}`
- `16d` → Replace with `{fontSize}`
- `Calibri Light` → Replace with `{fontFamily}`
- `Color.FromRgb(47, 84, 150)` → Replace with `{fontColor}`
- `12d` → Replace with `{beforeSpacing}`
- `1.07d` → Replace with `{lineSpacing}`
- `LineSpacingType.Multiple` → Replace with `{lineSpacingType}`

---

## Create Style through dialog

```xaml
<Button Content="Create style" Command="Syncfusion:SfRichTextBoxAdv.ShowStyleDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

---

## Apply Style

```xaml
<Button Content="Apply style" Command="Syncfusion:SfRichTextBoxAdv.ApplyStyleCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" CommandParameter="Heading 1"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

**Placeholders**
- `"Heading 1"` → Replace with `{styleName}`

---

## Get Styles

```csharp
 private DocumentStyle GetStyle(SfRichTextBoxAdv richTextBoxAdv, string styleName)
        {
            foreach (DocumentStyle style in richTextBoxAdv.Document.Styles)
            {
                if (style.Name == styleName)
                {
                    return style;
                }
            }
            return null;
        }
```
---

## Modify an existing style

```xaml
 <Button Content="Modify style" Command="Syncfusion:SfRichTextBoxAdv.ShowStylesDialogCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}"></Button>

 <syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
---

## Clear Formatting

```xaml
<Button Content="Clear formatting" Command="Syncfusion:SfRichTextBoxAdv.ClearFormattingCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}"></Button>

 <syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
---