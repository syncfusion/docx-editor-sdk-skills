# Document Protection

> Manage Document Protection —  Protection, Allow comments, Allow form fields, Read only, Tracked changes, Format restrictions, Editable range

---

## Protection

```javascript
// Get the Document Editor instance
var container = document.getElementById("container").ej2_instances[0];

// Enforce/Stop protection
// Possible values of 'protectionType' are NoProtection | ReadOnly | FormFieldsOnly | CommentsOnly | RevisionsOnly.
container.documentEditor.editor.enforceProtection('password', 'protectionType');
container.documentEditor.editor.stopProtection('password');
```

## Protect the document in CommentsOnly mode

```javascript

// Enforce/Stop protection (CommentsOnly)
container.documentEditor.editor.enforceProtection('password', 'CommentsOnly');
container.documentEditor.editor.stopProtection('password');
```

---

## Protect the document in Form filling Mode

```javascript

// Enforce/Stop protection (FormFieldsOnly)
container.documentEditor.editor.enforceProtection('password', 'FormFieldsOnly');
container.documentEditor.editor.stopProtection('password');
```
---

## Protect the document in "RevisionsOnly" mode

```javascript
// Enforce/Stop protection (RevisionsOnly)
container.documentEditor.editor.enforceProtection('password', 'RevisionsOnly');
container.documentEditor.editor.stopProtection('password');
```

---

## Read only

```javascript


// Enforce/Stop protection (ReadOnly)
container.documentEditor.editor.enforceProtection('password', 'ReadOnly');
container.documentEditor.editor.stopProtection('password');

// Enable read only mode in editor
container.documentEditor.isReadOnly = true;

// Enable read only mode in container
container.documentEditor.restrictEditing = true;
```

---

## Format restrictions

```javascript

// In enforce Protection method, second parameter denotes limitToFormatting and third parameter denotes isReadOnly.
container.documentEditor.editor.enforceProtection('password', true, true);
```

---

## Editable range

```javascript

// Inserts the editing region where everyone can edit.
container.documentEditor.editor.insertEditingRegion();

// Inserts the editing region where mentioned user can edit.
container.documentEditor.editor.insertEditingRegion('user');

// Highlight Editable range
container.documentEditor.userColor = '#fff000';

// Toogle Highlight Editable range
container.documentEditor.documentEditorSettings.highlightEditableRanges = true;
```

---
