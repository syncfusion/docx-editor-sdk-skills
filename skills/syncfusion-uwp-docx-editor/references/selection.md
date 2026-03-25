# Selection in UWP DOCX Editor

Selection support in the Syncfusion UWP DOCX Editor allows selecting, navigating, and manipulating document content within the editor.

---

## Manage selection brush color

```csharp
richTextBoxAdv.SelectionBrush = new SolidColorBrush(Color.FromArgb(0xFF, 0x00, 0x00, 0xFF));
```

**Placeholders**
- `new SolidColorBrush(Color.FromArgb(0xFF, 0x00, 0x00, 0xFF))` → Replace with `{selectionBrush}`
- `Color.FromArgb(0xFF, 0x00, 0x00, 0xFF)` → Replace with `{selectionColor}`

---

## Retrieve text position from document using paragraph and offset value

```csharp
// Gets the first block from the section, which is a paragraph.
ParagraphAdv paragraphAdv = sectionAdv.Blocks[0] as ParagraphAdv;

// Gets the text position of the specified paragraph at offset 24. 
// TextPosition is returned as null, if no such paragraph or offset exists in the document.
TextPosition startPosition = richTextBoxAdv.Document.GetTextPosition(paragraphAdv, 24);
```

**Placeholders**

- `0` → Replace with `{blockIndex}`
- `24` → Replace with `{offset}`

---

## Retrieve text position from document using table's paragraph and offset value

```csharp
// Gets the third block of a section, which is table.
TableAdv tableAdv = sectionAdv.Blocks[2] as TableAdv;

// Gets the third block from second row second cell of the table, which is paragraph.
ParagraphAdv paragraphAdv = tableAdv.Rows[1].Cells[1].Blocks[2] as ParagraphAdv;
TextPosition position = richTextBoxAdv.Document.GetTextPosition(paragraphAdv, 12);
```

**Placeholders**

- `2` → Replace with `{tableBlockIndex}`
- `1` (Rows index) → Replace with `{rowIndex}`
- `1` (Cells index) → Replace with `{cellIndex}`
- `2` (Blocks index) → Replace with `{blockIndex}`
- `12` → Replace with `{offset}`

---

## Move selection to particular position

```csharp
// Retrieves the position of the first paragraph start.
TextPosition startPosition = richTextBoxAdv.Document.GetTextPosition("0;0;0");

// Retrieves the position of the first paragraph at offset=20.
TextPosition endPosition = richTextBoxAdv.Document.GetTextPosition("0;0;20");

// Selects the text positions in forward direction.
richTextBoxAdv.Selection.Select(startPosition, endPosition);
```

**Placeholders**

- `"0;0;0"` / `"0;0;20"` → Replace with `{hierarchicalIndex}` *(format: `"sectionIndex;paragraphIndex;offset"`)*
- `startPosition` → Replace with `{startTextPosition}`
- `endPosition` → Replace with `{endTextPosition}`

---

## Multiple selection

```csharp
// Retrieves the position of the first paragraph start.
TextPosition startPosition1 = richTextBoxAdv.Document.GetTextPosition("0;0;0");

// Retrieves the position of the first paragraph at offset=20.
TextPosition endPosition1 = richTextBoxAdv.Document.GetTextPosition("0;0;20");

// Retrieves the position of the third paragraph start.
TextPosition startPosition2 = richTextBoxAdv.Document.GetTextPosition("0;2;0");

// Retrieves the position of the third paragraph at offset=20.
TextPosition endPosition2 = richTextBoxAdv.Document.GetTextPosition("0;2;20");

// Selects the first paragraph and third paragraph at a time, leaving second paragraph.
richTextBoxAdv.Selection.SelectionRanges.Add(startPosition1, endPosition1);
richTextBoxAdv.Selection.SelectionRanges.Add(startPosition2, endPosition2);
```

**Placeholders**

- `"0;0;0"` / `"0;0;20"` / `"0;2;0"` / `"0;2;20"` → Replace with `{hierarchicalIndex}` *(format: `"sectionIndex;paragraphIndex;offset"`)*
- `startPosition1` / `startPosition2` → Replace with `{startTextPosition}`
- `endPosition1` / `endPosition2` → Replace with `{endTextPosition}`

---

## Apply Formatting for selection

```csharp
// Applies character format for the selected text contents.
richTextBoxAdv.Selection.CharacterFormat.BaselineAlignment = Syncfusion.UI.Xaml.RichTextBoxAdv.BaselineAlignment.Subscript;

// Applies paragraph format for the selected paragraphs.
richTextBoxAdv.Selection.ParagraphFormat.AfterSpacing = 24;

// Applies page margin for the selected sections.
richTextBoxAdv.Selection.SectionFormat.PageMargin = new Thickness(96, 48, 96, 48);
```

