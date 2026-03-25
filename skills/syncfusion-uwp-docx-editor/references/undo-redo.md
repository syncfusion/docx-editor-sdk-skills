# Undo and Redo in UWP DOCX Editor

Undo and redo support in the Syncfusion UWP DOCX Editor allows reversing and reapplying document editing actions within the editor.

---

## Limit:
The undo and redo stacks are limited to 500 actions.



## UI Commands

## Undo command:

#### XAML
```xaml
<!-- Binds button to the UndoCommand -->
<Button Content="Undo" Command="{Binding ElementName=richTextBoxAdv, Path=UndoCommand, Mode=TwoWay}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
#### C#
```csharp
//// Execute Undo
 richTextBoxAdv.UndoCommand.Execute(richTextBoxAdv);
```


## Redo command:

#### XAML
```xaml
<!-- Binds button to the RedoCommand -->
<Button Content="Redo" Command="{Binding ElementName=richTextBoxAdv, Path=RedoCommand, Mode=TwoWay}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

#### C#
```csharp
//// Execute Redo
richTextBoxAdv.RedoCommand.Execute(richTextBoxAdv);
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
