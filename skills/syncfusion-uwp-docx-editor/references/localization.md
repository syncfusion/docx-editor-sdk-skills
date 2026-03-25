# Localization in UWP DOCX Editor

Localization support in the Syncfusion UWP DOCX Editor allows localizing the editor UI and built‑in components using culture‑specific resource files.
---

## 1. Configure app default language (Package.appxmanifest)

1. In Solution Explorer, expand your UWP project node and open `Package.appxmanifest` with the Manifest Designer.

2. On the Application tab set the **Default language** to the language code you want (for example, `en-US`).

3. Save the manifest.

- This makes the app aware of its default language and enables the platform to load the appropriate resources.

---

## 2. Add resource (.resw) files

1. Create a top-level `Resources` folder in your project.

2. Under `Resources` add language subfolders such as `en-US`, `fr-FR`, etc.

3. In each language subfolder add the Syncfusion resource files and your app's localization file. Typical names used by SfRichTextBoxAdv are:

- `Syncfusion.SfRichTextBoxAdv.UWP.Resources.resw`
- `Syncfusion.SfRibbon.Resources.resw` (only if you use SfRibbon)
- `Localization.Resources.resw` (your app-specific strings)

4. Add the required resource keys and localized values for each string the control uses (for example, dialog button text, radial menu item labels, etc.). You can use Visual Studio's Resource Designer to add keys and values.

Note: If your app does not use `SfRibbon`, you can skip the `Syncfusion.SfRibbon.Resources.resw` file.

---

## 3. Verify localization in SfRichTextBoxAdv

- When the resources are in place and the app language is set, `SfRichTextBoxAdv` will pick localized text from the resource files and the SfRichTextBoxAdv will display translated strings.