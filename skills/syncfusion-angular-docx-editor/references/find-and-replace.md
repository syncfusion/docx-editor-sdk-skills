# Find and Replace

Search for text in documents and replace single or multiple occurrences with alternatives. Supports case sensitivity and whole-word matching.

## Open Find and Replace Pane

Open the built-in Find and Replace dialog programmatically.

```typescript
this.documentEditor.showOptionsPane();
```

**Note:** Users can also open with keyboard shortcut `Ctrl+F`. Close with `Esc` key.

## Find Next Occurrence

Search for the next occurrence of text from the current cursor position.

```typescript
this.documentEditor.search.find('Some text', 'None');
```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`
- `'None'` → Replace with `{findOption}`

**Note:** Find options: `'None'`, `'WholeWord'`, `'CaseSensitive'`, `'CaseSensitiveWholeWord'`. Results are highlighted in yellow.

## Find All Occurrences

Search for all occurrences of text in the entire document.

```typescript
this.documentEditor.search.findAll('Some text', 'None');
```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`
- `'None'` → Replace with `{findOption}`

**Note:** All matches are highlighted in yellow. Use `searchResults` property to access results.

## Get Search Results

Access information about found search results.

```typescript
const length: number = this.documentEditor.search.searchResults.length;
const currentIndex: number = this.documentEditor.search.searchResults.index;
```

**Note:** `length` returns total matches found. `index` returns the currently selected result; change this property to navigate between results.

## Replace All Occurrences

Replace all found matches with a new text value.

```typescript
this.documentEditor.search.findAll('Some text');
this.documentEditor.search.searchResults.replaceAll('Mike');
```

**Placeholders**
- `'Some text'` → Replace with `{searchText}`
- `'Mike'` → Replace with `{replacementText}`

## Replace Single Occurrence

Replace one search result at a time by navigating through results and inserting text.

```typescript
this.documentEditor.search.findAll('works');

const searchLength: number = this.documentEditor.search.searchResults.length;

for (let i = searchLength - 1; i >= 0; i--) {
  // Move to each result
  this.documentEditor.search.searchResults.index = i;
  // Replace current occurrence
  this.documentEditor.editor.insertText('Hello');
}

this.documentEditor.search.searchResults.clear();
```

**Placeholders**
- `'works'` → Replace with `{searchText}`
- `'Hello'` → Replace with `{replacementText}`

**Note:** Supports control characters: `\r`, `\r\n`, `\n` (new paragraph), `\v` (line break), `\t` (tab).

## Customize find and replace
When to use: wire a custom UI (inputs/buttons) to the search API for tailored workflows.

```typescript
import { NgModule } from '@angular/core'
import { BrowserModule } from '@angular/platform-browser'
import { ButtonModule } from '@syncfusion/ej2-angular-buttons'
import { DocumentEditorAllModule } from '@syncfusion/ej2-angular-documenteditor'
import { ToolbarModule } from '@syncfusion/ej2-angular-navigations'
import { ComboBoxModule } from '@syncfusion/ej2-angular-dropdowns'
import {ColorPickerModule } from '@syncfusion/ej2-angular-inputs'



import { Component, ViewEncapsulation, ViewChild } from '@angular/core';
import {
    DocumentEditorComponent, SelectionService, EditorService, SearchService, OptionsPaneService
} from '@syncfusion/ej2-angular-documenteditor';

@Component({
imports: [
        
        ButtonModule,
        ToolbarModule,
        DocumentEditorAllModule,
        ComboBoxModule,
        ColorPickerModule
    ],


standalone: true,
      selector: 'app-container',
      //specifies the template string for the Document Editor component
      template: `<div style="width:100%;">
      <table>
          <tr>
              <td>
                  <label>Text to find:</label>
              </td>
              <td>
                  <input type="text" id="find_text" />
              </td>
          </tr>
          <tr>
              <td>
                  <label>Text to replace:</label>
              </td>
              <td>
                  <input type="text" id="replace_text" />
              </td>
          </tr>
          <tr>
              <td colspan="2">
                  <button ejs-button (click)="onReplaceButtonClick()" >Replace all</button>
              </td>
          </tr>
      </table>
      <ejs-documenteditor #document_editor id="container" height="330px" style="display:block" [enableSelection]=true [enableSearch]=true [enableEditor]=true [isReadOnly]=false (created)="onCreated()"></ejs-documenteditor>
      </div>`,
      encapsulation: ViewEncapsulation.None,
      providers: [SelectionService, EditorService, SearchService]
})

export class AppComponent {
    @ViewChild('document_editor')
    public documentEditor?: DocumentEditorComponent;

    onCreated(): void {
        if ((this.documentEditor as DocumentEditorComponent).isDocumentLoaded) {
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
            (this.documentEditor as DocumentEditorComponent).open(sfdt);
        }
    }

    public onReplaceButtonClick(): void {
        let textToFind: string = (document.getElementById('find_text') as HTMLInputElement).value;
        let textToReplace: string = (document.getElementById('replace_text') as HTMLInputElement).value;
        if (textToFind !== '') {
            // Find all the occurences of given text
            (this.documentEditor as DocumentEditorComponent).searchModule.findAll(textToFind);
            if ((this.documentEditor as DocumentEditorComponent).searchModule.searchResults.length > 0) {
                // Replace all the occurences of given text
                (this.documentEditor as DocumentEditorComponent).searchModule.searchResults.replaceAll(textToReplace);
            }
        }
    }
}
```

## Handle Search Results Change

React to search operation completion or result clearing.

```typescript
import { Component, ViewEncapsulation, ViewChild } from '@angular/core';
import {
    DocumentEditorComponent, EditorService, SelectionService, SfdtExportService, EditorHistoryService, BookmarkDialogService
} from '@syncfusion/ej2-angular-documenteditor';

@Component({
      selector: 'app-container',
      //specifies the template string for the Document Editor component
      template: `<ejs-documenteditor #document_editor  id="container" height="330px" style="display:block" [isReadOnly]=false [enableSelection]=true [enableSearch]=true (searchResultsChange)="onSearchResultChange()" > </ejs-documenteditor>`,
      encapsulation: ViewEncapsulation.None,
      providers: [EditorService, SelectionService, SfdtExportService]
})

export class AppComponent {
    @ViewChild('document_editor')
    public documentEditor: DocumentEditorComponent;

    // search result change event handler
    public onSearchResultChange(): void {

    }
}
```

**Note:** Event fires when: search completes, results are replaced, or results are explicitly cleared.

## Clear Search Results

Remove all highlighting and clear the search results.

```typescript
this.documentEditor.search.searchResults.clear();
```
