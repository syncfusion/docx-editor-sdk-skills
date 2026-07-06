# Getting Started with Syncfusion JavaScript Document Editor

## Table of Contents
- [When to Use This Reference](#when-to-use-this-reference)
- [Installation](#installation)
- [Setup for Local Development](#setup-for-local-development)
- [CSS References](#css-references)
- [Document Editor Container with Toolbar](#document-editor-container-with-toolbar)
- [Common Setup Gotchas](#common-setup-gotchas)

## When to Use This Reference

- Set up Document Editor component
- Create Document Editor implementation with toolbar

## Installation

The Syncfusion EJ2 Document Editor is available through the npm package registry. Before installation, ensure you have Node.js and npm installed on your machine.

### Install via npm

```bash
npm install @syncfusion/ej2-documenteditor --save
```

The `--save` flag adds the package to your project's `package.json` dependencies.

### Verify Installation

After installation, verify that the package is included in your `package.json`:

```json
{
  "dependencies": {
    "@syncfusion/ej2-documenteditor": "latest"
  }
}
```

## Setup for Local Development

### Using TypeScript with npm

For traditional TypeScript project setup:

```bash
mkdir my-editor-app
cd my-editor-app
npm init -y
npm install typescript ts-node @types/node --save-dev
npm install @syncfusion/ej2-documenteditor
```

### Using Webpack

For Webpack-based TypeScript projects:

```bash
npm install webpack webpack-cli webpack-dev-server typescript ts-loader --save-dev
npm install @syncfusion/ej2-documenteditor
```

## CSS References

The Document Editor component requires CSS files for styling. Add the following imports to your main CSS file or HTML file:

### Material Theme (Default)

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

### Other Available Themes

- Bootstrap: `bootstrap.css`
- Bootstrap 5: `bootstrap5.css`
- Material: `material.css`
- Material Dark: `material-dark.css`
- Tailwind CSS: `tailwind.css`

## Document Editor Container with Toolbar

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

### HTML Container

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

## Common Setup Gotchas

- **Missing styles**: All the `@syncfusion/ej2-*` CSS imports are required — the DOCX Editor uses styles from multiple packages.