# Ribbon Customization

Customize the Document Editor ribbon by modifying file menu, tabs, groups, and items to match your application's workflow and requirements.

## Requirred CSS
Only the delta imports required to support Ribbon styles.

```css
@import '../node_modules/@syncfusion/ej2-base/styles/material.css';
@import '../node_modules/@syncfusion/ej2-buttons/styles/material.css';
@import '../node_modules/@syncfusion/ej2-inputs/styles/material.css';
@import '../node_modules/@syncfusion/ej2-popups/styles/material.css';
@import '../node_modules/@syncfusion/ej2-lists/styles/material.css';
@import '../node_modules/@syncfusion/ej2-navigations/styles/material.css';
@import '../node_modules/@syncfusion/ej2-splitbuttons/styles/material.css';
@import '../node_modules/@syncfusion/ej2-dropdowns/styles/material.css';
@import '../node_modules/@syncfusion/ej2-angular-documenteditor/styles/material.css';
@import '../node_modules/@syncfusion/ej2-ribbon/styles/material.css';
```

## Customize File Menu

Modify file menu items by removing defaults and adding custom items with click handlers.

```typescript
/**
 * Add below codes in app.component.html file
 */
<ejs-documenteditorcontainer #documenteditor_default [enableToolbar]=true [locale]="culture" [toolbarMode]="'Ribbon'" (created)="onCreate()" (documentChange)="onDocumentChange()" height="600px" [serviceUrl]="hostUrl" style="display:block;" [fileMenuItems]="fileMenuItems" (fileMenuItemClick)="fileMenuItemClick($event)"></ejs-documenteditorcontainer>

/**
 * Add below codes in app.component.ts file
 */
import { Component, ViewChild, ViewEncapsulation } from '@angular/core';
import { ToolbarService, DocumentEditorContainerComponent, RibbonService, DocumentEditorContainerModule } from '@syncfusion/ej2-angular-documenteditor';
import { SwitchModule } from '@syncfusion/ej2-angular-buttons';

@Component({
    selector: 'app-root',
    templateUrl: 'app.component.html',
    encapsulation: ViewEncapsulation.None,
    providers: [ToolbarService, RibbonService],
    standalone: true,
    imports: [DocumentEditorContainerModule, SwitchModule]
})
export class AppComponent {
    public hostUrl: string = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';
    public toolbarMode: string = 'Ribbon';

    @ViewChild('documenteditor_default')
    public container!: DocumentEditorContainerComponent;

    public fileMenuItems: any = [
        "New",
        "Print",
        { text: 'Export', id: 'custom_item', iconCss: 'e-icons e-export' }
    ];

    public fileMenuItemClick(args: any): void {
        if (args.item.id) {
            this.container.documentEditor.save('Sample', 'Docx');
        }
    }
}
```

**Placeholders**
- `"New"`, `"Print"` → Replace with {builtInMenuItems}
- `'custom_item'` → Replace with {itemId}
- `'e-icons e-export'` → Replace with {iconCssClass}
- `'Sample'` → Replace with {documentName}
- `'Docx'` → Replace with {fileFormat}

**Note:** Assign `fileMenuItems` to the container's `[fileMenuItems]` binding and register `fileMenuItemClick` to the `(fileMenuItemClick)` event.

## Add Backstage Menu

Replace the file menu with a backstage navigation panel.

```typescript
/**
 * Add below codes in app.component.html file
 */
<ejs-documenteditorcontainer #documenteditor_default [enableToolbar]=true [locale]="culture" [toolbarMode]="'Ribbon'" (created)="onCreate()" (documentChange)="onDocumentChange()" height="600px" [serviceUrl]="hostUrl" style="display:block;" [backstageMenu]="backstageMenu"></ejs-documenteditorcontainer>

/**
 * Add below codes in app.component.ts file
 */
import { Component, ViewChild, ViewEncapsulation } from '@angular/core';
import { ToolbarService, DocumentEditorContainerComponent, RibbonService, DocumentEditorContainerModule } from '@syncfusion/ej2-angular-documenteditor';
import { SwitchModule } from '@syncfusion/ej2-angular-buttons';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    encapsulation: ViewEncapsulation.None,
    providers: [ToolbarService, RibbonService],
    standalone: true,
    imports: [DocumentEditorContainerModule, SwitchModule]
})
export class AppComponent {
    public hostUrl: string = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';

    @ViewChild('documenteditor_default', { static: true })
    public container!: DocumentEditorContainerComponent;

    public backstageMenu = {
        text: 'File',
        backButton: { text: 'close' },
        items: [
            { id: 'new', text: 'New', iconCss: 'e-icons e-de-ctnr-new' }
        ],
        visible: true,
    };
}
```

