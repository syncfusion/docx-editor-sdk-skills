# Customize Toolbar

Add, show, hide, enable, or disable items in the Document Editor toolbar.

## Add Custom Items

Insert new custom toolbar items alongside built-in items.

```ts
<template>
  <div id="app">
    <ejs-documenteditorcontainer ref="container" :toolbarItems='items' v-bind:toolbarClick='onToolbarClick'
      :enableToolbar='true'> </ejs-documenteditorcontainer>
  </div>
</template>

<script setup>
import { DocumentEditorContainerComponent as EjsDocumenteditorcontainer, Toolbar } from '@syncfusion/ej2-vue-documenteditor';
import { provide, ref } from 'vue';

const container = ref(null);
const onWrapText = function (text) {
  let content = '';
    const index = text.lastIndexOf(' ');
    if (index !== -1) {
        content = text.slice(0, index) + "<div class='e-de-text-wrap'>" + text.slice(index + 1) + "<div>";
    } else {
        content = text;
    }

    return content;
}
const items = [
  {
    prefixIcon: "e-de-ctnr-lock",
    tooltipText: "Disable Image",
    text: onWrapText("Disable Image"),
    id: "Custom"
  },
  'Undo', 'Redo', 'Separator', 'Image', 'Table', 'Hyperlink', 'Bookmark', 'TableOfContents', 'Separator', 'Header', 'Footer', 'PageSetup', 'PageNumber', 'Break', 'InsertFootnote', 'InsertEndnote', 'Separator', 'Find', 'Separator', 'Comments', 'TrackChanges', 'Separator', 'LocalClipboard', 'RestrictEditing', 'Separator', 'FormFields', 'UpdateFields','ContentControl']

provide('DocumentEditorContainer', [Toolbar]);

const onToolbarClick = function (args) {
  switch (args.item.id) {
    case 'Custom':
      //Disable image toolbar item.
      container.value.ej2Instances.toolbar.enableItems(4, false);
      break;
  }
}
</script>
```

**Placeholders**
- `'e-de-ctnr-lock'` → Replace with `{iconClass}`
- `'Disable Image'` → Replace with `{tooltipText}`
- `'Custom'` → Replace with `{customItemId}`

## Show or Hide Items

Control visibility of built-in or custom toolbar items.

```ts
const items = [
  'Undo', 'Redo',
  // 'Image',     // Hide by omitting from array
  'Table',
  'Hyperlink',
  'Separator',
  'Comments',
  'TrackChanges'
  // Include or exclude items as needed
];
```

## Enable or Disable Items

Control the enabled state of toolbar items by index or ID.

```ts
// Disable item by index
this.$refs.container.ej2Instances.toolbar.enableItems({itemIndex}, false);

// Enable item by index
this.$refs.container.ej2Instances.toolbar.enableItems({itemIndex}, true);

// Disable item by ID
this.$refs.container.ej2Instances.toolbar.enableItems('{customItemId}', false);

// Enable item by ID
this.$refs.container.ej2Instances.toolbar.enableItems('{customItemId}', true);
```

**Placeholders**
- `4` → Replace with `{itemIndex}`
- `'Custom'`` → Replace with `{customItemId}`

## Built-in Toolbar Items

Available predefined items for inclusion in the toolbar array:

- Basic: `Undo`, `Redo`, `Separator`
- Insertion: `Image`, `Table`, `Hyperlink`, `Bookmark`, `TableOfContents`
- Layout: `Header`, `Footer`, `PageSetup`, `PageNumber`, `Break`
- References: `InsertFootnote`, `InsertEndnote`
- Editing: `Find`
- Collaboration: `Comments`, `TrackChanges`, `LocalClipboard`
- Protection: `RestrictEditing`
- Forms: `FormFields`, `UpdateFields`, `ContentControl`

> **Note:** The default toolbar includes all standard items listed above. Customize by passing a custom `toolbarItems` array with the items you want to display. Built-in items are identified by their name strings (e.g., 'Image', 'Table'); custom items require an `id` property to handle events.
