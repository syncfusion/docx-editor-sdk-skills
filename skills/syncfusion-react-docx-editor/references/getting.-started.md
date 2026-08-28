# Getting started with React DOCX Editor
> Document Editor control creation — create document editor.

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Installation](#installation)
- [Setup for Local Development](#setup-for-local-development)
- [CSS Imports](#css-imports)
- [Document Editor Container with Toolbar ](#document-editor-container-with-toolbar)
- [Common Setup Gotchas](#common-setup-gotchas)

## When to Use This Skill

Use this skill when you need to:
- Set up Document Editor component
- Create Document Editor implementation with toolbar

## Installation

The Syncfusion React DOCX Editor is available through the npm package registry. Before installation, ensure you have Node.js and npm installed on your machine.

### Install via npm

```bash
npm install @syncfusion/ej2-react-documenteditor --save
```
The `--save` flag adds the package to your project's `package.json` dependencies.

### Verify Installation

After installation, verify that the package is included in your `package.json`:

```json
{
  "dependencies": {
    "@syncfusion/ej2-react-documenteditor": "latest"
  }
}
```

## Setup for Local Development

### Using Vite (Recommended)

Vite provides faster development environments with smaller bundle sizes compared to traditional tools.

```bash
npm create vite@latest documenteditor-app -- --template react-ts
cd documenteditor-app
npm run dev
```

### Using Create React App

For traditional React app setup:

```bash
npx create-react-app documenteditor-app
cd documenteditor-app
npm install @syncfusion/ej2-react-documenteditor
```

### Using Next.js

For Next.js projects:

```bash
npx create-next-app@latest documenteditor-app
cd documenteditor-app
npm install @syncfusion/ej2-react-documenteditor
```

## CSS Imports

### Install Theme Package

Install Syncfusion Tailwind3 theme package via npm:

```bash
npm install @syncfusion/ej2-tailwind3-theme
```

### Tailwind3 Theme (Default)

Add these to your `src/App.css`. Use the theme that matches your app (tailwind3, material, bootstrap5, fluent2, etc.).

```css
@import "../node_modules/@syncfusion/ej2-tailwind3-theme/styles/document-editor/index.css";
@import "../node_modules/@syncfusion/ej2-tailwind3-theme/styles/document-editor-container/index.css";
```

Import CSS in your App.tsx:

```tsx
import './App.css';
```

### Other Available Themes

Each theme has its own npm package. Install the one you want, then replace `tailwind3` in the import paths with the matching theme name.

| Theme | npm package |
|---|---|
| `tailwind3` (default) | `@syncfusion/ej2-tailwind3-theme` |
| `tailwind3-dark` | `@syncfusion/ej2-tailwind3-dark-theme` |
| `material3` | `@syncfusion/ej2-material3-theme` |
| `material3-dark` | `@syncfusion/ej2-material3-dark-theme` |
| `material` | `@syncfusion/ej2-material-theme` |
| `material-dark` | `@syncfusion/ej2-material-dark-theme` |
| `bootstrap5` | `@syncfusion/ej2-bootstrap5-theme` |
| `bootstrap5-dark` | `@syncfusion/ej2-bootstrap5-dark-theme` |
| `fluent2` | `@syncfusion/ej2-fluent2-theme` |
| `fluent2-dark` | `@syncfusion/ej2-fluent2-dark-theme` |

**Example:** To use the `material` theme instead of `tailwind3`:

```bash
npm install @syncfusion/ej2-material-theme
```

```css
  @import "../node_modules/@syncfusion/ej2-material-theme/styles/document-editor/index.css";
  @import "../node_modules/@syncfusion/ej2-material-theme/styles/document-editor-container/index.css";
```

## Document Editor Container with Toolbar 
**This is the default and recommended approach for most use cases.**

```tsx

import { DocumentEditorContainerComponent, Toolbar } from '@syncfusion/ej2-react-documenteditor';
import './App.css';

DocumentEditorContainerComponent.Inject(Toolbar);

function App() {
    return (
        <DocumentEditorContainerComponent 
            id="container" 
            height={'590px'} 
            serviceUrl="https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/" 
            enableToolbar={true}
        />
    );
}

export default App;
```

## Common Setup Gotchas
 
- **Missing styles**: All the `@syncfusion/ej2-*` CSS imports are required — the DOCX Editor uses styles from multiple packages.