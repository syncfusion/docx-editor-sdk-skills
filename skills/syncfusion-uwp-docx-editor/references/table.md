# Tables in UWP DOCX Editor

Table support in the Syncfusion UWP DOCX Editor allows creating and managing tables within documents.

---

## Insert Table

### XAML
```xaml
<RichTextBoxAdv:DocumentAdv>
    <RichTextBoxAdv:SectionAdv>
        <RichTextBoxAdv:TableAdv>
            <RichTextBoxAdv:TableRowAdv>
                <RichTextBoxAdv:TableCellAdv>
                    <RichTextBoxAdv:TableCellAdv.CellFormat>
                        <RichTextBoxAdv:CellFormat CellWidth="240"/>
                    </RichTextBoxAdv:TableCellAdv.CellFormat>
                    <RichTextBoxAdv:ParagraphAdv>
                        <RichTextBoxAdv:SpanAdv>Cell 1</RichTextBoxAdv:SpanAdv>
                    </RichTextBoxAdv:ParagraphAdv>
                </RichTextBoxAdv:TableCellAdv>
                <RichTextBoxAdv:TableCellAdv>
                    <RichTextBoxAdv:TableCellAdv.CellFormat>
                        <RichTextBoxAdv:CellFormat CellWidth="240"/>
                    </RichTextBoxAdv:TableCellAdv.CellFormat>
                    <RichTextBoxAdv:ParagraphAdv>
                        <RichTextBoxAdv:SpanAdv>Cell 2</RichTextBoxAdv:SpanAdv>
                    </RichTextBoxAdv:ParagraphAdv>
                </RichTextBoxAdv:TableCellAdv>
            </RichTextBoxAdv:TableRowAdv>
        </RichTextBoxAdv:TableAdv>
        <RichTextBoxAdv:ParagraphAdv/>
    </RichTextBoxAdv:SectionAdv>
</RichTextBoxAdv:DocumentAdv>
```

### C#
```csharp
// Initializes a document.
DocumentAdv document = new DocumentAdv();

// Initialize a section.
SectionAdv section = new SectionAdv();

// Initialize a table.
TableAdv tableAdv = new TableAdv();

// Initialize a row.
TableRowAdv tableRowAdv = new TableRowAdv();

// Initialize a table cell.
TableCellAdv tableCellAdv = new TableCellAdv();
tableCellAdv.CellFormat.CellWidth = 240;

// Initializes a paragraph.
ParagraphAdv paragraphAdv = new ParagraphAdv();
SpanAdv spanAdv = new SpanAdv();
spanAdv.Text = "Cell 1";
paragraphAdv.Inlines.Add(spanAdv);

tableCellAdv.Blocks.Add(paragraphAdv);
// Initialize and add any number of blocks to the cell here.

tableRowAdv.Cells.Add(tableCellAdv);
// Initialize and add any number of cells to the row here.

tableAdv.Rows.Add(tableRowAdv);
// Initialize and add any number of rows to the table here.

section.Blocks.Add(tableAdv);
// Initialize and add any number of blocks to the section here.

document.Sections.Add(section);
// Initialize and add any number of sections to the document here.

// Assign the document to the RichTextBoxAdv instance.
richTextBoxAdv.Document = document;
```
**Placeholders**
- `CellWidth="240"` → Replace with `{cellWidth}`

## Insert Table Commands
### XAML
```xaml
<!-- Inserts the table with default size of one row and two columns -->
<Button Content="Insert Table" Command="{Binding ElementName=richTextBoxAdv,Path=InsertTableCommand}"/>

<!-- Inserts the table with the size of two rows and three columns -->
<Button Content="Insert Table" Command="{Binding ElementName=richTextBoxAdv,Path=InsertTableCommand}" CommandParameter="2,3"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
### C#
```csharp
// Insert table at cursor: rows, columns
richTextBoxAdv.InsertTableCommand.Execute("2,3");
```

**Placeholders**
- `3,3` / `2,3` (rows,columns) → Replace with `{rows},{columns}`

---

## Insert Rows

### Insert Row Below
### XAML
```xaml
<!-- Inserts one row below to the current row -->
<Button Content="Insert Row" Command="{Binding ElementName=richTextBoxAdv,Path=InsertRowCommand}" CommandParameter="Below"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
**Placeholders**
- `"Below"` → Replace with `{rowPlacement}`

### C#
```csharp
// insert below
 richTextBoxAdv.InsertRowCommand.Execute(RowPlacement.Below);
```
 
**Placeholders**
- `RowPlacement.Below` → Replace with `rowPlacement`

---

