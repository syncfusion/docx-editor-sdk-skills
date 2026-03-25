# Restrict Editing

Control document editing by restricting changes to specific users or regions. Authorize users and highlight editable areas.

## Set Current User

Authorize the current user by name, email, or user group to access protected regions.

```typescript
this.container.documentEditor.currentUser = 'engineer@mycompany.com';
```

**Placeholders**
- `'engineer@mycompany.com'` → Replace with `{userNameOrEmail}`

**Note:** Set this before applying document protection. Used with range permissions to identify who can edit specific text areas.

## Highlight User's Editable Regions

Assign a color to visually distinguish editable areas assigned to the current user.

```typescript
this.container.documentEditor.userColor = '#fff000';
```

**Placeholders**
- `'#fff000'` → Replace with `{hexColor}`

**Note:** Color appears as background highlight on text regions the current user can edit.

## Toggle Highlight Editable Ranges

Show or hide the visual highlighting of editable text areas.

```typescript
this.container.documentEditor.documentEditorSettings.highlightEditableRanges = true;
this.container.documentEditor.documentEditorSettings.highlightEditableRanges = false;
```

**Placeholders**
- `true` → Replace with `{showHighlight}`

**Note:** When `true`, editable regions are highlighted with the `userColor`. When `false`, highlighting is disabled.

## Restrict Editing Pane

The Restrict Editing Pane provides a UI to manage document protection and permissions:

**Available Options:**
- **Allow Formatting** – Allow/disallow formatting changes in the document
- **Read Only** – Make document read-only
- **Add Users** – Add more users who can edit protected regions
- **Range Permissions** – Select document portions and assign them to specific users for editing
- **Start Protection** – Apply restrictions and set a password
- **Stop Protection** – Remove restrictions with password verification

**To enable in template:**
```typescript
// Include RestrictEditing toolbar item in toolbarItems
public items = ['RestrictEditing', ...otherItems];
```

**Note:** Users can access this pane via toolbar or menu. All protection settings are managed through this unified interface. Password is required to start and stop protection.

## Document Protection Modes

Restrict Editing pane supports multiple protection types across Document Editor:

### Protect the document in Form filling Mode

Restrict document editing to form fields only.

```typescript
this.documentEditor.editor.enforceProtection('123', 'FormFieldsOnly');
this.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{password}`

### Protect the document in CommentsOnly mode

Restrict editing to comment operations only; users can add or edit comments but cannot modify document content.

```typescript
this.documentEditor.editor.enforceProtection('123', 'CommentsOnly');
this.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{password}`

### Protect the document in "RevisionsOnly" mode

Restrict document to revision-only mode. Users can view and make corrections but cannot accept or reject changes.

```typescript
this.documentEditor.editor.enforceProtection('123', 'RevisionsOnly');
this.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{password}`

**Note:** Protection type options: `NoProtection`, `ReadOnly`, `FormFieldsOnly`, `CommentsOnly`, `RevisionsOnly`. Use `stopProtection` with the same password to disable.
