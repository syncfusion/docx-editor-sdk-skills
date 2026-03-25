# Character Formatting in UWP DOCX Editor

Character formatting support in the Syncfusion UWP DOCX Editor allows applying and retrieving character‑level text formatting using the `Selection.CharacterFormat` API.

---

## Insert Text (API)

```csharp
// Insert text at current cursor
richTextBoxAdv.Selection.InsertText("Hello World");
```

**Placeholders**
- `"Hello World"` → Replace with `{textToInsert}`

---

## Bold

```csharp
// set Bold
richTextBoxAdv.Selection.CharacterFormat.Bold = true;

// get Bold
 bool? isBold = richTextBoxAdv.Selection.CharacterFormat.Bold;
```

**Placeholders**
- `"true"` / `"false"` → Replace with `{boldValue}`

---

## Italic

```csharp
// set Italic
richTextBoxAdv.Selection.CharacterFormat.Italic = true;

// get Italic
bool? isItalic = richTextBoxAdv.Selection.CharacterFormat.Italic;
```

**Placeholders**
- `true` / `false` → Replace with `{italicValue}`

---

## Underline

```csharp
// Set Underline
richTextBoxAdv.Selection.CharacterFormat.Underline = Underline.Single; // 'Single' | 'None'

// Get Underline
Underline? underline =  richTextBoxAdv.Selection.CharacterFormat.Underline;
```

**Placeholders**
- `Underline.Single` / `Underline.None` → Replace with `{underlineStyle}`

---

## Strikethrough

```csharp
// Set Strikethrough
richTextBoxAdv.Selection.CharacterFormat.StrikeThrough = StrikeThrough.SingleStrike; // 'SingleStrike' | 'DoubleStrike' | 'None'

// Get Strikethrough
StrikeThrough? strikeThrough = richTextBoxAdv.Selection.CharacterFormat.StrikeThrough;
```

**Placeholders**
- `StrikeThrough.SingleStrike` / `StrikeThrough.DoubleStrike` / `StrikeThrough.None` → Replace with `{strikeThroughStyle}`

---

## Superscript / Subscript

```csharp
//Set Superscript
richTextBoxAdv.Selection.CharacterFormat.BaselineAlignment = BaselineAlignment.Superscript;

//Set Subscript
richTextBoxAdv.Selection.CharacterFormat.BaselineAlignment = BaselineAlignment.Subscript;

//Get baseline alignment
BaselineAlignment? baselineAlignment = richTextBoxAdv.Selection.CharacterFormat.BaselineAlignment;
```

**Placeholders**
- `BaselineAlignment.Superscript` / `BaselineAlignment.Subscript` → Replace with `{baselineAlignment}`

---

## Font Size

```csharp
//Set Font size
richTextBoxAdv.Selection.CharacterFormat.FontSize = 24;

//Get Font size
double fontSize = richTextBoxAdv.Selection.CharacterFormat.FontSize;
```

**Placeholders**
- `24` → Replace with `{fontSize}`

---

## Font Family

```csharp
//Set Font family
richTextBoxAdv.Selection.CharacterFormat.FontFamily = new FontFamily("Arial");

//Get Font family
FontFamily fontSize = richTextBoxAdv.Selection.CharacterFormat.FontFamily;
```

**Placeholders**
- `"Arial"` → Replace with `{fontFamily}`

---

## Font Color

```csharp
//Set Font color
richTextBoxAdv.Selection.CharacterFormat.FontColor = Colors.Red;

//Get Font color
Color? fontColor = richTextBoxAdv.Selection.CharacterFormat.FontColor;
```

**Placeholders**
- `Colors.Red` → Replace with `{fontColor}`

---

## Highlight Color

```csharp
//Set Highlight color
richTextBoxAdv.Selection.CharacterFormat.HighlightColor = HighlightColor.Yellow;

//Get Highlight color
HighlightColor? highlightColor = richTextBoxAdv.Selection.CharacterFormat.HighlightColor;
```

**Placeholders**
- `HighlightColor.Yellow` → Replace with `{highlightColor}`

---

## Clear Formatting

```csharp
 SfRichTextBoxAdv.ClearFormattingCommand.Execute(richTextBoxAdv);
```

---
