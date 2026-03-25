# Tables in WPF DOCX Editor

Table support in the Syncfusion WPF DOCX Editor allows creating and managing tables within documents.

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

// Initialize and add any number of blocks to the cell here.
tableCellAdv.Blocks.Add(paragraphAdv);

// Initialize and add any number of cells to the row here.
tableRowAdv.Cells.Add(tableCellAdv);

// Initialize and add any number of rows to the table here.
tableAdv.Rows.Add(tableRowAdv);

// Initialize and add any number of blocks to the section here.
section.Blocks.Add(tableAdv);

// Initialize and add any number of sections to the document here.
document.Sections.Add(section);

// Assign the documen to the RichTextBoxAdv instance.
richTextBoxAdv.Document = document;
```
**Placeholders**
- `CellWidth="240"` → Replace with `{cellWidth}`

## Insert Table Commands
### XAML
```xaml
<!-- Inserts the table with default size of one row and two columns -->
<Button Content="Insert Table" Command="RichTextBoxAdv:SfRichTextBoxAdv.InsertTableCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<!-- Inserts the table with the size of two rows and three columns -->
<Button Content="Insert Table" Command="RichTextBoxAdv:SfRichTextBoxAdv.InsertTableCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" CommandParameter="2,3"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
### C#
```csharp
// Insert table at cursor: rows, columns
SfRichTextBoxAdv.InsertTableCommand.Execute("3,3", richTextBoxAdv);
```

**Placeholders**
- `3,3` / `2,3` (rows,columns) → Replace with `{rows},{columns}`

---

## Insert Rows

### Insert Row Below
### XAML
```xaml
<!-- Inserts one row below to the current row -->
<Button Content="Insert Row" Command="RichTextBoxAdv:SfRichTextBoxAdv.InsertRowCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" CommandParameter="Below"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
**Placeholders**
- `"Below"` → Replace with `{rowPlacement}`

### C#
```csharp
// insert below
SfRichTextBoxAdv.InsertRowCommand.Execute(RowPlacement.Below, richTextBoxAdv);
```
 
**Placeholders**
- `RowPlacement.Below` → Replace with `rowPlacement`

---

### Insert Row above
### XAML
```xaml
<!-- Inserts one row above to the current row -->
<Button Content="Insert Row" Command="RichTextBoxAdv:SfRichTextBoxAdv.InsertRowCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" CommandParameter="Above"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
**Placeholders**
- `"Above"` → Replace with `{rowPlacement}`

### C#
```csharp
// insert below
SfRichTextBoxAdv.InsertRowCommand.Execute(RowPlacement.Above, richTextBoxAdv);
```

**Placeholders**
- `RowPlacement.Above` → Replace with `{rowPlacement}`
---

## Insert Columns

### Insert Column Left
### XAML
```xaml
<!-- Inserts one column to the left of current column -->
<Button Content="Insert Column" Command="RichTextBoxAdv:SfRichTextBoxAdv.InsertColumnCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" CommandParameter="Left"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

**Placeholders**
- `Left`  → Replace with `{columnPlacement}`


### C#
```csharp
// insert column to left
SfRichTextBoxAdv.InsertColumnCommand.Execute(ColumnPlacement.Left, richTextBoxAdv);
```
 
**Placeholders**
- `ColumnPlacement.Left` → Replace with `{columnPlacement}`
---

### Insert Column Right
### XAML
```xaml
<!-- Inserts one column to the right of current column -->
<Button Content="Insert Column" Command="RichTextBoxAdv:SfRichTextBoxAdv.InsertColumnCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" CommandParameter="Right"/>

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```
**Placeholders**
- `Right` (CommandParameter) → Replace with `{columnPlacement}`

### C#
```csharp
// insert column to right
SfRichTextBoxAdv.InsertColumnCommand.Execute(ColumnPlacement.Right, richTextBoxAdv);
```
**Placeholders**
- `ColumnPlacement.Right` → Replace with `{columnPlacement}`

## Select Table / Row / Column / Cell

### Select Table

### XAML
```xaml
<!--Selects the Table-->
<Button Content="Select Table" Command="RichTextBoxAdv:SfRichTextBoxAdv.SelectTableCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
SfRichTextBoxAdv.SelectTableCommand.Execute(null, richTextBoxAdv);
```
---

### Select Row

### XAML
```xaml
<!--Selects the Row-->
<Button Content="Select Row" Command="RichTextBoxAdv:SfRichTextBoxAdv.SelectRowCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
SfRichTextBoxAdv.SelectRowCommand.Execute(null, richTextBoxAdv);
```
---

### Select cell

### XAML
```xaml
<!--Selects the Cell--> 
<Button Content="Select Cell" Command="RichTextBoxAdv:SfRichTextBoxAdv.SelectCellCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
 SfRichTextBoxAdv.SelectCellCommand.Execute(null, richTextBoxAdv);
```
---

### Select Column

### XAML
```xaml
<!--Selects the Column-->
<Button Content="Select Column" Command="RichTextBoxAdv:SfRichTextBoxAdv.SelectColumnCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#
```csharp
SfRichTextBoxAdv.SelectColumnCommand.Execute(null, richTextBoxAdv);
```
---

## Delete Table / Row / Column

### Delete Table
```xaml
<!-- Deletes the Table -->
<Button Content="Delete Table" Command="RichTextBoxAdv:SfRichTextBoxAdv.DeleteTableCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

```csharp
SfRichTextBoxAdv.DeleteTableCommand.Execute(null, richTextBoxAdv);
```
---

### Delete Row
```xaml
<!-- Deletes the row -->
<Button Content="Delete Row" Command="RichTextBoxAdv:SfRichTextBoxAdv.DeleteRowCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

```csharp
SfRichTextBoxAdv.DeleteRowCommand.Execute(null, richTextBoxAdv);
```
---

### Delete Column
```xaml
<!-- Deletes the column -->
<Button Content="Delete Column" Command="RichTextBoxAdv:SfRichTextBoxAdv.DeleteColumnCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

```csharp

SfRichTextBoxAdv.DeleteColumnCommand.Execute(null, richTextBoxAdv);
```

---

## Merge Cells

### XAML
```xaml
// Merge selected cells
<!-- Merges the selected cells -->
<Button Content="Merge Cells" Command="RichTextBoxAdv:SfRichTextBoxAdv.MergeSelectedCellsCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />
```

```csharp
// Merge selected cells
SfRichTextBoxAdv.MergeSelectedCellsCommand.Execute(null, richTextBoxAdv);
```

---

## Change content alignment of selected cells

### XAML
```xaml
<!--Change cell content alignment with command parameter as comma separated(vertical alignment and text alignment)-->
<Button Content="Cell Content Alignment" Command="RichTextBoxAdv:SfRichTextBoxAdv.CellContentAlignmentCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" CommandParameter="Top,Left" />

<!--or-->

<!--Change cell content alignment with command parameter single sting (vertical alignment and text alignment)-->
<Button Content="Cell Content Alignment" Command="RichTextBoxAdv:SfRichTextBoxAdv.CellContentAlignmentCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}"  CommandParameter="CenterRight"/>
```

**Placeholders**
- `Top,Left` / `CenterRight` → Replace with `{cellContentAlignment}`
---