# Comments

Add, navigate, resolve, and protect comments in documents. Supports comment threads, mention support, and protection modes.

## Insert Comment

Add a comment to selected text.

```typescript
this.documentEditor.editor.insertComment('Test comment');
```

**Placeholders**
- `'Test comment'` → Replace with `{commentText}`

## Insert Comment with Author, Date, and Status

Add a comment with custom author, date, and resolution status.

```typescript
let specificDate = new Date(2024, 6, 23, 14, 30, 0);
let commentProperties: CommentProperties = {
  author: 'Nancy Davolio',
  dateTime: specificDate,
  isResolved: false
};

this.documentEditor.editor.insertComment('Hello world', commentProperties);
```

**Placeholders**
- `'Nancy Davolio'` → Replace with `{authorName}`
- `2024, 6, 23, 14, 30, 0` → Replace with `{year, month-1, day, hour, minute, second}`
- `'Hello world'` → Replace with `{commentText}`
- `false` → Replace with `{isResolved}`

## Reply to Comment

Add a reply to an existing comment.

```typescript
let specificDate = new Date(2024, 6, 23, 14, 30, 0);
let commentProperties: CommentProperties = {
  author: 'Nancy Davolio',
  dateTime: specificDate,
  isResolved: false
};

let comment: Comment = this.documentEditor.editor.insertComment('Hello world', commentProperties);
this.documentEditor.editor.insertReplyComment(comment.id, 'Reply text', commentProperties);
```

**Placeholders**
- `'Hello world'` → Replace with `{parentCommentText}`
- `'Reply text'` → Replace with `{replyCommentText}`

## Get Comments

Retrieve all comments in the document with properties.

```typescript
let commentInfo: CommentInfo[] = this.documentEditor.getComments();
```

## Navigate Comments

Move to the next or previous comment in the document.

```typescript
this.documentEditor.selection.navigateNextComment();
this.documentEditor.selection.navigatePreviousComment();
```

## Delete Comment

Delete the current selected comment or a specific comment by ID.

```typescript
// Delete current selected comment
this.documentEditor.editor.deleteComment();

// Delete by comment ID
let commentInfo: CommentInfo[] = this.documentEditor.getComments();
this.documentEditor.editor.deleteComment(commentInfo[0].id);

// Delete a reply comment
this.documentEditor.editor.deleteComment(commentInfo[0].replies[0].id);
```

## Delete All Comments

Remove all comments from the document.

```typescript
this.documentEditor.editor.deleteAllComments();
```

## Protect Document (Comments Only)

Restrict editing to comment operations only; users can add or edit comments but cannot modify document content.

```typescript
this.documentEditor.editor.enforceProtection('123', 'CommentsOnly');
this.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{password}`

**Note:** Protection type options: `NoProtection`, `ReadOnly`, `FormFieldsOnly`, `CommentsOnly`. Use `stopProtection` with the same password to disable.

## Enable Mention Support

Add mention suggestions in the comment box by typing `@` character.

```typescript
let mentionData = [
  { "Name": "Mary Kate", "EmailId": "marry@company.com" },
  { "Name": "Andrew James", "EmailId": "james@company.com" },
  { "Name": "Andrew Fuller", "EmailId": "andrew@company.com" }
];

let settings: DocumentEditorSettingsModel = {
  mentionSettings: {
    dataSource: mentionData,
    fields: { text: 'Name' }
  }
};

// Apply settings to DocumentEditorContainer
this.container.documentEditorSettings = settings;
```

**Placeholders**
- `mentionData` → Replace with `{mentionDataSource}`
- `'Name'` → Replace with `{displayField}`

## Handle Comment Events

Listen to comment actions (Post, Edit, Reply, Resolve, Reopen, Delete) and implement custom logic.

```typescript

import { Component, OnInit, ViewChild} from '@angular/core';
import { ToolbarService , DocumentEditorSettingsModel, DocumentEditorContainerModule, CommentActionEventArgs, DocumentEditorContainerComponent, beforeCommentActionEvent } from '@syncfusion/ej2-angular-documenteditor';
@Component({
  imports: [
    DocumentEditorContainerModule
  ],
  standalone: true,
  selector: 'app-root',
  // specifies the template string for the DocumentEditorContainer component
  template: `<ejs-documenteditorcontainer serviceUrl="https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/" height="600px" style="display:block" #documenteditor_default [documentEditorSettings]= "settings" (beforeCommentAction)="beforeComment($event)" [enableToolbar]=true> </ejs-documenteditorcontainer>`,
  providers: [ToolbarService]
})
export class AppComponent implements OnInit {
  @ViewChild('documenteditor_default', { static: true }) 
  public container!: DocumentEditorContainerComponent;
  public mentionData: any = [
    { "Name": "Mary Kate", "EmailId": "marry@company.com" },
    { "Name": "Andrew James", "EmailId": "james@company.com" },
    { "Name": "Andrew Fuller", "EmailId": "andrew@company.com" }
  ];
  public settings: DocumentEditorSettingsModel = { mentionSettings: { dataSource: this.mentionData, fields: { text: 'Name' } } };
  ngOnInit(): void {
    this.container.currentUser="Guest User";
  }
  // Event get triggerd on comment actions like Post, edit, reply, resolve and reopen
  public beforeComment(args: CommentActionEventArgs) {
    // Check the type and author of the comment and current user are different
    if (args.type === "Delete" && this.container.currentUser !== args.author) {
      // Cancel the comment action
      args.cancel = true;
    }
  }
}

```

**Placeholders**
- `'Delete'` → Replace with `{actionType}`
- `this.currentUser` → Replace with `{currentUserName}`
- `args.author` → Replace with `{commentAuthorProperty}`

**Note:** Available action types: Post, Edit, Reply, Resolve, Reopen, Delete. Use `args.cancel = true` to prevent the action.
