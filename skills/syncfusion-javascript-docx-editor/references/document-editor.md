# Document Editor Container

Initialize a fully integrated Document Editor Container with predefined toolbar, properties pane, and status bar for complete document editing experience.

## Install package
- npm package: `@syncfusion/ej2-documenteditor` 

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
@import "../node_modules/@syncfusion/ej2-documenteditor/styles/material.css";

```

## Initialize Document Editor Container

Set up the Document Editor Container with toolbar and core configuration.

```tsx
import './style.css';
import { DocumentEditorContainer, Toolbar } from '@syncfusion/ej2-documenteditor';

// Inject the Toolbar module
DocumentEditorContainer.Inject(Toolbar);

// Initialize container with settings
const documenteditor = new DocumentEditorContainer({ 
    enableToolbar: true, 
    height: '390px', 
    serviceUrl: 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/' 
});

// Render to DOM
documenteditor.appendTo('#DocumentEditor');
```

**Placeholders**
- `'390px'` → Replace with `{containerHeight}`
- `'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/'` → Replace with `{serviceUrl}`
- `'#DocumentEditor'` → Replace with `{containerId}`

## HTML Container

Add a div element to render the Document Editor Container.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document Editor Container</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" />
</head>
<body>
    <div id="DocumentEditor"></div>
</body>
</html>
```

## Key Configuration Options

- `enableToolbar` — Set to `true` to display the toolbar with formatting and document operation buttons.
- `height` — Define the container height (e.g., `'390px'` or `'100%'`).
- `serviceUrl` — Specify the server endpoint for operations requiring backend support (import, export, spell-check, etc.).

## Included UI Components

The Document Editor Container automatically includes:
- **Toolbar** — Provides formatting and document operation buttons.
- **Properties Pane** — Displays document properties and formatting options.
- **Status Bar** — Shows document statistics and editing state.
- **Document Editor** — Core editor for document creation and modification.

## Troubleshooting

**Styles not applied:** Verify all CSS imports use the same theme name.


