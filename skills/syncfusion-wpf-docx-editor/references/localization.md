# Localization in WPF DOCX Editor

Localization support in the Syncfusion WPF DOCX Editor allows localizing the editor UI and built‑in components using culture‑specific resource files.

---

**Overview:**
- Create resource files that contain translated text for the control and (optionally) the ribbon/dialogs.

- Set the application's `CurrentUICulture` before `InitializeComponent()` so the correct resources are loaded at startup.

**1) Set the current UI culture**

Place code to set the culture before `InitializeComponent()` in `App`/`MainWindow` constructor:

```csharp
public MainWindow()
{
		System.Threading.Thread.CurrentThread.CurrentUICulture =
				new System.Globalization.CultureInfo("fr-FR");

		InitializeComponent();
}
```

**2) Add resource files**
- Create a `Resources` folder in your project.

- Add the default (neutral) resources named:
	- `Syncfusion.SfRichTextBoxAdv.WPF.resx`
	- `Syncfusion.SfRichTextRibbon.WPF.resx` (only if you use `SfRichTextRibbon`)

- For each target culture create a culture-specific resource file using the pattern:
	- `Syncfusion.SfRichTextBoxAdv.WPF.{culture}.resx` (e.g. `Syncfusion.SfRichTextBoxAdv.WPF.fr.resx`)
	- `Syncfusion.SfRichTextRibbon.WPF.{culture}.resx` (if applicable)

In each `.resx` add resource keys (the control/dialog string identifiers) and their translated values. Example entries:

| Key | Value (fr) |
|-----|------------|
| InsertHyperlink | Insérer un lien |
| CancelButton | Annuler |

Note: if your app does not use the ribbon, you can skip the `Syncfusion.SfRichTextRibbon.WPF.*.resx` files.

**3) Where to put the files and naming notes**
- Put the `.resx` files under the `Resources` folder (or any folder in the project). Follow the filename convention above so .NET/Syncfusion can find the resource entries for the control.

**Placeholders**
- `"fr-FR"` / `"en-US"` → Replace with `{culture}`
- `Syncfusion.SfRichTextBoxAdv.WPF.resx` → Replace with `{resourceFileName}`
- `Syncfusion.SfRichTextRibbon.WPF.resx` → Replace with `{ribbonResourceFileName}`
