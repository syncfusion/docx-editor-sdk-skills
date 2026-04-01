# Document Editor - Editor Only Mode (Advanced)


> Advanced initialization for fine-grained control without the container toolbar.

Use this mode when you need **advanced customization** and control over the editor without the built-in container toolbar.

---
## ⚠️ CRITICAL: Single-Line Format REQUIRED

> **This is NOT optional.** You MUST use single-line chaining format for the Razor helper. Multi-line formatting **WILL cause runtime errors**. Do not reformat this code for readability.

---

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

## Document Editor
**This is the default and recommended approach for most use cases.**

### ✅ CORRECT Format (Single-Line Chaining - REQUIRED)

```cshtml
@Html.EJS().DocumentEditor("container").Height("590px").Width("890px").IsReadOnly(false).EnablePrint(true).EnableSelection(true).EnableEditor(true).EnableEditorHistory(true).EnableContextMenu(true).EnableSearch(true).EnableOptionsPane(true).EnableBookmarkDialog(true).EnableBordersAndShadingDialog(true).EnableFontDialog(true).EnableTableDialog(true).EnableParagraphDialog(true).EnableHyperlinkDialog(true).EnableImageResizer(true).EnableListDialog(true).EnablePageSetupDialog(true).EnableSfdtExport(true).EnableStyleDialog(true).EnableTableOfContentsDialog(true).EnableTableOptionsDialog(true).EnableTablePropertiesDialog(true).EnableTextExport(true).EnableWordExport(true).Render()

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0]; 
    });
</script>
```

### ❌ INCORRECT Format (DO NOT USE - Causes Runtime Errors)

```cshtml
<!-- This format WILL FAIL at runtime! -->
@Html.EJS().DocumentEditor("container").Height("590px").Width("890px").IsReadOnly(false).EnablePrint(true).EnableSelection(true).EnableEditor(true).Render()
```

**Why multi-line fails:** The Razor engine requires fluent API methods to be chained on a single line. Breaking methods across multiple lines interrupts the method chain and causes runtime parsing errors.


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

## Key Differences from Container Mode

| Feature | Editor Only | Container |
|---------|-----------|-----------|
| **Toolbar** | Not included (manual control) | Built-in toolbar |
| **Use Case** | Advanced customization, custom toolbars | Standard document editing |
| **Module Injection** | Manual (inject specific modules) | Automatic (Toolbar injected) |
| **Complexity** | Higher | Lower |
| **Flexibility** | Maximum | Limited |
