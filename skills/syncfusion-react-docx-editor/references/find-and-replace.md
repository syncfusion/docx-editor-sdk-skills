# Find and Replace

Search and replace text programmatically or via the built-in Options pane.

## Options Pane
```tsx
// Open the options/find pane UI
documentEditor.showOptionsPane();
```

## Search
```tsx
// Find next occurrence from current cursor
documentEditor.search.find('textToFind', 'None');

// Find all occurrences in the document
documentEditor.search.findAll('textToFind', 'None');
```

Options for the second parameter: 'None' | 'WholeWord' | 'CaseSensitive' | 'CaseSensitiveWholeWord'.

## Search results
```tsx
// Access the results container
let results = documentEditor.search.searchResults;

// Replace all found occurrences
documentEditor.search.findAll('old', 'None');
documentEditor.search.searchResults.replaceAll('newText');

// Clear highlight/results
documentEditor.search.searchResults.clear();
```

## Replace single occurrence
```tsx
// Iterate occurrences (replace one by one)
documentEditor.search.findAll('works');
for (let i = documentEditor.search.searchResults.length - 1; i >= 0; i--) {
  documentEditor.search.searchResults.index = i; // select occurrence
  documentEditor.editor.insertText('replacementText');
}
// Optionally clear results
documentEditor.search.searchResults.clear();
```

## Customize programmatically
```tsx
// Example: open doc, then run a replace-all flow
// (assumes document is already loaded in the editor instance)
if (documentEditor.search) {
  documentEditor.search.findAll('Company', 'WholeWord');
  if (documentEditor.search.searchResults.length > 0) {
    documentEditor.search.searchResults.replaceAll('Organization');
  }
}
```

**Placeholders**
- 'Some text' → Replace with {findText}
- 'Mike' → Replace with {replaceText}

## Notes
- Use `insertText` for single-occurrence replacements; it supports newlines (`\n`), tabs (`\t`), and paragraph breaks.
- The Options pane can also be opened via keyboard `Ctrl+F`.
# Find and Replace

---

## Show Options Pane
When to use: open the built-in find/replace UI for interactive searches.

```tsx
// show the Options (find/replace) pane
container.current.documentEditor.showOptionsPane();
```

---

## Find (single occurrence)
When to use: jump to the next match from the current cursor position.

```tsx
// find the next occurrence (options: 'None' | 'WholeWord' | 'CaseSensitive' | 'CaseSensitiveWholeWord')
container.current.documentEditor.search.find('Some text', 'None');
```

---

## Find all occurrences
When to use: highlight or enumerate every match in the document.

```tsx
container.current.documentEditor.search.findAll('Some text', 'None');
```

---

## Replace All
When to use: perform a bulk replace across all search results.

```tsx
// locate matches first, then replace all
container.current.documentEditor.search.findAll('Some text');
container.current.documentEditor.search.searchResults.replaceAll('Mike');
```

---

## Replace Single Occurrence
When to use: programmatically replace the currently-selected match.

```tsx
// iterate results and replace each occurrence one-by-one
const len = container.current.documentEditor.search.searchResults.length;
for (let i = len - 1; i >= 0; i--) {
	container.current.documentEditor.search.searchResults.index = i;
	container.current.documentEditor.editor.insertText('Hello');
}
// clear results after replacements
container.current.documentEditor.search.searchResults.clear();
```

---

## Inspect Search Results
When to use: read metadata about matches (count, current index) or control navigation.

```tsx
const results = container.current.documentEditor.search.searchResults;
console.log(results.length, results.index);
```

---

## Clear Search Results
When to use: remove highlights and reset the search state.

```ts
container.current.documentEditor.search.searchResults.clear();
```

---

## Customize find and replace
When to use: wire a custom UI (inputs/buttons) to the search API for tailored workflows.

```tsx
function replaceAllFromInputs() {
	const find = (document.getElementById('find_text') as HTMLInputElement).value;
	const replaceWith = (document.getElementById('replace_text') as HTMLInputElement).value;
	if (find) {
		container.current.documentEditor.search.findAll(find);
		if (container.current.documentEditor.search.searchResults.length > 0) {
			container.current.documentEditor.search.searchResults.replaceAll(replaceWith);
		}
	}
}
```

---

**Placeholders**
- 'Some text' → Replace with {searchText}
- 'Mike' → Replace with {replaceText}

**File changes (suggested)**
- `src/components/DocEditor.tsx` → enable `enableSearch` and `enableOptionsPane`; expose `ref` as `container`.
- `src/pages/FindReplaceDemo.tsx` → add inputs and call `replaceAllFromInputs()` from UI buttons.

