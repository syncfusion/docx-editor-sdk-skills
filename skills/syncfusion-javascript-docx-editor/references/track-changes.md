# Track Changes

> All track change operations — Enable/Disable track changes, accept, reject changes.

## Enable Track Changes

Activate revision tracking to record all document edits.

```ts
let container: DocumentEditorContainer = new DocumentEditorContainer({
  enableTrackChanges: true,
});
container.appendTo('#container');
```

Track changes are document-level settings. If opening an existing document without track changes enabled, you must re-enable via the `documentChange` event:

```ts
container.documentChange = (): void => {
  if (container !== null) {
    container.documentEditor.enableTrackChanges = true;
  }
};
```

## Show or Hide Revisions Pane

Toggle visibility of the revisions panel for managing tracked changes.

```ts
import { DocumentEditorContainer, Toolbar } from '@syncfusion/ej2-documenteditor';
DocumentEditorContainer.Inject(Toolbar);
let container: DocumentEditorContainer = new DocumentEditorContainer({
  enableTrackChanges: true,
});
container.serviceUrl = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';
container.appendTo('#container');
container.documentEditor.showRevisions = true; // To show revisions pane
container.documentEditor.showRevisions = false; // To hide revisions pane
```

## Retrieve All Revisions

Access the complete collection of tracked revisions in the document.

```ts
let revisions : RevisionCollection = container.documentEditor.revisions;
```

## Accept or Reject All Changes

Approve or discard all tracked revisions at once.

```ts
let revisions : RevisionCollection = container.documentEditor.revisions;
// Accept all changes
revisions.acceptAll();
// Reject all changes
revisions.rejectAll();
```

## Accept or Reject Specific Revision

Approve or discard individual tracked changes by index.

```ts
let revisions : RevisionCollection = container.documentEditor.revisions;
// Accept a specific revision
revisions.get(0).accept();
// Reject a specific revision
revisions.get(1).reject();
```

## Navigate Tracked Changes

Move sequentially through all revisions in the document.

```ts
// Navigate to next revision
container.documentEditor.selection.navigateNextRevision();
// Navigate to previous revision
container.documentEditor.selection.navigatePreviousRevision();
```

## Add Custom Metadata to Revisions

Attach custom metadata (roles, tags, identifiers) to tracked changes and display alongside author name.

```ts
let container: DocumentEditorContainer = new DocumentEditorContainer({ 
  height: '590px',
  enableTrackChanges: true,
  documentEditorSettings: {
    revisionSettings: { 
      customData: 'Developer',
      showCustomDataWithAuthor: true 
    }
  }
});
container.appendTo('#container');
```

**Placeholders**
- `'Developer'` → Replace with `{userRole}`
- `showCustomDataWithAuthor: true` → Set to `false` to hide custom metadata in Track Changes pane

**Note:** Custom metadata is preserved only in SFDT export. Other formats (DOCX) do not retain this data.

## Protect Document in Revisions-Only Mode

Restrict document editing so users can only view and make corrections; only the author can accept/reject changes.

```ts
// Enforce revisions-only protection with password
container.documentEditor.editor.enforceProtection('password123', 'RevisionsOnly');
// Stop protection
container.documentEditor.editor.stopProtection('password123');
```

**Placeholders**
- `'password123'` → Replace with `{protectionPassword}`
- `'RevisionsOnly'` → Allowed protection types: `'NoProtection'`, `'ReadOnly'`, `'FormFieldsOnly'`, `'CommentsOnly'`, `'RevisionsOnly'`

## Handle Revision Actions with Events

Intercept and validate accept/reject actions using `beforeAcceptRejectChanges` event.

```ts
function beforeAcceptRejectChanges(args) {
  // Allow only the revision author to accept/reject
  if (args.author !== container.currentUser) {
    args.cancel = true;
  }
}

let container = new DocumentEditorContainer({ 
  beforeAcceptRejectChanges: beforeAcceptRejectChanges.bind(this),
  enableToolbar: true,
  height: '590px',
  currentUser: 'Hary'
});
container.appendTo('#container');
```

**Placeholders**
- `'Hary'` → Replace with `{currentUserName}`
- `args.author` → Author name of the tracked revision
- `args.cancel` → Set to `true` to block the action

## File-based Changes

- Container initialization → Set `enableTrackChanges: true` before `appendTo()`
- Revision access → Use `container.documentEditor.revisions` for programmatic operations
- Event handlers → Bind to container properties before calling `appendTo()`
- Service URL → Required for full collaboration and revision syncing
