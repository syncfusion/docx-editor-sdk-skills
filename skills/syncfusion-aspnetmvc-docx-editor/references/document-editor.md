# Initialize Document Editor
> Document Editor control creation — create document editor.

## Install package
- NuGet package: `Syncfusion.EJ2.WordEditor.AspNet.Mvc5`

## Add stylesheet and script resources

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

## Register Syncfusion® Script Manager

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
