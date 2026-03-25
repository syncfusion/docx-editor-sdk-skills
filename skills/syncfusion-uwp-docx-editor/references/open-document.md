# Opening Documents in UWP DOCX Editor

Document opening support in the Syncfusion UWP DOCX Editor allows loading documents into the editor using built‑in APIs and commands.

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

## Open through dialog

### C#

```csharp
// Imports the document asynchronously.
async void ImportDocumentAsync()
{
    // Initializes the file open picker.
    FileOpenPicker fileOpenPicker = new FileOpenPicker();
    fileOpenPicker.FileTypeFilter.Add(".docx");
    fileOpenPicker.FileTypeFilter.Add(".doc");
    fileOpenPicker.FileTypeFilter.Add(".rtf");
    fileOpenPicker.FileTypeFilter.Add(".htm");
    fileOpenPicker.FileTypeFilter.Add(".html");
    fileOpenPicker.FileTypeFilter.Add(".txt");

    // Picks single storage file using file open picker.
    StorageFile storageFile = await fileOpenPicker.PickSingleFileAsync();

    if (storageFile != null)
        // Loads the storage file into RichTextBoxAdv asynchronously.
        await richTextBoxAdv.LoadAsync(storageFile);
}
```

---

## Open command
### XAML
```xaml
<!-- Binds button to the OpenDocumentCommand -->
<Button Content="Open" Command="{Binding ElementName=richTextBoxAdv, Path=OpenDocumentCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
### C#
```csharp
richTextBoxAdv.OpenDocumentCommand.Execute(richTextBoxAdv);
```

---

## Document loading overloads
## synchronous document loading overloads

### Load(WordDocument)

- Imports the specified `WordDocument` into the `SfRichTextBoxAdv` control.

```csharp
// Load from a Syncfusion DocIO WordDocument instance into UWP SfRichTextBoxAdv.
Assembly assembly = typeof(App).GetTypeInfo().Assembly;
using (WordDocument document = new WordDocument(assembly.GetManifestResourceStream("sample.docx"), FormatType.Docx))
{
     richTextBoxAdv.Load(document);
}
```

**Placeholders**
- `"sample.docx"` → Replace with `{fileName}`
- `wordDocument` → Replace with `{wordDocument}`

---

### Load(Stream, FormatType)

- Imports the specified `System.IO.Stream` in the specified `FormatType` into the `SfRichTextBoxAdv` control.

```csharp
public void LoadStream()
{
    // HTML content.
    string content = "<html><body><p>Hello world</p></body></html>";
    // Converts the string into byte array.
    byte[] bytes = Encoding.UTF8.GetBytes(content);
    // Initializes the stream.
    Stream stream = new MemoryStream();
    // Serializes the bytes into the stream.
    stream.Write(bytes, 0, bytes.Length);
    // Seeks the stream to starting position.
    stream.Position = 0;

    // Loads the stream into SfRichTextBoxAdv in HTML format.
    richTextBoxAdv.Load(stream, FormatType.Html);
}
```

**Placeholders**
- `"<html><body><p>Hello world</p></body></html>"` → Replace with `{content}`
- `FormatType.Html` → Replace with `{formatType}`

---

### Load(StorageFile)

- Imports the specified `Windows.Storage.StorageFile` into the `SfRichTextBoxAdv` control.

```csharp
public async void LoadFile()
{
    FileOpenPicker fileOpenPicker = new FileOpenPicker();
    fileOpenPicker.FileTypeFilter.Add(".doc");
    fileOpenPicker.FileTypeFilter.Add(".docx");
    fileOpenPicker.FileTypeFilter.Add(".dot");
    fileOpenPicker.FileTypeFilter.Add(".dotx");
    fileOpenPicker.FileTypeFilter.Add(".rtf");
    fileOpenPicker.FileTypeFilter.Add(".htm");
    fileOpenPicker.FileTypeFilter.Add(".html");
    fileOpenPicker.FileTypeFilter.Add(".xml");
    fileOpenPicker.FileTypeFilter.Add(".txt");
    StorageFile file = await fileOpenPicker.PickSingleFileAsync();

    if (file != null)
    {
        // Loads the file into SfRichTextBoxAdv.
        richTextBoxAdv.Load(file);
    }
}
```

**Placeholders**
- `file` → Replace with `{storageFile}`

---

## Asynchronous document loading overloads

## LoadAsync(WordDocument, CancellationToken)
- Asynchronously imports the specified `WordDocument` into the `SfRichTextBoxAdv` control.

```csharp
CancellationTokenSource cts = new CancellationTokenSource();
await richTextBoxAdv.LoadAsync(wordDocument, cts.Token);
```

**Placeholders**
- `wordDocument` → Replace with `{wordDocument}`
- `cts.Token` → Replace with `{cancellationToken}`

## LoadAsync(Stream, FormatType)

- Asynchronously imports the specified `System.IO.Stream` in the specified `FormatType` into the `SfRichTextBoxAdv` control.

```csharp
public async Task<bool> LoadStreamAsync()
{
    TaskCompletionSource<bool> tcs = new TaskCompletionSource<bool>();

    // HTML content.
    string content = "<html><body><p>Hello world</p></body></html>";
    // Converts the string into byte array.
    byte[] bytes = Encoding.UTF8.GetBytes(content);
    // Initializes the stream.
    Stream stream = new MemoryStream();
    // Serializes the bytes into the stream.
    stream.Write(bytes, 0, bytes.Length);
    // Seeks the stream to starting position.
    stream.Position = 0;

    // Loads the stream asynchronously into SfRichTextBoxAdv in HTML format.
    await richTextBoxAdv.LoadAsync(stream, FormatType.Html);

    tcs.SetResult(true);
    return await tcs.Task;
}
```

**Placeholders**
- `"<html><body><p>Hello world</p></body></html>"` → Replace with `{content}`
- `FormatType.Html` → Replace with `{formatType}`

## LoadAsync(Stream, FormatType, CancellationToken)

- Asynchronously imports the specified `System.IO.Stream` in the specified `FormatType` into the `SfRichTextBoxAdv` control with cancellation support.

```csharp
Task<bool> loadAsync = null;
public async Task<bool> LoadStreamAsync()
{
    TaskCompletionSource<bool> tcs = new TaskCompletionSource<bool>();

    // HTML content.
    string content = "<html><body><p>Hello world</p></body></html>";
    byte[] bytes = Encoding.UTF8.GetBytes(content);
    Stream stream = new MemoryStream();
    stream.Write(bytes, 0, bytes.Length);
    stream.Position = 0;

    CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
    // Loads the stream asynchronously into SfRichTextBoxAdv in HTML format.
    loadAsync = richTextBoxAdv.LoadAsync(stream, FormatType.Html, cancellationTokenSource.Token);

    await loadAsync;

    if (cancellationTokenSource != null)
        cancellationTokenSource.Dispose();
    cancellationTokenSource = null;
    loadAsync = null;

    tcs.SetResult(true);
    return await tcs.Task;
}
```

**Placeholders**
- `"<html><body><p>Hello world</p></body></html>"` → Replace with `{content}`
- `FormatType.Html` → Replace with `{formatType}`
- `loadAsync` → Replace with `{loadAsyncTask}`


## LoadAsync(StorageFile)

- Asynchronously imports the specified `Windows.Storage.StorageFile` into the `SfRichTextBoxAdv` control.

```csharp
public async Task<bool> LoadFileAsync()
{
    TaskCompletionSource<bool> tcs = new TaskCompletionSource<bool>();
    FileOpenPicker fileOpenPicker = new FileOpenPicker();
    fileOpenPicker.FileTypeFilter.Add(".doc");
    fileOpenPicker.FileTypeFilter.Add(".docx");
    fileOpenPicker.FileTypeFilter.Add(".dot");
    fileOpenPicker.FileTypeFilter.Add(".dotx");
    fileOpenPicker.FileTypeFilter.Add(".rtf");
    fileOpenPicker.FileTypeFilter.Add(".htm");
    fileOpenPicker.FileTypeFilter.Add(".html");
    fileOpenPicker.FileTypeFilter.Add(".xml");
    fileOpenPicker.FileTypeFilter.Add(".txt");
    StorageFile file = await fileOpenPicker.PickSingleFileAsync();

    if (file != null)
        // Loads the file asynchronously into SfRichTextBoxAdv.
        await richTextBoxAdv.LoadAsync(file);

    tcs.SetResult(true);
    return await tcs.Task;
}
```

**Placeholders**
- `file` → Replace with `{storageFile}`

## LoadAsync(StorageFile, CancellationToken)

- Asynchronously imports the specified `Windows.Storage.StorageFile` into the `SfRichTextBoxAdv` control with cancellation support.

```csharp
Task<bool> loadAsync = null;
public async Task<bool> LoadFileAsync()
{
    TaskCompletionSource<bool> tcs = new TaskCompletionSource<bool>();
    CancellationTokenSource cancellationTokenSource = null;

    FileOpenPicker fileOpenPicker = new FileOpenPicker();
    fileOpenPicker.FileTypeFilter.Add(".doc");
    fileOpenPicker.FileTypeFilter.Add(".docx");
    fileOpenPicker.FileTypeFilter.Add(".dot");
    fileOpenPicker.FileTypeFilter.Add(".dotx");
    fileOpenPicker.FileTypeFilter.Add(".rtf");
    fileOpenPicker.FileTypeFilter.Add(".htm");
    fileOpenPicker.FileTypeFilter.Add(".html");
    fileOpenPicker.FileTypeFilter.Add(".xml");
    fileOpenPicker.FileTypeFilter.Add(".txt");
    StorageFile file = await fileOpenPicker.PickSingleFileAsync();

    if (file != null)
    {
        cancellationTokenSource = new CancellationTokenSource();

        // Loads the file asynchronously into SfRichTextBoxAdv.
        loadAsync = richTextBoxAdv.LoadAsync(file, cancellationTokenSource.Token);
        await loadAsync;
    }

    if (cancellationTokenSource != null)
        cancellationTokenSource.Dispose();
    cancellationTokenSource = null;
    loadAsync = null;

    tcs.SetResult(true);
    return await tcs.Task;
}
```

**Placeholders**
- `file` → Replace with `{storageFile}`
- `loadAsync` → Replace with `{loadAsyncTask}`

---

## Asynchronous document loading settings

- `SfRichTextBoxAdv` exposes a `LoadAsyncSettings` object that lets you control how pages are loaded during asynchronous imports when the control is using `Pages` layout.

- These settings affects behavior only when `LayoutType` is set to `Pages`.

---

### IncrementalPageLoadCount

- Gets or sets the number of pages to be incrementally loaded after the initial pages are loaded during an asynchronous document loading operation. The default value is `3`

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" LayoutType="Pages">
    <RichTextBoxAdv:SfRichTextBoxAdv.LoadAsyncSettings>
        <!-- Defines page loading settings -->
        <RichTextBoxAdv:LoadAsyncSettings IncrementalPageLoadCount="1" />
    </RichTextBoxAdv:SfRichTextBoxAdv.LoadAsyncSettings>
</RichTextBoxAdv:SfRichTextBoxAdv>
```

