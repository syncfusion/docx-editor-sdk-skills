# Toolbar and Pane

Control the built-in toolbar and properties pane in `DocumentEditorContainerComponent`.

## Add Custom Toolbar Item
This lets you add app-specific commands beside the built-in editor actions.

```tsx
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
```

## Hide Built-in Toolbar Items
Use a trimmed `toolbarItems` array when only selected built-in commands should be visible.

```tsx
const toolbarItemsWithoutImage = toolbarItems.filter((item) => item !== 'Image');

container.toolbarItems = toolbarItemsWithoutImage;
```

## Enable or Disable Toolbar Items
This is useful for toggling commands based on selection or custom workflow state.

```tsx
function onToolbarClick(args: any) {
  if (args.item.id === 'Custom') {
    container.toolbar.enableItems(4, false);
  }
}

// Re-enable later if needed
container.toolbar.enableItems(4, true);
```

**Placeholders**
- 4 → Replace with {imageToolbarIndex}

## Hide Properties Pane
Set this when you want the container UI without the built-in formatting pane.

```tsx
<DocumentEditorContainerComponent showPropertiesPane={false} />
```

## Hide Toolbar
Set this when you want the container view but plan to use your own toolbar or no toolbar at all.

```tsx
<DocumentEditorContainerComponent enableToolbar={false} />
```

## Minimal Wiring
This compact example shows the container props and toolbar click handler together.

```tsx
<DocumentEditorContainerComponent
  id="container"
  ref={(scope) => {
    container = scope;
  }}
  toolbarItems={toolbarItems}
  toolbarClick={onToolbarClick}
  showPropertiesPane={false}
/>

function onToolbarClick(args: any) {
  if (args.item.id === 'Custom') {
    const idx = toolbarItems.findIndex(
      (item) => item === 'Image' || (item as CustomToolbarItemModel).id === 'Image'
    );
    const imageIndex = idx === -1 ? {imageToolbarIndex} : idx;
    container.toolbar.enableItems(imageIndex, false);
  }
}
```

**Note**
- `showPropertiesPane={false}` hides the built-in pane, but repositioning or customizing that pane is not supported.
- Default `toolbarItems` are `['New', 'Open', 'Separator', 'Undo', 'Redo', 'Separator', 'Image', 'Table', 'Hyperlink', 'Bookmark', 'TableOfContents', 'Separator', 'Header', 'Footer', 'PageSetup', 'PageNumber', 'Break', 'InsertFootnote', 'InsertEndnote', 'Separator', 'Find', 'Separator', 'Comments', 'TrackChanges', 'Separator', 'LocalClipboard', 'RestrictEditing', 'Separator', 'FormFields', 'UpdateFields', 'ContentControl']`.



