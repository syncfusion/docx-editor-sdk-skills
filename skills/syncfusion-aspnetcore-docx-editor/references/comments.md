# Comments

Add, reply, navigate, delete, protect, and customize comments in documents.

## Add Comment

Insert a basic comment at the current selection.

```javascript
documentEditor.editor.insertComment('Test comment');
```

**Placeholders**
- `'Test comment'` → Replace with `{commentText}`

## Add Comment with Metadata

Attach author name, date/time, and resolution status to comments for better tracking and collaboration.

```javascript
var commentDate = new Date(2024, 6, 23, 14, 30, 0);
var commentProperties = {
  author: 'Nancy Davolio',
  dateTime: commentDate,
  isResolved: false
};

documentEditor.editor.insertComment('Hello world', commentProperties);
```

**Placeholders**
- `'Nancy Davolio'` → Replace with `{authorName}`
- `new Date(2024, 6, 23, 14, 30, 0)` → Replace with `{commentDateTime}`
- `'Hello world'` → Replace with `{commentText}`
- `false` → Replace with `{isResolved}` (boolean: true for resolved, false for unresolved)

---

## Reply to Comment

```javascript
// Insert reply comment — reuse commentProperties from above
var parentComment = documentEditor.editor.insertComment('Parent comment', commentProperties);
documentEditor.editor.insertReplyComment(parentComment.id, 'Reply text', commentProperties);
```

**Placeholders**
- `'Parent comment'` → Replace with `{parentCommentText}`
- `'Reply text'` → Replace with `{replyCommentText}`

---

## Get Comments

```javascript
var commentInfo = documentEditor.getComments();
```

## Navigate Comments

```javascript
// Navigate to next comment
documentEditor.selection.navigateNextComment();

// Navigate to previous comment
documentEditor.selection.navigatePreviousComment();
```

---

## Delete Comment

When you want to remove the selected comment or delete by comment id.

### Delete Selected

```javascript
// Delete current selected comment
documentEditor.editor.deleteComment();

// Delete parent comment and its replies
var commentInfo = documentEditor.getComments();
documentEditor.editor.deleteComment(commentInfo[0].id);

// Delete a specific reply comment
documentEditor.editor.deleteComment(commentInfo[0].replies[0].id);
```

### Delete All

```javascript
documentEditor.editor.deleteAllComments();
```

---

## Protect Comments Only

When you need to restrict document editing to comments only.

```javascript
// Protect document (password required)
documentEditor.enforceProtection('password', 'CommentsOnly');

// Unprotect document
documentEditor.stopProtection('password');
```

**Placeholders**
- `'password'` → Replace with `{protectionPassword}`

**Note:** Supported protection types: `NoProtection` | `ReadOnly` | `FormFieldsOnly` | `CommentsOnly`

---

## Enable Mention in Comments

When you want users to tag people with `@` inside comments.

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

**Placeholders**
- `'Mary Kate'` → Replace with `{mentionName1}`
- `'marry@company.com'` → Replace with `{mentionEmail1}`
- `'Andrew James'` → Replace with `{mentionName2}`
- `'james@company.com'` → Replace with `{mentionEmail2}`
- `'Andrew Fuller'` → Replace with `{mentionName3}`
- `'andrew@company.com'` → Replace with `{mentionEmail3}`

---

## Comment Events

When you need to allow comment actions only for specific users.


```cshtml

<ejs-documenteditorcontainer id="container" serviceUrl="https://document.syncfusion.com/web-services/docx-editor/api/DocumentEditor/" beforeCommentAction="beforeComment" ></ejs-documenteditorcontainer>

<script>
    var documenteditor;    
    document.addEventListener('DOMContentLoaded', function () {        
        documenteditor = document.getElementById("container").ej2_instances[0];
        documenteditor.currentUser = "{currentUserName}";
    });
    function beforeComment(args){
        if(args.type === "Delete" && container.currentUser !== args.author){
            args.cancel = true;
        }
    }
</script>

```

**Placeholders**
- `currentUserName` → Replace with `{loggedInUserName}` (the authenticated user's name)
- `'Delete'` → Replace with comment action type: 'Post' | 'Edit' | 'Reply' | 'Resolve' | 'Reopen'

---

## File Changes

- `Pages/Index.cshtml` → Add comment buttons, initialize editor, wire `beforeCommentAction` event handler
- `Controllers/DocumentController.cs` (optional) → Add POST/PUT/DELETE endpoints only for server-side comment persistence


