# Ribbon

A concise reference for enabling and configuring the Ribbon UI in the Document Editor.

## Enable Ribbon
Use the `toolbarMode` prop on `DocumentEditorContainerComponent` to enable the Ribbon UI.

```ts
<template>
    <div class="control-section">
        <ejs-documenteditorcontainer ref="doceditcontainer" :toolbarMode="'Ribbon'"
        :serviceUrl="hostUrl" :enableToolbar='true' height='600px'></ejs-documenteditorcontainer>
    </div>
</template>
<script setup>
import { DocumentEditorContainerComponent, Toolbar, Ribbon } from "@syncfusion/ej2-vue-documenteditor";
import { onMounted, ref } from 'vue';

const documenteditorcontainer = ref(null);
provide('DocumentEditorContainer', [Toolbar, Ribbon]);
onMounted(function () {
   var obj = this.$refs.doceditcontainer.ej2Instances.documentEditor;  
})
</script>
```

## Ribbon Layouts
Switch between simplified and classic layouts using `ribbonLayout`.

```ts
<template>
    <div class="control-section">
        <ejs-documenteditorcontainer ref="doceditcontainer" :toolbarMode="'Ribbon'" :ribbonLayout="'Classic'"
        :serviceUrl="hostUrl" :enableToolbar='true' height='600px'></ejs-documenteditorcontainer>
    </div>
</template>
<script setup>
import { DocumentEditorContainerComponent, Toolbar, Ribbon } from "@syncfusion/ej2-vue-documenteditor";
import { onMounted, ref } from 'vue';

const documenteditorcontainer = ref(null);
provide('DocumentEditorContainer', [Toolbar, Ribbon]);
onMounted(function () {
   var obj = this.$refs.doceditcontainer.ej2Instances.documentEditor;  
})
</script>
```

## Requirred CSS

```css
@import '../node_modules/@syncfusion/ej2-base/styles/material.css';
@import '../node_modules/@syncfusion/ej2-buttons/styles/material.css';
@import '../node_modules/@syncfusion/ej2-inputs/styles/material.css';
@import '../node_modules/@syncfusion/ej2-popups/styles/material.css';
@import '../node_modules/@syncfusion/ej2-lists/styles/material.css';
@import '../node_modules/@syncfusion/ej2-navigations/styles/material.css';
@import '../node_modules/@syncfusion/ej2-splitbuttons/styles/material.css';
@import '../node_modules/@syncfusion/ej2-dropdowns/styles/material.css';
@import "../node_modules/@syncfusion/ej2-documenteditor/styles/material.css";
@import '../node_modules/@syncfusion/ej2-ribbon/styles/material.css';/* Required for Ribbon */
```

**Placeholders**
- 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/' -> Replace with `{serviceUrl}`

**File changes**
- src/styles.css -> add the two `@import` lines above