# Comments

> Add, reply, navigate, delete, protect, and customize comments.

---

## Add Comment

```tsx
documentEditor.editor.insertComment('Test comment');
```

**Placeholders**
- `'Test comment'` → Replace with `{commentText}`

### With Author, Date, and Status

When you need to create a comment with metadata.

```tsx
let specificDate = new Date(2024, 6, 23, 14, 30, 0);

let commentProperties: CommentProperties = {
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

---

## Reply to Comment

```tsx
// Insert reply comment — reuse CommentProperties from above
let comment: Comment = documentEditor.editor.insertComment('Parent comment', commentProperties);
documentEditor.editor.insertReplyComment(comment.id, 'Reply text', commentProperties);
```

**Placeholders**
- `'Parent comment'` → Replace with `{parentCommentText}`
- `'Reply text'` → Replace with `{replyCommentText}`

---

## Get Comments

```tsx
let commentInfo: CommentInfo[] = documentEditor.getComments();
```

---

## Navigate Comments

```tsx
documentEditor.selection.navigateNextComment();
documentEditor.selection.navigatePreviousComment();
```

---

## Delete Comment

When you want to remove the selected comment or delete by comment id.

### Delete Selected

```tsx
// Delete current selected comment
documentEditor.editor.deleteComment();

// Delete parent comment and its replies
let commentInfo: CommentInfo[] = documentEditor.getComments();
documentEditor.editor.deleteComment(commentInfo[0].id);

// Delete a specific reply comment
documentEditor.editor.deleteComment(commentInfo[0].replies[0].id);
```

### Delete All

```tsx
documentEditor.editor.deleteAllComments();
```

---

## Enable Mention in Comments

When you want users to tag people with `@` inside comments.

```tsx
let mentionData = [
  { Name: 'Mary Kate', EmailId: 'marry@company.com' },
  { Name: 'Andrew James', EmailId: 'james@company.com' },
  { Name: 'Andrew Fuller', EmailId: 'andrew@company.com' }
];

let settings = {
  mentionSettings: { dataSource: mentionData, fields: { text: 'Name' } }
};

<DocumentEditorContainerComponent
  id="container"
  ref={(scope) => { container = scope; }}
  documentEditorSettings={settings}
/>
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

```tsx
// Prevent non-author from deleting the comment
function beforeCommentAction(args: CommentActionEventArgs) {
  if (args.type === 'Delete' && container.current.currentUser !== args.author) {
    args.cancel = true; // cancel action
  }
}

<DocumentEditorContainerComponent
  id="container"
  ref={container}
  beforeCommentAction={beforeCommentAction}
  currentUser="Guest User"
/>
```

**Placeholders**
- `'Guest User'` → Replace with `{currentUser}`
