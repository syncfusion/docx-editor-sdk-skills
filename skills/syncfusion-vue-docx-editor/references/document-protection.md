# Document Protection

> Manage Document Protection —  Protection, Allow comments, Allow form fields, Read only, Tracked changes, Format restrictions, Editable range

## Document Protection Modes

Restrict Editing pane supports multiple protection types across Document Editor:

### Protect the document in Form filling Mode

Restrict document editing to form fields only.

```ts
// Enforce protection with password and FormFieldsOnly mode
this.$refs.container.ej2Instances.documentEditor.editor.enforceProtection('123', 'FormFieldsOnly');

// Stop document protection
this.$refs.container.ej2Instances.documentEditor.editor.stopProtection('123');
```

### Protect the document in CommentsOnly mode

Restrict editing to comment operations only; users can add or edit comments but cannot modify document content.

```ts
//enforce protection
this.$refs.container.ej2Instances.documentEditor.editor.enforceProtection('123', 'CommentsOnly');
//stop the document protection
this.$refs.container.ej2Instances.documentEditor.editor.stopProtection('123');
```

### Protect the document in "RevisionsOnly" mode

Restrict document to revision-only mode. Users can view and make corrections but cannot accept or reject changes.

```ts
// Enforce revisions-only protection with password
this.$refs.container.ej2Instances.documentEditor.editor.enforceProtection('123', 'RevisionsOnly');

// Stop document protection
this.$refs.container.ej2Instances.documentEditor.editor.stopProtection('123');
```

### Protect the document in "Read only" mode

```ts

// Enforce/Stop protection (ReadOnly)
this.$refs.container.ej2Instances.documentEditor.editor..enforceProtection('123', 'ReadOnly');
this.$refs.container.ej2Instances.documentEditor.editor..stopProtection('123');

// Enable read only mode in editor
container.documentEditor.isReadOnly = true;

// Enable read only mode in container
this.$refs.container.ej2Instances.documentEditor.restrictEditing = true;
```

**Placeholders**
- `'123'` → Replace with `{password}`

### Format restrictions

```ts
// In enforce Protection method, second parameter denotes limitToFormatting and third parameter denotes isReadOnly.
this.$refs.container.ej2Instances.documentEditor.editor.enforceProtection('password', true, true);
```

### Editable range

```ts

// Inserts the editing region where everyone can edit.
this.$refs.doceditcontainer.ej2Instances.documentEditor.editor.insertEditingRegion();

// Inserts the editing region where mentioned user can edit.
this.$refs.doceditcontainer.ej2Instances.documentEditor.editor.insertEditingRegion('user');

this.$refs.doceditcontainer.ej2Instances.documentEditor.currentUser = 'engineer@mycompany.com';

// Highlight Editable range
this.$refs.doceditcontainer.ej2Instances.documentEditor..userColor = '#fff000';

// Toogle Highlight Editable range
this.$refs.doceditcontainer.ej2Instances.documentEditor.documentEditorSettings.highlightEditableRanges = true;
```


**Note:** Protection type options: `NoProtection`, `ReadOnly`, `FormFieldsOnly`, `CommentsOnly`, `RevisionsOnly`. Use `stopProtection` with the same password to disable.