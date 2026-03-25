
# Automatic Suggestion in WPF DOCX Editor

Automatic suggestion support in the Syncfusion WPF DOCX Editor enables inline mention‑based suggestions using configurable trigger characters and customizable suggestion providers.

---

**Overview**
- `SfRichTextBoxAdv` shows an inline suggestion list when the user types a mention character (default `@`).

- The list filters as the user types; use arrow keys to navigate and `Tab`/`Enter` (or mouse) to insert the selected item. By default the inserted item is a hyperlink.

## Enable Name suggestions
Add suggestion items (example uses a resource array) and wire a `NameSuggestionProvider` to the editor's `SuggestionSettings`:

### XAML
```xaml
<Window.Resources>
	<x:Array Type="{x:Type RichTextBoxAdv:NameSuggestionItem}" x:Key="suggestionItems">
		<RichTextBoxAdv:NameSuggestionItem Name = "Nancy Davolio" Link="mailto:nancy.davolio@northwindtraders.com" ImageSource="/Assets/People_Circle0.png" />
		<RichTextBoxAdv:NameSuggestionItem Name = "Andrew Fuller" Link="mailto:andrew.fuller@northwindtraders.com" ImageSource="/Assets/People_Circle5.png"/>
		<RichTextBoxAdv:NameSuggestionItem Name = "Steven Buchanan" Link="mailto:steven.buchanan@northwindtraders.com" ImageSource="/Assets/People_Circle18.png"/>
	</x:Array>
</Window.Resources>
    <Grid>
        <RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextboxadv" LayoutType="Continuous">
            <RichTextBoxAdv:SfRichTextBoxAdv.SuggestionSettings>
                <RichTextBoxAdv:SuggestionSettings>
                    <RichTextBoxAdv:SuggestionSettings.SuggestionProviders>
                        <RichTextBoxAdv:NameSuggestionProvider     ItemsSource="{StaticResource suggestionItems}">
                        </RichTextBoxAdv:NameSuggestionProvider>
                    </RichTextBoxAdv:SuggestionSettings.SuggestionProviders>
                </RichTextBoxAdv:SuggestionSettings>
            </RichTextBoxAdv:SfRichTextBoxAdv.SuggestionSettings>
        </RichTextBoxAdv:SfRichTextBoxAdv>
    </Grid>
```

**Placeholders**
- `"Nancy Davolio"` / `"Andrew Fuller"` / `"Steven Buchanan"` → Replace with `{personName}`
- `"mailto:nancy.davolio@northwindtraders.com"` → Replace with `{emailLink}`
- `"/Assets/People_Circle0.png"` → Replace with `{imageSource}`

### C#
```csharp
    ISuggestionProvider suggestionProvider = new NameSuggestionProvider();
	List<NameSuggestionItem> suggestionItems = new List<NameSuggestionItem>();

	NameSuggestionItem suggestionItem = new NameSuggestionItem();
	suggestionItem.Name = "Nancy Davolio";
	suggestionItem.Link = "mailto:nancy.davolio@northwindtraders.com";
	BitmapImage bitmapImage = new BitmapImage(new Uri(new DirectoryInfo(@"..\..\Assets\People_Circle0.png").FullName));
	suggestionItem.ImageSource = bitmapImage;
	suggestionItems.Add(suggestionItem);

	suggestionItem = new NameSuggestionItem();
	suggestionItem.Name = "Andrew Fuller";
	suggestionItem.Link = "mailto:andrew.fuller@northwindtraders.com";
	bitmapImage = new BitmapImage(new Uri(new DirectoryInfo(@"..\..\Assets\People_Circle5.png").FullName));
	suggestionItem.ImageSource = bitmapImage;
	suggestionItems.Add(suggestionItem);

	suggestionItem = new NameSuggestionItem();
	suggestionItem.Name = "Steven Buchanan";
	suggestionItem.Link = "mailto:steven.buchanan@northwindtraders.com";
	bitmapImage = new BitmapImage(new Uri(new DirectoryInfo(@"..\..\Assets\People_Circle18.png").FullName));
	suggestionItem.ImageSource = bitmapImage;
	suggestionItems.Add(suggestionItem);

	(suggestionProvider as NameSuggestionProvider).ItemsSource = suggestionItems;
	richTextboxadv.SuggestionSettings.SuggestionProviders.Add(suggestionProvider);
```

