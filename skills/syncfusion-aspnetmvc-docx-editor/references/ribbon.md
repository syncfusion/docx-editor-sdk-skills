# Ribbon

Enabling and configuring the Ribbon UI in the Document Editor.

## Enable Ribbon

Switch the toolbar mode from standard toolbar to the Ribbon UI.

```cshtml
@Html.EJS().DocumentEditorContainer("container").Height("590px").EnableToolbar(true).Render()
 
<script>
ej.documenteditor.DocumentEditorContainer.Inject(ej.documenteditor.Toolbar, ej.documenteditor.Ribbon);

    
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('container').ej2_instances[0];
  container.toolbarMode = 'Ribbon';
});

</script>
```

**Note**: Default `toolbarMode` is `"Toolbar"`; set to `"Ribbon"` to display the full-featured Ribbon interface.

## Ribbon Layouts

Choose between simplified or classic ribbon layout options.

```cshtml
@Html.EJS().DocumentEditorContainer("container").Height("590px").EnableToolbar(true).Render()
 
<script>
ej.documenteditor.DocumentEditorContainer.Inject(ej.documenteditor.Toolbar, ej.documenteditor.Ribbon);

    
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('container').ej2_instances[0];
  container.ribbonLayout = 'Classic';
  container.toolbarMode = 'Ribbon';
});

</script>
```

**Options**: `"Simplified"` (default, compact) or `"Classic"` (traditional Office-style)