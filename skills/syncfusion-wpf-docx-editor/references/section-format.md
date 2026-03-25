# Section Formatting in WPF DOCX Editor

Section formatting support in the Syncfusion WPF DOCX Editor allows controlling page‑level layout and header/footer behavior within documents.


---

## Set Page Size

### XAML
```xaml
<!-- Defines a Section of page size 480 x 520 pixels. --> 
<RichTextBoxAdv:SectionAdv>
    <RichTextBoxAdv:SectionAdv.SectionFormat>
        <RichTextBoxAdv:SectionFormat PageSize="480 520"/>
    </RichTextBoxAdv:SectionAdv.SectionFormat>
    <!-- Define the blocks, headers and footers of the section. --> 
</RichTextBoxAdv:SectionAdv>
```

**Placeholders**
- `PageSize="480 520"` → Replace with `{pageSize}` *(format: `{pageWidth} {pageHeight}`)*


### C#
```csharp
// Defines a Section of page size 480 x 520 pixels.
SectionAdv section = new SectionAdv();
SectionFormat sectionFormat = new SectionFormat();
sectionFormat.PageSize = new Size(480, 520);
section.SectionFormat = sectionFormat;
```
**Placeholders**
- `480` → Replace with `{pageWidth}`
- `520` → Replace with `{pageHeight}`


---

## Set Page Margins

### XAML
```xaml
<!-- Defines a Section with left and right page margins as 96 pixels and top and bottom margins as 48 pixels respectively. --> 
<RichTextBoxAdv:SectionAdv>
    <RichTextBoxAdv:SectionAdv.SectionFormat>
        <RichTextBoxAdv:SectionFormat PageMargin="96 48 96 48"/>
    </RichTextBoxAdv:SectionAdv.SectionFormat>
    <!-- Define the blocks, headers and footers of the section. --> 
</RichTextBoxAdv:SectionAdv>
```

**Placeholders**
- `PageMargin="96 48 96 48"` → Replace with `{pageMargin}` *(format: `{left} {top} {right} {bottom}`)*


### C#
```csharp
// Defines a Section with left and right page margins as 96 pixels and top and bottom margins as 48 pixels respectively.
SectionAdv section = new SectionAdv();
SectionFormat sectionFormat = new SectionFormat();
sectionFormat.PageMargin = new Thickness(96, 48, 96, 48);
section.SectionFormat = sectionFormat;
```

**Placeholders**
- `96` → Replace with `{left}` / `{right}`
- `48` → Replace with `{top}` / `{bottom}`
```

---

## Set Header distance

### XAML
```xaml
<!-- Defines a Section with header distance of 96 pixels. --> 
<RichTextBoxAdv:SectionAdv>
    <RichTextBoxAdv:SectionAdv.SectionFormat>
        <RichTextBoxAdv:SectionFormat HeaderDistance="96"/>
    </RichTextBoxAdv:SectionAdv.SectionFormat>
    <!-- Define the blocks, headers and footers of the section. --> 
</RichTextBoxAdv:SectionAdv>
```
**Placeholders**
- `HeaderDistance="96"` → Replace with `{headerDistance}`

### C#
```csharp
// Defines a Section with header distance of 96 pixels.
SectionAdv section = new SectionAdv();
SectionFormat sectionFormat = new SectionFormat();
sectionFormat.HeaderDistance = 96;
section.SectionFormat = sectionFormat;
```

**Placeholders**
- `96` → Replace with `{headerDistance}`

---

## Set Footer distance

### XAML
```xaml
<!-- Defines a Section with footer distance of 48 pixels. --> 
<RichTextBoxAdv:SectionAdv>
    <RichTextBoxAdv:SectionAdv.SectionFormat>
        <RichTextBoxAdv:SectionFormat FooterDistance="48"/>
    </RichTextBoxAdv:SectionAdv.SectionFormat>
    <!-- Define the blocks, headers and footers of the section. --> 
</RichTextBoxAdv:SectionAdv>
```

**Placeholders**
- `FooterDistance="48"` → Replace with `{footerDistance}`

### C#
```csharp
// Defines a Section with footer distance of 48 pixels.
SectionAdv section = new SectionAdv();
SectionFormat sectionFormat = new SectionFormat();
sectionFormat.FooterDistance = 48;
section.SectionFormat = sectionFormat;
```

**Placeholders**
- `48` → Replace with `{footerDistance}`
---

## Set Different First Page in Section

How to specify that a section has different first page header and footer.

### XAML
```xaml
<!-- Defines a Section that has different first page header and footer. --> 
<RichTextBoxAdv:SectionAdv>
    <RichTextBoxAdv:SectionAdv.SectionFormat>
        <RichTextBoxAdv:SectionFormat DifferentFirstPage="True"/>
    </RichTextBoxAdv:SectionAdv.SectionFormat>
    <!-- Define the blocks, headers and footers of the section. --> 
</RichTextBoxAdv:SectionAdv>
```

**Placeholders**
- `DifferentFirstPage="True"` → Replace with `{differentFirstPage}`

### C#
```csharp
// Defines a Section that has different first page header and footer.
SectionAdv section = new SectionAdv();
SectionFormat sectionFormat = new SectionFormat();
sectionFormat.DifferentFirstPage = true;
section.SectionFormat = sectionFormat;
```

**Placeholders**
- `true` / `false` → Replace with `{differentFirstPage}`

---

## Set Different Odd And EvenPages in Section

How to specify that a section has different odd and even pages header and footer.

### XAML
```xaml
<!-- Defines a Section that has different odd and even pages header and footer. --> 
<RichTextBoxAdv:SectionAdv>
    <RichTextBoxAdv:SectionAdv.SectionFormat>
        <RichTextBoxAdv:SectionFormat DifferentOddAndEvenPages="True"/>
    </RichTextBoxAdv:SectionAdv.SectionFormat>
    <!-- Define the blocks, headers and footers of the section. --> 
</RichTextBoxAdv:SectionAdv>
```
**Placeholders**
- `DifferentOddAndEvenPages="True"` → Replace with `{differentOddAndEvenPages}`

### C#
```csharp
// Defines a Section that has different odd and even pages header and footer.
SectionAdv section = new SectionAdv();
SectionFormat sectionFormat = new SectionFormat();
sectionFormat.DifferentOddAndEvenPages = true;
section.SectionFormat = sectionFormat;
```

**Placeholders**
- `true` / `false` → Replace with `{differentOddAndEvenPages}`

---