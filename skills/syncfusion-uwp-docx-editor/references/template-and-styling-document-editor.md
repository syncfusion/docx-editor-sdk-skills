# Templates and Styling in UWP DOCX Editor

Template and styling support in the Syncfusion UWP DOCX Editor allows customizing the appearance and visual structure of the editor control using UWP styles and templates.


---

##  Default style and template for the SfRichTextBoxAdv control

### XAML
```xaml
<Style TargetType="RichTextBoxAdv:SfRichTextBoxAdv" xmlns:RichTextBoxAdv="using:Syncfusion.UI.Xaml.RichTextBoxAdv">
    <Setter Property="Template">
        <Setter.Value>
            <ControlTemplate TargetType="RichTextBoxAdv:SfRichTextBoxAdv">
                <Border Background="{TemplateBinding Background}" BorderBrush="{TemplateBinding BorderBrush}" BorderThickness="{TemplateBinding BorderThickness}">
                    <Grid>
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition Width="Auto"/>
                            <ColumnDefinition Width="*"/>
                        </Grid.ColumnDefinitions>
                        <Grid x:Name="OptionsPane" Visibility="Collapsed"/>
                        <Grid Grid.Column="1">
                            <Grid.ColumnDefinitions>
                                <ColumnDefinition Width="*"/>
                                <ColumnDefinition Width="Auto"/>
                            </Grid.ColumnDefinitions>
                            <Grid.RowDefinitions>
                                <RowDefinition Height="*"/>
                                <RowDefinition Height="Auto"/>
                            </Grid.RowDefinitions>
                            <ContentControl x:Name="content" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Grid.Row="0" Grid.Column="0" />
                            <ScrollBar x:Name="HorizontalScrollBar" Grid.Column="0" Height="16" Visibility="Collapsed" IsTabStop="False" Minimum="0" Orientation="Horizontal" Grid.Row="1"/>
                            <ScrollBar x:Name="VerticalScrollBar" Grid.Column="1" IsTabStop="False" Visibility="Collapsed" Minimum="0" Orientation="Vertical" Grid.Row="0" Width="16"/>
                        </Grid>
                    </Grid>
                </Border>
            </ControlTemplate>
        </Setter.Value>
    </Setter>
</Style>
```

## Styling the SfRichTextBoxAdv

Demonstrates how to customize the style for SfRichTextBoxAdv control.

### XAML
```xaml
<Style x:Key="RichTextBoxAdvCustomStyle" TargetType="RichTextBoxAdv:SfRichTextBoxAdv" xmlns:RichTextBoxAdv="using:Syncfusion.UI.Xaml.RichTextBoxAdv">
    <Setter Property="BorderThickness" Value="1"/>
    <Setter Property="Template">
        <Setter.Value>
            <ControlTemplate TargetType="RichTextBoxAdv:SfRichTextBoxAdv">
                <Border Background="{TemplateBinding Background}" BorderBrush="{TemplateBinding BorderBrush}" BorderThickness="{TemplateBinding BorderThickness}">
                    <Grid>
                        <Grid.RowDefinitions>
                            <RowDefinition Height="Auto"/>
                            <RowDefinition Height="*"/>
                        </Grid.RowDefinitions>
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition Width="Auto"/>
                            <ColumnDefinition Width="*"/>
                        </Grid.ColumnDefinitions>
                        <Border Background="Gray" Grid.Row="0" Grid.Column="0" Grid.ColumnSpan="2">
                            <TextBlock Text="Rich Text Editor" FontSize="28" HorizontalAlignment="Center" Foreground="White"/>
                        </Border>
                        <Grid x:Name="OptionsPane" Visibility="Collapsed" Grid.Row="1" Grid.Column="0"/>
                        <Grid Grid.Row="1" Grid.Column="1">
                            <Grid.ColumnDefinitions>
                                <ColumnDefinition Width="Auto"/>
                                <ColumnDefinition Width="*"/>
                            </Grid.ColumnDefinitions>
                            <Grid.RowDefinitions>
                                <RowDefinition Height="*"/>
                                <RowDefinition Height="Auto"/>
                            </Grid.RowDefinitions>
                            <ContentControl x:Name="content" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Grid.Row="0" Grid.Column="1" />
                            <ScrollBar x:Name="HorizontalScrollBar" Grid.Column="0" Height="16" Visibility="Collapsed" IsTabStop="False" Minimum="0" Orientation="Horizontal" Grid.Row="1"/>
                            <ScrollBar x:Name="VerticalScrollBar" Grid.Column="0" IsTabStop="False" Visibility="Collapsed" Minimum="0" Orientation="Vertical" Grid.Row="0" Width="16"/>
                        </Grid>
                    </Grid>
                </Border>
            </ControlTemplate>
        </Setter.Value>
    </Setter>
</Style>
```

- The following code example demonstrates how to apply the custom style for SfRichTextBoxAdv control. 

### XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" ManipulationMode="All" Style="{StaticResource RichTextBoxAdvCustomStyle}"/>
```