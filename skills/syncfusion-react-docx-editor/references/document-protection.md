# Document Protection

> Manage Document Protection —  Protection, Allow comments, Allow form fields, Read only, Tracked changes, Format restrictions, Editable range

---

## Protection

```tsx
// Enforce/Stop protection
// Possible values of 'protectionType' are NoProtection |ReadOnly |FormFieldsOnly |CommentsOnly | RevisionsOnly.
container.documentEditor.editor.enforceProtection('password', 'protectionType');
container.documentEditor.editor.stopProtection('password');
```

## Protect the document in CommentsOnly mode

```tsx
// Enforce/Stop protection (CommentsOnly)
container.documentEditor.editor.enforceProtection('password', 'CommentsOnly');
container.documentEditor.editor.stopProtection('password');
```

---

## Protect the document in Form filling Mode

```tsx
// Enforce/Stop protection (FormFieldsOnly)
container.documentEditor.editor.enforceProtection('password', 'FormFieldsOnly');
container.documentEditor.editor.stopProtection('password');
```
---

## Protect the document in "RevisionsOnly" mode

```tsx
// Enforce/Stop protection (RevisionsOnly)
container.documentEditor.editor.enforceProtection('password', 'RevisionsOnly');
container.documentEditor.editor.stopProtection('password');
```

---

## Read only

```tsx
// Enforce/Stop protection (CommentsOnly)
container.documentEditor.editor.enforceProtection('password', 'ReadOnly');
container.documentEditor.editor.stopProtection('password');

// Enable read only mode in editor
container.documentEditor.isReadOnly = true;

// Enable read only mode in container
container.restrictEditing = true;
```

---

## Format restrictions

```tsx
// In enforce Protection method, second parameter denotes limitToFormatting and third parameter denotes isReadOnly.
container.documentEditor.editor.enforceProtection('password', true, true);
```

---

## Editable range

```tsx

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