**Placeholders**
- `IncrementalPageLoadCount="1"` → Replace with `{incrementalPageLoadCount}`

### C#
```csharp
// Defines the control.
SfRichTextBoxAdv richTextBoxAdv = new SfRichTextBoxAdv();
//Defines the asycnhronous loading settings.
LoadAsyncSettings loadAsyncSettings = new LoadAsyncSettings();
loadAsyncSettings.IncrementalPageLoadCount = 1;

richTextBoxAdv.LoadAsyncSettings = loadAsyncSettings;
```

**Placeholders**
- `1` → Replace with `{incrementalPageLoadCount}`

---

### InitialPageLoadCount

- Gets or sets the number of pages to be loaded initially during an asynchronous document loading operation.The default value is `5`

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" LayoutType="Pages">
    <RichTextBoxAdv:SfRichTextBoxAdv.LoadAsyncSettings>
        <!-- Defines page loading settings -->
        <RichTextBoxAdv:LoadAsyncSettings InitialPageLoadCount="2" />
    </RichTextBoxAdv:SfRichTextBoxAdv.LoadAsyncSettings>
</RichTextBoxAdv:SfRichTextBoxAdv>
```

**Placeholders**
- `InitialPageLoadCount="2"` → Replace with `{initialPageLoadCount}`

### C#
```csharp
// Defines the control.
SfRichTextBoxAdv richTextBoxAdv = new SfRichTextBoxAdv();
//Defines the asycnhronous loading settings.
LoadAsyncSettings loadAsyncSettings = new LoadAsyncSettings();
loadAsyncSettings.InitialPageLoadCount = 2;

