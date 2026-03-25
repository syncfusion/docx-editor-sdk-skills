# Document Editor in WPF

The Syncfusion WPF DOCX Editor provides a rich document editing control for creating and interacting with Word documents in WPF applications.

---

## XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" 
xmlns:RichTextBoxAdv="clr-namespace:Syncfusion.Windows.Controls.RichTextBoxAdv;assembly=SyncfusionSfRichTextBoxAdv.Wpf" />
```
---

## C# (programmatic)
```csharp
// Initializes a new instance of RichTextBoxAdv.
SfRichTextBoxAdv richTextBoxAdv = new SfRichTextBoxAdv();
```

## Creating Document editor with Ribbon
```xaml

<Syncfusion:RibbonWindow x:Class="DocumentEditor.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:DocumentEditor"
        mc:Ignorable="d"
        xmlns:Syncfusion="http://schemas.syncfusion.com/wpf"
        Title="MainWindow" Height="350" Width="525">
<Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="*"/>
        </Grid.RowDefinitions>
        <Syncfusion:SfRichTextRibbon x:Name="richTextRibbon 
                                    SnapsToDevicePixels="True" 
                                    DataContext="{Binding ElementName=richTextBoxAdv}" />
        <Syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" Background="#F1F1F1" />
</Grid>
</Syncfusion:RibbonWindow>
```
---