**Placeholders**
- `'File'` → Replace with `{backstageTitle}`
- `'close'` → Replace with `{backButtonText}`
- `'new'` → Replace with `{itemId}`
- `'New'` → Replace with `{itemText}`

**Note:** Assign `backstageMenu` to the container's `[backstageMenu]` binding. When enabled, default file menu items are automatically hidden.

## Show or Hide Tab

Toggle visibility of built-in or custom ribbon tabs.

```typescript
this.container.ribbon.showTab('Home', false);
this.container.ribbon.showTab('custom_tab', false);
this.container.ribbon.showTab('Insert', true);
```

**Placeholders**
- `'Home'` → Replace with `{tabName}`
- `false` → Replace with `{isVisible}`

## Add Tab

Insert a new custom tab at the end or before a specific existing tab.

```typescript
import { Component, ViewChild, ViewEncapsulation, AfterViewInit } from '@angular/core';
import { ToolbarService, DocumentEditorContainerComponent, RibbonService, DocumentEditorContainerModule } from '@syncfusion/ej2-angular-documenteditor';
import { SwitchModule } from '@syncfusion/ej2-angular-buttons';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    encapsulation: ViewEncapsulation.None,
    providers: [ToolbarService, RibbonService],
    standalone: true,
    imports: [DocumentEditorContainerModule, SwitchModule]
})
export class AppComponent implements AfterViewInit {
    public hostUrl: string = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';

    @ViewChild('documenteditor_default', { static: true })
    public container!: DocumentEditorContainerComponent;

    ngAfterViewInit(): void {
        setTimeout(() => {

            // To add the tab at end of tab
            const ribbonTab = {
                header: 'Custom Tab',
                id: 'custom_tab',
                groups: [
                    {
                        header: 'Custom Group',
                        collections: [
                            {
                                items: [
                                    {
                                        type: 'Button',
                                        buttonSettings: {
                                            content: 'New',
                                            iconCss: 'e-icons e-de-ctnr-new',
                                            clicked: () => {
                                                this.container.documentEditor.openBlank();
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            };
            this.container.ribbon.addTab(ribbonTab);

            // To add the tab before the Insert tab(exising tab)

            this.container.ribbon?.addTab(ribbonTab, 'Insert');
        })
    }
}
```

**Placeholders**
- `'Custom Tab'` → Replace with `{tabHeader}`
- `'custom_tab'` → Replace with `{tabId}`
- `'Insert'` → Replace with `{beforeTabName}`

## Show or Hide Group

Control visibility of groups within a ribbon tab by index or ID.

```typescript
// By position
this.container.ribbon.showGroup({ tabId: 'Home', index: 1 }, false);
this.container.ribbon.showGroup({ tabId: 'Home', index: 1 }, true);

// By ID
this.container.ribbon.showGroup('custom_group', false);
```

**Placeholders**
- `'Home'` → Replace with `{tabId}`
- `1` → Replace with `{groupIndex}`
- `false` → Replace with `{isVisible}`
- `'custom_group'` → Replace with `{groupId}`

## Add Group

Insert a new custom group into a tab at the end or at a specified index.