**Placeholders**
- `"Nancy Davolio"` / `"Andrew Fuller"` / `"Steven Buchanan"` → Replace with `{personName}`
- `"mailto:nancy.davolio@northwindtraders.com"` → Replace with `{emailLink}`
- `@"..\..\Assets\People_Circle0.png"` / `@"..\..\Assets\People_Circle5.png"` / `@"..\..\Assets\People_Circle18.png"` → Replace with `{imagePath}`
- `new BitmapImage(new Uri(new DirectoryInfo(...).FullName))` → Replace with `{imageSource}`

## Customize SuggestionBox ItemTemplate & Style
- By default, the drop-down window lists the filtered items as an image, display text and link. 

- If you want to remove the image or link. You can write your own item Template.

```xaml
<Window.Resources>
        <x:Array Type="{x:Type RichTextBoxAdv:NameSuggestionItem}" x:Key="suggestionItems">
            <RichTextBoxAdv:NameSuggestionItem Name = "Nancy Davolio" Link="mailto:nancy.davolio@northwindtraders.com"  />
            <RichTextBoxAdv:NameSuggestionItem Name = "Andrew Fuller" Link="mailto:andrew.fuller@northwindtraders.com" />
            <RichTextBoxAdv:NameSuggestionItem Name = "Steven Buchanan" Link="mailto:steven.buchanan@northwindtraders.com"/>
        </x:Array>
        <Style x:Key="SuggestionBoxStyle" TargetType="ListBox">
            <Setter Property="MinWidth" Value="300" />
            <Setter Property="MinHeight" Value="250" />
            <Setter Property="Background" Value="#FFDBF5FB"/>
            <Setter Property="ItemTemplate">
                <Setter.Value>
                    <DataTemplate DataType="local:NameSuggestionItem">
                        <StackPanel Orientation="Vertical" Height="50" VerticalAlignment="Center" Margin="12,15,0,0">
                            <TextBlock Text="{Binding Name}" FontFamily="microsoft sans serif" FontSize="14"  />
                            <TextBlock Text="{Binding Link}" FontFamily="microsoft sans serif" Foreground="Gray" FontSize="10" />
                        </StackPanel>
                    </DataTemplate>
                </Setter.Value>
            </Setter>
        </Style>
</Window.Resources>
    <Grid>
        <RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextboxadv" LayoutType="Continuous">
            <RichTextBoxAdv:SfRichTextBoxAdv.SuggestionSettings>
                <RichTextBoxAdv:SuggestionSettings>
                    <RichTextBoxAdv:SuggestionSettings.SuggestionProviders>
                        <RichTextBoxAdv:NameSuggestionProvider ItemsSource="{StaticResource suggestionItems}" 
                                                               SuggestionBoxStyle="{StaticResource SuggestionBoxStyle}">
                        </RichTextBoxAdv:NameSuggestionProvider>
                    </RichTextBoxAdv:SuggestionSettings.SuggestionProviders>
                </RichTextBoxAdv:SuggestionSettings>
            </RichTextBoxAdv:SfRichTextBoxAdv.SuggestionSettings>
        </RichTextBoxAdv:SfRichTextBoxAdv>
    </Grid>
```

