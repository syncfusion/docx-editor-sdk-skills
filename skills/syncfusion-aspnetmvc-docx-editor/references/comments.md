# Comments

> Add, reply, navigate, delete, restrict, and customize comments.

**Setup**  
All JavaScript examples assume `var documentEditor = document.getElementById('container').ej2_instances[0].documentEditor;` is available. Adapt the container ID as needed.

## Add Comment

Insert a simple comment into the document.

```javascript
documentEditor.editor.insertComment('Test comment');
```

**Placeholders**
- `'Test comment'` → Replace with `{commentText}`

## Add Comment with Author, Date, and Status

Create a comment with metadata like author, timestamp, and resolution status.

```javascript
var specificDate = new Date(2024, 6, 23, 14, 30, 0);

var commentProperties = {
  author: 'Nancy Davolio',
  dateTime: specificDate,
  isResolved: false
};
documentEditor.editor.insertComment('Hello world', commentProperties);
```

**Placeholders**
- `'Nancy Davolio'` → Replace with `{authorName}`
- `new Date(2024, 6, 23, 14, 30, 0)` → Replace with `{commentDateTime}`
- `'Hello world'` → Replace with `{commentText}`

## Reply to Comment

Add a response to an existing comment. Reuse the `commentProperties` object from "Add Comment with Author, Date, and Status" or define it locally.

```javascript
var comment = documentEditor.editor.insertComment('Parent comment', commentProperties);
documentEditor.editor.insertReplyComment(comment.id, 'Reply text', commentProperties);
```

**Placeholders**
- `'Parent comment'` → Replace with `{parentCommentText}`
- `'Reply text'` → Replace with `{replyCommentText}`

## Get Comments

Retrieve all comments from the document.

```javascript
var commentinfo = documentEditor.getComments();
```

## Navigate Comments

Move between comment locations in the document.

```javascript
documentEditor.selection.navigateNextComment();
documentEditor.selection.navigatePreviousComment();
```

## Delete Comment

Remove individual or all comments from the document.

### Delete Selected Comments

```javascript
// Delete current selected comment
documentEditor.editor.deleteComment();

// Delete parent comment and its replies
var commentinfo = documentEditor.getComments();
documentEditor.editor.deleteComment(commentinfo[0].id);

// Delete a specific reply comment
documentEditor.editor.deleteComment(commentinfo[0].replies[0].id);
```

### Delete All Comments

```javascript
documentEditor.editor.deleteAllComments();
```

## Enable Mention in Comments

Allow users to tag people with `@` syntax inside comments. Set mention settings in the `Created` event handler before the document loads.

```javascript
function onCreated() {
    var mentionData = [
      { Name: 'Mary Kate', EmailId: 'marry@company.com' },
      { Name: 'Andrew James', EmailId: 'james@company.com' },
      { Name: 'Andrew Fuller', EmailId: 'andrew@company.com' }
    ];
    documentEditor.documentEditorSettings.mentionSettings = { 
        dataSource: mentionData, 
        fields: { text: 'Name' } 
    };
}
```

```cshtml
@Html.EJS().DocumentEditorContainer("container").Created("onCreated").EnableToolbar(true).Render()
```

**Placeholders**
- `'Mary Kate'` → Replace with `{mentionName1}`
- `'marry@company.com'` → Replace with `{mentionEmail1}`
- `'Andrew James'` → Replace with `{mentionName2}`
- `'james@company.com'` → Replace with `{mentionEmail2}`
- `'Andrew Fuller'` → Replace with `{mentionName3}`
- `'andrew@company.com'` → Replace with `{mentionEmail3}`

## Restrict Comment Actions via Event

Allow or prevent comment actions (delete, edit, etc.) based on user or role.

```javascript
// Prevent non-author from deleting comments
function beforeComment(args) {
  if (args.type === 'Delete' && documentEditor.currentUser !== args.author) {
    args.cancel = true; // cancel action
  }
}
```

```cshtml
@Html.EJS().DocumentEditorContainer("container").EnableToolbar(true).Height("590px").BeforeCommentAction("beforeComment").Render()
```

**Placeholders**
- `'Guest User'` → Replace with `{currentUser}`