**Placeholders**
- `Syncfusion.UI.Xaml.RichTextBoxAdv.BaselineAlignment.Subscript` → Replace with `{baselineAlignment}`
- `24` → Replace with `{afterSpacing}`
- `new Thickness(96, 48, 96, 48)` → Replace with `{pageMargin}`

---

## Binding Selection format properties

The SfRichTextBoxAdv provides support to bind the rich-text format options of selection content.

### XAML
```xaml
<!-- Binds the toggle button to Selection bold character format -->
<ToggleButton x:Name="toggleButton" Content="Bold" IsChecked="{Binding Path=Selection.CharacterFormat.Bold, Mode=TwoWay, ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```


### C#
```csharp
// Initializes the new binding for toggle bold.
Binding binding = new Binding() { Source = richTextBoxAdv, Path = new PropertyPath("Selection.CharacterFormat.Bold"), Mode = BindingMode.TwoWay };

// Binds the IsChecked property to Selection.CharacterFormat.Bold property of RichTextBoxAdv.
toggleButton.SetBinding(ToggleButton.IsCheckedProperty, binding);
```

---

## Get the selection start and end

```csharp
//Retrieves the selection start position. 
TextPosition selectionStart = richTextBoxAdv.Selection.Start;

//Retrieves the selection end position.
TextPosition selectionEnd = richTextBoxAdv.Selection.End;
```

---

## Get the selection start and end hierarchical index

```csharp
//Retrieves the selection start position's HierarchicalIndex. 
string startHierarchicalIndex = richTextBoxAdv.Selection.Start.HierarchicalIndex;

//Retrieves the selection end position's HierarchicalIndex.
string endHierarchicalIndex = richTextBoxAdv.Selection.End.HierarchicalIndex;
```

---

## Move Selection to the word, paragraph , Line start and end

#### Move selection from the selection start
```csharp
//Gets the paragraph at which the start textposition lies.
ParagraphAdv selectionStartParagraph = richTextBoxAdv.Selection.Start.Paragraph;

// Moves the text position to the beginning of the next paragraph.
richTextBoxAdv.Selection.Start.MoveToNextParagraphStart();
// Moves the text position to the end of the previous paragraph.
richTextBoxAdv.Selection.Start.MoveToPreviousParagraphEnd();

// Moves the text position to the beginning of the paragraph.
richTextBoxAdv.Selection.Start.MoveToParagraphStart();
// Moves the text position to the end of the paragraph.
richTextBoxAdv.Selection.Start.MoveToParagraphEnd();

// Moves the text position to the beginning of the line.
richTextBoxAdv.Selection.Start.MoveToLineStart();
// Moves the text position to the end of the line.
richTextBoxAdv.Selection.Start.MoveToLineEnd();

// Moves the text position to the beginning of the word.
richTextBoxAdv.Selection.Start.MoveToWordStart();
// Moves the text position to the end of the word.
richTextBoxAdv.Selection.Start.MoveToWordEnd();
```

#### Move selection from the selection end
```csharp
// Gets the paragraph at which the end text position lies.
 ParagraphAdv selectionEndParagraph = richTextBoxAdv.Selection.End.Paragraph;

// Moves the text position to the beginning of the next paragraph.
 richTextBoxAdv.Selection.End.MoveToNextParagraphStart();
// Moves the text position to the end of the previous paragraph.
 richTextBoxAdv.Selection.End.MoveToPreviousParagraphEnd();

// Moves the text position to the beginning of the paragraph.
richTextBoxAdv.Selection.End.MoveToParagraphStart();
// Moves the text position to the end of the paragraph.
richTextBoxAdv.Selection.End.MoveToParagraphEnd();

// Moves the text position to the beginning of the line.
richTextBoxAdv.Selection.End.MoveToLineStart();
// Moves the text position to the end of the line.
richTextBoxAdv.Selection.End.MoveToLineEnd();

// Moves the text position to the beginning of the word.
richTextBoxAdv.Selection.End.MoveToWordStart();
// Moves the text position to the end of the word.
richTextBoxAdv.Selection.End.MoveToWordEnd();
 ```

 ### Select all in document
 ```csharp
//Select all the contents in the document.
richTextBoxAdv.SelectAllCommand.Execute(richTextBoxAdv);
 ```
---

