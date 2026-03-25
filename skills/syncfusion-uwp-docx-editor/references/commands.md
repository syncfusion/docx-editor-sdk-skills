# Commands in UWP DOCX Editor

The Syncfusion UWP DOCX Editor provides a comprehensive set of routed UI commands for document editing, formatting, navigation, and document operations.

---

## How to use commands

For example, the Bold command — shown below — demonstrates how to use a command in XAML and in code-behind; follow this pattern for other available commands.

### XAML
```xaml
<!-- Bind Button to BoldCommand on the richTextBoxAdv instance -->
<Button Content="Bold" Command="{Binding ElementName=richTextBoxAdv, Path=BoldCommand, Mode=TwoWay}" />

<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
// Execute BoldCommand on the SfRichTextBoxAdv instance
richTextBoxAdv.BoldCommand.Execute(null);

// Execute TextAlignmentCommand with parameter
richTextBoxAdv.TextAlignmentCommand.Execute(TextAlignment.Right);
```

---

## Character formatting

| Command | Description | Parameter |
| --- | --- | --- |
| `BoldCommand` | Toggle bold for selected text | None |
| `ItalicCommand` | Toggle italic for selected text | None |
| `UnderlineCommand` | Apply underline for selected text | `Underline` |
| `StrikeThroughCommand` | Apply strike-through for selected text | `StrikeThrough` |
| `BaselineAlignmentCommand` | Apply baseline alignment (subscript/superscript) | `BaselineAlignment` |
| `FontFamilyCommand` | Apply font family | `FontFamily` |
| `FontSizeCommand` | Apply font size | `double` (font size) |
| `FontColorCommand` | Apply font color | `Color` |
| `HighlightColorCommand` | Apply highlight color | `Highlight Color` value |

---

## Paragraph formatting

| Command | Description | Parameter |
| --- | --- | --- |
| `TextAlignmentCommand` | Apply paragraph alignment | `TextAlignment` |
| `LeftIndentCommand` | Set left indent | `double` (value)  |
| `RightIndentCommand` | Set right indent | `double` (value)  |
| `IncreaseIndentCommand` | Increase paragraph indent | None |
| `DecreaseIndentCommand` | Decrease paragraph indent | None |
| `LineSpacingCommand` | Set line spacing | `double` (value)  |
| `LineSpacingTypeCommand` | Set line spacing type | `LineSpacingType` |
| `BeforeSpacingCommand` | Set spacing before paragraph | `double` |
| `AfterSpacingCommand` | Set spacing after paragraph | `double` |

---

## Clipboard

| Command | Description | Parameter |
| --- | --- | --- |
| `CopyCommand` | Copy selection to clipboard | None |
| `CutCommand` | Cut selection to clipboard | None |
| `PasteCommand` | Paste clipboard synchronously | None |
| `PasteAsyncCommand` | Paste clipboard asynchronously | None |

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
| `DeleteAllCommentsCommand` | Remove all comments | None |
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
| `MergeSelectedCellsCommand` | Merge selected cells | None |
| `SelectCellCommand` | Select a specific cell | None |
| `SelectRowCommand` | Select whole row | None |
| `SelectColumnCommand` | Select whole column | None |
| `SelectTableCommand` | Select the entire table | None |
| `TableAlignmentCommand` | Apply table alignment | `TableAlignment` |
| `TableLeftIndentCommand` | Set left indent for table | `double` (value) |
| `AutoFitTableCommand` | Auto-fit table columns | `AutoFitType` |
| `CellContentAlignmentCommand` | Set cell content alignment | alignment value (e.g., "Top,Left") |
| `CellTopMarginCommand` | Set cell top margin | `double` (value) |
| `CellBottomMarginCommand` | Set cell bottom margin | `double` (value) |
| `CellLeftMarginCommand` | Set cell left margin | `double` (value)|
| `CellRightMarginCommand` | Set cell right margin | `double` (value) |
| `CellSpacingCommand` | Set cell spacing | `double` (value) |
| `CellVerticalAlignmentCommand` | Set cell vertical alignment | alignment value |
| `DefaultCellTopMarginCommand` | Set default top margin for table cells | `double` (value) |
| `DefaultCellBottomMarginCommand` | Set default bottom margin for table cells | `double` (value) |
| `DefaultCellLeftMarginCommand` | Set default left margin for table cells | `double` (value) |
| `DefaultCellRightMarginCommand` | Set default right margin for table cells | `double` (value) |

---

## UI / Dialog / Pane commands

| Command | Description | Parameter |
| --- | --- | --- |
| `ShowHyperlinkDialogCommand` | Show hyperlink dialog | None |
| `ShowOptionsPaneCommand` | Show options pane | None |
| `ShowSpellingPaneCommand` | Show the spelling pane | None |

---

## Navigation / Key handling

| Command | Description | Parameter |
| --- | --- | --- |
| `EnterKeyCommand` | Handles Enter key action | None |
| `DeleteCommand` | Handles Delete key action | None |

---

## Insert / Hyperlink / Picture

| Command | Description | Parameter |
| --- | --- | --- |
| `InsertHyperlinkCommand` | Insert a hyperlink at selection | hyperlink object/string |
| `RemoveHyperlinkCommand` | Remove the selected hyperlink | None |
| `InsertPictureCommand` | Insert picture at selection | image/object |
| `CopyHyperlinkCommand` | Copy hyperlink to clipboard | None |
| `InsertBreakCommand` | Insert break at selection | break type |

---

## Spelling / Proofing

| Command | Description | Parameter |
| --- | --- | --- |
| `CheckSpellingCommand` | Run spelling check on document | None |
| `ChangeSpellingCommand` | Change selected misspelled word | replacement word |
| `ChangeAllSpellingCommand` | Replace all occurrences of a misspelled word | replacement word |
| `IgnoreAllSpellingErrorsCommand` | Ignore occurrences of a misspelled word | word to ignore |

---

## Other commands

| Command | Description | Parameter |
| --- | --- | --- |
| `PageFitCommand` | Set page fit mode for viewer | `PageFitType` |
| `LayoutTypeCommand` | Switch layout type (Pages/Flow) | `LayoutType` |
| `AddToDictionaryCommand` | Add custom word to dictionary | `string` |
| `SelectAllCommand` | Select all content | None |

---