# Form Fields

> Insert, inspect, update, fill, reset, and protect form fields.

---

## Insert Form Fields

```tsx
// Insert Text form field
documentEditor.editor.insertFormField('Text');

// Insert Checkbox form field
documentEditor.editor.insertFormField('CheckBox');

// Insert DropDown form field
documentEditor.editor.insertFormField('DropDown');
```

---

## Get Form Field Names

```tsx
let formFieldsNames: string[] = documentEditor.getFormFieldNames();
```

---

## Form Field Properties

### Get Form Field Properties

```tsx
// Text form field
let textfieldInfo: TextFormFieldInfo = documentEditor.getFormFieldInfo('Text1') as TextFormFieldInfo;

// Checkbox form field
let checkboxfieldInfo: CheckBoxFormFieldInfo = documentEditor.getFormFieldInfo('Check1') as CheckBoxFormFieldInfo;

// DropDown form field
let dropdownfieldInfo: DropDownFormFieldInfo = documentEditor.getFormFieldInfo('Drop1') as DropDownFormFieldInfo;
```

**Placeholders**
- `'Text1'` → Replace with `{textFieldName}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `'Drop1'` → Replace with `{dropdownFieldName}`

### Set Form Field Properties

When you need to rename fields or update default values.

```tsx
// Set text form field properties
let textfieldInfo: TextFormFieldInfo = documentEditor.getFormFieldInfo('Text1') as TextFormFieldInfo;
textfieldInfo.defaultValue = 'Hello';
textfieldInfo.format = 'Uppercase';
textfieldInfo.type = 'Text';
textfieldInfo.name = 'Text2';
documentEditor.setFormFieldInfo('Text1', textfieldInfo);

// Set checkbox form field properties
let checkboxfieldInfo: CheckBoxFormFieldInfo = documentEditor.getFormFieldInfo('Check1') as CheckBoxFormFieldInfo;
checkboxfieldInfo.defaultValue = true;
checkboxfieldInfo.name = 'Check2';
documentEditor.setFormFieldInfo('Check1', checkboxfieldInfo);

// Set dropdown form field properties
let dropdownfieldInfo: DropDownFormFieldInfo = documentEditor.getFormFieldInfo('Drop1') as DropDownFormFieldInfo;
dropdownfieldInfo.dropdownItems = ['One', 'Two', 'Three'];
dropdownfieldInfo.name = 'Drop2';
documentEditor.setFormFieldInfo('Drop1', dropdownfieldInfo);
```

**Placeholders**
- `'Text1'` → Replace with `{textFieldName}`
- `'Hello'` → Replace with `{defaultTextValue}`
- `'Text2'` → Replace with `{newTextFieldName}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `'Check2'` → Replace with `{newCheckboxFieldName}`
- `['One', 'Two', 'Three']` → Replace with `{dropdownItems}`
- `'Drop1'` → Replace with `{dropdownFieldName}`
- `'Drop2'` → Replace with `{newDropdownFieldName}`

**Note**
- If the new field name already exists, the old field name is cleared. Use unique names.

---

## Form Field Shading

```tsx
// Set a custom shading color (for example, white) 
container.current.documentEditorSettings.formFieldSettings.shadingColor = '#ffffff';

// Disable form field shading entirely 
container.current.documentEditorSettings.formFieldSettings.applyShading = false;
```

**Placeholders**
- `'#ffffff'` → Replace with `{shadingColor}`

**Note**
- This affects only the application UI and is not preserved in exported documents.

---

## Form Filling Mode

```tsx
// Popup mode
container.current.documentEditorSettings.formFieldSettings.formFillingMode = 'Popup';

// Inline mode
container.current.documentEditorSettings.formFieldSettings.formFillingMode = 'Inline';
```

---

## Export Form Field Data

```tsx
let formFieldData: FormFieldData[] = documentEditor.exportFormData();
```

---

## Import Form Field Data

```tsx
let textformField: FormFieldData = { fieldName: 'Text1', value: 'Hello World' };
let checkformField: FormFieldData = { fieldName: 'Check1', value: true };
let dropdownformField: FormFieldData = { fieldName: 'Drop1', value: 1 };

documentEditor.importFormData([textformField, checkformField, dropdownformField]);
```

**Placeholders**
- `'Text1'` → Replace with `{textFieldName}`
- `'Hello World'` → Replace with `{textFieldValue}`
- `'Check1'` → Replace with `{checkboxFieldName}`
- `true` → Replace with `{checkboxValue}`
- `'Drop1'` → Replace with `{dropdownFieldName}`
- `1` → Replace with `{dropdownIndex}`

---

## Reset Form Fields

```tsx
documentEditor.resetFormFields();
```