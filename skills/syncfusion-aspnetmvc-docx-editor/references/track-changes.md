# Track Changes

> All track change operations — Enable/Disable track changes, accept, reject changes.

---

## Enable Track Changes

```cshtml
@Html.EJS().DocumentEditorContainer("container").EnableToolbar(true).EnableTrackChanges(true).Render()
```

---

## Enable Track Changes on Document Load 

When you need track changes enabled for every opened document.

```javascript

@Html.EJS().DocumentEditorContainer("container").DocumentChange("onDocumentChange").Render()

<script>
    function onDocumentChange() {
        var container = document.getElementById("container").ej2_instances[0];
        if(container !== null){
           container.documentEditor.enableTrackChanges = true;
        }
    }
</script>
```

## Show / Hide Revisions Pane

```javascript
// Show / hide programmatically
var container = document.getElementById('container').ej2_instances[0];
container.documentEditor.showRevisions = true;  // show
container.documentEditor.showRevisions = false; // hide
```

## Get all tracked revisions

```javascript
// Get revisions collection
var container = document.getElementById('container').ej2_instances[0];
var revisions = container.documentEditor.revisions;
```

## Accept or Reject all changes

```javascript
var container = document.getElementById('container').ej2_instances[0];
var revisions = container.documentEditor.revisions;
revisions.acceptAll(); // Accept all
revisions.rejectAll(); // Reject all
```

## Navigate between tracked changes

```javascript
// From current selection
var container = document.getElementById('container').ej2_instances[0];
container.documentEditor.selection.navigateNextRevision();
container.documentEditor.selection.navigatePreviousRevision();
```

## Protect Track Changes Only

```javascript
// Protect the document in revisions-only mode
var container = document.getElementById('container').ej2_instances[0];
container.documentEditor.editor.enforceProtection('password', 'RevisionsOnly');

// Remove protection
container.documentEditor.editor.stopProtection('password');
```

**Placeholders**
- `'password'` → Replace with `{protectionPassword}`

**Note**
- Protection types include `NoProtection`, `ReadOnly`, `FormFieldsOnly`, `CommentsOnly`, and `RevisionsOnly`.

---

## Work with Revisions — Detailed Operations

### Accept or reject a specific revision
When to use: programmatically accept or reject individual changes.

```javascript
var container = document.getElementById('container').ej2_instances[0];
var revisions = container.documentEditor.revisions;
revisions.get(0).accept(); // Accept specific revision
revisions.get(1).reject(); // Reject specific revision
```

### Get content from specific revision
When to use: retrieve the text content of a particular tracked change.

```javascript
var container = document.getElementById('container').ej2_instances[0];
var revisions = container.documentEditor.revisions;
var content = revisions.get(0).getContent(); // Retrieves the text content of the revision
console.log(content);
```

### Custom metadata along with author
When to use: display extra revision metadata (e.g., role, status) with the author name in the Track Changes pane.

```javascript

@Html.EJS().DocumentEditorContainer("container").EnableTrackChanges(true).DocumentEditorSettings("settings").Render()

<script>
    var settings = { revisionSettings: { customData: 'Developer', showCustomDataWithAuthor: true } };
</script>

```

**Placeholders**
- `'Developer'` → Replace with `{revisionCustomData}`

**Note**
- `customData` is preserved in SFDT, but not in DOCX or other export formats.

---

## Set Colors for Revision Types

Override the default author-based color for specific revision types.

```cshtml
    @Html.EJS().DocumentEditorContainer("container").EnableTrackChanges(true).EnableToolbar(true).Height("590px").Render()
```

```javascript
@section Scripts {
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            var container = document.getElementById("container").ej2_instances[0];

            container.documentEditorSettings.revisionSettings = {
                insertRevisionColor: '#22C55E',
                deleteRevisionColor: '#EF4444',
                insertedRowColor: '#f6fa06',
                deletedRowColor: '#3a02bb'
            };
        });
    </script>
}
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

```cshtml
    @Html.EJS().DocumentEditorContainer("container").EnableTrackChanges(true).EnableToolbar(true).Height("590px").Render()
```

```javascript
@section Scripts {
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            var container = document.getElementById("container").ej2_instances[0];

            // Apply revision colors dynamically
            container.documentEditorSettings.revisionSettings.revisionColors = [
                '#0000ff', '#bb00ff', '#c14f16'
            ];
        });
    </script>
}
```

**Placeholders**
- `'#0000ff'`, `'#bb00ff'`, `'#c14f16'` → Replace with `{authorColors}` (an array of hex color strings applied to authors in order)

**Note**
- The first author gets the first color, the second gets the next, and so on. If there are more authors than colors, the assignment starts again from the beginning of the array.
