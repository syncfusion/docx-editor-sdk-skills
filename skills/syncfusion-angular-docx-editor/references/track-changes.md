# Track Changes

Keep a record of all edits and changes to a document. Accept or reject modifications, and control who can edit revisions.

## Enable Track Changes

Turn on change tracking for the document to record all editing operations as revisions.

```typescript
 <ejs-documenteditor [enableTrackChanges]=true height="330px" style="display:block"></ejs-documenteditor>

```
## Enable Track Changes on Document Load 

When you need track changes enabled for every opened document.

```tsx
<ejs-documenteditorcontainer #documenteditor_default [enableToolbar]=true [locale]="culture" (created)="onCreate()" (documentChange)="onDocumentChange()" height="600px" [serviceUrl]="hostUrl"  style="display:block;"></ejs-documenteditorcontainer>

onDocumentChange(): void {
  if (this.container !== null) {
    this.container.documentEditor.enableTrackChanges = true;
  }
}
```

**Note:** Track changes are document-level settings. Enable during the `documentChange` event to apply to all opened documents.

## Work with Revisions

### Get all tracked revisions

Retrieve all tracked revisions from the current document.

```typescript
// Get revisions collection
let revisions: RevisionCollection = this.documentEditor.revisions;
```

### Accept or Reject all changes

```typescript
//Get revisions from the current document
let revisions : RevisionCollection = this.documentEditor.revisions;
//Accept all tracked changes
revisions.acceptAll();
//Reject all tracked changes
revisions.rejectAll();
```

### Accept or reject a specific revision

Accept a tracked change by index.

```typescript
let revisions: RevisionCollection = this.documentEditor.revisions;
revisions.get(0).accept(); // Accept specific revision
revisions.get(1).reject(); // Reject specific revision
```

**Placeholders**
- `1` → Replace with `{revisionIndex}`

## Navigate to Next Revision

Move to the next tracked change from the current selection.

```typescript
this.documentEditor.selection.navigateNextRevision();
```

## Navigate to Previous Revision

Move to the previous tracked change from the current selection.

```typescript
this.documentEditor.selection.navigatePreviousRevision();
```

## Add Custom Metadata to Revisions

Attach custom metadata (roles, tags, identifiers) to tracked revisions and display with author name.

```typescript
let settings = {
  revisionSettings: {
    customData: 'Developer',
    showCustomDataWithAuthor: true
  }
};

this.container.documentEditorSettings = settings;
```

**Placeholders**
- `'Developer'` → Replace with `{customMetadata}`

**Note:**
- `customData` is preserved in SFDT, but not in DOCX or other export formats.

## Protect Document (Revisions Only)

Restrict document to revision-only mode. Users can view and make corrections but cannot accept or reject changes.

```typescript
this.documentEditor.editor.enforceProtection('123', 'RevisionsOnly');
this.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with {password}

**Note:** Protection type options: `NoProtection`, `ReadOnly`, `FormFieldsOnly`, `CommentsOnly`, `RevisionsOnly`. Use `stopProtection` with the same password to disable.

## Handle Accept/Reject Event

Restrict accept/reject actions based on author or custom logic.

```typescript

import { Component, OnInit, ViewChild } from '@angular/core';
import {
  ToolbarService,
  DocumentEditorContainerComponent,
} from '@syncfusion/ej2-angular-documenteditor';
import { ClickEventArgs } from '@syncfusion/ej2-navigations';
import {
  CustomToolbarItemModel,
  DocumentEditorContainerModule,
} from '@syncfusion/ej2-angular-documenteditor';

@Component({
  selector: 'app-container',
  standalone: true,
  imports: [DocumentEditorContainerModule],
  providers: [ToolbarService],
  template: `
    <ejs-documenteditorcontainer #documenteditor_default 
      serviceUrl="https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/" 
      height="600px" 
      style="display:block" 
      (beforeAcceptRejectChanges)="beforeAcceptRejectChanges($event)"
      [enableToolbar]="true">
    </ejs-documenteditorcontainer>
  `,
})
export class AppComponent implements OnInit {
  @ViewChild('documenteditor_default')
  public container?: DocumentEditorContainerComponent;

  ngOnInit(): void {}
  beforeAcceptRejectChanges(args: { author: string; cancel: boolean }) {
    // Check the author of the revision
    if (args.author !== 'Hary') {
      // Cancel the accept/reject action
      args.cancel = true;
    }
  }
}
```

**Placeholders**
- `'Hary'` → Replace with `{authorName}`

**Note:** Set `args.cancel = true` to prevent the accept or reject action.
