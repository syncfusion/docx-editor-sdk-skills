# Form Fields

Insert, manage, and protect form fields in the document for data collection and form filling.

## Insert Form Field

Add a Text, CheckBox, or DropDown form field to the document.

```ts
this.$refs.documenteditor.ej2Instances.editor.insertFormField('Text');
this.$refs.documenteditor.ej2Instances.editor.insertFormField('CheckBox');
this.$refs.documenteditor.ej2Instances.editor.insertFormField('DropDown');
```

## Retrieve Form Field Names

Get all form field names in the current document.

```ts
this.$refs.documenteditor.ej2Instances.getFormFieldNames();
```

## Get Form Field Properties

Retrieve properties of a specific form field by name.

```ts
const textFieldInfo = this.$refs.documenteditor.ej2Instances.getFormFieldInfo('{textFieldName}');
const checkboxFieldInfo = this.$refs.documenteditor.ej2Instances.getFormFieldInfo('{checkboxFieldName}');
const dropdownFieldInfo = this.$refs.documenteditor.ej2Instances.getFormFieldInfo('{dropdownFieldName}');
```
**Placeholders**

- `'Text1'` → Replace with `{textFieldName}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `'Drop1'` → Replace with `{dropdownFieldName}`

## Modify Form Field Properties

Update properties of a form field (name, default value, format, dropdown items).

```ts
// Set text form field properties
const textfieldInfo = this.$refs.documenteditor.ej2Instances.getFormFieldInfo('Text1');
textfieldInfo.defaultValue = "Hello";
textfieldInfo.format = "Uppercase";
textfieldInfo.type = "Text";
textfieldInfo.name = "Text2";
this.$refs.documenteditor.ej2Instances.setFormFieldInfo('Text1',textfieldInfo);

// Set checkbox form field properties
const checkboxfieldInfo = this.$refs.documenteditor.ej2Instances.getFormFieldInfo('Check1');
checkboxfieldInfo.defaultValue = true;
checkboxfieldInfo.name = "Check2";
this.$refs.documenteditor.ej2Instances.setFormFieldInfo('Check1',checkboxfieldInfo);

// Set checkbox form field properties
const dropdownfieldInfo = this.$refs.documenteditor.ej2Instances.getFormFieldInfo('Drop1');
dropdownfieldInfo.dropDownItems = ['One','Two', 'Three'];
dropdownfieldInfo.name = "Drop2";
this.$refs.documenteditor.ej2Instances.setFormFieldInfo('Drop1',dropdownfieldInfo);

```

**Placeholders**
- `'Text1'` → Replace with `{currentFieldName}`
- `"Hello"` → Replace with `{defaultValue}`
- `"Uppercase"` → Replace with `{format}`
- `"Text2"` → Replace with `{newFieldName}`
- `['One', 'Two', 'Three']` → Replace with `{dropdownItems}`


> **Note:** Ensure new form field names are unique. If a field already exists with the new name, the old name will be cleared and become inaccessible.

## Customize Form Field Shading

Set custom shading color or disable shading for form fields at the application level.

```ts
// Set custom shading color
this.$refs.doceditcontainer.ej2Instances.documentEditorSettings.formFieldSettings.shadingColor = '#e12222';

// Disable form field shading
this.$refs.doceditcontainer.ej2Instances.documentEditorSettings.formFieldSettings.applyShading = false;
```
**Placeholders**

- `'#e12222'` → Replace with `{shadingColor}`

> **Note:** Shading customization is UI-only and will not be preserved when exporting the document.

## Export Form Field Data

Retrieve all form field data from the document.

```ts
const formFieldData = this.$refs.documenteditor.ej2Instances.exportFormData();
```

## Import Form Field Data

Initialize form fields with values.

```ts
const formData = [
  { fieldName: '{textFieldName}', value: 'Hello World' },
  { fieldName: '{checkboxFieldName}', value: true },
  { fieldName: '{dropdownFieldName}', value: 1 }
];
this.$refs.documenteditor.ej2Instances.importFormData(formData);
```
**Placeholders**

- `'Text1'` → Replace with `{textFieldName}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `'Drop1'` → Replace with `{dropdownFieldName}`

## Reset Form Fields

Reset all form fields in the document to their default values.

```ts
this.$refs.documenteditor.ej2Instances.resetFormFields();
```

## Protect Document for Form Filling

Restrict document editing to form fields only.

```ts
// Enforce protection with password and FormFieldsOnly mode
this.$refs.container.ej2Instances.documentEditor.editor.enforceProtection('123', 'FormFieldsOnly');

// Stop document protection
this.$refs.container.ej2Instances.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{password}`

> **Note:** Protection types are `NoProtection`, `ReadOnly`, or `FormFieldsOnly`. First parameter in `enforceProtection` is the password; second parameter is the protection type. The `stopProtection` method requires the password.
