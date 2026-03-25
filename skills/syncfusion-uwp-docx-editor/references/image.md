# Images in UWP DOCX Editor

Image support in the Syncfusion UWP DOCX Editor allows inserting and managing images within documents using built‑in commands and APIs.


---

## Insert Image

## XAML

```xaml
<!-- Binds button to the InsertPictureCommand -->
<Button Content="Insert Picture" Command="{Binding ElementName=richTextBoxAdv, Path=InsertPictureCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

```csharp
    // Inserts the specified image at the current selection position.
    // If the selection is not empty, selected contents are removed first.
    richTextBoxAdv.Selection.InsertPicture(object picture);
```

**Placeholders**
- `picture` → Replace with `{pictureSource}`

---

## Supported image formats

`SfRichTextBoxAdv` supports common raster image formats such as:

- Bitmap images (`.bmp`)
- JPEG (`.jpg`, `.jpeg`)
- PNG (`.png`)

Metafile images are not supported. When inserting from streams or files, ensure the data is a supported raster image format.

---

## Text wrapping styles

Currently, `SfRichTextBoxAdv` preserves image and textbox shapes with the following wrapping styles:

- Inline
- Square
- Top and Bottom
- Front/Behind Text

---

## Text wrapping style preservation
- At present, only **image preservation** with the above text-wrapping styles is supported.

- Modifying **existing wrapping styles** is **not supported**.
