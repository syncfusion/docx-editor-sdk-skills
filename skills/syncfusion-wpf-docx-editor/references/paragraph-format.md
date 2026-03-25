# Paragraph Formatting in WPF DOCX Editor

Paragraph formatting support in the Syncfusion WPF DOCX Editor allows controlling paragraph layout and text flow within documents.


---

## Set Indentation

```csharp
richTextBoxAdv.Selection.ParagraphFormat.LeftIndent = 24;

richTextBoxAdv.Selection.ParagraphFormat.RightIndent = 30;
```

**Placeholders**
- `24` → Replace with `{leftIndent}`
- `30` → Replace with `{rightIndent}`

---

## First Line Indent

```csharp
richTextBoxAdv.Selection.ParagraphFormat.FirstLineIndent = 24;
```

**Placeholders**
- `24` → Replace with `{firstLineIndent}`

---

## Increase / Decrease Indent

```csharp
SfRichTextBoxAdv.IncreaseIndentCommand.Execute("24", richTextBoxAdv);

SfRichTextBoxAdv.DecreaseIndentCommand.Execute("24", richTextBoxAdv);   
```

**Placeholders**
- `"24"` → Replace with `{indentAmount}`

---

## Set Alignment

```csharp
richTextBoxAdv.Selection.ParagraphFormat.TextAlignment = TextAlignment.Center; // 'Left' | 'Right' | 'Justify'
```

**Placeholders**
- `TextAlignment.Center` → Replace with `{textAlignment}`

---

## Line Spacing

```csharp
richTextBoxAdv.Selection.ParagraphFormat.LineSpacingType = LineSpacingType.Exactly; // 'AtLeast' | 'Multiple'

richTextBoxAdv.Selection.ParagraphFormat.LineSpacing = 6;
```

**Placeholders**
- `LineSpacingType.Exactly` → Replace with `{lineSpacingType}`
- `6` → Replace with `{lineSpacing}`

---

## Paragraph Spacing

```csharp
richTextBoxAdv.Selection.ParagraphFormat.AfterSpacing = 24;

richTextBoxAdv.Selection.ParagraphFormat.BeforeSpacing = 24;
```

**Placeholders**
- `24` (AfterSpacing) → Replace with `{afterSpacing}`
- `24` (BeforeSpacing) → Replace with `{beforeSpacing}`


## Paragraph Right to Left direction

```csharp
//  Defines the right-to-left direction for the paragraph.
richTextBoxAdv.Selection.ParagraphFormat.Bidi = true;
```

**Placeholders**
- `true` / `false` → Replace with `{bidi}`

---