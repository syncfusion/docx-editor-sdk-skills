# Find and Replace

Search for text, navigate results, and replace occurrences programmatically or via the Options pane.

## Options Pane

Open the built-in find/replace UI (shows results list, navigation, replace tab).

```ts
import { DocumentEditor, Selection, Editor, Search, OptionsPane, EditorHistory } from '@syncfusion/ej2-documenteditor';
DocumentEditor.Inject(Selection, Search, Editor, OptionsPane, EditorHistory);
let documenteditor: DocumentEditor = new DocumentEditor({ height: '370px', enableSelection: true, enableSearch: true, enableEditor: true, isReadOnly: false, enableOptionsPane: true, enableEditorHistory : true });
documenteditor.appendTo('#DocumentEditor');
let sfdt: string = `{
    "sections": [
        {
            "blocks": [
                {
                    "inlines": [
                        {
                            "characterFormat": {
                                "bold": true,
                                "italic": true
                            },
                            "text": "Adventure Works Cycles, the fictitious company on which the AdventureWorks sample databases are based, is a large, multinational manufacturing company. The company manufactures and sells metal and composite bicycles to North American, European and Asian commercial markets. While its base operation is located in Bothell, Washington with 290 employees, several regional sales teams are located throughout their market base."
                        }
                    ]
                }
            ]
        }
    ]
}`;
documenteditor.open(sfdt);
document.getElementById('showhidepane').addEventListener('click', () => {
    // Programmatically open the OptionsPane (keyboard shortcut also available)
    documenteditor.showOptionsPane();
});
```

## Find

Locate text from the current cursor or across the document using search options.

```ts
// Find next occurrence from cursor
documentEditor.search.find('Some text', 'None');

// Find all occurrences and highlight them
documentEditor.search.findAll('Some text', 'None');
```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`
- `'None'` → Allowed options: `'None'`, `'WholeWord'`, `'CaseSensitive'`, `'CaseSensitiveWholeWord'`

## Search Results

Work with the SearchResults collection to inspect, replace, or clear search hits.

```ts
let results = documentEditor.search.searchResults;
let count = results.length; // total matches
// Replace all matches with newText
results.replaceAll('Mike');
// Clear results after operations
results.clear();
```

**Placeholders**
- `'Mike'` → Replace with `{replacementText}`

## Replace Single Occurrence

Replace the currently selected match using editor insert APIs (supports control characters).

```ts
documentEditor.search.findAll('works');

let searchLength: number = documentEditor.search.searchResults.length;

for (let i = 0; i < searchLength; i++) {
    // It will move selection to specific searched index,move to each occurrence one by one
    documentEditor.search.searchResults.index = i;
    // Replace it with some text
    documentEditor.editor.insertText('Hello');
}

documentEditor.search.searchResults.clear();
```
**Placeholders**
- `'Hello'` → Replace with `{replacementText}`

**Note:** `insertText` accepts control characters: `"\r"`, `"\n"`, `"\v"`, `"\t"`.

## SearchResultsChange Event

React to changes in the search results collection (added, cleared, replaced).

```ts
documenteditor.searchResultsChange = function() {

};
```

## Customize find and replace

When to use: wire a custom UI (inputs/buttons) to the search API for tailored workflows.

```ts
document.getElementById('replace_all').addEventListener('click', () => {
    let textToFind: string = (document.getElementById('find_text') as HTMLInputElement).value;
    let textToReplace: string = (document.getElementById('replace_text') as HTMLInputElement).value;
    if (textToFind !== '') {
        // Find all the occurences of given text
        documenteditor.searchModule.findAll(textToFind);
        if (documenteditor.searchModule.searchResults.length > 0) {
            // Replace all the occurences of given text
            documenteditor.searchModule.searchResults.replaceAll(textToReplace);
        }
    }
});
```

**Placeholders**
- `'find_text'` → Replace with `{find input element id}`
- `'replace_text'` → Replace with `{replace input element id}`

## File-based Changes

- Container setup → Ensure `container` or `documentEditor` is initialized before calling search APIs
- UI wiring → Hook `searchResultsChange` handler where search UI is rendered
- Batch replace → Use `search.searchResults.replaceAll()` for atomic replace-all operations

