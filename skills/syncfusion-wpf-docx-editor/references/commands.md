# Commands in WPF DOCX Editor

The Syncfusion WPF DOCX Editor provides a comprehensive set of routed UI commands for document editing, formatting, navigation, and document operations.

---

## How to use commands 

For example, the Copy command — shown below — demonstrates how to use a command in XAML and in code-behind; follow this pattern for other available commands.

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


## Character formatting

| Command | Description | Parameter |
| --- | --- | --- |
| `BoldCommand` | Toggle bold for selected text | None |
| `ItalicCommand` | Toggle italic for selected text | None |
| `UnderlineCommand` | Apply underline style | `Underline` value |
| `ToggleUnderlineCommand` | Toggle underline for selected text | `Underline` value |
| `StrikeThroughCommand` | Apply strike-through | `strike-through` value |
| `BaselineAlignmentCommand` | Apply baseline alignment (subscript/superscript) | `BaselineAlignment` value |
| `FontFamilyCommand` | Apply font family | `FontFamily` |
| `FontSizeCommand` | Apply font size | `double` (font size) |
| `DecreaseFontSizeCommand` | Decrease font size | `double` (font size) |
| `IncreaseFontSizeCommand` | Increase font size | `double` (font size) |
| `FontColorCommand` | Apply font color | `Color` |
| `HighlightColorCommand` | Apply highlight color | `Highlight Color` value |
| `ToggleHighlightColorCommand` | Toggle highlight color | None |

---

## Paragraph formatting

| Command | Description | Parameter |
| --- | --- | --- |
| `TextAlignmentCommand` | Apply paragraph alignment | `TextAlignment` (Left/Center/Right/Justify) |
| `LeftIndentCommand` | Set left indent | `double` (value) |
| `RightIndentCommand` | Set right indent | `double` (value) |
| `FirstLineIndentCommand` | Set first-line indent | `double` (value) |
| `IncreaseIndentCommand` | Increase paragraph indent | None |
| `DecreaseIndentCommand` | Decrease paragraph indent | None |
| `LineSpacingCommand` | Set line spacing | `double` (value) |
| `LineSpacingTypeCommand` | Set line spacing type | `LineSpacingType` |
| `BeforeSpacingCommand` | Set spacing before paragraph | `double` |
| `AfterSpacingCommand` | Set spacing after paragraph | `double` |
| `ToggleBeforeSpacingCommand` | Toggle before spacing | None |

---

## Lists (change/insert/clear)

| Command | Description | Parameter |
| --- | --- | --- |
| `ShowListDialogCommand` | Show list dialog | None |
| `ApplyStyleCommand` | Apply named style (can change list styles) | `string` (style name) |
| `ClearFormattingCommand` | Remove formatting (list included if applied via formatting) | None |

---

## Clipboard

| Command | Description | Parameter |
| --- | --- | --- |
| `CopyCommand` | Copy selection to clipboard | None |
| `CutCommand` | Cut selection to clipboard | None |
| `PasteCommand` | Paste clipboard at caret | None |

---

## History

| Command | Description | Parameter |
| --- | --- | --- |
| `UndoCommand` | Undo last edit | None |
| `RedoCommand` | Redo last undone edit | None |

---

## Import / Export / Document operations

| Command | Description | Parameter |
| --- | --- | --- |
| `OpenDocumentCommand` | Open an existing document | None |
| `SaveDocumentCommand` | Save current document | None |
| `SaveAsDocumentCommand` | Save document with new name | None |
| `NewDocumentCommand` | Create a new document | None |
| `PrintDocumentCommand` | Print current document | None |

---

## Comments

| Command | Description | Parameter |
| --- | --- | --- |
| `NewCommentCommand` | Add a comment at selection | None |
| `DeleteCommentCommand` | Delete selected comment | None |
| `DeleteAllCommentsCommand` | Remove all comments in document | None |
| `NextCommentCommand` | Navigate to next comment | None |
| `PreviousCommentCommand` | Navigate to previous comment | None |
| `ShowCommentsCommand` | Show/hide comments pane | None |

---

## Table commands