**Placeholders**
- `"Nancy Davolio"` / `"Andrew Fuller"` / `"Steven Buchanan"` → Replace with `{personName}`
- `"mailto:nancy.davolio@northwindtraders.com"` → Replace with `{emailLink}`
- `MinWidth="300"` → Replace with `{suggestionBoxMinWidth}`
- `MinHeight="250"` → Replace with `{suggestionBoxMinHeight}`
- `Background="#FFDBF5FB"` → Replace with `{suggestionBoxBackground}`
- `FontFamily="microsoft sans serif"` → Replace with `{fontFamily}`
- `FontSize="14"` / `FontSize="10"` → Replace with `{fontSize}`
- `Foreground="Gray"` → Replace with `{foregroundColor}`
- `SuggestionBoxStyle="{StaticResource SuggestionBoxStyle}"` → Replace with `{suggestionBoxStyle}`

## Custom mention character
Set `MentionCharacter` on the provider to change the trigger (example uses `#`):

### XAML
```xaml
<Grid>
    <RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextboxadv" LayoutType="Continuous">
        <RichTextBoxAdv:SfRichTextBoxAdv.SuggestionSettings>
            <RichTextBoxAdv:SuggestionSettings>
                <RichTextBoxAdv:SuggestionSettings.SuggestionProviders>
                    <RichTextBoxAdv:NameSuggestionProvider MentionCharacter="#" 
							   ItemsSource="{StaticResource suggestionItems}">
                    </RichTextBoxAdv:NameSuggestionProvider>
                </RichTextBoxAdv:SuggestionSettings.SuggestionProviders>
			</RichTextBoxAdv:SuggestionSettings>
		</RichTextBoxAdv:SfRichTextBoxAdv.SuggestionSettings>
	</RichTextBoxAdv:SfRichTextBoxAdv>
</Grid>
```

**Placeholders**
- `MentionCharacter="#"` → Replace with `{mentionCharacter}`

### C#
```csharp
ISuggestionProvider suggestionProvider = new NameSuggestionProvider();
suggestionProvider.MentionCharacter = '#';
richTextboxadv.SuggestionSettings.SuggestionProviders.Add(suggestionProvider);
```

**Placeholders**
- `'#'` → Replace with `{mentionCharacter}`

## Multiple suggestion providers
You can register multiple providers (each with its own `MentionCharacter`, `ItemsSource`, and `SuggestionBoxStyle`):

### XAML
```xaml
<Window.Resources>
	<Style x:Key="SuggestionBoxStyle" TargetType="ListBox">
		<Setter Property="MinWidth" Value="300" />
		<Setter Property="MinHeight" Value="250" />
		<Setter Property="ItemTemplate">
			<Setter.Value>
				<DataTemplate DataType="local:NameSuggestionItem">
					<StackPanel Orientation="Vertical" Height="50" Width="200" VerticalAlignment="Center" Margin="12,15,0,0">
						<TextBlock Text="{Binding Name}" FontFamily="microsoft sans serif" FontSize="14"  />
						<TextBlock Text="{Binding Link}" FontFamily="microsoft sans serif" Foreground="Gray" FontSize="10" />
					</StackPanel>
				</DataTemplate>
			</Setter.Value>
		</Setter>
	</Style>
        
	<x:Array Type="{x:Type RichTextBoxAdv:NameSuggestionItem}" x:Key="suggestionItems">
		<RichTextBoxAdv:NameSuggestionItem Name = "Nancy Davolio" Link="mailto:nancy.davolio@northwindtraders.com" ImageSource="/Assets/People_Circle0.png" />
		<RichTextBoxAdv:NameSuggestionItem Name = "Andrew Fuller" Link="mailto:andrew.fuller@northwindtraders.com" ImageSource="/Assets/People_Circle5.png"/>
		<RichTextBoxAdv:NameSuggestionItem Name = "Steven Buchanan" Link="mailto:steven.buchanan@northwindtraders.com" ImageSource="/Assets/People_Circle18.png"/>
	</x:Array>

	<x:Array Type="{x:Type RichTextBoxAdv:NameSuggestionItem}" x:Key="suggestionItems01">
		<RichTextBoxAdv:NameSuggestionItem Name = "Desktop App" Link="10 queries"  />
		<RichTextBoxAdv:NameSuggestionItem Name = "Mobile App" Link="13 queries" />
		<RichTextBoxAdv:NameSuggestionItem Name = "Web App" Link="15 queries"/>
	</x:Array>
</Window.Resources>
<Grid>
	<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextboxadv" LayoutType="Continuous">
		<RichTextBoxAdv:SfRichTextBoxAdv.SuggestionSettings>
			<RichTextBoxAdv:SuggestionSettings>
				<RichTextBoxAdv:SuggestionSettings.SuggestionProviders>
					<RichTextBoxAdv:NameSuggestionProvider 
							   ItemsSource="{StaticResource suggestionItems}">
					</RichTextBoxAdv:NameSuggestionProvider>
					<RichTextBoxAdv:NameSuggestionProvider MentionCharacter="#" 
								   ItemsSource="{StaticResource suggestionItems01}"
								   SuggestionBoxStyle="{StaticResource SuggestionBoxStyle}">
					</RichTextBoxAdv:NameSuggestionProvider>
				</RichTextBoxAdv:SuggestionSettings.SuggestionProviders>
			</RichTextBoxAdv:SuggestionSettings>
		</RichTextBoxAdv:SfRichTextBoxAdv.SuggestionSettings>
	</RichTextBoxAdv:SfRichTextBoxAdv>
</Grid>
```

