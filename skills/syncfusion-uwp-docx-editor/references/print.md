# Printing in UWP DOCX Editor

Printing support in the UWP DOCX Editor allows printing document pages using built‑in rendering APIs integrated with the UWP printing framework.

---

## Registering for printing

- How to register for printing and 

- How to implement print document event handlers.

```csharp
// Initializes a list of BitmapImage to store images of pages.
List<BitmapImage> pageImages = new List<BitmapImage>();

// Initializes PrintDocument instance.
PrintDocument printDocument = new PrintDocument();
IPrintDocumentSource printDocumentSource;

// Registers for Printing
void RegisterForPrinting()
{
    // Hooks print task requested event handler.
    PrintManager printManager = PrintManager.GetForCurrentView();
    printManager.PrintTaskRequested += PrintManager_PrintTaskRequested;

    // Initializes the print document source.
    printDocumentSource = printDocument.DocumentSource;

    // Hooks print document event handlers.
    printDocument.Paginate += PrintDocument_Paginate;
    printDocument.GetPreviewPage += PrintDocument_GetPreviewPage;
    printDocument.AddPages += PrintDocument_AddPages;
}

// Print Task Requested event handler
private void PrintManager_PrintTaskRequested(PrintManager sender, PrintTaskRequestedEventArgs args)
{
    PrintTask printTask = null;
    printTask = args.Request.CreatePrintTask("Document", sourceRequested =>
    {
        // Prints Task event handler invoked when the print job is completed.
        printTask.Completed += PrintTask_Completed;
        sourceRequested.SetSource(printDocumentSource);
    });
}

// Print Task Completed Event Handler
private void PrintTask_Completed(PrintTask sender, PrintTaskCompletedEventArgs args)
{
    pageImages.Clear();
}

// Print Document Paginate event handler.
private void PrintDocument_Paginate(object sender, PaginateEventArgs e)
{
    int pageCount = richTextBoxAdv.PageCount;
    PrintDocument printDocument = sender as PrintDocument;
    // Report the number of preview pages created.
    printDocument.SetPreviewPageCount(pageCount, PreviewPageCountType.Intermediate);
}

// Print Document Get Preview Page event handler.
private void PrintDocument_GetPreviewPage(object sender, GetPreviewPageEventArgs e)
{
    PrintDocument printDocument = sender as PrintDocument;
    int currentPreviewPage = 0;
    Interlocked.Exchange(ref currentPreviewPage, e.PageNumber - 1);
    if (pageImages.Count >= e.PageNumber)
    {
        BitmapImage bitmap = pageImages[e.PageNumber - 1];
        Image image = new Image();
        image.Source = bitmap;
        printDocument.SetPreviewPage(e.PageNumber, image);
    }
}

// Print Document Add Pages event handler.
private void PrintDocument_AddPages(object sender, AddPagesEventArgs e)
{
    int pageCount = richTextBoxAdv.PageCount;
    for (int i = 0; i < pageImages.Count; i++)
    {
        Image image = new Image();
        image.Source = pageImages[i];
        printDocument.AddPage(image);
    }
    printDocument.AddPagesComplete();
}
```

## Retrieve pages and invoke print UI

- How to retrieve each page in SfRichTextBoxAdv as bitmap image and how to invoke printing

```csharp
// Gets the page images asynchronously.
async Task<bool> GetPageImagesAsync()
{
    TaskCompletionSource<bool> taskCompletionSource = new TaskCompletionSource<bool>();
    // Clears the page images.
    pageImages.Clear();
    int pageCount = richTextBoxAdv.PageCount;
    for (int i = 0; i < pageCount; i++)
    {
        // Retrieve page in RichTextBoxAdv as BitmapImage by specifying page number.
        BitmapImage bitmapImage = await richTextBoxAdv.GetPageAsImageAsync(i);
        pageImages.Add(bitmapImage);
    }
    taskCompletionSource.SetResult(true);
    return await taskCompletionSource.Task;
}

// Invokes printing asynchronously.
async void InvokePrintAsync()
{
    bool pagesRetrieved = await GetPageImagesAsync();
    if (pagesRetrieved)
        await PrintManager.ShowPrintUIAsync();
}
```

## Unregister printing

- How to unregister printing and print document event handlers.

```csharp
// Unregisters printing.
void UnRegisterPrinting()
{
    // Unhooks the print document event handlers.
    if (printDocument != null)
    {
        printDocument.Paginate -= PrintDocument_Paginate;
        printDocument.GetPreviewPage -= PrintDocument_GetPreviewPage;
        printDocument.AddPages -= PrintDocument_AddPages;
        printDocumentSource = null;
        printDocument = null;
    }
    // Unhooks the print task requested event handler.
    PrintManager printManager = PrintManager.GetForCurrentView();
    printManager.PrintTaskRequested -= PrintManager_PrintTaskRequested;
}
```

## Print document

### XAML
```xaml
<!-- Binds button to the PrintDocumentCommand -->
<Button Content="Print" Command="{Binding ElementName=richTextBoxAdv, Path=PrintDocumentCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
richTextBoxAdv.PrintDocumentCommand.Execute(richTextBoxAdv);
```

## Shortcut
Keyboard shortcut: `Ctrl+P` also invokes printing.

## Print completed event
- `SfRichTextBoxAdv` exposes `PrintCompleted` to notify when printing finishes. Hook and unhook the event as shown below:

```csharp
// Hook the event
richTextBoxAdv.PrintCompleted += RichTextBoxAdv_PrintCompleted;

private void RichTextBoxAdv_PrintCompleted(object sender, PrintCompletedEventArgs args)
{
    // Printing finished — inspect args for status or show notification
}

// Unhook when no longer needed
richTextBoxAdv.PrintCompleted -= RichTextBoxAdv_PrintCompleted;
```

## Hide comments while printing

- By default comments are printed. To hide comments in the printed output set `PrintComments` on the control's `EditorSettings`.

```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv">
    <RichTextBoxAdv:SfRichTextBoxAdv.EditorSettings>
        <RichTextBoxAdv:EditorSettings PrintComments="False" />
    </RichTextBoxAdv:SfRichTextBoxAdv.EditorSettings>
</RichTextBoxAdv:SfRichTextBoxAdv>
```

```csharp
richTextBoxAdv.EditorSettings.PrintComments = false;
```

---