| Command | Description | Parameter |
| --- | --- | --- |
| `InsertTableCommand` | Insert table at selection | `rows,columns` |
| `InsertRowCommand` | Insert row in selected table | `RowPlacement` |
| `InsertColumnCommand` | Insert column in selected table | `ColumnPlacement` |
| `DeleteRowCommand` | Delete selected row | None |
| `DeleteColumnCommand` | Delete selected column | None |
| `DeleteTableCommand` | Delete selected table | None |
| `MergeSelectedCellsCommand` | Merge currently selected cells | None |
| `SelectCellCommand` | Select a specific cell | None |
| `SelectRowCommand` | Select whole row | None |
| `SelectColumnCommand` | Select whole column | None |
| `SelectTableCommand` | Select the entire table | None |
| `TableAlignmentCommand` | Apply table alignment | `TableAlignment` value |
| `TableLeftIndentCommand` | Set left indent for table | `double` |

---

## UI / Dialog / Pane commands

| Command | Description | Parameter |
| --- | --- | --- |
| `ShowFontDialogCommand` | Show font selection dialog | None |
| `ShowParagraphDialogCommand` | Show paragraph dialog | None |
| `ShowFindAndReplaceDialogCommand` | Show find/replace dialog | `bool` (show find or replace tab) |
| `ShowTableDialogCommand` | Show table dialog | None |
| `ShowInsertTableDialogCommand` | Show insert-table dialog | None |
| `ShowHyperlinkDialogCommand` | Show hyperlink dialog | None |
| `ShowListDialogCommand` | Show list dialog | None |
| `ShowOptionsPaneCommand` | Show options pane | None |

---

## Navigation / Key handling commands

| Command | Description | Parameter |
| --- | --- | --- |
| `LeftKeyCommand`, `RightKeyCommand`, `UpKeyCommand`, `DownKeyCommand` | Handle arrow navigation | None |
| `HomeKeyCommand`, `EndKeyCommand`, `PageUpKeyCommand`, `PageDownKeyCommand` | Handle navigation keys | None |
| `ControlLeftKeyCommand`, `ControlRightKeyCommand`, `ControlUpKeyCommand`, `ControlDownKeyCommand` | Ctrl+arrow navigation | None |
| `ControlShiftDownKeyCommand`, `ControlShiftEndKeyCommand`, `ControlShiftHomeKeyCommand`, `ControlShiftLeftKeyCommand`, `ControlShiftRightKeyCommand`, `ControlShiftUpKeyCommand` | Performs selection for CTRL + SHIFT + *   keys. | None |
|  `ShiftDownKeyCommand`, `ShiftEndKeyCommand`, `ShiftEnterKeyCommand`, `ShiftHomeKeyCommand`, `ShiftLeftKeyCommand`, `ShiftRightKeyCommand`, `ShiftTabKeyCommand`, `ShiftUpKeyCommand` | Performs selection for SHIFT + *   keys. | None |
| `EnterKeyCommand`, `ShiftEnterKeyCommand`, `TabKeyCommand`, `ShiftTabKeyCommand`, `SpaceKeyCommand`, `BackSpaceKeyCommand`, `DeleteKeyCommand` | Key handling commands | None |

---

## Insert / Hyperlink / Picture

| Command | Description | Parameter |
| --- | --- | --- |
| `InsertHyperlinkCommand` | Insert a hyperlink at selection | Hyperlink to be inserted |
| `RemoveHyperlinkCommand` | Remove the selected hyperlink | None |
| `InsertPictureCommand` | Insert picture at selection | Picture to be inserted |
| `NavigateHyperlinkCommand` | Invoke navigation for selected hyperlink | None |

---

## Spelling / Proofing

| Command | Description | Parameter |
| --- | --- | --- |
| `CheckSpellingCommand` | Run spelling check on document | None |
| `ChangeSpellingCommand` | Change selected misspelled word | The word to be replaced |
| `ChangeAllSpellingCommand` | Replace all occurrences of a misspelled word | The word to be replaced |
| `IgnoreAllSpellingErrorsCommand` | Ignore all occurrences of a misspelled word | word to ignore |

---

## Other commands

| Command | Description | Parameter |
| --- | --- | --- |
| `PageFitCommand` | Set page fit mode for the viewer | `PageFitType` |
| `LayoutTypeCommand` | Switch layout type (Pages/Flow) | `LayoutType` |
| `ApplyStyleCommand` | Apply named style to paragraph | `string` (style name) |
| `ClearFormattingCommand` | Remove formatting from selection | None |
| `AddToDictionaryCommand` | Add custom word to dictionary | `string` (word) |

---