```typescript
import { Component, ViewChild, ViewEncapsulation, AfterViewInit } from '@angular/core';
import { ToolbarService, DocumentEditorContainerComponent, RibbonService, DocumentEditorContainerModule } from '@syncfusion/ej2-angular-documenteditor';
import { SwitchModule } from '@syncfusion/ej2-angular-buttons';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    encapsulation: ViewEncapsulation.None,
    providers: [ToolbarService, RibbonService],
    standalone: true,
    imports: [DocumentEditorContainerModule, SwitchModule]
})
export class AppComponent implements AfterViewInit {
    public hostUrl: string = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';

    @ViewChild('documenteditor_default', { static: true })
    public container!: DocumentEditorContainerComponent;

    ngAfterViewInit(): void {
        setTimeout(() => {

            // Add the new group at the end of the Home tab
            const ribbonGroup = {
                header: 'Custom Group',
                collections: [
                    {
                        items: [
                            {
                                type: 'Button',
                                buttonSettings: {
                                    content: 'New',
                                    iconCss: 'e-icons e-de-ctnr-new',
                                    clicked: () => {
                                        this.container.documentEditor.openBlank();
                                    }
                                }
                            }
                        ]
                    }
                ]
            };
            this.container.ribbon?.addGroup('Home', ribbonGroup);

            // Add the new group at the specified index of the Home tab (before the Clipboard group)

            this.container.ribbon?.addGroup('Home', ribbonGroup, 1);
        });
    }
}
```

**Placeholders**
- `'Custom Group'` → Replace with `{groupHeader}`
- `'Home'` → Replace with `{tabId}`
- `1` → Replace with `{insertIndex}`

## Show or Hide Item

Toggle visibility of individual items within groups by index position or item ID.

```typescript
// By position (Hide Bold and Italic)
this.container.ribbon.showItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [5, 6] }, false);

// By position (Show Bold and Italic)
this.container.ribbon.showItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [5, 6] }, true);

// By ID
this.container.ribbon.showItems('custom_item', false);
```

**Placeholders**
- `'Home'` → Replace with `{tabId}`
- `2` → Replace with `{groupIndex}`
- `[5, 6]` → Replace with `{itemIndexes}`
- `false` → Replace with `{isVisible}`
- `'custom_item'` → Replace with `{itemId}`

## Enable or Disable Item

Control the enabled state of ribbon items to restrict user interactions.

```typescript
// Disable underline (index 7)
this.container.ribbon.enableItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [7] }, false);

// Enable underline
this.container.ribbon.enableItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [7] }, true);

// By ID
this.container.ribbon.enableItems('custom_item', false);
```

**Placeholders**
- `'Home'` → Replace with `{tabId}`
- `2` → Replace with `{groupIndex}`
- `[7]` → Replace with `{itemIndexes}`
- `false` → Replace with `{isEnabled}`
- `'custom_item'` → Replace with `{itemId}`

## Add Item

Insert a new custom item into a ribbon group at the end or at a specified position.

```typescript
import { Component, ViewChild, ViewEncapsulation, AfterViewInit } from '@angular/core';
import { ToolbarService, DocumentEditorContainerComponent, RibbonService, DocumentEditorContainerModule } from '@syncfusion/ej2-angular-documenteditor';
import { SwitchModule } from '@syncfusion/ej2-angular-buttons';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    encapsulation: ViewEncapsulation.None,
    providers: [ToolbarService, RibbonService],
    standalone: true,
    imports: [DocumentEditorContainerModule, SwitchModule]
})
export class AppComponent implements AfterViewInit {
    public hostUrl: string = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';

    @ViewChild('documenteditor_default', { static: true })
    public container!: DocumentEditorContainerComponent;

    ngAfterViewInit(): void {
        // To add the item at the end of the specified group (the item will be added at the end of the Undo group)
        setTimeout(() => {
            const ribbonItem = {
                type: 'Button',
                buttonSettings: {
                    content: 'New',
                    iconCss: 'e-icons e-de-ctnr-new',
                    clicked: () => {
                        this.container.documentEditor.openBlank();
                    }
                }
            };

            this.container.ribbon?.addItem({ tabId: 'Home', index: 0 }, ribbonItem);

            // To add the item before the specified item index (the item will be added before the Redo item in the Undo group)

            this.container.ribbon?.addItem({ tabId: 'Home', index: 0 }, ribbonItem, 1);
        });
    }
}
```

**Placeholders**
- `'Home'` → Replace with `{tabId}`
- `0` → Replace with `{groupIndex}`
- `'New'` → Replace with `{itemContent}`
- `'e-icons e-de-ctnr-new'` → Replace with `{iconCssClass}`
- `1` → Replace with `{itemPosition}`
