# Initialize Document Editor
> Document Editor control creation — create document editor.

## When to Use This Skill

Use this skill when you need to:
- Set up Document Editor component
- Create Document Editor implementation with toolbar

---

## Table of Contents
- [Install NuGet Package](#install-nuget-package)
- [Add Namespace to Web.config](#add-namespace-to-webconfig)
- [Add stylesheet and script resources in _Layout.cshtml](#add-stylesheet-and-script-resources-in-_layoutcshtml)
- [Register Script Manager](#register-script-manager)
- [CSS and Scripts Imports](#css-and-scripts-imports)
- [Document Editor Container with Toolbar](#document-editor-container-with-toolbar)

## Install Nuget Package
Install the required Syncfusion NuGet package:

**Package Manager Console:**

```powershell
Install-Package Syncfusion.EJ2.MVC5
```

```powershell
Install-Package Syncfusion.EJ2.WordEditor.AspNet.Mvc5
```

Dependencies installed automatically:
- `Newtonsoft.Json` (JSON serialization)
- `Syncfusion.Licensing` (license validation)

## Add Namespace to Web.config

Add the Syncfusion namespace in `Views\Web.config`:

```xml
<namespaces>
    <add namespace="Syncfusion.EJ2"/>
</namespaces>
```

## Add stylesheet and script resources in _Layout.cshtml

Include theme and script CDN inside the <head> of `~/Pages/Shared/_Layout.cshtml` file

```html
<head>
    ...
    <!-- Syncfusion ASP.NET MVC controls styles -->
    <link rel="stylesheet" href="https://cdn.syncfusion.com/ej2/33.1.44/fluent.css" />
    <!-- Syncfusion ASP.NET MVC controls scripts -->
    <script src="https://cdn.syncfusion.com/ej2/33.1.44/dist/ej2.min.js"></script>
</head>
```

## Register Script Manager

Register the Syncfusion script manager by adding the following to the end of the `<body>` in your `~/Views/Shared/_Layout.cshtml` (or `~/Pages/Shared/_Layout.cshtml`) so server-side helpers render required scripts:

```cs
<body>
    ...
    <!-- Syncfusion ASP.NET MVC Script Manager -->
    @Html.EJS().ScriptManager()
</body>
```
Notes:
- Adjust asset paths above to where the Syncfusion static assets are installed in your project (Content/Scripts or CDN).


## Document Editor Container with Toolbar 
**This is the default and recommended approach for most use cases.**

```cs

@Html.EJS().DocumentEditorContainer("container").Height("590px").EnableToolbar(true).Render()

<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor = document.getElementById("container").ej2_instances[0];
    });
</script>

```
