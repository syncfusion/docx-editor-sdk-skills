# Track Changes

> All track change operations — Enable/Disable track changes, accept, reject changes.

---

## Enable Track Changes

```tsx
// Basic prop usage
<DocumentEditorComponent
  id="container"
  ref={(scope) => { documentEditor = scope; }}
  enableTrackChanges={true}
/>
```


## Enable Track Changes on Document Load 

When you need track changes enabled for every opened document.

```tsx
container.current.documentChange = () => {
  if (container.current !== null) {
    container.current.documentEditor.enableTrackChanges = true;
  }
};
```

---

## Show / Hide Revisions Pane

```tsx
// Show / hide programmatically
container.documentEditor.showRevisions = true;  // show
container.documentEditor.showRevisions = false; // hide
```

---

## Work with Revisions

### Get all tracked revisions

```tsx
// Get revisions collection
let revisions: RevisionCollection = documentEditor.revisions;
```

### Accept or Reject all changes

```tsx
let revisions: RevisionCollection = documentEditor.revisions;
revisions.acceptAll(); // Accept all
revisions.rejectAll(); // Reject all
```

### Accept or reject a specific revision

```tsx
let revisions: RevisionCollection = documentEditor.revisions;
revisions.get(0).accept(); // Accept specific revision
revisions.get(1).reject(); // Reject specific revision
```

### Get content from specific revision

```tsx
let revisions: RevisionCollection = documentEditor.revisions;
revisions.get(0).getContent(); //Retrieves the text content of the revision
```

---

## Navigate between tracked changes

```tsx
// From current selection
container.documentEditor.selection.navigateNextRevision();
container.documentEditor.selection.navigatePreviousRevision();
```

---

## Custom metadata along with author

When you want the review pane to show extra revision metadata with the author.

```tsx
// Show customData with author in Track Changes pane
const settings = {
  revisionSettings: { customData: 'Developer', showCustomDataWithAuthor: true }
};

<DocumentEditorContainerComponent
  id="container"
  ref={(scope) => { container = scope; }}
  enableTrackChanges={true}
  documentEditorSettings={settings}
/>
```

**Placeholders**
- `'Developer'` → Replace with `{revisionCustomData}`

**Note**
- `customData` is preserved in SFDT, but not in DOCX or other export formats.

---

## Set Colors for Revision Types

Override the default author-based color for specific revision types.

```tsx
// Customize revision type colors
const settings = {
  revisionSettings: {
    insertRevisionColor: '#22C55E',
    deleteRevisionColor: '#EF4444',
    insertedRowColor: '#f6fa06',
    deletedRowColor: '#3a02bb'
  }
};

<DocumentEditorContainerComponent
  id="container"
  ref={(scope) => { container = scope; }}
  enableTrackChanges={true}
  documentEditorSettings={settings}
/>
```

**Placeholders**
- `'#22C55E'` → Replace with `{insertRevisionColor}`
- `'#EF4444'` → Replace with `{deleteRevisionColor}`
- `'#f6fa06'` → Replace with `{insertedRowColor}`
- `'#3a02bb'` → Replace with `{deletedRowColor}`

**Note**
- These settings only affect how revisions are displayed in the DOCX Editor and are not stored in the document.
- By default, all revision types use author-specific colors (`'byAuthor'`).

---

## Custom Colors for Track Changes

Assign a color per author from a custom array, applied in order.

```tsx
// Set a color order for track changes
const settings = {
  revisionSettings: { revisionColors: ['#0000ff', '#bb00ff', '#c14f16'] }
};

<DocumentEditorContainerComponent
  id="container"
  ref={(scope) => { container = scope; }}
  documentEditorSettings={settings}
/>
```

**Placeholders**
- `'#0000ff'`, `'#bb00ff'`, `'#c14f16'` → Replace with `{authorColors}` (an array of hex color strings applied to authors in order)

**Note**
- The first author gets the first color, the second gets the next, and so on. If there are more authors than colors, the assignment starts again from the beginning of the array.

---

## Protect Track Changes Only

When you want users to edit under tracked revisions without accepting or rejecting changes.

```tsx
// Protect the document in revisions-only mode
documentEditor.editor.enforceProtection('123', 'RevisionsOnly');

// Remove protection
documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{protectionPassword}`

**Note**
- Protection types include `NoProtection`, `ReadOnly`, `FormFieldsOnly`, `CommentsOnly`, and `RevisionsOnly`.


## Restrict accept/reject via event

When you need to allow accept or reject only for specific authors.

```tsx
// beforeAcceptRejectChanges handler example
const beforeAcceptRejectChanges = (args) => {
  if (args.author !== 'Hary') {
    args.cancel = true; // prevent accept/reject for others
  }
};

<DocumentEditorContainerComponent
  id="container"
  ref={(scope) => { container = scope; }}
  enableTrackChanges={true}
  beforeAcceptRejectChanges={beforeAcceptRejectChanges}
/>
```

**Placeholders**
- `'Hary'` → Replace with `{allowedAuthor}`

---
