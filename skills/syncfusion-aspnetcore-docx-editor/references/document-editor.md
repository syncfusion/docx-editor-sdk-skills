# Getting Started with Document Editor

Set up and initialize the Syncfusion Document Editor control in your ASP.NET Core application.

## Prerequisites

Ensure your system meets the [ASP.NET Core system requirements](https://ej2.syncfusion.com/aspnetcore/documentation/system-requirements) before installation.

## Install NuGet Package

Add the Syncfusion ASP.NET Core package to your project using the NuGet Package Manager.

```powershell
dotnet add package Syncfusion.EJ2.AspNet.Core
```

**Dependencies:** This package requires [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/) for JSON serialization and [Syncfusion.Licensing](https://www.nuget.org/packages/Syncfusion.Licensing/) for license validation.

## Register Tag Helper

Import the Syncfusion tag helper in your `_ViewImports.cshtml` file to use Document Editor components.

```html
@addTagHelper *, Syncfusion.EJ2
```

**File:** `~/Pages/_ViewImports.cshtml`

## Add Stylesheet and Script Resources

Reference the Syncfusion theme and script files in your `_Layout.cshtml` file.

```html
<head>
    ...
    <!-- Syncfusion ASP.NET Core controls styles -->
    <link rel="stylesheet" href="https://cdn.syncfusion.com/ej2/{product_version}/fluent.css" />
    <!-- Syncfusion ASP.NET Core controls scripts -->
    <script src="https://cdn.syncfusion.com/ej2/{product_version}/dist/ej2.min.js"></script>
</head>
```

**File:** `~/Pages/Shared/_Layout.cshtml`

## Register Script Manager

Add the Syncfusion script manager at the end of the `<body>` tag in your layout file.

```html
<body>
    ...
    <!-- Syncfusion ASP.NET Core Script Manager -->
    <ejs-scripts></ejs-scripts>
</body>
```

**File:** `~/Pages/Shared/_Layout.cshtml`

## Choose Component Option

The Document Editor comes in two variants:

- **DocumentEditor** - Lightweight, customizable component for building your own UI
- **DocumentEditorContainer** - Complete solution with toolbar, properties pane, and status bar

## Add Document Editor Control
Add the Document Editor Container tag helper to your page. This container includes toolbar, properties pane, and status bar.

**Document Editor Container (with toolbar and properties pane):**


```cshtml

<ejs-documenteditorcontainer id="container" ></ejs-documenteditorcontainer>

<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor = document.getElementById("container").ej2_instances[0];
    });
</script>
```

**File:** `~/Pages/Index.cshtml`

## Run the Application

Press <kbd>Ctrl</kbd>+<kbd>F5</kbd> (Windows) or <kbd>⌘</kbd>+<kbd>F5</kbd> (macOS) to run the application. The Document Editor control will render in your default web browser.

## Styling & Themes

For different theme options (CDN, NPM, or Custom Resource Generator), refer to the [Themes documentation](https://ej2.syncfusion.com/aspnetcore/documentation/appearance/theme).

## Script Reference Methods

For alternative approaches to adding script references, refer to the [Adding Script References documentation](https://ej2.syncfusion.com/aspnetcore/documentation/common/adding-script-references).
