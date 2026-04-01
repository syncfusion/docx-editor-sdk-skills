# Document Protection

> Manage Document Protection —  Protection, Allow comments, Allow form fields, Read only, Tracked changes, Format restrictions, Editable range

---

## Document Protection Modes

Restrict Editing pane supports multiple protection types across Document Editor:
- **Form Fields Only** – Users can only fill form fields
- **Comments Only** – Users can only add/edit comments
- **Revisions Only** – Users can only suggest changes via track changes
- **Read Only** – Document is read-only
- **Custom Ranges** – Users can edit only assigned text ranges


## Protect Document in Comments-Only Mode

```ts
let container: DocumentEditorContainer = new DocumentEditorContainer({
  enableToolbar: true,
  height: '590px',
});
DocumentEditorContainer.Inject(Toolbar);
container.serviceUrl =
  'http://localhost:5000/api/documenteditor/';
container.appendTo('#container');
//enforce protection
container.documentEditor.editor.enforceProtection('123', 'CommentsOnly');
//stop the document protection
container.documentEditor.editor.stopProtection('123');
```

## Protect Document in Form-Filling Mode

```ts
//enforce protection
container.documentEditor.editor.enforceProtection('123', 'FormFieldsOnly');

//stop the document protection
container.documentEditor.editor.stopProtection('123');
```

## Protect Document in Revisions-Only Mode

```ts
// Enforce revisions-only protection with password
container.documentEditor.editor.enforceProtection('123', 'RevisionsOnly');

// Stop protection
container.documentEditor.editor.stopProtection('123');
```

## Read only

```ts
// Enforce/Stop protection (CommentsOnly)
container.documentEditor.editor.enforceProtection('123', 'ReadOnly');
container.documentEditor.editor.stopProtection('123');

// Enable read only mode in editor
container.documentEditor.isReadOnly = true;

// Enable read only mode in container
container.restrictEditing = true;
```
## Format restrictions

```ts
// In enforce Protection method, second parameter denotes limitToFormatting and third parameter denotes isReadOnly.
container.documentEditor.editor.enforceProtection('123', true, true);
```

**Placeholders**
- `'123'` → Replace with `{protectionPassword}`
- `'CommentsOnly'` → Allowed values: `'NoProtection'`, `'ReadOnly'`, `'FormFieldsOnly'`, `'CommentsOnly'`


## Editable range

```ts

// Inserts the editing region where everyone can edit.
container.documentEditor.editor.insertEditingRegion();

// Inserts the editing region where mentioned user can edit.
container.documentEditor.editor.insertEditingRegion('user');

// Highlight Editable range
container.documentEditor.userColor = '#fff000';

// Toogle Highlight Editable range
container.documentEditor.documentEditorSettings.highlightEditableRanges = true;
```