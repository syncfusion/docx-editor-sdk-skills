# Find and Replace

Search and replace text interactively or programmatically via the built-in Options pane.

## Setup

All JavaScript code examples assume `documentEditor` is already initialized as:
```javascript
var documentEditor = document.getElementById('container').ej2_instances[0];
```

This is the standard container instance pattern for accessing the Syncfusion DOCX Editor API.

## Show Options Pane

Open the built-in find/replace UI for interactive search and replace operations.

```javascript
// Open the find/replace pane (also accessible via Ctrl+F)
documentEditor.showOptionsPane();
```

## Find Single Occurrence

Jump to the next match from the current cursor position.

```javascript
// Find next occurrence
documentEditor.search.find('Some text', 'None');
```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`

**Search Options**: `'None'` | `'WholeWord'` | `'CaseSensitive'` | `'CaseSensitiveWholeWord'`

## Find All Occurrences

Highlight and enumerate every match in the document.

```javascript
// Find all matches
documentEditor.search.findAll('Some text', 'None');
```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`

## Search Results

Access and manipulate the collection of matches found.

```javascript
// Get results metadata
var results = documentEditor.search.searchResults;
console.log('Total matches:', results.length);
console.log('Current index:', results.index);

// Clear highlights and reset search state
documentEditor.search.searchResults.clear();
```

## Replace All Occurrences

Perform bulk replacement across all found matches.

```javascript
// Find matches, then replace all
documentEditor.search.findAll('Some text', 'None');
documentEditor.search.searchResults.replaceAll('Mike');

```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`
- `'Mike'` → Replace with `{replaceText}`

## Replace Single Occurrence

Programmatically replace each match one-by-one with custom logic.

```javascript
// Iterate results in reverse and replace each occurrence
var len = documentEditor.search.searchResults.length;
for (var i = len - 1; i >= 0; i--) {
  documentEditor.search.searchResults.index = i;
  documentEditor.editor.insertText('Hello');
}
// Clear results after replacements
documentEditor.search.searchResults.clear();
```

**Placeholders**
- `'Hello'` → Replace with `{replacementText}`

**Note**: Use `insertText()` for single replacements; it supports newlines (`\n`), tabs (`\t`), and paragraph breaks.

## Custom Find and Replace UI

Wire a custom search interface to the search API for tailored workflows.

```javascript
function replaceAllFromInputs() {
  var findInput = document.getElementById('find_text').value;
  var replaceInput = document.getElementById('replace_text').value;
  
  if (findInput) {
    documentEditor.search.findAll(findInput, 'None');
    if (documentEditor.search.searchResults.length > 0) {
      documentEditor.search.searchResults.replaceAll(replaceInput);
    }
  }
}

// Call from UI button: onclick="replaceAllFromInputs()"
```

**Placeholders**
- `'find_text'` → Replace with `{findInputId}`
- `'replace_text'` → Replace with `{replaceInputId}`

## Enable Search UI Components

Configure the DocumentEditorContainer to include search and replace options at initialization.

```cshtml
@Html.EJS().DocumentEditor("container").EnableSelection(true).EnableSearch(true).IsReadOnly(false).EnableEditor(true).EnableOptionsPane(true).Render()
```

**Note**: `EnableSearch` enables the programmatic search API; `EnableOptionsPane` adds the built-in find/replace pane UI to the container.
