# Customize Toolbar

Manage toolbar items, enable/disable commands, and control pane visibility in the DocumentEditorContainer.

## Setup

All JavaScript code examples assume `container` is already initialized as:
```javascript
var container = document.getElementById('container').ej2_instances[0];
```

This is the standard container instance pattern for accessing the Syncfusion DOCX Editor Container API.

## Add Custom Toolbar Item

Add app-specific commands beside built-in editor actions.

```javascript
var customItem = {
  prefixIcon: 'e-de-ctnr-lock',
  tooltipText: 'Disable Image',
  text: 'Disable Image',
  id: 'Custom'
};

container.toolbarItems = [customItem, 'Undo', 'Redo', 'Separator', 'Image'];
```

**Placeholders**
- `'e-de-ctnr-lock'` → Replace with `{iconClass}`
- `'Disable Image'` → Replace with `{tooltipText}`

## Remove Built-in Toolbar Items

Filter the toolbar to show only selected built-in commands.

```javascript
var toolbarItemsFiltered = container.toolbarItems.filter(function(item) {
  return item !== 'Image' && item !== 'Table';
});
container.toolbarItems = toolbarItemsFiltered;
```

## Enable or Disable Toolbar Items

Toggle commands based on selection, user role, or workflow state.

```javascript
// Disable the item at index 4
container.toolbar.enableItems(4, false);

// Re-enable later
container.toolbar.enableItems(4, true);
```

**Placeholders**
- `4` → Replace with `{toolbarItemIndex}`


## Hide Properties Pane

Remove the built-in formatting panel from the container UI.

```cshtml
@Html.EJS().DocumentEditorContainer("container").ShowPropertiesPane(false).Render()
```

**Note**: Repositioning or customizing the properties pane is not supported; use `ShowPropertiesPane(false)` only.

## Hide Toolbar

Remove the toolbar from the container UI when using a custom toolbar or no toolbar.

```cshtml
@Html.EJS().DocumentEditorContainer("container").EnableToolbar(false).Render()
```

## Configure at Initialization

Combine toolbar customization settings in the Razor component.

```cshtml
@Html.EJS().DocumentEditorContainer("container").Created("onDocCreate") .EnableToolbar(true).Render()

<script>
  function onDocCreate() {
    var container = document.getElementById('container').ej2_instances[0];
    
    var customItem = {
      prefixIcon: 'e-de-ctnr-lock',
      tooltipText: 'Custom Action',
      text: 'Custom',
      id: 'Custom'
    };
    
    container.toolbarItems = [customItem, 'Undo', 'Redo', 'Separator', 'Image'];
    
    container.toolbarClick = function(args) {
      if (args.item.id === 'Custom') {
        console.log('Custom item clicked');
      }
    };
  }
</script>
```

## Default Toolbar Items

Reference list of all built-in toolbar items:
`'New'`, `'Open'`, `'Separator'`, `'Undo'`, `'Redo'`, `'Separator'`, `'Image'`, `'Table'`, `'Hyperlink'`, `'Bookmark'`, `'TableOfContents'`, `'Separator'`, `'Header'`, `'Footer'`, `'PageSetup'`, `'PageNumber'`, `'Break'`, `'InsertFootnote'`, `'InsertEndnote'`, `'Separator'`, `'Find'`, `'Separator'`, `'Comments'`, `'TrackChanges'`, `'Separator'`, `'LocalClipboard'`, `'RestrictEditing'`, `'Separator'`, `'FormFields'`, `'UpdateFields'`, `'ContentControl'`
