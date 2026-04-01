# Find and Replace

Search for text, navigate results, and replace occurrences in documents using built-in UI and APIs.

## Open Options Pane

Display the built-in find and replace interface for users to search and replace interactively (keyboard shortcut: Ctrl+F).

```ts
this.$refs.documenteditor.showOptionsPane();
```

> **Note:** Press Esc to close the pane. The UI provides search, result navigation, and replace options without code.

## Find Next Occurrence

Search for the next instance of text from the current cursor position.

```ts
this.$refs.documenteditor.ej2Instances.search.find('{searchText}', '{findOptions}');
```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`
- `'None'` → Replace with `{findOptions}`

**Find Options:**
- `'None'` - Basic search
- `'WholeWord'` - Match whole words only
- `'CaseSensitive'` - Case-sensitive matching
- `'CaseSensitiveWholeWord'` - Both case-sensitive and whole word

## Find All Occurrences

Highlight all instances of text throughout the entire document in yellow.

```ts
this.$refs.documenteditor.ej2Instances.search.findAll('{searchText}', '{findOptions}');
```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`
- `'None'` → Replace with `{findOptions}`

## Replace All Occurrences

Replace every instance of the searched text with replacement text in a single operation.

```ts
this.$refs.documenteditor.ej2Instances.search.findAll('{searchText}');
this.$refs.documenteditor.ej2Instances.search.searchResults.replaceAll('{replacementText}');
```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`
- `'Mike'` → Replace with `{replacementText}`

## Replace One at a Time

Replace search results individually by navigating through matches and inserting text.

```ts
this.$refs.documenteditor.ej2Instances.search.findAll('{searchText}');
const searchLength = this.$refs.documenteditor.ej2Instances.search.searchResults.length;

for (let i = searchLength - 1; i >= 0; i--) {
  // Navigate to each result (iterate backward to preserve indices)
  this.$refs.documenteditor.ej2Instances.search.searchResults.index = i;
  // Replace with new text
  this.$refs.documenteditor.ej2Instances.editor.insertText('{replacementText}');
}

// Clear highlights
this.$refs.documenteditor.ej2Instances.search.searchResults.clear();
```

**Placeholders**
- `'works'` → Replace with `{searchText}`
- `'Hello'` → Replace with `{replacementText}`

> **Note:** The insertText API supports control characters:
> - `"\r"`, `"\r\n"`, `"\n"` - Insert paragraph break
> - `"\v"` - Insert line break (no paragraph)
> - `"\t"` - Insert tab space

## Access Search Results

Get metadata about the current search operation.

```ts
const results = this.$refs.documenteditor.ej2Instances.search.searchResults;

// Total number of matches found
const totalMatches = results.length;

// Currently selected result index
const currentIndex = results.index;

// Navigate to specific result
results.index = {resultIndex};
```

**Placeholders**
- `0` → Replace with `{resultIndex}`

## Listen to Search Results Change

Handle events when search results are updated (search completed, replaced, or cleared).

```ts
const handleSearchResultsChange = () => {
  const searchResults = this.$refs.documenteditor.ej2Instances.search.searchResults;
  console.log(`Found ${searchResults.length} matches`);
};

// Register in component:
this.$refs.documenteditor.searchResultsChange = handleSearchResultsChange;
```

## Clear Search Results

Remove all search highlights and reset the search state.

```ts
this.$refs.documenteditor.ej2Instances.search.searchResults.clear();
```

> **Note:** Clearing results deselects all highlighted matches and resets the result index to prepare for the next search.

## Customize find and replace
When to use: wire a custom UI (inputs/buttons) to the search API for tailored workflows.

```ts
function replaceAllFromInputs() {
    let textToFind = (document.getElementById('find_text')).value;
    let textToReplace = (document.getElementById('replace_text')).value;
    if (textToFind !== '') {
        // Find all the occurences of given text
        this.$refs.documenteditor.ej2Instances.search.findAll(textToFind);
        if (this.$refs.documenteditor.ej2Instances.searchModule.searchResults.length > 0) {
            // Replace all the occurences of given text
            this.$refs.documenteditor.ej2Instances.search.searchResults.replaceAll(textToReplace);
        }
    }
}
```