richTextBoxAdv.LoadAsyncSettings = loadAsyncSettings;
```

**Placeholders**
- `2` → Replace with `{initialPageLoadCount}`

---

### ShowPageNumber

- Gets or sets a value indicating whether the loading page number popup is visible in the `SfRichTextBoxAdv` control. The default value is `true`.

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" LayoutType="Pages">
    <RichTextBoxAdv:SfRichTextBoxAdv.LoadAsyncSettings>
        <!-- Defines page loading settings -->
        <RichTextBoxAdv:LoadAsyncSettings ShowPageNumber="false" />
    </RichTextBoxAdv:SfRichTextBoxAdv.LoadAsyncSettings>
</RichTextBoxAdv:SfRichTextBoxAdv>
```

**Placeholders**
- `ShowPageNumber="false"` → Replace with `{showPageNumber}`

### C#
```csharp
// Defines the control.
SfRichTextBoxAdv richTextBoxAdv = new SfRichTextBoxAdv();
//Defines the asycnhronous loading settings.
richTextBoxAdv.LoadAsyncSettings.ShowPageNumber = false;
```

**Placeholders**
- `false` → Replace with `{showPageNumber}`

---

## Events

`SfRichTextBoxAdv` exposes events to notify when document importstart and complete. 

### Events table

| Event | Description |
| --- | --- |
| `DocumentChanging` | Triggered when the document starts loading. |
| `DocumentChanged` | Triggered after the document has been successfully loaded. |


```csharp
// Subscribe to events.
richTextBoxAdv.DocumentChanging += RichTextBoxAdv_DocumentChanging;
richTextBoxAdv.DocumentChanged += RichTextBoxAdv_DocumentChanged;

private void RichTextBoxAdv_DocumentChanging(object sender, EventArgs e)
{
    // Document load started 
}

private void RichTextBoxAdv_DocumentChanged(object sender, EventArgs e)
{
    // Document load completed 
}

```

**Placeholders**
- `RichTextBoxAdv_DocumentChanging` → Replace with `{documentChangingHandler}`
- `RichTextBoxAdv_DocumentChanged` → Replace with `{documentChangedHandler}`