**Placeholders**
- `"Nancy Davolio"` / `"Andrew Fuller"` / `"Steven Buchanan"` → Replace with `{personName}`
- `"Desktop App"` / `"Mobile App"` / `"Web App"` → Replace with `{itemName}`
- `"mailto:nancy.davolio@northwindtraders.com"` → Replace with `{emailLink}`
- `"10 queries"` / `"13 queries"` / `"15 queries"` → Replace with `{itemDescription}`
- `"/Assets/People_Circle0.png"` / `"/Assets/People_Circle5.png"` / `"/Assets/People_Circle18.png"` → Replace with `{imageSource}`
- `MinWidth="300"` → Replace with `{suggestionBoxMinWidth}`
- `MinHeight="250"` → Replace with `{suggestionBoxMinHeight}`
- `FontFamily="microsoft sans serif"` → Replace with `{fontFamily}`
- `FontSize="14"` / `FontSize="10"` → Replace with `{fontSize}`
- `Foreground="Gray"` → Replace with `{foregroundColor}`
- `MentionCharacter="#"` → Replace with `{mentionCharacter}`

### C#
```csharp
ISuggestionProvider suggestionProvider = new NameSuggestionProvider();
List<NameSuggestionItem> suggestionItems = new List<NameSuggestionItem>();

NameSuggestionItem suggestionItem1 = new NameSuggestionItem();
suggestionItem1.Name = "Nancy Davolio";
suggestionItem1.Link = "mailto:nancy.davolio@northwindtraders.com";
BitmapImage bitmapImage = new BitmapImage(new Uri(new DirectoryInfo(@"..\..\Assets\People_Circle0.png").FullName));
suggestionItem1.ImageSource = bitmapImage;
suggestionItems.Add(suggestionItem1);

NameSuggestionItem suggestionItem2 = new NameSuggestionItem();
suggestionItem2.Name = "Andrew Fuller";
suggestionItem2.Link = "mailto:andrew.fuller@northwindtraders.com";
bitmapImage = new BitmapImage(new Uri(new DirectoryInfo(@"..\..\Assets\People_Circle5.png").FullName));
suggestionItem2.ImageSource = bitmapImage;
suggestionItems.Add(suggestionItem2);

NameSuggestionItem suggestionItem3 = new NameSuggestionItem();
suggestionItem3.Name = "Steven Buchanan";
suggestionItem3.Link = "mailto:steven.buchanan@northwindtraders.com";
bitmapImage = new BitmapImage(new Uri(new DirectoryInfo(@"..\..\Assets\People_Circle18.png").FullName));
suggestionItem3.ImageSource = bitmapImage;
suggestionItems.Add(suggestionItem3);

(suggestionProvider as NameSuggestionProvider).ItemsSource = suggestionItems;
richTextboxadv.SuggestionSettings.SuggestionProviders.Add(suggestionProvider);

ISuggestionProvider suggestionProviderAppType = new NameSuggestionProvider();
suggestionProviderAppType.SuggestionBoxStyle = this.Resources["SuggestionBoxStyle"] as System.Windows.Style;
suggestionProviderAppType.MentionCharacter = '#';
List<NameSuggestionItem> appTypes = new List<NameSuggestionItem>();

NameSuggestionItem desktopApp = new NameSuggestionItem();
desktopApp.Name = "Desktop App";
desktopApp.Link = "10 queries";
desktopApp.ImageSource = bitmapImage;
appTypes.Add(desktopApp);

NameSuggestionItem mobileApp = new NameSuggestionItem();
mobileApp.Name = "Mobile App";
mobileApp.Link = "13 queries";
mobileApp.ImageSource = bitmapImage;
appTypes.Add(mobileApp);

NameSuggestionItem webApp = new NameSuggestionItem();
webApp.Name = "Web App";
webApp.Link = "15 queries";
webApp.ImageSource = bitmapImage;
appTypes.Add(webApp);

(suggestionProviderAppType as NameSuggestionProvider).ItemsSource = appTypes;
richTextboxadv.SuggestionSettings.SuggestionProviders.Add(suggestionProviderAppType);
```

