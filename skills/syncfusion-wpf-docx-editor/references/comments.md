# Comments in WPF DOCX Editor

Comments support in the Syncfusion WPF DOCX Editor enables users to add, delete, navigate, and manage comments within a document for review and collaboration scenarios. This feature provides commands to insert and remove comments, navigate between comments, show or hide the comments panel, handle comment-related events, and customize the visual appearance of comments using editor settings and event arguments.

---


## Show Comments

XAML:

```xaml
<Button Content="Show Comments"
        Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowCommentsCommand"
        CommandTarget="{Binding ElementName=richTextBoxAdv}"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

C#:

```csharp
SfRichTextBoxAdv.ShowCommentsCommand.Execute(null, richTextBoxAdv);
```

---

## New Comment (Add Comment)

XAML:

```xaml
<Button Content="New Comment"
        Command="RichTextBoxAdv:SfRichTextBoxAdv.NewCommentCommand"
        CommandTarget="{Binding ElementName=richTextBoxAdv}"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

C#:

```csharp
SfRichTextBoxAdv.NewCommentCommand.Execute(null, richTextBoxAdv);
```

---

## Delete Comment

XAML:

```xaml
<Button Content="Delete Comment"
        Command="RichTextBoxAdv:SfRichTextBoxAdv.DeleteCommentCommand"
        CommandTarget="{Binding ElementName=richTextBoxAdv}"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

C#:

```csharp
SfRichTextBoxAdv.DeleteCommentCommand.Execute(null, richTextBoxAdv);
```

---

## Delete All Comments

XAML:

```xaml
<Button Content="Delete All Comments"
        Command="RichTextBoxAdv:SfRichTextBoxAdv.DeleteAllCommentsCommand"
        CommandTarget="{Binding ElementName=richTextBoxAdv}"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

C#:

```csharp
SfRichTextBoxAdv.DeleteAllCommentsCommand.Execute(null, richTextBoxAdv);
```

---

## Previous Comment

XAML:

```xaml
<Button Content="Previous Comment"
        Command="RichTextBoxAdv:SfRichTextBoxAdv.PreviousCommentCommand"
        CommandTarget="{Binding ElementName=richTextBoxAdv}"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

C#:

```csharp
SfRichTextBoxAdv.PreviousCommentCommand.Execute(null, richTextBoxAdv);
```

---

## Next Comment

XAML:

```xaml
<Button Content="Next Comment"
        Command="RichTextBoxAdv:SfRichTextBoxAdv.NextCommentCommand"
        CommandTarget="{Binding ElementName=richTextBoxAdv}"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

C#:

```csharp
SfRichTextBoxAdv.NextCommentCommand.Execute(null, richTextBoxAdv);
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