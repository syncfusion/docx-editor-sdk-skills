# Toolbar and Pane

Control the built-in toolbar and properties pane in `DocumentEditorContainerComponent`.

## Add Custom Toolbar Item
This lets you add app-specific commands beside the built-in editor actions.

```javascript
const customItem = {
  prefixIcon: 'e-de-ctnr-lock',
  tooltipText: 'Disable Image',
  text: 'Disable Image',
  id: 'Custom'
};

const toolbarItems = [
  customItem,
  'Undo',
  'Redo',
  'Separator',
  'Image'
];

// Apply to container
var container = document.getElementById("container").ej2_instances[0];
container.toolbarItems = toolbarItems;
```

## Hide Built-in Toolbar Items
Use a trimmed `toolbarItems` array when only selected built-in commands should be visible.

```javascript
// Filter out unwanted items (e.g., remove 'Image')
var toolbarItemsWithoutImage = toolbarItems.filter((item) => item !== 'Image');
container.toolbarItems = toolbarItemsWithoutImage;
```

## Hide Properties Pane
Set this when you want the container UI without the built-in formatting pane.

```cshtml
<ejs-documenteditorcontainer id="container" showPropertiesPane="false"></ejs-documenteditorcontainer>
```

## Hide Toolbar
Set this when you want the container view but plan to use your own toolbar or no toolbar at all.

```cshtml
<ejs-documenteditorcontainer id="container" enableToolbar="false"></ejs-documenteditorcontainer>
```

## Minimal Wiring
This compact example shows the container props and toolbar click handler together.

```cshtml
<ejs-documenteditorcontainer 
    id="container" 
    created="onDocCreate"
    showPropertiesPane="false">
</ejs-documenteditorcontainer>
```

```javascript
function onDocCreate() {
  var container = document.getElementById("container").ej2_instances[0];
  
  var toolItem = {
    prefixIcon: 'e-de-ctnr-lock',
    tooltipText: 'Disable Image',
    text: 'Disable Image',
    id: 'Custom'
  };
  
  container.toolbarItems = [
    toolItem, 'Undo', 'Redo', 'Separator', 'Image', 'Table', 
    'Hyperlink', 'Bookmark', 'TableOfContents', 'Separator', 
    'Header', 'Footer', 'PageSetup', 'PageNumber', 'Break', 
    'InsertFootnote', 'InsertEndnote', 'Separator', 'Find', 
    'Separator', 'Comments', 'TrackChanges', 'Separator', 
    'LocalClipboard', 'RestrictEditing', 'Separator', 'FormFields', 
    'UpdateFields', 'ContentControl'
  ];
  
  container.toolbarClick = function (args) {
    if (args.item.id === 'Custom') {
      const idx = container.toolbarItems.findIndex(
        (item) => item === 'Image' || (typeof item === 'object' && item.id === 'Image')
      );
      const imageIndex = idx === -1 ? {imageToolbarIndex} : idx;
      container.toolbar.enableItems(imageIndex, false);
    }
  };
}
```

**Note**
- `showPropertiesPane="false"` hides the built-in pane, but repositioning or customizing that pane is not supported.
- Default `toolbarItems` are `['New', 'Open', 'Separator', 'Undo', 'Redo', 'Separator', 'Image', 'Table', 'Hyperlink', 'Bookmark', 'TableOfContents', 'Separator', 'Header', 'Footer', 'PageSetup', 'PageNumber', 'Break', 'InsertFootnote', 'InsertEndnote', 'Separator', 'Find', 'Separator', 'Comments', 'TrackChanges', 'Separator', 'LocalClipboard', 'RestrictEditing', 'Separator', 'FormFields', 'UpdateFields', 'ContentControl']`.

## Enable or Disable Toolbar Items
This is useful for toggling commands based on selection or custom workflow state.

```javascript
function onToolbarClick(args) {
  if (args.item.id === 'Custom') {
    container.toolbar.enableItems(4, false);
  }
}

// Re-enable later if needed
container.toolbar.enableItems(4, true);
```

**Placeholders**
- 4 → Replace with {imageToolbarIndex}