**Placeholders**
- `"Nancy Davolio"` / `"Andrew Fuller"` / `"Steven Buchanan"` → Replace with `{personName}`
- `"Desktop App"` / `"Mobile App"` / `"Web App"` → Replace with `{itemName}`
- `"mailto:nancy.davolio@northwindtraders.com"` → Replace with `{emailLink}`
- `"10 queries"` / `"13 queries"` / `"15 queries"` → Replace with `{itemDescription}`
- `@"..\..\Assets\People_Circle0.png"` / `@"..\..\Assets\People_Circle5.png"` / `@"..\..\Assets\People_Circle18.png"` → Replace with `{imagePath}`
- `bitmapImage` → Replace with `{imageSource}`
- `'#'` → Replace with `{mentionCharacter}`

## SuggestionBox empty message

- When no suggestions are found the control displays a message (default: “We couldn’t find the person you were looking for.”). 

## SuggestionBox empty message localization

You can override this string via the resource key `SuggestionBoxErrorMessage` in the `Syncfusion.SfRichTextBoxAdv.WPF.resx` satellite resource for your app.

Steps:
- Add a `Resources` folder to your project.

- Add the default `Syncfusion.SfRichTextBoxAdv.WPF.resx` into `Resources`.

- Change the value for `SuggestionBoxErrorMessage` in the culture-specific `.resx`.

## Custom suggestion provider

- By default, we have implemented NameSuggestionProvider as suggestion provider. And you can implement your own suggestion provider, inheriting from ISuggestionProvider. 

- Which helps you to customize the search and insert selected item functionalities.

The following sample code demonstrates how to create your own suggestion provider inherited from ISuggestionProvider.

