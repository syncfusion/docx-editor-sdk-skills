# Initialize Document Editor
> Document Editor control creation — create document editor.

## Install package
- npm package: `@syncfusion/ej2-angular-documenteditor` 

## CSS Imports

Add these to your `src/styles.css`. Use the theme that matches your app (tailwind3, material, bootstrap5, fluent2, etc.).

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

```

## Document Editor Container with Toolbar 
**This is the default and recommended approach for most use cases.**

```typescript
import { DocumentEditorContainerModule } from '@syncfusion/ej2-angular-documenteditor';
import { Component, OnInit } from '@angular/core';
import { ToolbarService } from '@syncfusion/ej2-angular-documenteditor';

@Component({
    imports: [        
        DocumentEditorContainerModule
    ],
    standalone: true,
    selector: 'app-root',
    template: `<ejs-documenteditorcontainer 
                   serviceUrl="https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/" 
                   height="600px" 
                   style="display:block" 
                   [enableToolbar]=true>
               </ejs-documenteditorcontainer>`,
    providers: [ToolbarService]
})
export class AppComponent implements OnInit {
    ngOnInit(): void {
    }
}

```

## Common Setup Gotchas

- **Missing styles**: All the `@syncfusion/ej2-*` CSS imports are required — the DOCX Editor uses styles from multiple packages.