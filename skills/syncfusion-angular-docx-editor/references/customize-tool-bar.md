# Toolbar Customization

Customize the Document Editor toolbar by adding, showing, hiding, enabling, or disabling items to match your application's needs.

## Add Custom Item

Define and insert new custom toolbar items with click handlers.

```typescript
import { Component, OnInit, ViewChild } from '@angular/core';
import {
  ToolbarService,
  DocumentEditorContainerComponent,
} from '@syncfusion/ej2-angular-documenteditor';
import { ClickEventArgs } from '@syncfusion/ej2-navigations';
import {
  CustomToolbarItemModel,
  DocumentEditorContainerModule,
} from '@syncfusion/ej2-angular-documenteditor';

@Component({
  selector: 'app-container',
  standalone: true,
  imports: [DocumentEditorContainerModule],
  providers: [ToolbarService],
  template: `
    <ejs-documenteditorcontainer #documenteditor_default 
      serviceUrl="https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/" 
      height="600px" 
      style="display:block" 
      [toolbarItems]="items" 
      (toolbarClick)="onToolbarClick($event)" 
      (created)="onCreate()" 
      [enableToolbar]="true">
    </ejs-documenteditorcontainer>
  `,
})
export class AppComponent implements OnInit {
  @ViewChild('documenteditor_default')
  public container?: DocumentEditorContainerComponent;

  // Define custom toolbar item
  public toolItem: CustomToolbarItemModel = {
    prefixIcon: 'e-de-ctnr-lock',
    tooltipText: 'Disable Image',
    text: this.onWrapText('Disable Image'),
    id: 'Custom',
  };

  // Define toolbar items array
  public items = [
    this.toolItem,
    'Undo',
    'Redo',
    'Separator',
    'Image',
    'Table',
    'Hyperlink',
    'Bookmark',
    'TableOfContents',
    'Separator',
    'Header',
    'Footer',
    'PageSetup',
    'PageNumber',
    'Break',
    'InsertFootnote',
    'InsertEndnote',
    'Separator',
    'Find',
    'Separator',
    'Comments',
    'TrackChanges',
    'Separator',
    'LocalClipboard',
    'RestrictEditing',
    'Separator',
    'FormFields',
    'UpdateFields',
    'ContentControl',
  ];

  ngOnInit(): void {}

  // Called when the DocumentEditorContainer is created
  onCreate() {
    // Logic to handle the creation of the editor
  }

  // Event handler for toolbar clicks
  onToolbarClick(args: ClickEventArgs): void {
    switch (args.item.id) {
      case 'Custom':
        // Disable the image toolbar item
        if (this.container) {
          this.container.toolbar.enableItems(4, false);
        }
        break;
    }
  }

  // Wrap text with custom HTML
  private onWrapText(text: string): string {
    let content: string = '';
    const index: number = text.lastIndexOf(' ');

    if (index !== -1) {
      content =
        text.slice(0, index) +
        "<div class='e-de-text-wrap'>" +
        text.slice(index + 1) +
        '</div>';
    } else {
      content = text;
    }

    return content;
  }
}

```

**Placeholders**
- `'e-de-ctnr-lock'` → Replace with {iconCssClass}
- `'Disable Image'` → Replace with {tooltipText}
- `'Custom'` → Replace with {customItemId}
- `4` → Replace with {targetItemIndex}

**Note:** Assign `items` to the container's `[toolbarItems]` binding and register `onToolbarClick` to the `(toolbarClick)` event.

## Enable or Disable Item

Control the enabled state of toolbar items by index or item ID.

```typescript
this.container?.toolbar.enableItems(4, false);
this.container?.toolbar.enableItems(4, true);
```

**Placeholders**
- `4` → Replace with `{itemIndex}`
- `false` → Replace with `{isEnabled}`

**Note:** Item indices are based on the order in the `toolbarItems` array. Separator items also count in the index.

## Show or Hide Items

Display or hide existing toolbar items using the `toolbarItems` array.

```typescript
public items = [
  'Undo',
  'Redo',
  'Separator',
  'Image',
  'Table',
  'Hyperlink',
  'Bookmark',
  'TableOfContents',
  'Separator',
  'Header',
  'Footer',
  'PageSetup',
  'PageNumber',
  'Break',
  'InsertFootnote',
  'InsertEndnote',
  'Separator',
  'Find',
  'Separator',
  'Comments',
  'TrackChanges',
  'Separator',
  'LocalClipboard',
  'RestrictEditing',
  'Separator',
  'FormFields',
  'UpdateFields',
  'ContentControl'
];
```

**Placeholders**
- `'Image'`, `'Table'`, etc. → Replace with `{toolbarItemName}`

**Note:**
- Default `toolbarItems` are `['New', 'Open', 'Separator', 'Undo', 'Redo', 'Separator', 'Image', 'Table', 'Hyperlink', 'Bookmark', 'TableOfContents', 'Separator', 'Header', 'Footer', 'PageSetup', 'PageNumber', 'Break', 'InsertFootnote', 'InsertEndnote', 'Separator', 'Find', 'Separator', 'Comments', 'TrackChanges', 'Separator', 'LocalClipboard', 'RestrictEditing', 'Separator', 'FormFields', 'UpdateFields', 'ContentControl']`.