```csharp
internal class AppTypeSuggestionProvider : DependencyObject, ISuggestionProvider
{
#region Property
public char MentionCharacter
{
	get
	{
		return (char)GetValue(MentionCharacterProperty);
	}
	set
	{
		SetValue(MentionCharacterProperty, value);
	}
}

public Style SuggestionBoxStyle
{
	get
	{
		return (Style)GetValue(SuggestionBoxStyleProperty);
	}
	set
	{
		SetValue(SuggestionBoxStyleProperty, value);
	}
}

public IEnumerable ItemsSource
{
	get
	{
		return (IEnumerable)GetValue(ItemsSourceProperty);
	}
	set
	{
		SetValue(ItemsSourceProperty, value);
	}
}

public static DependencyProperty MentionCharacterProperty
{
	get
	{
		return mentionCharacterProperty;
	}
}

public static DependencyProperty ItemsSourceProperty
{
	get
	{
		return itemsSourceProperty;
	}
}

public static DependencyProperty SuggestionBoxStyleProperty
{
	get
	{
		return suggestionBoxStyleProperty;
	}
}
#endregion

#region Static Dependency Properties
/// <summary>
/// Identifies the MentionCharacter dependency property.
/// </summary>
private static DependencyProperty mentionCharacterProperty = DependencyProperty.Register("MentionCharacter", typeof(char), typeof(NameSuggestionProvider), new PropertyMetadata('@'));

/// <summary>
/// Identifies the ItemSource dependency property.
/// </summary>
private static DependencyProperty itemsSourceProperty = DependencyProperty.Register("ItemsSource", typeof(IEnumerable), typeof(NameSuggestionProvider), new PropertyMetadata(null));

/// <summary>
/// Identifies the SuggestionBoxStyle dependency property.
/// </summary>
private static DependencyProperty suggestionBoxStyleProperty = DependencyProperty.Register("SuggestionBoxStyle", typeof(Style), typeof(NameSuggestionProvider), new PropertyMetadata(null));
#endregion

public void Dispose()
{
	ClearValue(mentionCharacterProperty);
	if (ItemsSource != null)
	{
		foreach (NameSuggestionItem itemSource in ItemsSource)
		{
			itemSource.Dispose();
		}
		ClearValue(itemsSourceProperty);
	}
	ClearValue(suggestionBoxStyleProperty);
}

public void InsertSelectedItem(SfRichTextBoxAdv richTextBoxAdv, object selectedItem)
{
	NameSuggestionItem nameSuggestionItem = selectedItem as NameSuggestionItem;
	richTextBoxAdv.Selection.InsertText(MentionCharacter + nameSuggestionItem.Name);
}

public List<object> Search(string searchText)
{
	List<object> matchedItems = new List<object>();
	foreach (NameSuggestionItem item in ItemsSource)
	{
		if (item.Name.ToUpperInvariant().StartsWith(searchText.ToUpperInvariant()))
		{
			matchedItems.Add(item);
		}
	}
	return matchedItems;
}
}
```
### Sample

[Sample custom provider example]:
(https://github.com/SyncfusionExamples/WPF-RichTextBox-Examples/tree/main/Samples/Automatic%20Suggestion/Custom%20Suggestion%20Provider)

## Customize search behavior
- In default searching, it list the items which contains the typed text. 

- You can modify the searching logic like list the items starts or ends with typed text, by implementing your own suggestion provider and overriding the Search method.

The following sample code demonstrates how to override search operation in your suggestion provider.

```csharp
public List<object> Search(string searchText)
{
	List<object> matchedItems = new List<object>();
	foreach (NameSuggestionItem item in ItemsSource)
	{
		if (item.Name.ToUpperInvariant().StartsWith(searchText.ToUpperInvariant()))
		{
			matchedItems.Add(item);
		}
	}
	return matchedItems;
}
```

## Customize insert behavior
- By default, the selected item from the suggestions list is inserted as hyperlink. 

- you can insert it as plain text or without link, by implementing your own suggestion provider and overriding the “InsertSelectedItem” method.

The following sample code demonstrates how to override insert selected item operation in your suggestion provider.

```csharp
public void InsertSelectedItem(SfRichTextBoxAdv richTextBoxAdv, object selectedItem)
{
	NameSuggestionItem nameSuggestionItem = selectedItem as NameSuggestionItem;
	richTextBoxAdv.Selection.InsertText(MentionCharacter + nameSuggestionItem.Name);
}
```

## Version note
This feature is supported starting from `V18.4.0.30`.