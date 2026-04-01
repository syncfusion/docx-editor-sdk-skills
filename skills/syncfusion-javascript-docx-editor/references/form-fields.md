# Form Fields

Insert, inspect, update, fill, reset, and protect form fields.

## Insert Form Field

Add a new form field of specified type at the current cursor position.

```ts
// Insert Text form field
documentEditor.editor.insertFormField('Text');

// Insert Checkbox form field
documentEditor.editor.insertFormField('CheckBox');

// Insert Dropdown form field
documentEditor.editor.insertFormField('DropDown');
```

## Get Form Field Names

Retrieve all form field names in the document.

```ts
let formFieldsNames: string[] = documentEditor.getFormFieldNames();
```

## Get Form Field Properties

Access properties of a specific form field by its bookmark name.

```ts
//Get Text form field by using bookmark name.
let textfieldInfo: TextFormFieldInfo = documentEditor.getFormFieldInfo('Text1') as TextFormFieldInfo;
//Checkbox form field by using bookmark name.
let checkboxfieldInfo: CheckBoxFormFieldInfo = documentEditor.getFormFieldInfo('Check1') as CheckBoxFormFieldInfo;
//Dropdown form field by using bookmark name.
let dropdownfieldInfo: DropDownFormFieldInfo = documentEditor.getFormFieldInfo('Drop1') as DropDownFormFieldInfo;
```
**Placeholders**
- `'Text1'` → Replace with `{textFieldName}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `'Drop1'` → Replace with `{dropdownFieldName}`

## Set Form Field Properties

Modify form field configuration and register changes.

```ts
// Set text form field properties
let textfieldInfo: TextFormFieldInfo = documentEditor.getFormFieldInfo('Text1') as TextFormFieldInfo;
textfieldInfo.defaultValue = "Hello";
textfieldInfo.format = "Uppercase";
textfieldInfo.type = "Text";
textfieldInfo.name = "Text2";
documentEditor.setFormFieldInfo('Text1', textfieldInfo);

// Set checkbox form field properties
let checkboxfieldInfo: CheckBoxFormFieldInfo = documentEditor.getFormFieldInfo('Check1') as CheckBoxFormFieldInfo;
checkboxfieldInfo.defaultValue = true;
checkboxfieldInfo.name = "Check2";
documentEditor.setFormFieldInfo('Check1', checkboxfieldInfo);

// Set checkbox form field properties
let dropdownfieldInfo: DropDownFormFieldInfo = documentEditor.getFormFieldInfo('Drop1') as DropDownFormFieldInfo;
dropdownfieldInfo.dropdownItems  = ['One', 'Two', 'Three']
dropdownfieldInfo.name = "Drop2";
documentEditor.setFormFieldInfo('Drop1', dropdownfieldInfo);
```

**Placeholders**
- `'Text1'`, `'Check1'`, `'Drop1'` → Replace with `{formFieldBookmarkName}`
- `'Hello'` → Replace with `{defaultTextValue}`
- `'Uppercase'` → Allowed format values: `'Uppercase'`, `'Lowercase'`, `'None'`
- `'Text2'`, `'Check2'`, `'Drop2'` → Replace with `{newFormFieldName}`
- `['One', 'Two', 'Three']` → Replace with `{dropdownOptionsList}`

**Note:** Ensure form field names are unique. If a name conflicts with an existing field, the old field becomes inaccessible.

## Customize Form Field Shading

Control visual appearance of form fields with custom background color or disable shading.

```ts
// Set custom shading color
container.documentEditorSettings.formFieldSettings.shadingColor = '#ffffff';

// Disable shading entirely
container.documentEditorSettings.formFieldSettings.applyShading = false;
```

**Placeholders**
- `'#ffffff'` → Replace with `{hexColorCode}`

**Note:** Shading customization applies only to the UI and is not preserved in document exports.

## Export Form Field Data

Extract all form field values from the document.

```ts
let formFieldDate: FormFieldData[] = documentEditor.exportFormData();
```

## Import Form Field Data

Prefill form fields with data values.

```ts
let textformField: FormFieldData = { fieldName: 'Text1', value: 'Hello World' };
let checkformField: FormFieldData = { fieldName: 'Check1', value: true };
let dropdownformField: FormFieldData = { fieldName: 'Drop1', value: 1 };
//Import form field data
this.container.documentEditor.importFormData([textformField, checkformField, dropdownformField]);
```

**Placeholders**
- `'Text1'`, `'Check1'`, `'Drop1'` → Replace with `{formFieldBookmarkName}`
- `'Hello World'` → Replace with `{textFieldValue}`
- `true`, `1` → Boolean for checkboxes, index for dropdowns

## Reset Form Fields

Clear all form fields to their default values.

```ts
documentEditor.resetFormFields();
```

## Protect Document in Form-Filling Mode

Restrict editing to form fields only. Users can fill fields but cannot modify the document structure.

```ts
let container: DocumentEditorContainer = new DocumentEditorContainer({
  enableToolbar: true,
  height: '590px',
});
DocumentEditorContainer.Inject(Toolbar);
container.serviceUrl =
  'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/';
container.appendTo('#container');

//enforce protection
container.documentEditor.editor.enforceProtection('123', 'FormFieldsOnly');

//stop the document protection
container.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{protectionPassword}`
- `'FormFieldsOnly'` → Allowed protection types: `'NoProtection'`, `'ReadOnly'`, `'FormFieldsOnly'`, `'CommentsOnly'`

## File-based Changes

- Form field insertion → Call via `documentEditor.editor.insertFormField(type)`
- Form field metadata → Access/modify via `getFormFieldInfo()` and `setFormFieldInfo()`
- Shading settings → Configure via `container.documentEditorSettings.formFieldSettings` before render
- Data import/export → Use `importFormData()` and `exportFormData()` for batch operations
- Protection → Set before document use via `enforceProtection(password, 'FormFieldsOnly')`
