# Document Editor

Create and initialize a basic Document Editor component for viewing and editing Word documents with customizable options.

## Initialize Document Editor

Set up the core Document Editor component with essential configuration.

```tsx
import { DocumentEditor } from '@syncfusion/ej2-documenteditor';

const documenteditor = new DocumentEditor({ 
    isReadOnly: false, 
    height: '370px', 
    serviceUrl: 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/' 
});

documenteditor.enableAllModules();
documenteditor.appendTo('#DocumentEditor');
```

**Placeholders**
- `'370px'` → Replace with `{editorHeight}`
- `'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/'` → Replace with `{serviceUrl}`
- `'#DocumentEditor'` → Replace with `{containerId}`

## HTML Container

Add a div element to render the Document Editor.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document Editor</title>
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

- `isReadOnly` — Set to `true` to prevent document editing.
- `height` — Define the editor container height (e.g., `'370px'` or `'100%'`).
- `serviceUrl` — Specify the server endpoint for operations requiring backend support (import, export, spell-check, etc.).

## Dependencies Required

Ensure the following npm package is installed:

```bash
npm install @syncfusion/ej2-documenteditor
```

The package automatically installs its dependencies:
- `@syncfusion/ej2-base`
- `@syncfusion/ej2-buttons`
- `@syncfusion/ej2-dropdowns`
- `@syncfusion/ej2-inputs`
- `@syncfusion/ej2-navigations`
- `@syncfusion/ej2-popups`
- Other supporting modules
