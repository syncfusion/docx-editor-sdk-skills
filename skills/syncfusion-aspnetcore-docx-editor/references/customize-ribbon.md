# Ribbon Customization

Customize the Document Editor ribbon by modifying menus, tabs, groups, and items to match your application workflow.

## Customize File Menu
Remove default File menu items and add custom items with event handlers.

```cshtml
<ejs-documenteditorcontainer 
    id="container" 
    toolbarMode="Ribbon"
    fileMenuItems="@(new object[] {
        'New',
        'Print',
        new { text = 'Export', id = 'custom_item', iconCss = 'e-icons e-export' }
    })"
    fileMenuItemClick="onFileMenuItemClick">
</ejs-documenteditorcontainer>

<script>
    ej.documenteditor.DocumentEditorContainer.Inject(ej.documenteditor.Toolbar, ej.documenteditor.Ribbon);
    
    function onFileMenuItemClick(args) {
        if (args.item.id === 'custom_item') {
            var container = document.getElementById('container').ej2_instances[0];
            container.documentEditor.save('{fileName}', 'Docx');
        }
    }
</script>
```

**Placeholders**
- 'Print' → Replace with {itemName}
- 'Export' → Replace with {menuLabel}
- 'custom_item' → Replace with {customItemId}
- 'e-icons e-export' → Replace with {iconCss}
- '{fileName}' → Replace with {fileName}

## Add Backstage Menu
Replace the standard File menu with a backstage panel for modern file operations.

```cshtml

@{
    // Define backstage menu values in a property
    var backstageMenuConfig = new
    {
        text = "File",
        backButton = new { text = "Close" },
        items = new object[]
        {
            new { id = "openFile", text = "Open", iconCss = "e-icons e-open" },
            new { id = "saveFile", text = "Save", iconCss = "e-icons e-save" }
        }
    };
}

<!-- Document Editor with backstage menu -->
<ejs-documenteditorcontainer 
    id="container"
    toolbarMode="Ribbon"
    backstageMenu="@backstageMenuConfig">
</ejs-documenteditorcontainer>
```

**Placeholders**
- 'File' → Replace with {menuTitle}
- 'Close' → Replace with {backButtonLabel}
- '{itemId}' → Replace with {itemId}
- '{itemLabel}' → Replace with {itemLabel}
- '{iconCss}' → Replace with {iconCss}

## Show/Hide Tab
Control visibility of ribbon tabs by name or custom ID.

```javascript
container.ribbon.showTab('Home', false);
container.ribbon.showTab('{customTabId}', true);
```

## Add Tab
Insert custom tabs at the end or before a specific built-in tab.

```javascript
var ribbonTab = {
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
          clicked: function () {
            container.documentEditor.openBlank();
          }
        }
      }]
    }]
  }]
};

// Add tab at end
container.ribbon.addTab(ribbonTab);

// Add tab before specific tab
container.ribbon.addTab(ribbonTab, 'Insert');
```

**Placeholders**
- '{tabName}' → Replace with {name}
- '{customTabId}' → Replace with {id}
- '{groupName}' → Replace with {name}
- '{buttonLabel}' → Replace with {label}
- '{iconCss}' → Replace with {iconCss}

## Show/Hide Group

Toggle visibility of groups within a ribbon tab.

```javascript
// Hide group by index
container.ribbon.showGroup({ tabId: 'Home', index: 1 }, false);

// Show group by index
container.ribbon.showGroup({ tabId: 'Home', index: 1 }, true);

// Hide custom group by ID
container.ribbon.showGroup('custom_group', false);

// Show custom group by ID
container.ribbon.showGroup('custom_group', true);
```

## Add Group

Insert custom groups into ribbon tabs.

```javascript
var ribbonGroup = {
  header: '{groupHeader}',
  collections: [{
    items: [{
      type: 'Button',
      buttonSettings: {
        content: '{buttonText}',
        iconCss: '{iconCss}',
        clicked: function () {
          container.documentEditor.openBlank();
        }
      }
    }]
  }]
};

// Add group at end of tab
container.ribbon.addGroup('Home', ribbonGroup);

// Add group at specific position
container.ribbon.addGroup('Home', ribbonGroup, 1);
```

**Placeholders**
- '{groupHeader}' → Replace with {name}
- '{buttonText}' → Replace with {label}
- '{iconCss}' → Replace with {iconCss}

## Show/Hide Item

Toggle visibility of ribbon items within a group.

```javascript
// Hide items by index
container.ribbon.showItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [5, 6] }, false);

// Show items by index
container.ribbon.showItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [5, 6] }, true);

// Hide item by ID
container.ribbon.showItems('custom_item', false);

// Show item by ID
container.ribbon.showItems('custom_item', true);
```

## Enable/Disable Item

Control the enabled/disabled state of ribbon items.

```javascript
// Disable item by index
container.ribbon.enableItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [7] }, false);

// Enable item by index
container.ribbon.enableItems({ tabId: 'Home', groupIndex: 2, itemIndexes: [7] }, true);

// Disable item by ID
container.ribbon.enableItems('custom_item', false);

// Enable item by ID
container.ribbon.enableItems('custom_item', true);
```

## Add Item

Insert new buttons or controls into ribbon groups.

```javascript
var ribbonItem = {
  type: 'Button',
  buttonSettings: {
    content: '{buttonText}',
    iconCss: '{iconCss}',
    clicked: function () {
      container.documentEditor.openBlank();
    }
  }
};

// Add item at end of group
container.ribbon.addItem({ tabId: 'Home', index: 0 }, ribbonItem);

// Add item at specific position
container.ribbon.addItem({ tabId: 'Home', index: 0 }, ribbonItem, 1);
```

**Placeholders**
- '{buttonText}' → Replace with {label}
- '{iconCss}' → Replace with {iconCss}