## Get text from current selected content

 ```csharp
// To get the selected content as text
string selectedContentText = richTextBoxAdv.Selection.Text;
```

---


## Get the whole document content as text

 ```csharp
// To select all the content in document
richTextBoxAdv.SelectAllCommand.Execute(richTextBoxAdv);

// To get the content as text
string selectedContentText = richTextBoxAdv.Selection.Text;
```
---

## Identify whether two text positions denotes the same position

### Using Methods
 ```csharp
public bool IsAtSamePosition()
{
TextPosition position1 = richTextBoxAdv.Document.GetTextPosition("0;0;0");
ParagraphAdv paragraph = richTextBoxAdv.Document.Sections[0].Blocks[0] as ParagraphAdv;
TextPosition position2 = richTextBoxAdv.Document.GetTextPosition(paragraph, 0);

if (position1.IsAtSamePosition(position2))
    return true;

return false;
}
 ```
 
 **Placeholders**

- `"0;0;0"` → Replace with `{hierarchicalIndex}` *(format: `"sectionIndex;paragraphIndex;offset"`)*
- `0` (Sections index) / `0` (Blocks index) → Replace with `{sectionIndex}` / `{blockIndex}`
- `0` (offset) → Replace with `{offset}`
- `position1` → Replace with `{textPosition1}`
- `position2` → Replace with `{textPosition2}`


 ### Using Property
  ```csharp
bool isEmptySelection =  richTextBoxAdv.Selection.IsEmpty;
 ```
---


##  Identify whether two text positions lies in the same document.

 ```csharp
public bool IsInSameDocument()
{
TextPosition position1 = richTextBoxAdv.Document.GetTextPosition("0;4;2");
ParagraphAdv paragraph = richTextBoxAdv.Document.Sections[0].Blocks[0] as ParagraphAdv;
TextPosition position2 = richTextBoxAdv.Document.GetTextPosition(paragraph, 0);

if (position1.IsInSameDocument(position2))
    return true;

return false;
}
 ```
 
**Placeholders**
- `"0;4;2"` → Replace with `{hierarchicalIndex}` *(format: `"sectionIndex;paragraphIndex;offset"`)*
- `0` (Sections index) → Replace with `{sectionIndex}`
- `0` (Blocks index) → Replace with `{blockIndex}`
- `0` (offset) → Replace with `{offset}`
- `position1` → Replace with `{textPosition1}`
- `position2` → Replace with `{textPosition2}`
 
---

##  Delete the selected content.
### XAML
```xaml
<!-- Binds button to the DeleteCommand -->
<Button Content="Delete" Command="{Binding ElementName=richTextBoxAdv, Path=DeleteCommand, Mode=TwoWay}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
//Deletes the selected content in SfRichTextBoxAdv control.
bool isDeleted = richTextBoxAdv.Selection.Delete();
```
---


## Keyboard shortcuts to perform selection

### Navigation shortcuts
| Navigation Shortcut | Description |
| --- | --- |
| Right Arrow | Navigates one position forward. |
| Left Arrow | Navigates one position backward. |
| Down Arrow | Navigates to the same position on the next line. |
| Up Arrow | Navigates to the same position on the previous line. |
| Home | Navigates to the start of the current line. |
| End | Navigates to the end of the current line. |
| Ctrl + Home | Navigates to the document start position. |
| Ctrl + End | Navigates to the document end position. |
| Ctrl + Right | Navigates to the next word start position. |
| Ctrl + Left | Navigates to the current word start position. |
| Ctrl + Down | Navigates to the next paragraph start position. |
| Ctrl + Up | Navigates to the current paragraph start position. |

### Selection shortcuts

| Selection Shortcut | Description |
| --- | --- |
| Shift + Right Arrow | Extends selection one position forward. |
| Shift + Left Arrow | Extends selection one position backward. |
| Shift + Down Arrow | Extends selection to the same position on the next line. |
| Shift + Up Arrow | Extends selection to the same position on the previous line. |
| Shift + Home | Extends selection to the start of the current line. |
| Shift + End | Extends selection to the end of the current line. |
| Ctrl + Shift + Home | Extends selection to the document start position. |
| Ctrl + Shift + End | Extends selection to the document end position. |
| Ctrl + Shift + Right | Extends selection to the current word end position. |
| Ctrl + Shift + Left | Extends selection to the current word start position. |
| Ctrl + Shift + Down | Extends selection to the current paragraph end position. |
| Ctrl + Shift + Up | Extends selection to the current paragraph start position. |
| Ctrl + A | Selects the entire document. |

---

