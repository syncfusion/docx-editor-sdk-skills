# Getting started with Angular DOCX Editor
> Document Editor control creation — create document editor.

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Installation](#installation)
- [Package Setup](#package-setup)
- [Install Theme Package](#install-theme-package)
- [CSS Imports](#css-imports)
- [Document Editor Container with Toolbar](#document-editor-container-with-toolbar)
- [Common Setup Gotchas](#common-setup-gotchas)

## When to Use This Skill

Use this skill when you need to:
- Set up Document Editor component
- Create Document Editor implementation with toolbar

## Installation

Install Syncfusion Angular DOCX Editor component via npm:

```bash
npm install @syncfusion/ej2-angular-documenteditor
```

## Package Setup

Import the DocumentEditorContainerModule in your Angular module:

```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { DocumentEditorContainerModule } from '@syncfusion/ej2-angular-documenteditor';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, DocumentEditorContainerModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

## Install Theme Package

Install Syncfusion Tailwind3 theme package via npm:

```bash
npm install @syncfusion/ej2-tailwind3-theme
```

## CSS Imports

Add these to your `src/styles.css`. Use the theme that matches your app (tailwind, material, bootstrap5, fluent2, fabric, etc.):

```css
@import "../node_modules/@syncfusion/ej2-tailwind3-theme/styles/document-editor/index.css";
@import "../node_modules/@syncfusion/ej2-tailwind3-theme/styles/document-editor-container/index.css";
```

**Available themes:**
- tailwind (default)
- tailwind-dark
- material
- material-dark
- bootstrap5
- bootstrap5-dark
- fabric
- fabric-dark
- fluent2
- fluent2-dark

## Document Editor Container with Toolbar
**This is the default and recommended approach for most use cases.**

Create a DOCX Editor component with minimal configuration:

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