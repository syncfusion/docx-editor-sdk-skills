# Find and Replace in UWP DOCX Editor

Find and replace support in the Syncfusion UWP DOCX Editor allows searching and replacing text within documents using built‑in APIs and commands.

---

## Show Find and Replace Pane


### XAML
```xaml
<!-- Bind the button to the control command that shows the options pane. -->
<Button Content="Show Options Pane" Command="{Binding ElementName=richTextBoxAdv, Path=ShowOptionsPaneCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
richTextBoxAdv.ShowOptionsPaneCommand.Execute(richTextBoxAdv);
```

---

## Find immediate occurrence

```csharp

// Finds the first occurrence of the specified text (from the current selection).
TextSearchResult textSearchResult = richTextBoxAdv.Find("Panda", FindOptions.CaseSensitive);

// Find using a regular expression pattern
TextSearchResult regexResult = richTextBoxAdv.Find(new Regex(@"\bS\S*"), FindOptions.CaseSensitive);

// Note: The second parameter is optional and specifies find options.
// Possible values: 'None' | 'WholeWord' | 'CaseSensitive' | 'CaseSensitiveWholeWord'.
```

**Placeholders**
- `"Panda"` → Replace with `{searchText}`
- `FindOptions.CaseSensitive` → Replace with `{findOptions}`
- `new Regex(@"\bS\S*")` → Replace with `{regexPattern}`

---

## Find all occurrences

```csharp
// Finds all the occurrence of the specified text in the document.
TextSearchResults textSearchResults = richTextBoxAdv.FindAll("Panda", FindOptions.CaseSensitive);

// Find all the occurrence using  a regular expression pattern 
TextSearchResults regexResults = richTextBoxAdv.FindAll(new Regex(@"\bS\S*"), FindOptions.None);

// Note: The second parameter is optional and specifies find options.
// Possible values: 'None' | 'WholeWord' | 'CaseSensitive' | 'CaseSensitiveWholeWord'.
```

**Placeholders**
- `"Panda"` → Replace with `{searchText}`
- `FindOptions.CaseSensitive` / `FindOptions.None` → Replace with `{findOptions}`
- `new Regex(@"\bS\S*")` → Replace with `{regexPattern}`

---

## Replace

```csharp
// Finds the text "colour" that matches whole word in the document.
TextSearchResult textSearchResult = richTextBoxAdv.Find("colour", FindOptions.WholeWord);

// If any text search result found, replace it with the text "color".
if (textSearchResult != null)
    textSearchResult.Replace("color");
```

**Placeholders**
- `"colour"` → Replace with `{searchText}`
- `FindOptions.WholeWord` → Replace with `{findOptions}`
- `"color"` → Replace with `{replacementText}`

---

## Replace All

```csharp
// Finds the text "analyse" that matches whole word in the document.
TextSearchResults textSearchResults = richTextBoxAdv.FindAll("analyse", FindOptions.WholeWord);

// If any text search results found, replace all occurrences with the text "analyze".
if(textSearchResults != null)
    textSearchResults.ReplaceAll("analyze");
```

**Placeholders**
- `"analyse"` → Replace with `{searchText}`
- `FindOptions.WholeWord` → Replace with `{findOptions}`
- `"analyze"` → Replace with `{replacementText}`


## Select the search result
```csharp
// Finds the first occurrence of the specified text from the current selection.
TextSearchResult textSearchResult = richTextBoxAdv.Find("Panda", FindOptions.CaseSensitive);

// Select the found text in the editor.
richTextBoxAdv.Selection.Select(textSearchResult.Start, textSearchResult.End);
```

**Placeholders**
- `"Panda"` → Replace with `{searchText}`
- `FindOptions.CaseSensitive` → Replace with `{findOptions}`
- `textSearchResult.Start` → Replace with `{startPosition}`
- `textSearchResult.End` → Replace with `{endPosition}`

## Format the search result
```csharp
// Finds the first occurrence of the specified text from the current selection.
TextSearchResult textSearchResult = richTextBoxAdv.Find("Panda", FindOptions.CaseSensitive);

// Select the found text in the editor.
richTextBoxAdv.Selection.Select(textSearchResult.Start, textSearchResult.End);

// Apply bold formatting to the current selection.
richTextBoxAdv.Selection.CharacterFormat.Bold = true;
```

**Placeholders**
- `"Panda"` → Replace with `{searchText}`
- `FindOptions.CaseSensitive` → Replace with `{findOptions}`
- `textSearchResult.Start` → Replace with `{startPosition}`
- `textSearchResult.End` → Replace with `{endPosition}`
- `true` / `false` → Replace with `{boldValue}`

## Select all search results
```csharp
// Finds all words that start with 'S' in the SfRichTextBoxAdv document.
TextSearchResults textSearchResults = richTextBoxAdv.FindAll(new Regex(@"\bS\S*"), FindOptions.None);

// If any text search results are found, add each result range to the selection.
if (textSearchResults != null)
{
    for (int j = 0; j < textSearchResults.Count; j++)
    {
        TextSearchResult textSearchResult = textSearchResults[j];

        // Add the search result text range to the selection.
        richTextBoxAdv.Selection.SelectionRanges.Add(textSearchResult.Start, textSearchResult.End);
    }
}
```

**Placeholders**
- `new Regex(@"\bS\S*")` → Replace with `{regexPattern}`
- `FindOptions.None` → Replace with `{findOptions}`
- `textSearchResult.Start` → Replace with `{startPosition}`
- `textSearchResult.End` → Replace with `{endPosition}`

## Format all the search results
```csharp
// Finds all words that start with 'S' in the SfRichTextBoxAdv document.
TextSearchResults textSearchResults = richTextBoxAdv.FindAll(new Regex(@"\bS\S*"), FindOptions.None);

// If any text search results are found, add each result range to the selection.
if (textSearchResults != null)
{
    for (int j = 0; j < textSearchResults.Count; j++)
    {
        TextSearchResult textSearchResult = textSearchResults[j];

        // Add the search result text range to the selection.
        richTextBoxAdv.Selection.SelectionRanges.Add(textSearchResult.Start, textSearchResult.End);
    }

    // Apply highlight color to the current selection.
    richTextBoxAdv.Selection.CharacterFormat.HighlightColor = HighlightColor.Yellow;
}
```

**Placeholders**
- `HighlightColor.Yellow` → Replace with `{highlightColor}`