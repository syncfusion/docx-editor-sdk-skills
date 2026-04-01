# Comments

Enable users to add, navigate, reply to, and manage comments in documents with optional metadata and protection controls.

## Insert Comments

Add a comment to selected text in the document.

```ts
documentEditor.editor.insertComment('Test comment');
```

## Insert Comments with Author and Metadata

Add a comment with custom author, timestamp, and resolution status.

```ts
// Create a specific date: July 23, 2024, at 2:30:00 PM.
// Note: July is represented by 6 (0-based index).
let specificDate = new Date(2024, 6, 23, 14, 30, 0); 

let commentProperties: CommentProperties = { 
    author: 'Nancy Davolio',          // The author of the comment.
    dateTime: specificDate,           // The date and time when the comment is created.
    isResolved: false                 // The status of the comment; false indicates it is unresolved.
};
// Insert the comment with the specified properties into the document editor.
documentEditor.editor.insertComment('Hello world', commentProperties);
```

**Placeholders**
- `'Nancy Davolio'` → Replace with `{authorName}`
- `new Date(2024, 6, 23, 14, 30, 0)` → Replace with `{commentDate}`
- `'Hello world'` → Replace with `{commentText}`

## Insert Reply Comments

Add a reply to an existing parent comment with author and timestamp.

```ts
let specificDate = new Date(2024, 6, 23, 14, 30, 0);
// Define the properties of the comment including author, date, and resolution status.
let commentProperties: CommentProperties = { 
    author: 'Nancy Davolio',          // The author of the comment.
    dateTime: specificDate,           // The date and time when the comment is created.
    isResolved: false                 // The status of the comment; false indicates it is unresolved.
};
// Insert the comment with the specified properties into the Document Editor.
let comment: Comment = documentEditor.editor.insertComment('Hello world', commentProperties);
// Insert a reply comment with specified properties into the Document Editor
documentEditor.editor.insertReplyComment(comment.id, 'Hello world', commentProperties);
```

## Retrieve All Comments

Get all comments in the document with their properties and replies.

```ts
//Get Comments in the document along with the properties author, date, status.
let commentinfo: CommentInfo[] = container.documentEditor.getComments();
```

## Navigate Comments

Move between comments sequentially in the document.

```ts
//Navigate to next comment
documentEditor.selection.navigateNextComment();
//Navigate to previous comment
documentEditor.selection.navigatePreviousComment();
```

## Delete Comment

Remove a specific comment or reply by ID, or delete the currently selected comment.

```ts
//Delete the current selected comment.
container.documentEditor.editor.deleteComment();
//Get Comments in the document along with the properties author, date, status.
let commentinfo: CommentInfo[] = container.documentEditor.getComments();
//Delete the particular parent comments and all of its reply comments
container.documentEditor.editor.deleteComment(commentinfo[0].id);
//Delete the particular reply comment.
container.documentEditor.editor.deleteComment(commentinfo[0].replies[0].id);
```

## Delete All Comments

Remove all comments from the document at once.

```ts
//Delete all the comments present in the current document.
documentEditor.editor.deleteAllComments();
```

## Protect Document in Comments-Only Mode

Restrict document editing to comments and replies only. Use a password to protect/unprotect.

```ts
let container: DocumentEditorContainer = new DocumentEditorContainer({
  enableToolbar: true,
  height: '590px',
});
DocumentEditorContainer.Inject(Toolbar);
container.serviceUrl =
  'http://localhost:5000/api/documenteditor/';
container.appendTo('#container');
//enforce protection
container.documentEditor.editor.enforceProtection('123', 'CommentsOnly');
//stop the document protection
container.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{protectionPassword}`
- `'CommentsOnly'` → Allowed values: `'NoProtection'`, `'ReadOnly'`, `'FormFieldsOnly'`, `'CommentsOnly'`

## Enable Mention Support in Comments

Allow users to tag and mention people by typing `@` in comment boxes.

```ts
let mentionData: any = [
    { "Name": "Mary Kate", "EmailId": "marry@company.com" },
    { "Name": "Andrew James", "EmailId": "james@company.com" },
    { "Name": "Andrew Fuller", "EmailId": "andrew@company.com"}
];
let container: DocumentEditorContainer = new DocumentEditorContainer({ enableToolbar: true,height: '590px',
// Enable mention support in document editor
  documentEditorSettings: {
    mentionSettings: { dataSource: mentionData, fields: { text: 'Name' }},
  }
});
DocumentEditorContainer.Inject(Toolbar);
container.serviceUrl = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';
container.appendTo('#container');
```

**Placeholders**
- `mentionData` array → Replace with `{userListDataSource}`
- `'Name'` → Replace with `{displayField}`

## Handle Comment Actions with Events

Intercept and validate comment actions (post, edit, reply, resolve, delete) using `beforeCommentAction` event.

```ts
import { DocumentEditorContainer, Toolbar, CommentActionEventArgs } from '@syncfusion/ej2-documenteditor';
// Inject require modules.
DocumentEditorContainer.Inject(Toolbar);
let mentionData: any = [
    { "Name": "Mary Kate", "EmailId": "marry@company.com" },
    { "Name": "Andrew James", "EmailId": "james@company.com" },
    { "Name": "Andrew Fuller", "EmailId": "andrew@company.com"}
];
let container: DocumentEditorContainer = new DocumentEditorContainer({ enableToolbar: true,height: '590px', beforeCommentAction:beforecomment,
// Enable mention support in document editor
  documentEditorSettings: {
    mentionSettings: { dataSource: mentionData, fields: { text: 'Name' }},
  }
});
DocumentEditorContainer.Inject(Toolbar);
container.serviceUrl = 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';
container.appendTo('#container');
container.currentUser="Guest User";

// Event get triggerd on comment actions like Post, edit, reply, resolve and reopen
function beforecomment(args : CommentActionEventArgs){
    // Check the type and author of the comment and current user are different
    if(args.type === "Delete" && container.currentUser !== args.author){
        // Cancel the comment action
        args.cancel = true;
    }
}
```

**Placeholders**
- `"Guest User"` → Replace with `{currentUserName}`
- `args.type` → Allowed values: `"Post"`, `"Edit"`, `"Reply"`, `"Resolve"`, `"Reopen"`, `"Delete"`

## File-based Changes

- `documentEditor` instance → Call comment methods via `.editor` property
- Event handlers → Assign to container properties before `appendTo()`
- Service URL → Must host DocumentEditor web service for full functionality
