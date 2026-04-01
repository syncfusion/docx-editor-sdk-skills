# Document Editor - Editor Only Mode (Advanced)
> Advanced initialization for fine-grained control without the container toolbar.

Use this mode when you need **advanced customization** and control over the editor without the built-in container toolbar.

## Install package
- npm package: `@syncfusion/ej2-vue-documenteditor`

## Editor Only Mode Implementation

```vue
<template>
  <DocumentEditorComponent
    id="container"
    height="370px"
    :serviceUrl="serviceUrl"
    :isReadOnly="false"
    :enablePrint="true"
    :enableSelection="true"
    :enableEditor="true"
    :enableEditorHistory="true"
    :enableContextMenu="true"
    :enableSearch="true"
    :enableOptionsPane="true"
    :enableBookmarkDialog="true"
    :enableBordersAndShadingDialog="true"
    :enableFontDialog="true"
    :enableTableDialog="true"
    :enableParagraphDialog="true"
    :enableHyperlinkDialog="true"
    :enableImageResizer="true"
    :enableListDialog="true"
    :enablePageSetupDialog="true"
    :enableSfdtExport="true"
    :enableStyleDialog="true"
    :enableTableOfContentsDialog="true"
    :enableTableOptionsDialog="true"
    :enableTablePropertiesDialog="true"
    :enableTextExport="true"
    :enableWordExport="true"
  />
</template>

<script>
import { DocumentEditorComponent, Print, SfdtExport, WordExport, TextExport, Selection, Search, Editor, ImageResizer, EditorHistory, ContextMenu, OptionsPane, HyperlinkDialog, TableDialog, BookmarkDialog, TableOfContentsDialog, PageSetupDialog, StyleDialog, ListDialog, ParagraphDialog, BulletsAndNumberingDialog, FontDialog, TablePropertiesDialog, BordersAndShadingDialog, TableOptionsDialog, CellOptionsDialog, StylesDialog } from '@syncfusion/ej2-vue-documenteditor';

export default {
  name: "App",
  components: {
    "ejs-documenteditor": DocumentEditorComponent
  },
  data() {
    return {
      serviceUrl: 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/'
    };
  },
  provide: {
    //Inject require modules.
    DocumentEditor: [Print, SfdtExport, WordExport, TextExport, Selection, Search, Editor, ImageResizer, EditorHistory, ContextMenu, OptionsPane, HyperlinkDialog, TableDialog, BookmarkDialog, TableOfContentsDialog, PageSetupDialog, StyleDialog, ListDialog, ParagraphDialog, BulletsAndNumberingDialog, FontDialog, TablePropertiesDialog, BordersAndShadingDialog, TableOptionsDialog, CellOptionsDialog, StylesDialog]
  }
}
</script>

<style scoped>
#container {
  width: 100%;
  height: 370px;
}
</style>
```

## Key Differences from Container Mode

| Feature | Editor Only | Container |
|---------|-----------|-----------|
| **Toolbar** | Not included (manual control) | Built-in toolbar |
| **Use Case** | Advanced customization, custom toolbars | Standard document editing |
| **Module Injection** | Manual (inject specific modules) | Automatic (Toolbar injected) |
| **Complexity** | Higher | Lower |
| **Flexibility** | Maximum | Limited |

