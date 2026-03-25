# Radial Menu in UWP DOCX Editor

The UWP DOCX Editor provides a built‑in radial menu that offers quick access to rich‑text formatting options.

---

> **Note**
>
> The built-in radial menu is not supported on Windows Phone devices.

## Enable / disable Radial Menu

### XAML
Set `EnableRadialMenu` on the control to enable or disable the built-in radial menu.

```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv"
                                  ManipulationMode="All"
                                  EnableRadialMenu="True"
                                  xmlns:RichTextBoxAdv="using:Syncfusion.UI.Xaml.RichTextBoxAdv" />
```

**Placeholders**
- `ManipulationMode="All"` → Replace with `{manipulationMode}`
- `EnableRadialMenu="True"` → Replace with `{enableRadialMenu}`

### C#

```csharp
// Initializes a new instance of SfRichTextBoxAdv.
SfRichTextBoxAdv richTextBoxAdv = new SfRichTextBoxAdv();
richTextBoxAdv.ManipulationMode = ManipulationModes.All;

//Disables the built-in radial menu in RichTextBoxAdv.
richTextBoxAdv.EnableRadialMenu = false;
```

**Placeholders**
- `ManipulationModes.All` → Replace with `{manipulationMode}`
- `false` → Replace with `{enableRadialMenu}`

---


## Customizing radial menu appearance

- How to customize the radial menu rim, navigation button, radial pointer and slider.

```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBox" ManipulationMode="All" AcceptsTab="True" xmlns:RichTextBoxAdv="using:Syncfusion.UI.Xaml.RichTextBoxAdv">
  <!-- Specify resources for this instance -->
  <RichTextBoxAdv:SfRichTextBoxAdv.Resources>
  
    <!-- Custom style for Radial Menu -->
    <Style TargetType="radialMenu:SfRadialMenu">
      <Setter Property="RimBackground" Value="#EFEFEF"/>
      <Setter Property="RimActiveBrush" Value="#0071BC"/>
      <Setter Property="NavigationButtonStyle" Value="{StaticResource RTERadialMenuNavigationButtonStyle}"/>
    </Style>
    
    <!-- Custom Style for Radial Pointer -->
    <Style TargetType="radialMenu:RadialPointer" x:Key="RadialPointerStyle">
      <Setter Property="Height" Value="2"/>
      <Setter Property="IsTabStop" Value="False"/>
      <Setter Property="Template">
        <Setter.Value>
          <ControlTemplate TargetType="radialMenu:RadialPointer">
            <Border  Background="#0071BC"/>
          </ControlTemplate>
        </Setter.Value>
      </Setter>
    </Style>
    
    <!-- Custom Style for Radial Slider -->
    <Style TargetType="radialMenu:SfRadialSlider">
      <Setter Property="Foreground" Value="#0071BC"/>
      <Setter Property="InnerRimFill" Value="#0071BC"/>
      <Setter Property="OuterRimStroke" Value="#0071BC"/>
      <Setter Property="PointerStyle" Value="{StaticResource RadialPointerStyle}"/>
    </Style>
    
    <!-- Custom Style for Navigation Button -->
    <Style x:Key="RTERadialMenuNavigationButtonStyle" TargetType="Button">
      <Setter Property="FontFamily" Value="Segoe UI Symbol"/>
      <Setter Property="BorderBrush" Value="#0071BC"/>
      <Setter Property="Template">
        <Setter.Value>
          <ControlTemplate TargetType="Button">
            <Grid Background="Transparent" Margin="-5">
              <VisualStateManager.VisualStateGroups>
                <VisualStateGroup x:Name="CommonStates">
                  <VisualState x:Name="Normal"/>
                  <VisualState x:Name="PointerOver">
                    <Storyboard>
                      <ObjectAnimationUsingKeyFrames Storyboard.TargetProperty="Fill" Storyboard.TargetName="BackgroundEllipse">
                        <DiscreteObjectKeyFrame KeyTime="0" Value="LightGray"/>
                      </ObjectAnimationUsingKeyFrames>
                    </Storyboard>
                  </VisualState>
                </VisualStateGroup>
              </VisualStateManager.VisualStateGroups>
              <Ellipse Fill="White" x:Name="BackgroundEllipse" />
              <Ellipse Stroke="{TemplateBinding BorderBrush}" StrokeThickness="2"  Fill="Transparent"/>
              <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
            </Grid>
          </ControlTemplate>
        </Setter.Value>
      </Setter>
    </Style>
  </RichTextBoxAdv:SfRichTextBoxAdv.Resources>
</RichTextBoxAdv:SfRichTextBoxAdv>
```

> **Note**
>
> A sample demonstrating how to customize the built-in radial menu style can be downloaded from the following link:  
> [Sample](http://www.syncfusion.com/downloads/support/directtrac/general/ze/RadialMenuCustomization-1397995223)
