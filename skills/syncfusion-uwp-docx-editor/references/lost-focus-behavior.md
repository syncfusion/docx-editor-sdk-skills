# How to show blinking cursor and selection highlight even when the control lost focus

- The `SfRichTextBoxAdv` control can show the blinking caret and/or the selection highlight even when it does not have keyboard focus. 

- Use the `LostFocusBehavior` property to control this behavior.

Supported values:
- `None` — Do not display caret or selection highlight when the control loses focus.
- `ShowCaret` — Display the caret (blinking cursor) when the control loses focus.
- `ShowSelection` — Display the selection highlight when the control loses focus.

---

## XAML

```xaml
<!-- Show selection highlight even when the control doesn't have focus -->
<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" LostFocusBehavior="ShowSelection" />
```

**Placeholders**
- `LostFocusBehavior="ShowSelection"` → Replace with `{lostFocusBehavior}`

## C#

```csharp
// Show caret when control loses focus
richTextBoxAdv.LostFocusBehavior = LostFocusBehavior.ShowCaret;

// Show selection highlight when control loses focus
richTextBoxAdv.LostFocusBehavior = LostFocusBehavior.ShowSelection;

// Revert to default (no caret/selection when unfocused)
richTextBoxAdv.LostFocusBehavior = LostFocusBehavior.None;
```

**Placeholders**
- `LostFocusBehavior.ShowCaret` / `LostFocusBehavior.ShowSelection` / `LostFocusBehavior.None`
  → Replace with `{lostFocusBehavior}`

---