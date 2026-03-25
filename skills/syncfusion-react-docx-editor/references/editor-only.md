# Document Editor - Editor Only Mode (Advanced)
> Advanced initialization for fine-grained control without the container toolbar.

Use this mode when you need **advanced customization** and control over the editor without the built-in container toolbar.

## Install package
- npm package: `@syncfusion/ej2-react-documenteditor`

## Editor Only Mode Implementation

```tsx

import {
    DocumentEditorComponent, DocumentEditor, RequestNavigateEventArgs, ViewChangeEventArgs,
    Print, SfdtExport, WordExport, TextExport, Selection, Search, Editor, ImageResizer, EditorHistory,
    ContextMenu, OptionsPane, HyperlinkDialog, TableDialog, BookmarkDialog, TableOfContentsDialog,
    PageSetupDialog, StyleDialog, ListDialog, ParagraphDialog, BulletsAndNumberingDialog, FontDialog,
    TablePropertiesDialog, BordersAndShadingDialog, TableOptionsDialog, CellOptionsDialog, StylesDialog
} from '@syncfusion/ej2-react-documenteditor';


DocumentEditorComponent.Inject(Print, SfdtExport, WordExport, TextExport, Selection, Search, Editor, ImageResizer, EditorHistory, ContextMenu, OptionsPane, HyperlinkDialog, TableDialog, BookmarkDialog, TableOfContentsDialog, PageSetupDialog, StyleDialog, ListDialog, ParagraphDialog, BulletsAndNumberingDialog, FontDialog, TablePropertiesDialog, BordersAndShadingDialog, TableOptionsDialog, CellOptionsDialog, StylesDialog);

function App() {
    return (
        <DocumentEditorComponent 
            id="container" 
            height={'330px'} 
            serviceUrl="https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/" 
            isReadOnly={false}
            enablePrint={true}
            enableSelection={true}
            enableEditor={true}
            enableEditorHistory={true}
            enableContextMenu={true}
            enableSearch={true}
            enableOptionsPane={true}
            enableBookmarkDialog={true}
            enableBordersAndShadingDialog={true}
            enableFontDialog={true}
            enableTableDialog={true}
            enableParagraphDialog={true}
            enableHyperlinkDialog={true}
            enableImageResizer={true}
            enableListDialog={true}
            enablePageSetupDialog={true}
            enableSfdtExport={true}
            enableStyleDialog={true}
            enableTableOfContentsDialog={true}
            enableTableOptionsDialog={true}
            enableTablePropertiesDialog={true}
            enableTextExport={true}
            enableWordExport={true}
        />
    );
}

export default App;

```

## Key Differences from Container Mode

| Feature | Editor Only | Container |
|---------|-----------|-----------|
| **Toolbar** | Not included (manual control) | Built-in toolbar |
| **Use Case** | Advanced customization, custom toolbars | Standard document editing |
| **Module Injection** | Manual (inject specific modules) | Automatic (Toolbar injected) |
| **Complexity** | Higher | Lower |
| **Flexibility** | Maximum | Limited |

