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
