# Ribbon

A concise reference for enabling and configuring the Ribbon UI in the Document Editor.

## Enable Ribbon
Use the `toolbarMode` prop on `DocumentEditorContainerComponent` to enable the Ribbon UI.

```typescript
/**
 * Add below codes in app.component.html file
 */
<ejs-documenteditorcontainer #documenteditor_default [enableToolbar]=true [locale]="culture" [toolbarMode]="'Ribbon'" (created)="onCreate()" (documentChange)="onDocumentChange()" height="600px" [serviceUrl]="hostUrl" style="display:block;" [toolbarMode]="toolbarMode"></ejs-documenteditorcontainer>

/**
 * Add below codes in app.component.ts file
 */
import { Component, ViewEncapsulation, ViewChild } from '@angular/core';
import { ToolbarService, DocumentEditorContainerComponent, RibbonService, DocumentEditorContainerModule } from '@syncfusion/ej2-angular-documenteditor';
import { SwitchModule } from '@syncfusion/ej2-angular-buttons';

@Component({
    selector: 'app-root',
    templateUrl: 'app.component.html',
    encapsulation: ViewEncapsulation.None,
    providers: [ToolbarService, RibbonService],
    standalone: true,
    imports: [DocumentEditorContainerModule, SwitchModule,  ]
})
export class AppComponent {
    public hostUrl: string = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';

    @ViewChild('documenteditor_default')
    public container: DocumentEditorContainerComponent;
    public toolbarMode: string = 'Ribbon'; // Options: 'Ribbon' or 'Toolbar'
}
```

## Ribbon Layouts
Switch between simplified and classic layouts using `ribbonLayout`.

```typescript
/**
 * Add below codes in app.component.html file
 */
<ejs-documenteditorcontainer #documenteditor_default [enableToolbar]=true [locale]="culture" [toolbarMode]="'Ribbon'" (created)="onCreate()" (documentChange)="onDocumentChange()" height="600px" [serviceUrl]="hostUrl" style="display:block;" [toolbarMode]="toolbarMode" [ribbonLayout]="ribbonLayout"></ejs-documenteditorcontainer>

/**
 * Add below codes in app.component.ts file
 */
import { Component, ViewEncapsulation, ViewChild } from '@angular/core';
import { ToolbarService, DocumentEditorContainerComponent, RibbonService, DocumentEditorContainerModule } from '@syncfusion/ej2-angular-documenteditor';
import { SwitchModule } from '@syncfusion/ej2-angular-buttons';

@Component({
    selector: 'app-root',
    templateUrl: 'app.component.html',
    encapsulation: ViewEncapsulation.None,
    providers: [ToolbarService, RibbonService],
    standalone: true,
    imports: [DocumentEditorContainerModule, SwitchModule,  ]
})
export class AppComponent {
    public hostUrl: string = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';

    @ViewChild('documenteditor_default')
    public container!: DocumentEditorContainerComponent;
    public toolbarMode: string = 'Ribbon'; // Options: 'Ribbon' or 'Toolbar'
    public ribbonLayout: string= 'Simplified'; // Options: 'Simplified' or 'Classic'
}
```

## Requirred CSS

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
@import '../node_modules/@syncfusion/ej2-ribbon/styles/material.css';/* Required for Ribbon */
```

**Placeholders**
- 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/' -> Replace with `{serviceUrl}`

**File changes**
- src/styles.css -> add the two `@import` lines above