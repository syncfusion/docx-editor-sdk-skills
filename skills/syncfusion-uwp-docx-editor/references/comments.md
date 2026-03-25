# Comments in UWP DOCX Editor

Comments support in the Syncfusion UWP DOCX Editor enables users to add, delete, navigate, and manage comments within a document for review and collaboration scenarios. This feature provides commands to insert and remove comments, navigate between comments, show or hide the comments panel, handle comment-related events, and customize the visual appearance of comments using editor settings and event arguments.

---


## Show Comments

XAML:

```xaml
<!-- Binds button to the ShowCommentsCommand -->
<Button Content="Show Comments" Command="{Binding ElementName=richTextBoxAdv, Path=ShowCommentsCommand, Mode=TwoWay}" />
```

---

## New Comment (Add Comment)

XAML:

```xaml
<!-- Binds button to the NewCommentCommand -->
<Button Content="New Comment" Command="{Binding ElementName= richTextBoxAdv, Path=NewCommentCommand, Mode=TwoWay}" />
```

---

## Delete Comment

XAML:

```xaml
<!-- Binds button to the DeleteCommentCommand -->
<Button Content="Delete Comment" Command="{Binding ElementName=richTextBoxAdv, Path=DeleteCommentCommand, Mode=TwoWay}"/>
```

---

## Delete All Comments

XAML:

```xaml
<!-- Binds button to the DeleteCommentCommand -->
<Button Content="Delete Comment" Command="{Binding ElementName=richTextBoxAdv, Path=DeleteAllCommentsCommand, Mode=TwoWay}"/>
```

---

## Previous Comment

XAML:

```xaml
<!-- Binds button to the PreviousCommentCommand -->
<Button Content="Previous Comment" Command="{Binding ElementName=richTextBoxAdv, Path=PreviousCommentCommand, Mode=TwoWay}" />
```

---

## Next Comment

XAML:

```xaml
<!-- Binds button to the NextCommentCommand -->
<Button Content="Next Comment" Command="{Binding ElementName=richTextBoxAdv, Path=NextCommentCommand, Mode=TwoWay}" />
```

---

## Events
C#:

```csharp
// Hooks the CommentAdding event of RichTextBoxAdv.
richTextBoxAdv.CommentAdding += RichTextBoxAdv_CommentAdding;

private void RichTextBoxAdv_CommentAdding(object obj, CommentAddingEventArgs args)
{
   
}
```

**Placeholders**
- `RichTextBoxAdv_CommentAdding` → Replace with `{commentAddingHandler}`

---

## Change visual of comments

C#:

```csharp
// Hooks the CommentAdding event of RichTextBoxAdv.
richTextBoxAdv.CommentAdding += RichTextBoxAdv_CommentAdding;

private void RichTextBoxAdv_CommentAdding(object obj, CommentAddingEventArgs args)
{
   // Defines the background brush for the comment.
    args.VisualStyle.BackgroundBrush = new SolidColorBrush(Color.FromArgb(0xff, 0xff, 0xa8, 0xa8));

    // Defines the border brush for the comment.
    args.VisualStyle.BorderBrush = new SolidColorBrush(Color.FromArgb(0xff, 0xFF, 0x01, 0x01));

    // Defines the highlight color for the commented content.
    args.VisualStyle.HighlightColor = Color.FromArgb(0xff, 0xFf, 0xa8, 0x8);
}
```

**Placeholders**
- `new SolidColorBrush(Color.FromArgb(0xff, 0xff, 0xa8, 0xa8))` → Replace with `{backgroundBrush}`
- `new SolidColorBrush(Color.FromArgb(0xff, 0xFF, 0x01, 0x01))` → Replace with `{borderBrush}`
- `Color.FromArgb(0xff, 0xFf, 0xa8, 0x8)` → Replace with `{highlightColor}`

---

## Comment panel visibility

C#:

```csharp
SfRichTextBoxAdv richTextBoxAdv = new SfRichTextBoxAdv();
bool isCommentPaneVisible = richTextBoxAdv.EditorSettings.IsCommentPaneVisible;
```

---