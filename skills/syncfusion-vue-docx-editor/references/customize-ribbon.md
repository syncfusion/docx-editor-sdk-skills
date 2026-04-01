# Customize Ribbon

Modify File menu, tabs, groups, and items in the Document Editor ribbon to match your application requirements.

## File Menu Customization

Replace or add custom items to the File menu.

```ts
<template>
<div class="control-section">
    <ejs-documenteditorcontainer ref="container" :toolbarMode="'Ribbon'" 
    :serviceUrl="hostUrl" :enableToolbar='true' height='600px' :fileMenuItems="fileMenuItems"
    @fileMenuItemClick="fileMenuClick"></ejs-documenteditorcontainer>
</div>
</template>
<script setup>
import { DocumentEditorContainerComponent, Toolbar, Ribbon } from "@syncfusion/ej2-vue-documenteditor";
import { onMounted, ref } from 'vue';

const documenteditorcontainer = ref(null);
provide('DocumentEditorContainer', [Toolbar, Ribbon]);
const fileMenuItems = [
  'New',
  'Print',
  { text: 'Export', id: 'custom_item', iconCss: 'e-icons e-export' }
];
function fileMenuClick(args) {
  if (args.item && args.item.id === 'custom_item') {
    container.value.ej2Instances.documentEditor.save('Sample', 'Docx');
  }
}
onMounted(() => {
  const editorInstance = container.value?.ej2Instances?.documentEditor;
});
</script>
```

**Placeholders**
- `'Export'` → Replace with `{customItemLabel}`
- `'custom_item'` → Replace with `{customItemId}`
- `'e-icons e-export'` → Replace with `{iconClass}`

## Backstage Menu

Add a backstage menu as an alternative to the File menu (automatically hides default File menu items).

```ts
<template>
<div class="control-section">
    <ejs-documenteditorcontainer ref="container" :toolbarMode="'Ribbon'" 
    :serviceUrl="hostUrl" :enableToolbar='true' height='600px' :backstageMenu="backstageMenu"
    @backstageItemClick="handleBackstageItemClick"></ejs-documenteditorcontainer>
</div>
</template>

<script>
import { DocumentEditorContainerComponent, Toolbar, Ribbon } from "@syncfusion/ej2-vue-documenteditor";
export default {
  components: {
    'ejs-documenteditorcontainer': DocumentEditorContainerComponent,
  },
  provide: {
    DocumentEditorContainer: [Toolbar, Ribbon]
  },
  data() {
    return {
      backstageMenu: {
        text: 'File',
        backButton: { text: 'close' },
        items: [
          { id: 'new', text: 'New', iconCss: 'e-icons e-de-ctnr-new' }
        ],
        visible: true
      }
    };
  },
  methods: {
    handleBackstageItemClick(args) {
      if (args.item) {
        this.$refs.container.ej2Instances.documentEditor.openBlank();
      }
    }
  }
};
</script>
```

**Placeholders**
- `'new'` → Replace with `{itemId}`
- `'New'` → Replace with `{itemLabel}`
- `'e-icons e-de-ctnr-new'` → Replace with `{iconClass}`

## Show or Hide Tab

Toggle visibility of built-in or custom tabs.

```ts
// Hide the Home tab
this.$refs.doceditcontainer.ej2Instances.ribbon.showTab('Home', false);

// Show a custom tab
this.$refs.doceditcontainer.ej2Instances.ribbon.showTab('{customTabId}', true);
```

**Placeholders**
- `'Home'` → Replace with `{builtInTabName}` (e.g., Home, Insert, Review, View)
- `'custom_tab'` → Replace with `{customTabId}`

## Add Tab

Insert a new custom tab to the ribbon (at the end or before an existing tab).

```ts
const ribbonTab = {
  header: 'Custom Tab',
  id: 'custom_tab',
  groups: [{
    header: 'Custom Group',
    collections: [{
      items: [{
        type: 'Button',
        buttonSettings: {
          content: 'New',
          iconCss: 'e-icons e-de-ctnr-new',
          clicked: () => {
            // Button action
          }
        }
      }]
    }]
  }]
};

// Add at end of ribbon
this.$refs.container.ej2Instances.ribbon.addTab(ribbonTab);

// Add before existing tab
this.$refs.container.ej2Instances.ribbon.addTab(ribbonTab, 'insert');

```

