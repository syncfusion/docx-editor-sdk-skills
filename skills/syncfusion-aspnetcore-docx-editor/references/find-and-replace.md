# Find and Replace

Search and replace text programmatically or via the built-in Options pane.

## Options Pane
```javascript
container.documentEditor.showOptionsPane();
```

## Search
```javascript
// Find next occurrence from current cursor
container.documentEditor.search.find('textToFind', 'None');

// Find all occurrences in the document
container.documentEditor.search.findAll('textToFind', 'None');
```

Options for the second parameter: 'None' | 'WholeWord' | 'CaseSensitive' | 'CaseSensitiveWholeWord'.

## Search results
```javascript
// Access the results container
let results = container.documentEditor.search.searchResults;

// Replace all found occurrences
container.documentEditor.search.findAll('old', 'None');
container.documentEditor.search.searchResults.replaceAll('newText');

// Clear highlight/results
container.documentEditor.search.searchResults.clear();
```

## Replace single occurrence
```javascript
// Iterate occurrences (replace one by one)
container.documentEditor.search.findAll('works');
for (let i = container.documentEditor.search.searchResults.length - 1; i >= 0; i--) {
  container.documentEditor.search.searchResults.index = i; // select occurrence
  container.documentEditor.editor.insertText('replacementText');
}
// Optionally clear results
container.documentEditor.search.searchResults.clear();
```

## Customize programmatically
```javascript
// Example: run a find-all then replace-all flow
// (assumes document is already loaded in the editor instance)
if (container.documentEditor.search) {
  container.documentEditor.search.findAll('Company', 'WholeWord');
  if (container.documentEditor.search.searchResults.length > 0) {
    container.documentEditor.search.searchResults.replaceAll('Organization');
  }
}
```

**Placeholders**
- 'Company' → Replace with {findText}
- 'Organization' → Replace with {replaceText}

## Notes
- Use `insertText` for single-occurrence replacements; it supports newlines (`\n`), tabs (`\t`), and paragraph breaks.
- The Options pane can also be opened via keyboard `Ctrl+F`.

---