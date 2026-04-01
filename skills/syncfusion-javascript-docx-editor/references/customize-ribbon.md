# Ribbon Customization

Customize the Document Editor ribbon by modifying menus, tabs, groups, and items to match your application workflow.

## Customize File Menu

Remove default File menu items and add custom items with event handlers.

```ts
const fileMenuItemClick = (args) => {
  if (args.item.id === '{customItemId}') {
    container.documentEditor.save('{fileName}', 'Docx');
  }
};

let container = new DocumentEditorContainer({
  enableToolbar: true,
  toolbarMode: 'Ribbon',
  fileMenuItems: [
    'New',
    'Print',
    { text: '{menuLabel}', id: '{customItemId}', iconCss: '{iconCss}' }
  ],
  fileMenuItemClick: fileMenuItemClick
});
```

**Placeholders**
- 'Print' → Replace with {itemName}
- '{menuLabel}' → Replace with {label}
- '{customItemId}' → Replace with {id}
- '{iconCss}' → Replace with {iconClass}

## Add Backstage Menu

Replace the standard File menu with a backstage panel for modern file operations.

```ts
let container = new DocumentEditorContainer({
  enableToolbar: true,
  toolbarMode: 'Ribbon',
  backstageMenu: {
    text: 'File',
    backButton: { text: 'Close' },
    items: [
      { id: '{itemId}', text: '{itemLabel}', iconCss: '{iconCss}' }
    ]
  }
});
```

**Placeholders**
- 'File' → Replace with {menuTitle}
- 'Close' → Replace with {backButtonLabel}

## Show/Hide Tab

Control visibility of ribbon tabs by name or custom ID.

```ts
container.ribbon.showTab('Home', false);
container.ribbon.showTab('{customTabId}', true);
```

## Add Tab

Insert custom tabs at the end or before a specific built-in tab.

```ts
const ribbonTab = {
  header: '{tabName}',
  id: '{customTabId}',
  groups: [{
    header: '{groupName}',
    collections: [{
      items: [{
        type: 'Button',
        buttonSettings: {
          content: '{buttonLabel}',
          iconCss: '{iconCss}',
          clicked: () => container.documentEditor.openBlank()
        }
      }]
    }]
  }]
};

container.ribbon.addTab(ribbonTab);
container.ribbon.addTab(ribbonTab, 'Insert');
```

**Placeholders**
- '{tabName}' → Replace with {name}
- '{customTabId}' → Replace with {id}
- '{groupName}' → Replace with {name}
- '{buttonLabel}' → Replace with {label}

## Show/Hide Group

Toggle group visibility within tabs by index or ID.

```ts
container.ribbon.showGroup({ tabId: 'Home', index: 1 }, false);
container.ribbon.showGroup('{customGroupId}', true);
```

## Add Group

Insert custom groups into existing tabs at any position.

```ts
const ribbonGroup = {
  header: '{groupName}',
  collections: [{
    items: [{
      type: 'Button',
      buttonSettings: {
        content: '{buttonLabel}',
        iconCss: '{iconCss}',
        clicked: () => container.documentEditor.openBlank()
      }
    }]
  }]
};

container.ribbon.addGroup('Home', ribbonGroup);
container.ribbon.addGroup('Home', ribbonGroup, 1);
```

## Show/Hide Item

Toggle visibility of ribbon items within groups by index or ID.

```ts
container.ribbon.showItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [5, 6] }, false);
container.ribbon.showItems('{customItemId}', true);
```

## Enable/Disable Item

Enable or disable ribbon items to control availability without hiding them.

```ts
container.ribbon.enableItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [7] }, false);
container.ribbon.enableItems('{customItemId}', true);
```

## Add Item

Insert new items into ribbon groups at any position.

```ts
const ribbonItem = {
  type: 'Button',
  buttonSettings: {
    content: '{buttonLabel}',
    iconCss: '{iconCss}',
    clicked: () => container.documentEditor.openBlank()
  }
};

container.ribbon.addItem({ tabId: 'Home', index: 0 }, ribbonItem);
container.ribbon.addItem({ tabId: 'Home', index: 0 }, ribbonItem, 1);
```

**Placeholders**
- '{buttonLabel}' → Replace with {label}
- '{iconCss}' → Replace with {cssClass}
- 'Home' → Replace with {tabId}
