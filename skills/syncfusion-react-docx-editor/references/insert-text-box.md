# Insert Text Box

Insert a configurable text box shape into the document.

## Insert Text Box Using API

Opens the Text Box dialog programmatically, allowing users to configure and insert a text box.

```tsx
container.current.documentEditor.showDialog('TextBox');
```

**Placeholders**
- `container` → Replace with `{ref to the DocumentEditorContainer instance}`