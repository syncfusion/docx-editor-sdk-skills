# Form Fields

> Insert, inspect, update, fill, reset, and protect form fields.

---

## Insert Form Fields

```javascript
// Get the Document Editor instance
var container = document.getElementById("container").ej2_instances[0];

// Insert Text form field
container.documentEditor.editor.insertFormField('Text');

// Insert Checkbox form field
container.documentEditor.editor.insertFormField('CheckBox');

// Insert Dropdown form field
container.documentEditor.editor.insertFormField('DropDown');
```

---

## Get Form Field Names

Retrieve all form field names currently in the document.

```javascript
var formFieldNames = container.documentEditor.getFormFieldNames();
```

---

## Form Field Properties

### Get Form Field Properties

```javascript

// Get Text form field
var textFieldInfo = container.documentEditor.getFormFieldInfo('Text1');

// Get Checkbox form field
var checkboxFieldInfo = container.documentEditor.getFormFieldInfo('Check1');

// Get Dropdown form field
var dropdownFieldInfo = container.documentEditor.getFormFieldInfo('Drop1');
```

**Placeholders**
- 'Text1' → Replace with `{textFieldName}`
- 'Check1' → Replace with `{checkboxFieldName}`
- 'Drop1' → Replace with `{dropdownFieldName}`

### Set Form Field Properties

```javascript

// Set text form field properties
var textFieldInfo = container.documentEditor.getFormFieldInfo('Text1');
textFieldInfo.defaultValue = 'Hello';
textFieldInfo.format = 'Uppercase';
textFieldInfo.type = 'Text';
textFieldInfo.name = 'Text2';
container.documentEditor.setFormFieldInfo('Text1', textFieldInfo);

// Set checkbox form field properties
var checkboxFieldInfo = container.documentEditor.getFormFieldInfo('Check1');
checkboxFieldInfo.defaultValue = true;
checkboxFieldInfo.name = 'Check2';
container.documentEditor.setFormFieldInfo('Check1', checkboxFieldInfo);

// Set dropdown form field properties
var dropdownFieldInfo = container.documentEditor.getFormFieldInfo('Drop1');
dropdownFieldInfo.dropdownItems = ['One', 'Two', 'Three'];
dropdownFieldInfo.name = 'Drop2';
container.documentEditor.setFormFieldInfo('Drop1', dropdownFieldInfo);
```

**Placeholders**
- 'Text1' → Replace with `{textFieldName}`
- 'Hello' → Replace with `{defaultTextValue}`
- 'Text2' → Replace with `{newTextFieldName}`
- 'Check1' → Replace with `{checkboxFieldName}`
- 'Check2' → Replace with `{newCheckboxFieldName}`
- 'Drop1' → Replace with `{dropdownFieldName}`
- ['One', 'Two', 'Three'] → Replace with `{dropdownItems}`
- 'Drop2' → Replace with `{newDropdownFieldName}`

**Note**
- If the new field name already exists, the old field name is cleared. Use unique names.

---

## Export Form Field Data

```javascript

var formFieldData = container.documentEditor.exportFormData();
```

---

## Import Form Field Data

```javascript

var textFormField = { fieldName: 'Text1', value: 'Hello World' };
var checkFormField = { fieldName: 'Check1', value: true };
var dropdownFormField = { fieldName: 'Drop1', value: 1 };

container.documentEditor.importFormData([textFormField, checkFormField, dropdownFormField]);
```

**Placeholders**
- 'Text1' → Replace with `{textFieldName}`
- 'Hello World' → Replace with `{textFieldValue}`
- 'Check1' → Replace with `{checkboxFieldName}`
- `true` → Replace with `{checkboxValue}`
- 'Drop1' → Replace with `{dropdownFieldName}`
- `1` → Replace with `{dropdownIndex}`

## Form Field Shading

```javascript

// Set a custom shading color (for example, white) 
container.documentEditor.documentEditorSettings.formFieldSettings.shadingColor = '#ffffff';

// Disable form field shading entirely 
container.documentEditor.documentEditorSettings.formFieldSettings.applyShading = false;
```

**Placeholders**
- `'#ffffff'` → Replace with `{shadingColor}`

**Note**
- This affects only the application UI and is not preserved in exported documents.

---

## Form Filling Mode

```javascript

// Popup mode
container.documentEditor.documentEditorSettings.formFieldSettings.formFillingMode = 'Popup';

// Inline mode
container.documentEditor.documentEditorSettings.formFieldSettings.formFillingMode = 'Inline';
```

---

## Reset Form Fields

```javascript

container.documentEditor.resetFormFields();
```
