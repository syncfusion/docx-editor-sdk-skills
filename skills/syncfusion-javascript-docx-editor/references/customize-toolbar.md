# Toolbar and Properties Pane

Control the built-in toolbar and properties pane in `DocumentEditorContainer`.

## Add Custom Toolbar Item

This lets you add app-specific commands beside the built-in editor actions.

```ts
const customItem: CustomToolbarItemModel = {
  prefixIcon: 'e-de-ctnr-lock',
  tooltipText: 'Disable Image',
  text: 'Disable Image',
  id: 'Custom',
};

const toolbarItems: (CustomToolbarItemModel | ToolbarItem)[] = [
  customItem,
  'Undo',
  'Redo',
  'Separator',
  'Image',
];

let container = new DocumentEditorContainer({
  toolbarItems: toolbarItems
});
container.appendTo('#container');
```

## Hide Built-in Toolbar Items

Use a trimmed `toolbarItems` array when only selected built-in commands should be visible.

```ts
const toolbarItemsWithoutImage = toolbarItems.filter((item) => item !== 'Image');
```

## Enable or Disable Toolbar Items

This is useful for toggling commands based on selection or custom workflow state.

```ts
function onToolbarClick(args: any) {
  if (args.item.id === 'Custom') {
    container.toolbar.enableItems(4, false);
  }
}

container.toolbarClick = onToolbarClick;

// Re-enable later if needed
container.toolbar.enableItems(4, true);
```

**Placeholders**
- `4` → Replace with `{toolbarItemIndex}`

## Hide Properties Pane

Set this when you want the container UI without the built-in formatting pane.

```ts
let container = new DocumentEditorContainer({
  showPropertiesPane: false
});
```

## Hide Toolbar

Set this when you want the container view but plan to use your own toolbar or no toolbar at all.

```ts
let container = new DocumentEditorContainer({
  enableToolbar: false
});
```

## Minimal Wiring

This compact example shows the container configuration and toolbar click handler together.

```ts

let container = new DocumentEditorContainer({
  toolbarItems: toolbarItems,
  enableToolbar: true,
  showPropertiesPane: true,
  height: '600px'
});
container.appendTo('#container');

container.toolbarClick = (args: any): void => {
    switch (args.item.id) {
        case 'Custom':
            //Disable image toolbar item.
            container.toolbar.enableItems(4, false);
            break;
    }
};
```

**Note**
- `showPropertiesPane: false` hides the built-in pane, but repositioning or customizing that pane is not supported.
- Default `toolbarItems` are `['New', 'Open', 'Separator', 'Undo', 'Redo', 'Separator', 'Image', 'Table', 'Hyperlink', 'Bookmark', 'TableOfContents', 'Separator', 'Header', 'Footer', 'PageSetup', 'PageNumber', 'Break', 'InsertFootnote', 'InsertEndnote', 'Separator', 'Find', 'Separator', 'Comments', 'TrackChanges', 'Separator', 'LocalClipboard', 'RestrictEditing', 'Separator', 'FormFields', 'UpdateFields', 'ContentControl']`.
