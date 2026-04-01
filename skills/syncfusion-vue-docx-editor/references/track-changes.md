# Track Changes

Record, review, and manage document edits with tracked revisions and accept/reject workflows.

## Enable Track Changes

Activate track changes on the Document Editor to record all editing operations as revisions.

```ts
// Component-level: enable in template
<ejs-documenteditorcontainer :enableTrackChanges='true'></ejs-documenteditorcontainer>

// Runtime: enable when document opens
mounted() {
  this.$refs.container.ej2Instances.documentEditor.enableTrackChanges = true;
}
```

> **Note:** Track changes are document-level settings. When opening a document, if track changes are disabled in the document, setting `enableTrackChanges = true` will not override it. Enable track changes on the `documentChange` event to apply it to all opened documents.

## Show or Hide Revisions Pane

Toggle the visibility of the revisions pane to display tracked changes.

```ts
// Show revisions pane
this.$refs.container.ej2Instances.documentEditor.showRevisions = true;

// Hide revisions pane
this.$refs.container.ej2Instances.documentEditor.showRevisions = false;
```

## Get Tracked Revisions

Retrieve all revisions from the current document.

```ts
const revisions = this.$refs.container.ej2Instances.documentEditor.revisions;
```

## Accept or Reject All Changes

Apply or discard all tracked revisions at once.

```ts
const revisions = this.$refs.container.ej2Instances.documentEditor.revisions;

// Accept all revisions
revisions.acceptAll();

// Reject all revisions
revisions.rejectAll();
```

## Accept or Reject Specific Change

Approve or discard individual revisions by index.

```ts
const revisions = this.$refs.container.ej2Instances.documentEditor.revisions;

// Accept a specific revision
revisions.get({revisionIndex}).accept();

// Reject a specific revision
revisions.get({revisionIndex}).reject();
```

**Placeholders**
- `0` → Replace with `{revisionIndex}`
- `1` → Replace with `{revisionIndex}`

## Navigate Between Changes

Move through tracked revisions in the document.

```ts
// Go to next tracked change
this.$refs.container.ej2Instances.documentEditor.selection.navigateNextRevision();

// Go to previous tracked change
this.$refs.container.ej2Instances.documentEditor.selection.navigatePreviousRevision();
```

## Add Custom Metadata to Revisions

Attach additional metadata (role, tag, identifier) to tracked revisions and display it with the author name.

```ts
const settings = {
  revisionSettings: {
    customData: '{customMetadata}',
    showCustomDataWithAuthor: true
  }
};

// Apply in component: :documentEditorSettings="settings"
```

**Placeholders**
- `'Developer'` → Replace with `{customMetadata}`

> **Note:** Custom metadata is preserved only in SFDT export format. Other formats (DOCX, PDF) do not retain custom data.

## Protect Document for Revisions Only

Restrict the document so users can only add revisions but cannot accept or reject them.

```ts
// Enforce revisions-only protection with password
this.$refs.container.ej2Instances.documentEditor.editor.enforceProtection('{password}', 'RevisionsOnly');

// Stop document protection
this.$refs.container.ej2Instances.documentEditor.editor.stopProtection('{password}');
```

**Placeholders**
- `'123'` → Replace with `{password}`

> **Note:** Protection types are `NoProtection`, `ReadOnly`, `FormFieldsOnly`, `CommentsOnly`, or `RevisionsOnly`. Only the document author can accept/reject changes in `RevisionsOnly` mode after unprotecting.

## Restrict Changes by Author

Prevent specific authors from accepting or rejecting revisions using the `beforeAcceptRejectChanges` event.

```ts
const beforeAcceptRejectChanges = (args) => {
  if (args.author !== '{authorizedAuthor}') {
    args.cancel = true; // Block accept/reject for non-authorized authors
  }
};

// Register in component: @beforeAcceptRejectChanges="beforeAcceptRejectChanges"
```

**Placeholders**
- `'Hary'` → Replace with `{authorizedAuthor}`

> **Note:** `args.author` contains the revision author name. Set `args.cancel = true` to block the action; leave undefined or false to allow it.
