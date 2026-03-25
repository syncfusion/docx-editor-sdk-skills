# Form Fields

Insert, manage, and protect form fields (Text, CheckBox, DropDown) in documents for data collection and form filling.

## Insert Form Field

Add a form field to the document by type.

```typescript
//Insert Text form field
this.documentEditor.editor.insertFormField('Text');
//Insert Checkbox form field
this.documentEditor.editor.insertFormField('CheckBox');
//Insert Drop down form field
this.documentEditor.editor.insertFormField('DropDown');
```

**Placeholders**
- `'Text'` → Replace with `{fieldType}`

## Get Form Field Names

Retrieve all form field names in the current document.

```typescript
let formFieldNames: string[] = this.documentEditor.getFormFieldNames();
```

## Get Form Field Properties

Retrieve properties of a specific form field.

```typescript
//Text form field
let textfieldInfo: TextFormFieldInfo = this.documentEditor.getFormFieldInfo('Text1') as TextFormFieldInfo;
//Checkbox form field
let checkboxfieldInfo: CheckBoxFormFieldInfo = this.documentEditor.getFormFieldInfo('Check1') as CheckBoxFormFieldInfo;
//Dropdown form field
let dropdownfieldInfo: DropDownFormFieldInfo = this.documentEditor.getFormFieldInfo('Drop1') as DropDownFormFieldInfo;
```

**Placeholders**
- `'Text1'` → Replace with `{textFieldName}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `'Drop1'` → Replace with `{dropdownFieldName}`

## Set Form Field Properties

Modify properties of an existing form field.

```typescript
// Set text form field properties
let textfieldInfo: TextFormFieldInfo = this.documentEditor.getFormFieldInfo('Text1') as TextFormFieldInfo;
textfieldInfo.defaultValue = "Hello";
textfieldInfo.format = "Uppercase";
textfieldInfo.type = "Text";
textfieldInfo.name = "Text2";
this.documentEditor.setFormFieldInfo('Text1',textfieldInfo);

// Set checkbox form field properties
let checkboxfieldInfo: CheckBoxFormFieldInfo = this.documentEditor.getFormFieldInfo('Check1') as CheckBoxFormFieldInfo;
checkboxfieldInfo.defaultValue = true;
checkboxfieldInfo.name = "Check2";
this.documentEditor.setFormFieldInfo('Check1',checkboxfieldInfo);

// Set checkbox form field properties
let dropdownfieldInfo: DropDownFormFieldInfo = this.documentEditor.getFormFieldInfo('Drop1') as DropDownFormFieldInfo;
dropdownfieldInfo.dropdownItems = ['One','Two', 'Three'];
dropdownfieldInfo.name = "Drop2";
this.documentEditor.setFormFieldInfo('Drop1',dropdownfieldInfo);
```

**Placeholders**
- `'Text1'` → Replace with `{currentFieldName}`
- `"Hello"` → Replace with `{defaultValue}`
- `"Uppercase"` → Replace with `{format}`
- `"Text2"` → Replace with `{newFieldName}`
- `['One', 'Two', 'Three']` → Replace with `{dropdownItems}`

**Note:** Ensure the new field name is unique; renaming to an existing name will clear the old field's properties.

## Customize Form Field Shading

Set custom shading color or disable shading for form fields in the UI.

```typescript
// Set a custom shading color (for example, white) 
this.container.documentEditorSettings.formFieldSettings.shadingColor = '#ffffff';

// Disable form field shading entirely 
this.container.documentEditorSettings.formFieldSettings.applyShading = false;
```

**Placeholders**
- `'#ffffff'` → Replace with `{hexColor}`

**Note:** Shading customization affects only the application UI and is not preserved when exporting the document.

## Export Form Field Data

Export all form field values from the document.

```typescript
let formFieldData: FormFieldData[] = this.documentEditor.exportFormData();
```

## Import Form Field Data

Prefill form fields with values.

```typescript
let textformField: FormFieldData = {fieldName: 'Text1', value: 'Hello World'};
let checkformField: FormFieldData = {fieldName: 'Check1', value: true};
let dropdownformField: FormFieldData = {fieldName: 'Drop1', value: 1};
//Import form field data
this.documentEditor.importFormData([textformField,checkformField,dropdownformField]);
```

**Placeholders**
- `'Text1'` → Replace with `{fieldName}`
- `'Hello World'` → Replace with `{textValue}`
- `true` → Replace with `{booleanValue}`
- `1` → Replace with `{dropdownIndex}`

## Reset Form Fields

Reset all form fields to their default values.

```typescript
this.documentEditor.resetFormFields();
```

## Protect Document for Form Filling

Restrict document editing to form fields only.

```typescript
this.documentEditor.editor.enforceProtection('123', 'FormFieldsOnly');
this.documentEditor.editor.stopProtection('123');
```

**Placeholders**
- `'123'` → Replace with `{password}`

**Note:** `enforceProtection` parameters: password and protection type (FormFieldsOnly, ReadOnly, CommentsOnly, or NoProtection). Use `stopProtection` with the same password to disable protection.
