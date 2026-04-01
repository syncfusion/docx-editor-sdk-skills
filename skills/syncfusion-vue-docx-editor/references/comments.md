# Comments

> Add, reply, navigate, delete, protect, and customize comments.

---

## Add Comment

Add a simple comment to the selected text.

```ts
this.$refs.documenteditor.ej2Instances.editor.insertComment('{commentText}');
```

**Placeholders**
- `'{commentText}'` → Replace with your comment text

### With Author, Date, and Status

When you need to create a comment with metadata.

```ts
let specificDate = new Date(2024, 6, 23, 14, 30, 0);

let commentProperties = {
  author: '{authorName}',
  dateTime: specificDate,
  isResolved: false
};
this.$refs.documenteditor.ej2Instances.editor.insertComment('{commentText}', commentProperties);
```

**Placeholders**
- `'{authorName}'` → Replace with `{authorName}`
- `new Date(2024, 6, 23, 14, 30, 0)` → Replace with `{commentDateTime}`
- `'{commentText}'` → Replace with `{commentText}`

---

## Reply to Comment

Add a reply to an existing comment with metadata.

```ts
let specificDate = new Date(2024, 6, 23, 14, 30, 0);
let commentProperties = {
  author: '{authorName}',
  dateTime: specificDate,
  isResolved: false
};
let comment = this.$refs.documenteditor.ej2Instances.editor.insertComment('{parentCommentText}', commentProperties);
this.$refs.documenteditor.ej2Instances.editor.insertReplyComment(comment.id, '{replyCommentText}', commentProperties);
```

**Placeholders**
- `'{authorName}'` → Replace with `{authorName}`
- `'{parentCommentText}'` → Replace with `{parentCommentText}`
- `'{replyCommentText}'` → Replace with `{replyCommentText}`

---

## Get Comments

Retrieve all comments in the document with their properties and replies.

```ts
let commentInfo = this.$refs.container.ej2Instances.documentEditor.getComments();
```

---

## Navigate Comments

Move between comments in the document.

```ts
this.$refs.documenteditor.ej2Instances.selection.navigateNextComment();
this.$refs.documenteditor.ej2Instances.selection.navigatePreviousComment();
```

---

## Delete Comment

Remove a single comment, parent comment with all replies, or specific reply.

### Delete Selected

```ts
// Delete currently selected comment
this.$refs.container.ej2Instances.documentEditor.editor.deleteComment();

// Delete parent comment and all replies by ID
let commentInfo = this.$refs.container.ej2Instances.documentEditor.getComments();
this.$refs.container.ej2Instances.documentEditor.editor.deleteComment(commentInfo[0].id);

// Delete a specific reply comment
this.$refs.container.ej2Instances.documentEditor.editor.deleteComment(commentInfo[0].replies[0].id);
```

### Delete All

```ts
this.$refs.documenteditor.ej2Instances.editor.deleteAllComments();
```

---

## Enable Mention in Comments

Allow users to tag people with `@` inside comments. Displays suggestions from a data source.

```vue
<template>
  <DocumentEditorContainerComponent 
    id="container" 
    height="590px" 
    :serviceUrl="serviceUrl" 
    :documentEditorSettings='settings'
    :enableToolbar="true"
  />
</template>

<script>
import { DocumentEditorContainerComponent, Toolbar } from '@syncfusion/ej2-vue-documenteditor';

export default {
  name: 'App',
  components: {
    DocumentEditorContainerComponent
  },
  data() {
    return {
      serviceUrl: 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/',
      settings: {
        mentionSettings: {
          dataSource: [
            { Name: '{mentionName1}', EmailId: '{mentionEmail1}' },
            { Name: '{mentionName2}', EmailId: '{mentionEmail2}' },
            { Name: '{mentionName3}', EmailId: '{mentionEmail3}' }
          ],
          fields: { text: 'Name' }
        }
      }
    }
  },
  provide: {
    DocumentEditorContainer: [Toolbar]
  }
}
</script>
```

**Placeholders**
- `'{mentionName1}'` → Replace with `{mentionName1}`
- `'{mentionEmail1}'` → Replace with `{mentionEmail1}`
- `'{mentionName2}'` → Replace with `{mentionName2}`
- `'{mentionEmail2}'` → Replace with `{mentionEmail2}`
- `'{mentionName3}'` → Replace with `{mentionName3}`
- `'{mentionEmail3}'` → Replace with `{mentionEmail3}`

---

---

## Comment Events

Restrict or customize comment operations using the `beforeCommentAction` event. Example: allow only the comment author to delete.

```vue
<template>
  <div id="app">
    <ejs-documenteditorcontainer 
      ref="container" 
      height="590px" 
      :beforeCommentAction="beforeCommentHandler"
      :enableToolbar='true' 
      :currentUser="'{currentUser}'"
    >
    </ejs-documenteditorcontainer>
  </div>
</template>

<script>
import { DocumentEditorContainerComponent as EjsDocumenteditorcontainer, Toolbar } from '@syncfusion/ej2-vue-documenteditor';

export default {
  components: {
    EjsDocumenteditorcontainer
  },
  methods: {
    beforeCommentHandler(args) {
      if (args.type === 'Delete' && this.$refs.container.ej2Instances.currentUser !== args.author) {
        args.cancel = true; // Prevent non-authors from deleting
      }
    }
  },
  provide: {
    DocumentEditorContainer: [Toolbar]
  }
}
</script>
```

**Placeholders**
- `'{currentUser}'` → Replace with `{currentUser}`