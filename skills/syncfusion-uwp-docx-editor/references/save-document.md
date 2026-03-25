# Saving Documents in UWP DOCX Editor

Document saving support in the Syncfusion UWP DOCX Editor allows exporting document content to files and streams using built‑in APIs and commands.


---

## Supported formats
Document formats supported by the UWP Document editor:

- Word Document (`*.docx`)
- Word 97 - 2003 Document (`*.doc`)
- Word Template (`*.dotx`)
- Word 97 - 2003 template (`*.dot`)
- Web Page (`*.htm`, `*.html`)
- Rich Text Format (`*.rtf`)
- Word XML Document (`*.xml`)
- Text File (`*.txt`)
- XAML FlowDocument (`*.xaml`)

---

## Save command

### XAML
```xaml
<!-- Binds button to the SaveDocumentCommand -->
<Button Content="Save" Command="{Binding ElementName=richTextBoxAdv, Path=SaveDocumentCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
### C#
```csharp
richTextBoxAdv.SaveDocumentCommand.Execute(richTextBoxAdv);
```
---

## Document saving  overloads
## synchronous document saving overloads

### Save(Stream, FormatType)

Exports the SfRichTextBoxAdv content into the specified System.IO.Stream in specified FormatType.

```csharp
public void SaveStream()
{
// Initializes the stream.
Stream stream = new MemoryStream();

// Exports the content into the stream as Docx Format.
richTextBoxAdv.Save(stream, FormatType.Docx);

// Seek the stream to starting position.
stream.Position = 0;

// Process the stream here.

}
```

---

### Save(StorageFile)

Exports the SfRichTextBoxAdv content into the Windows.Storage.StorageFile.

```csharp
public async void SaveFile()
{
    FileSavePicker fileSavePicker = new FileSavePicker();
    fileSavePicker.SuggestedStartLocation = PickerLocationId.DocumentsLibrary;
    fileSavePicker.FileTypeChoices.Add("Word Document", new List<string>() { ".docx" });
    fileSavePicker.FileTypeChoices.Add("Word 97-2003 Document", new List<string>() { ".doc" });
    fileSavePicker.FileTypeChoices.Add("Word Template", new List<string>() { ".dotx" });
    fileSavePicker.FileTypeChoices.Add("Word 97-2003 Template", new List<string>() { ".dot" });
    fileSavePicker.FileTypeChoices.Add("Rich Text Document", new List<string>() { ".rtf" });
    fileSavePicker.FileTypeChoices.Add("Web Page, Filtered", new List<string>() { ".html" });
    fileSavePicker.FileTypeChoices.Add("Word XML Document", new List<string>() { ".xml" });
    fileSavePicker.FileTypeChoices.Add("Plain Text", new List<string>() { ".txt" });
    fileSavePicker.SuggestedFileName = "New Document";
    StorageFile file = await fileSavePicker.PickSaveFileAsync();
// Exports the content into the file.
if (file != null)
    richTextBoxAdv.Save(file);

} 
```

---

## Asynchronous document saving overloads

## SaveAsync(Stream, FormatType)
Asynchronously exports the SfRichTextBoxAdv document content as specified FormatType into the System.IO.Stream.

```csharp
public async void SaveStream()
{
// Initializes the stream.
Stream stream = new MemoryStream();

// Exports the content into the stream as Docx Format asynchronously.
await richTextBoxAdv.SaveAsync(stream, FormatType.Docx);

// Seek the stream to starting position.
stream.Position = 0;

// Process the stream here.

}
```

## SaveAsync(StorageFile)

Asynchronously exports the SfRichTextBoxAdv content into the specified Windows.Storage.StorageFile.

```csharp
public async void SaveFile()
{
    FileSavePicker fileSavePicker = new FileSavePicker();
    fileSavePicker.SuggestedStartLocation = PickerLocationId.DocumentsLibrary;
    fileSavePicker.FileTypeChoices.Add("Word Document", new List<string>() { ".docx" });
    fileSavePicker.FileTypeChoices.Add("Word 97-2003 Document", new List<string>() { ".doc" });
     fileSavePicker.FileTypeChoices.Add("Word Template", new List<string>() { ".dotx" });
    fileSavePicker.FileTypeChoices.Add("Word 97-2003 Template", new List<string>() { ".dot" });
    fileSavePicker.FileTypeChoices.Add("Rich Text Document", new List<string>() { ".rtf" });
    fileSavePicker.FileTypeChoices.Add("Web Page, Filtered", new List<string>() { ".html" });
    fileSavePicker.FileTypeChoices.Add("Word XML Document", new List<string>() { ".xml" });
    fileSavePicker.FileTypeChoices.Add("Plain Text", new List<string>() { ".txt" });
    fileSavePicker.SuggestedFileName = "New Document";
    StorageFile file = await fileSavePicker.PickSaveFileAsync();
// Exports the content into the file asynchronously.
if (file != null)
    await richTextBoxAdv.SaveAsync(file);

}
```

## Events

`SfRichTextBoxAdv` exposes events to notify when document export start and complete. 

### Events table

| Event | Description |
| --- | --- |
| `DocumentSaving` | This event is triggered when the document starts saving. |
| `DocumentSaved` | This event is triggered after the document is successfully saved. |


```csharp
// Subscribe to events.
richTextBoxAdv.DocumentSaving += RichTextBoxAdv_DocumentSaving;
richTextBoxAdv.DocumentSaved += RichTextBoxAdv_DocumentSaved;

private void RichTextBoxAdv_DocumentSaving(object sender, EventArgs e)
{
    // Document save started 
}

private void RichTextBoxAdv_DocumentSaved(object sender, EventArgs e)
{
    // Document save completed 
}

```