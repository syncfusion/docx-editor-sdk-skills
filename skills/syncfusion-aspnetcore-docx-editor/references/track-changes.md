# Track Changes

> All track change operations — Enable/Disable track changes, accept, reject changes.

---

## Enable Track Changes

```cshtml

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true enableTrackChanges=true created="onCreated" height="590px"></ejs-documenteditorcontainer>

```


## Enable Track Changes on Document Load 

When you need track changes enabled for every opened ot loaded document.

```javascript
// Enable track changes whenever a document is loaded/opened
var documentEditor = document.getElementById('container').ej2_instances[0];
documentEditor.documentChange = function () {
  if (documentEditor !== null) {
    documentEditor.enableTrackChanges = true;
  }
};
```

---

## Show / Hide Revisions Pane

```javascript
// Show / hide programmatically
var container = document.getElementById('container').ej2_instances[0];
container.documentEditor.showRevisions = true;  // show
container.documentEditor.showRevisions = false; // hide
```

---

## Work with Revisions

### Get all tracked revisions

```javascript
// Get revisions collection
var revisions = container.documentEditor.revisions;
```

### Accept or Reject all changes

```javascript
var revisions = container.documentEditor.revisions;
revisions.acceptAll(); // Accept all
revisions.rejectAll(); // Reject all
```

### Accept or reject a specific revision

```javascript
var revisions = container.documentEditor.revisions;
revisions.get(0).accept(); // Accept specific revision
revisions.get(1).reject(); // Reject specific revision
```

### Get content from specific revision

```javascript
var revisions = container.documentEditor.revisions;
revisions.get(0).getContent(); //Retrieves the text content of the revision
```

---

## Navigate between tracked changes

```javascript
// From current selection
container.documentEditor.selection.navigateNextRevision();
container.documentEditor.selection.navigatePreviousRevision();
```

---

## Custom metadata along with author

When you want the review pane to show extra revision metadata with the author.

```cshtml
// Show customData with author in Track Changes pane
<ejs-documenteditorcontainer id="container" documentEditorSettings="settings"  height="590px" enableTrackChanges=true></ejs-documenteditorcontainer>

<script>
    var settings = { revisionSettings: { customData: 'Developer', showCustomDataWithAuthor: true} };
</script>

```

**Placeholders**
- 'Developer' → Replace with `{revisionCustomData}`

**Note**
- `customData` is preserved in SFDT, but not in DOCX or other export formats.

---

## Protect Track Changes Only

When you want users to edit under tracked revisions without accepting or rejecting changes.

```javascript
// Protect the document in revisions-only mode
container.documentEditor.editor.enforceProtection('123', 'RevisionsOnly');

// Remove protection
container.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{protectionPassword}`

**Note**
- Protection types include `NoProtection`, `ReadOnly`, `FormFieldsOnly`, `CommentsOnly`, and `RevisionsOnly`.


## Restrict accept/reject via event

When you need to allow accept or reject only for specific authors.

```javascript

var beforeAcceptRejectChanges = function (args) {
  if (args.author !== 'Hary') {
    args.cancel = true; // prevent accept/reject for others
  }
};

// Register the handler
container.documentEditor.beforeAcceptRejectChanges = beforeAcceptRejectChanges;
```

**Placeholders**
- `'Hary'` → Replace with `{allowedAuthor}`
---
