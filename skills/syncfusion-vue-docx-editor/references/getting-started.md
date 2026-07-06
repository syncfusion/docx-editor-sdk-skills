> Document Editor control creation — create document editor.

## Table of Contents
- [When to Use](#when-to-use)
- [Vue 3 Project Setup](#vue-3-project-setup)
- [Vue 2 Project Setup](#vue-2-project-setup)
- [Import CSS Styles](#import-css-styles)
- [Document Editor Container with Toolbar](#document-editor-container-with-toolbar)
- [Running Your Project](#running-your-project)
- [Common Setup Gotchas](#common-setup-gotchas)

## When to Use

Use this skill when you need to:
- Set up Document Editor component
- Create Document Editor implementation with toolbar

---

## Vue 3 Project Setup

### Create a New Vue 3 Application with Vite

Run the following command to create a new Vue 3 project:

```bash
npm create vite@latest documenteditor-app -- --template vue
```

**Project Configuration Steps:**

1. **Navigate to the created project:**
   ```bash
   cd documenteditor-app
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```
   
   Or using yarn:
   ```bash
   yarn install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

### Install Syncfusion Vue Document Editor Package

The Document Editor package is available in the public npm registry. Install it using the following command:

```bash
npm install @syncfusion/ej2-vue-documenteditor --save
```

Or using yarn:

```bash
yarn add @syncfusion/ej2-vue-documenteditor
```

## Vue 2 Project Setup

### Using Vue CLI

Generate a Vue 2 project using Vue-CLI with these commands:

```bash
npm install -g @vue/cli
vue create quickstart
```

When prompted, select the option: `Default ([Vue 2] babel, eslint)` from the menu.

Then navigate to the project and start the development server:

```bash
cd quickstart
npm run serve
```

Or using yarn:

```bash
yarn global add @vue/cli
vue create quickstart
cd quickstart
yarn run serve
```

### Install Document Editor Package for Vue 2

After creating your Vue 2 project, install the Syncfusion Document Editor package:

```bash
npm install @syncfusion/ej2-vue-documenteditor --save
```

Or using yarn:

```bash
yarn add @syncfusion/ej2-vue-documenteditor
```

> **Note:** The `@syncfusion/ej2-vue-documenteditor` package supports both Vue 2 and Vue 3. Vue 2 users should ensure compatibility with their project's Vue version.

## Import CSS Styles

Syncfusion components require CSS stylesheets to display correctly. Import the Material theme (or your preferred theme) into the `<style>` section of your main component file.

### Vue 3 (App.vue or src/app.vue)

```vue
<style>
  @import "../node_modules/@syncfusion/ej2-base/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-buttons/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-inputs/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-dropdowns/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-lists/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-navigations/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-popups/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-splitbuttons/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-documenteditor/styles/material.css";
</style>
```

### Vue 2 (App.vue)

```vue
<style>
  @import "../node_modules/@syncfusion/ej2-base/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-buttons/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-inputs/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-dropdowns/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-lists/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-navigations/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-popups/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-splitbuttons/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-documenteditor/styles/material.css";
</style>
```

### Available Themes

Replace `material` in the import paths with any of the following themes:

- **material** (default)
- **material-dark**
- **bootstrap5**
- **bootstrap5-dark**
- **tailwind**
- **tailwind-dark**
- **fluent2**
- **fluent2-dark**

**Example:** To use the bootstrap5 theme, replace `material.css` with `bootstrap5.css` in all import statements.

## Document Editor Container with Toolbar 

**This is the default and recommended approach for most use cases.**

#### Vue 3 (App.vue)

```vue
<template>
  <ejs-documenteditorcontainer 
   height="590px"
   :serviceUrl="serviceUrl" 
   :enableToolbar="true"> 
  </ejs-documenteditorcontainer>
</template>

<script setup>
  import { provide } from 'vue';
  import { DocumentEditorContainerComponent as EjsDocumenteditorcontainer, Toolbar } from '@syncfusion/ej2-vue-documenteditor';
  
  // Use the following service URL only for demo purposes
  const serviceUrl = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';

  provide('DocumentEditorContainer', [Toolbar]);
</script>

<style>
  @import "../node_modules/@syncfusion/ej2-base/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-buttons/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-inputs/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-dropdowns/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-lists/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-navigations/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-popups/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-splitbuttons/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-documenteditor/styles/material.css";
</style>
```

#### Vue 2 (App.vue)

```vue
<template>
  <div id="app">
    <ejs-documenteditorcontainer
      height="590px"
      :serviceUrl="serviceUrl"
      :enableToolbar="true">
    </ejs-documenteditorcontainer>
  </div>
</template>

<script>
import { DocumentEditorContainerComponent, Toolbar } from '@syncfusion/ej2-vue-documenteditor';

export default {
  name: "App",

  components: {
    "ejs-documenteditorcontainer": DocumentEditorContainerComponent
  },

  data() {
    // Use the following service URL only for demo purposes
    return {
      serviceUrl: 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/'
    };
  },

  provide: {
    // Inject required modules.
    DocumentEditorContainer: [Toolbar]
  }
};
</script>

<style>
  @import "../node_modules/@syncfusion/ej2-base/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-buttons/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-inputs/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-dropdowns/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-lists/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-navigations/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-popups/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-splitbuttons/styles/material.css";
  @import "../node_modules/@syncfusion/ej2-documenteditor/styles/material.css";
</style>
```

## Running Your Project

### Vue 3 (Vite)

To start the development server for your Vue 3 project:

```bash
npm run dev
```

The application will be available at `http://localhost:5173` (or the next available port).

### Vue 2 (Vue CLI)

To start the development server for your Vue 2 project:

```bash
npm run serve
```

Or using yarn:

```bash
yarn run serve
```

## Common Setup Gotchas
 
- **Missing styles**: All the `@syncfusion/ej2-*` CSS imports are required — the DOCX Editor uses styles from multiple packages.