### Insert Row above
### XAML
```xaml
<!-- Inserts one row above to the current row -->
<Button Content="Insert Row" Command="{Binding ElementName=richTextBoxAdv,Path=InsertRowCommand}" CommandParameter="Above"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
**Placeholders**
- `"Above"` → Replace with `{rowPlacement}`

### C#
```csharp
// insert above
richTextBoxAdv.InsertRowCommand.Execute(RowPlacement.Above);
```

**Placeholders**
- `RowPlacement.Above` → Replace with `{rowPlacement}`
---

## Insert Columns

### Insert Column Left
### XAML
```xaml
<!-- Inserts one column to the left of current column -->
<Button Content="Insert Column" Command="{Binding ElementName=richTextBoxAdv,Path=InsertColumnCommand}" CommandParameter="Left"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

**Placeholders**
- `Left`  → Replace with `{columnplacement}`


### C#
```csharp
// insert column to left
richTextBoxAdv.InsertColumnCommand.Execute(ColumnPlacement.Left);
```
 
**Placeholders**
- `ColumnPlacement.Left` → Replace with `{columnPlacement}`
---

### Insert Column Right
### XAML
```xaml
<!-- Inserts one column to the right of current column -->
<Button Content="Insert Column" Command="{Binding ElementName=richTextBoxAdv,Path=InsertColumnCommand}" CommandParameter="Right"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
**Placeholders**
- `Right` (CommandParameter) → Replace with `{columnplacement}`

### C#
```csharp
// insert column to right
richTextBoxAdv.InsertColumnCommand.Execute(ColumnPlacement.Right);
```
**Placeholders**
- `ColumnPlacement.Right` → Replace with `{columnplacement}`

## Select Table / Row / Column / Cell

### Select Table

### XAML
```xaml
<!--Selects the Table-->
<Button Content="Select Table" Command="{Binding ElementName=richTextBoxAdv,Path=SelectTableCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
richTextBoxAdv.SelectTableCommand.Execute(null);
```
---

### Select Row

### XAML
```xaml
<!--Selects the Row-->
<Button Content="Select Row" Command="{Binding ElementName=richTextBoxAdv,Path=SelectRowCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
richTextBoxAdv.SelectRowCommand.Execute(null);
```
---

### Select cell

### XAML
```xaml
<!--Selects the Cell--> 
<Button Content="Select Cell" Command="{Binding ElementName=richTextBoxAdv,Path=SelectCellCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
richTextBoxAdv.SelectCellCommand.Execute(null);
```
---

### Select Column

### XAML
```xaml
<!--Selects the Column-->
<Button Content="Select Column" Command="{Binding ElementName=richTextBoxAdv,Path=SelectColumnCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
richTextBoxAdv.SelectColumnCommand.Execute(null);
```
---

## Delete Table / Row / Column

### Delete Table
```xaml
<!-- Deletes the Table -->
<Button Content="Delete Table" Command="{Binding ElementName=richTextBoxAdv,Path=DeleteTableCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

```csharp
richTextBoxAdv.DeleteTableCommand.Execute(null);
```
---

### Delete Row
```xaml
<!-- Deletes the row -->
<Button Content="Delete Row" Command="{Binding ElementName=richTextBoxAdv,Path=DeleteRowCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

```csharp
richTextBoxAdv.DeleteRowCommand.Execute(null);
```
---

### Delete Column
```xaml
<!-- Deletes the column -->
<Button Content="Delete Column" Command="{Binding ElementName=richTextBoxAdv,Path=DeleteColumnCommand}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

```csharp
richTextBoxAdv.DeleteColumnCommand.Execute(null);
```

---

## Merge Cells

### XAML
```xaml
// Merge selected cells
<!-- Merges the selected cells -->
<Button Content="Merge Cells" Command="{Binding ElementName=richTextBoxAdv,Path=MergeSelectedCellsCommand}" />
```

```csharp
// Merge selected cells
richTextBoxAdv.MergeSelectedCellsCommand.Execute(null);
```

---

## Change content alignment of selected cells

### XAML
```xaml
<!--Change cell content alignment with command parameter as comma separated(vertical alignment and text alignment)-->
<Button Content="Cell Content Alignment" Command="{Binding ElementName=richTextBoxAdv,Path=CellContentAlignmentCommand}" CommandParameter="Top,Left" />

<!--or-->

<!--Change cell content alignment with command parameter single sting (vertical alignment and text alignment)-->
<Button Content="Cell Content Alignment" Command="{Binding ElementName=richTextBoxAdv,Path=CellContentAlignmentCommand}" CommandParameter="CenterRight"/>
```

**Placeholders**
- `Top,Left` / `CenterRight` → Replace with `{cellContentAlignment}`
---