# Undo and Redo in WPF DOCX Editor

Undo and redo support in the Syncfusion WPF DOCX Editor allows reversing and reapplying document editing actions within the editor.

---

## Limit:
The undo and redo stacks are limited to 500 actions.



## UI Commands

## Undo command:

#### XAML
```xaml
<!-- Binds button to the UndoCommand -->
<Button Content="Undo" Command="RichTextBoxAdv:SfRichTextBoxAdv.UndoCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
#### C#
```csharp
//// Execute Undo
SfRichTextBoxAdv.UndoCommand.Execute(null, richTextBoxAdv);
```


## Redo command:

#### XAML
```xaml
<!-- Binds button to the RedoCommand -->
<Button Content="Redo" Command="RichTextBoxAdv:SfRichTextBoxAdv.RedoCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

#### C#
```csharp
//// Execute Redo
SfRichTextBoxAdv.RedoCommand.Execute(null, richTextBoxAdv);
```
---

## Keyboard shortcuts:
Standard shortcuts such as Ctrl+Z (undo) and Ctrl+Y (redo) are supported by default.


## Enable / Disable Undo-Redo

- The undo feature is enabled by default. Toggle it using `EditorSettings.IsUndoEnabled`.

#### XAML
```xaml
<Syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv">
	<Syncfusion:SfRichTextBoxAdv.EditorSettings>
		<Syncfusion:EditorSettings IsUndoEnabled="False"/>
	</Syncfusion:SfRichTextBoxAdv.EditorSettings>
</Syncfusion:SfRichTextBoxAdv>
```

#### C#
```csharp
//// Disable undo programmatically
richTextBoxAdv.EditorSettings.IsUndoEnabled = false;
```


## Disable Undo for Style modification

- To disable undo only for style modification actions, set `EditorSettings.CanUndoStyle="False"`.

#### XAML
```xaml
<Syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv">
	<Syncfusion:SfRichTextBoxAdv.EditorSettings>
		<Syncfusion:EditorSettings CanUndoStyle="False"/>
	</Syncfusion:SfRichTextBoxAdv.EditorSettings>
</Syncfusion:SfRichTextBoxAdv>
```

#### C#
```csharp
//// Disable undo for style changes
richTextBoxAdv.EditorSettings.CanUndoStyle = false;
```

---
