# Ribbon

A concise reference for enabling and configuring the Ribbon UI in the Document Editor.

## Enable Ribbon
Use the `toolbarMode` property on `DocumentEditorContainer` to enable the Ribbon UI.

```ts
import { DocumentEditorContainer, Ribbon } from '@syncfusion/ej2-documenteditor';

DocumentEditorContainer.Inject(Ribbon);

// Initialize the Document Editor Container with Ribbon mode enabled
let container = new DocumentEditorContainer({
    enableToolbar: true,
    toolbarMode: 'Ribbon', // Options: 'Ribbon' or 'Toolbar'
    height: '590px'
});

container.serviceUrl = '{serviceUrl}';
container.appendTo('#container');
```

## Ribbon Layouts
Switch between simplified and classic layouts using `ribbonLayout`.

```ts
import { DocumentEditorContainer, Ribbon } from '@syncfusion/ej2-documenteditor';

DocumentEditorContainer.Inject(Ribbon);

// Initialize the Document Editor Container with Ribbon mode enabled
let container = new DocumentEditorContainer({
    enableToolbar: true,
    toolbarMode: 'Ribbon', // Options: 'Ribbon' or 'Toolbar'
    ribbonLayout: 'Classic', // Options: 'Simplified' or 'Classic'
    height: '590px'
});

container.serviceUrl = '{serviceUrl}';
container.appendTo('#container');
```

## Required CSS

```css
@import '../node_modules/@syncfusion/ej2-base/styles/material.css';
@import '../node_modules/@syncfusion/ej2-buttons/styles/material.css';
@import '../node_modules/@syncfusion/ej2-inputs/styles/material.css';
@import '../node_modules/@syncfusion/ej2-popups/styles/material.css';
@import '../node_modules/@syncfusion/ej2-lists/styles/material.css';
@import '../node_modules/@syncfusion/ej2-navigations/styles/material.css';
@import '../node_modules/@syncfusion/ej2-splitbuttons/styles/material.css';
@import '../node_modules/@syncfusion/ej2-dropdowns/styles/material.css';
@import '../node_modules/@syncfusion/ej2-documenteditor/styles/material.css';
@import '../node_modules/@syncfusion/ej2-ribbon/styles/material.css';/* Required for Ribbon */
```

**Placeholders**
- `{serviceUrl}` → Replace with your backend service URL (e.g., `https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/`)

**File changes**
- `src/styles.css` → Add the CSS `@import` lines above
