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

## Set Colors for Revision Types

Override the default author-based color for specific revision types.

```ts
let container: DocumentEditorContainer = new DocumentEditorContainer({
  enableToolbar: true,
  enableTrackChanges: true,
  height: '590px',
  // Use the following service URL only for demo purposes
  serviceUrl: 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/'
});

container.documentEditorSettings.revisionSettings = {
  insertRevisionColor: '#22C55E',
  deleteRevisionColor: '#EF4444',
  insertedRowColor: '#f6fa06',
  deletedRowColor: '#3a02bb'
};
```

**Placeholders**
- `'#22C55E'` → Replace with `{insertRevisionColor}`
- `'#EF4444'` → Replace with `{deleteRevisionColor}`
- `'#f6fa06'` → Replace with `{insertedRowColor}`
- `'#3a02bb'` → Replace with `{deletedRowColor}`

**Note:** These settings only affect how revisions are displayed in the DOCX Editor and are not stored in the document. By default, all revision types use author-specific colors (`'byAuthor'`).

## Custom Colors for Track Changes

Assign a color per author from a custom array, applied in order.

```ts
container.documentEditorSettings.revisionSettings.revisionColors = [
  '#0e76b1',
  '#bb00ff',
  '#c14f16'
];
```

**Placeholders**
- `'#0e76b1'`, `'#bb00ff'`, `'#c14f16'` → Replace with `{authorColors}` (an array of hex color strings applied to authors in order)

**Note:** The first author gets the first color, the second gets the next, and so on. If there are more authors than colors, the assignment starts again from the beginning of the array.

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
