# Document Editor (Editor-only)

Instructions and code snippets for using the lightweight, editor-only `DocumentEditor` (no container).

## Prerequisites

Ensure your system meets the [ASP.NET Core system requirements](https://ej2.syncfusion.com/aspnetcore/documentation/system-requirements) before installation.

## Install NuGet Package

Add the Syncfusion ASP.NET Core package to your project using the NuGet Package Manager.

```powershell
dotnet add package Syncfusion.EJ2.AspNet.Core
```

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
    <!-- Syncfusion ASP.NET Core controls styles -->
    <link rel="stylesheet" href="https://cdn.syncfusion.com/ej2/{{ site.ej2version }}/fluent.css" />
    <!-- Syncfusion ASP.NET Core controls scripts -->
    <script src="https://cdn.syncfusion.com/ej2/{{ site.ej2version }}/dist/ej2.min.js"></script>
</head>
```

**File:** `~/Pages/Shared/_Layout.cshtml`

## Register Script Manager

Add the Syncfusion script manager at the end of the `<body>` tag in your layout file.

```html
<body>
    <!-- Syncfusion ASP.NET Core Script Manager -->
    <ejs-scripts></ejs-scripts>
</body>
```

**File:** `~/Pages/Shared/_Layout.cshtml`

## Add Document Editor Control (Editor-only)

Add the lightweight `DocumentEditor` tag helper to your page when you want to build a custom UI without the full container.

**Basic Document Editor:**


```cshtml
<ejs-documenteditor id="container" isReadOnly = "false" enableEditor = "true" ></ejs-documenteditor>

<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor = document.getElementById("container").ej2_instances[0];
    });
</script>
```

**File:** `~/Pages/Index.cshtml`

## Run the Application

Press <kbd>Ctrl</kbd>+<kbd>F5</kbd> (Windows) or <kbd>⌘</kbd>+<kbd>F5</kbd> (macOS) to run the application. The editor will render in your default web browser.
