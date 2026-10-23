# Insert Text Box

Insert a configurable text box shape into the document.

## Insert Text Box Using API

Opens the Text Box dialog programmatically, allowing users to configure and insert a text box.

**Setup**  
All JavaScript examples assume `var documentEditor = document.getElementById('container').ej2_instances[0].documentEditor;` is available. Adapt the container ID as needed.

```javascript
documentEditor.showDialog('TextBox');
```

**Placeholders**
- `'container'` → Replace with `{container element id}`