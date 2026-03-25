# Document Editor - Editor Only Mode (Advanced)
> Advanced initialization for fine-grained control without the container toolbar.

Use this mode when you need **advanced customization** and control over the editor without the built-in container toolbar.

## Install package
- npm package: `@syncfusion/ej2-angular-documenteditor`

## Editor Only Mode Implementation

```typescript
import { DocumentEditorModule } from '@syncfusion/ej2-angular-documenteditor';
import { Component, OnInit } from '@angular/core';
import { 
    PrintService, 
    SfdtExportService, 
    WordExportService, 
    TextExportService, 
    SelectionService, 
    SearchService, 
    EditorService, 
    ImageResizerService, 
    EditorHistoryService, 
    ContextMenuService, 
    OptionsPaneService, 
    HyperlinkDialogService, 
    TableDialogService, 
    BookmarkDialogService, 
    TableOfContentsDialogService, 
    PageSetupDialogService, 
    StyleDialogService, 
    ListDialogService, 
    ParagraphDialogService, 
    BulletsAndNumberingDialogService, 
    FontDialogService, 
    TablePropertiesDialogService, 
    BordersAndShadingDialogService, 
    TableOptionsDialogService, 
    CellOptionsDialogService, 
    StylesDialogService 
} from '@syncfusion/ej2-angular-documenteditor';

@Component({
    imports: [        
        DocumentEditorModule
    ],
    standalone: true,
    selector: 'app-root',
    template: `<ejs-documenteditor 
                   id="container" 
                   height="330px" 
                   serviceUrl="https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/" 
                   [isReadOnly]=false 
                   [enablePrint]=true 
                   [enableSelection]=true 
                   [enableEditor]=true 
                   [enableEditorHistory]=true 
                   [enableContextMenu]=true 
                   [enableSearch]=true 
                   [enableOptionsPane]=true>
               </ejs-documenteditor>`,
    providers: [
        PrintService, 
        SfdtExportService, 
        WordExportService, 
        TextExportService, 
        SelectionService, 
        SearchService, 
        EditorService, 
        ImageResizerService, 
        EditorHistoryService, 
        ContextMenuService, 
        OptionsPaneService, 
        HyperlinkDialogService, 
        TableDialogService, 
        BookmarkDialogService, 
        TableOfContentsDialogService, 
        PageSetupDialogService, 
        StyleDialogService, 
        ListDialogService, 
        ParagraphDialogService, 
        BulletsAndNumberingDialogService, 
        FontDialogService, 
        TablePropertiesDialogService, 
        BordersAndShadingDialogService, 
        TableOptionsDialogService, 
        CellOptionsDialogService, 
        StylesDialogService
    ]
})
export class AppComponent implements OnInit {
    ngOnInit(): void {
    }
}
```

## Key Differences from Container Mode

| Feature | Editor Only | Container |
|---------|-----------|-----------|
| **Toolbar** | Not included (manual control) | Built-in toolbar |
| **Use Case** | Advanced customization, custom toolbars | Standard document editing |
| **Module Injection** | Manual (inject specific modules) | Automatic (Toolbar injected) |
| **Complexity** | Higher | Lower |
| **Flexibility** | Maximum | Limited |