**Placeholders**
- `'Custom Tab'` → Replace with `{tabLabel}`
- `'custom_tab'` → Replace with `{tabId}`
- `'Custom Group'` → Replace with `{groupLabel}`
- `'New'` → Replace with `{buttonLabel}`
- `'e-icons e-de-ctnr-new'` → Replace with `{iconClass}`
- `'Insert'` → Replace with `{targetTabName}`

## Show or Hide Group

Toggle visibility of groups within a tab.

```ts
// Hide group by index
this.$refs.doceditcontainer.ej2Instances.ribbon.showGroup(
  { tabId: '{tabName}', index: {groupIndex} },
  false
);

// Hide group by custom ID
this.$refs.doceditcontainer.ej2Instances.ribbon.showGroup('{customGroupId}', false);

// Show group
this.$refs.doceditcontainer.ej2Instances.ribbon.showGroup(
  { tabId: '{tabName}', index: {groupIndex} },
  true
);
```

**Placeholders**
- `'Home'` → Replace with `{tabName}`
- `1` → Replace with `{groupIndex}`
- `'custom_group'` → Replace with `{customGroupId}`

## Add Group

Insert a new group into a ribbon tab (at the end or at a specific index).

```ts
const ribbonGroup = {
  header: 'Custom Group',
  collections: [{
    items: [{
      type: 'Button',
      buttonSettings: {
        content: 'New',
        iconCss: 'e-icons e-de-ctnr-new',
        clicked: () => {
          // Group item action
        }
      }
    }]
  }]
};

// Add at end of tab
this.$refs.container.ej2Instances.ribbon.addGroup('Home' ribbonGroup);

// Add at specific index
this.$refs.container.ej2Instances.ribbon.addGroup('Home', ribbonGroup, 1);
```

**Placeholders**
- `'Custom Group'` → Replace with `{groupLabel}`
- `'New'` → Replace with `{buttonLabel}`
- `'e-icons e-de-ctnr-new'` → Replace with `{iconClass}`
- `'Home'` → Replace with `{tabName}`
- `1` → Replace with `{insertIndex}`

## Show or Hide Item

Toggle visibility of items within a ribbon group.

```ts
// To hide the Bold and Italic items using ribbon item information
this.$refs.container.ej2Instances.ribbon.showItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [5, 6] } , false);

// To show the Bold and Italic items using ribbon item information
this.$refs.container.ej2Instances.ribbon.showItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [5, 6] } , true);

// To hide the item using item id
this.$refs.container.ej2Instances.ribbon.showItems('custom_item', false);
```

**Placeholders**
- `'Home'` → Replace with `{tabName}`
- `2` → Replace with `{groupIndex}`
- `[5, 6]` → Replace with `{itemIndices}`
- `'custom_item'` → Replace with `{customItemId}`

## Enable or Disable Item

Control the enabled state of items in the ribbon.

```ts
// To disable the underline using ribbon item info
this.$refs.container.ej2Instances.ribbon.enableItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [7] },false);

// To enable the underline using ribbon item info
this.$refs.container.ej2Instances.ribbon.enableItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [7] },true);

// To disable the item using id
this.$refs.container.ej2Instances.ribbon.enableItems('custom_item', false);
```

**Placeholders**
- `'Home'` → Replace with `{tabName}`
- `2` → Replace with `{groupIndex}`
- `[7]` → Replace with `{itemIndices}`
- `'custom_item'` → Replace with `{customItemId}`

## Add Item

Insert a new item into a ribbon group (at the end or at a specific index).

```ts
const ribbonItem = {
  type: 'Button',
  buttonSettings: {
    content: 'New',
    iconCss: 'e-icons e-de-ctnr-new',
    clicked: () => {
      // Item action
    }
  }
};

// Add at end of group
this.$refs.container.ej2Instances.ribbon.addItem(
  { tabId: 'Home', index: 0 },
  ribbonItem
);

// Add at specific item index
this.$refs.container.ej2Instances.ribbon.addItem(
  { tabId: 'Home', index: 0 }, ribbonItem, 1);
```

**Placeholders**
- `'New'` → Replace with `{itemLabel}`
- `'e-icons e-de-ctnr-new'` → Replace with `{iconClass}`
- `'Home'` → Replace with `{tabName}`
- `0` → Replace with `{groupIndex}`
- `1` → Replace with `{itemIndex}`

> **Note:** Set `toolbarMode="Ribbon"` in the DocumentEditorContainer component to enable ribbon customization. All customization APIs work on the `ribbon` instance accessed via `this.$refs.container.ej2Instances.ribbon`.
