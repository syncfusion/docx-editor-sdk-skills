# Document Protection

Manage document access with protection modes, editable ranges, and read-only enforcement.

## Setup

All JavaScript code examples assume `container` is already initialized as:
```javascript
var container = document.getElementById('container').ej2_instances[0];
```

This is the standard container instance pattern for accessing the Syncfusion DOCX Editor Container API.

## Enforce Protection

Apply password-protected restrictions to control how users interact with the document.

```javascript
// Enforce protection with a specific protection type
container.documentEditor.editor.enforceProtection('myPassword', 'CommentsOnly');

// Stop protection (removes restrictions)
container.documentEditor.editor.stopProtection('myPassword');
```

**Placeholders**
- `'myPassword'` → Replace with `{protectionPassword}`
- `'CommentsOnly'` → Replace with `{protectionType}`

**Protection Types**:
- `'NoProtection'` - No restrictions (default)
- `'ReadOnly'` - Entire document is read-only
- `'FormFieldsOnly'` - Only form fields can be edited
- `'CommentsOnly'` - Only comments can be added
- `'RevisionsOnly'` - Only tracked changes (revisions) can be made

## Comments-Only Protection

Allow document editing only via comments; content is read-only.

```javascript
container.documentEditor.editor.enforceProtection('myPassword', 'CommentsOnly');
```

**Placeholders**
- `'myPassword'` → Replace with `{protectionPassword}`

## Form Fields-Only Protection

Lock document content; only form fields are editable.

```javascript
container.documentEditor.editor.enforceProtection('myPassword', 'FormFieldsOnly');
```

**Placeholders**
- `'myPassword'` → Replace with `{protectionPassword}`

## Revisions-Only Protection

Enable track changes mode; users can only make revisions, not direct edits.

```javascript
container.documentEditor.editor.enforceProtection('myPassword', 'RevisionsOnly');
```

**Placeholders**
- `'myPassword'` → Replace with `{protectionPassword}`

## Read-Only Mode

Prevent all editing; document is view-only.

```javascript
// Enforce read-only protection
container.documentEditor.editor.enforceProtection('myPassword', 'ReadOnly');

// Enable read-only on the editor instance
container.documentEditor.isReadOnly = true;

// Enable read-only on the container (UI-level)
container.restrictEditing = true;
```

**Note**: `isReadOnly` controls API-level protection; `restrictEditing` disables UI editing controls. Both can be used together.

**Placeholders**
- `'myPassword'` → Replace with `{protectionPassword}`

## Format Restrictions

Restrict document formatting while allowing content editing.

```javascript
// Enforce protection with format restrictions
// Second parameter 'true' = format restriction; third parameter 'true' = read-only
container.documentEditor.editor.enforceProtection('myPassword', true, true);
```

**Note**: When both format restrictions and read-only are enabled, the document is locked with limited formatting changes allowed.

**Placeholders**
- `'myPassword'` → Replace with `{protectionPassword}`

## Editable Ranges

Define specific regions where users can edit even when the document is otherwise protected.

```javascript
// Create an editable region for all users
container.documentEditor.editor.insertEditingRegion();

// Create an editable region for a specific user
container.documentEditor.editor.insertEditingRegion('john@example.com');

// Highlight editable ranges with a color
container.documentEditor.userColor = '#fff000';

// Toggle editable range highlighting
container.documentEditor.documentEditorSettings.highlightEditableRanges = true;
```

**Placeholders**
- `'john@example.com'` → Replace with `{userEmail}`
- `'#fff000'` → Replace with `{highlightColor}`

**Note**: Editable ranges are useful in protected documents to allow specific users or sections to be modified. Highlighting helps users visually identify editable areas.

