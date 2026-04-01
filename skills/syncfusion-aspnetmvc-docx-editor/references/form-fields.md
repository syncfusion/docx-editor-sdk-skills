# Form Fields

Insert, inspect, update, fill, reset, and protect form fields in the document.

## Setup

All JavaScript code examples assume the following initialization pattern:

```javascript
var documentEditor = document.getElementById('container').ej2_instances[0].documentEditor;
```

## Insert Form Fields

Insert text, checkbox, or dropdown form fields at the current cursor position.

```javascript
// Insert Text form field
documentEditor.editor.insertFormField('Text');

// Insert Checkbox form field
documentEditor.editor.insertFormField('CheckBox');

// Insert DropDown form field
documentEditor.editor.insertFormField('DropDown');
```

## Get Form Field Names

Retrieve all form field names in the document.

```javascript
var formFieldsNames = documentEditor.getFormFieldNames();
```

## Form Field Properties

### Get Form Field Properties

Retrieve the definition of a specific form field by name.

```javascript
// Text form field
var textfieldInfo = documentEditor.getFormFieldInfo('Text1');

// Checkbox form field
var checkboxfieldInfo = documentEditor.getFormFieldInfo('Check1');

// DropDown form field
var dropdownfieldInfo = documentEditor.getFormFieldInfo('Drop1');
```

**Placeholders**
- `'Text1'` → Replace with `{textFieldName}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `'Drop1'` → Replace with `{dropdownFieldName}`

### Set Form Field Properties

Update field default values, format, and available options.

```javascript
// Set text form field properties
var textfieldInfo = documentEditor.getFormFieldInfo('Text1');
textfieldInfo.defaultValue = 'Hello';
textfieldInfo.format = 'Uppercase';
textfieldInfo.type = 'Text';
documentEditor.setFormFieldInfo('Text1', textfieldInfo);

// Set checkbox form field properties
var checkboxfieldInfo = documentEditor.getFormFieldInfo('Check1');
checkboxfieldInfo.defaultValue = true;
documentEditor.setFormFieldInfo('Check1', checkboxfieldInfo);

// Set dropdown form field properties
var dropdownfieldInfo = documentEditor.getFormFieldInfo('Drop1');
dropdownfieldInfo.dropDownItems = ['One', 'Two', 'Three'];
documentEditor.setFormFieldInfo('Drop1', dropdownfieldInfo);
```

**Placeholders**
- `'Text1'` → Replace with `{textFieldName}`
- `'Hello'` → Replace with `{defaultTextValue}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `true` → Replace with `{checkboxValue}`
- `['One', 'Two', 'Three']` → Replace with `{dropdownItems}`
- `'Drop1'` → Replace with `{dropdownFieldName}`

**Note**: If the new field name already exists, the old field name is cleared. Use unique names for each field.

## Export Form Field Data

Extract all form field values from the document as a JSON object or array.

```javascript
var formFieldData = documentEditor.exportFormData();
```

## Import Form Field Data

Populate form fields with values programmatically.

```javascript
var textformField = { fieldName: 'Text1', value: 'Hello World' };
var checkformField = { fieldName: 'Check1', value: true };
var dropdownformField = { fieldName: 'Drop1', value: 1 };

documentEditor.importFormData([textformField, checkformField, dropdownformField]);
```

**Placeholders**
- `'Text1'` → Replace with `{textFieldName}`
- `'Hello World'` → Replace with `{textFieldValue}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `true` → Replace with `{checkboxValue}`
- `'Drop1'` → Replace with `{dropdownFieldName}`
- `1` → Replace with `{dropdownIndex}`

## Reset Form Fields

Clear all form field values in the document to their default states.

```javascript
documentEditor.resetFormFields();
```
