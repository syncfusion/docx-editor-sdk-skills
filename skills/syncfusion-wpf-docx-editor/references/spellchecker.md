# Spell Checker in WPF DOCX Editor

Spell checker support in the Syncfusion WPF DOCX Editor allows detecting and correcting spelling errors within documents.


---

## Available spell checking options

* Ignore words in UPPERCASE.

* Ignore words that contain numbers.

* Ignore URIs.


---

## Enable spell checking

## XAML
```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv">
	<RichTextBoxAdv:SfRichTextBoxAdv.SpellChecker>
		<RichTextBoxAdv:SpellChecker IsEnabled="True" IgnoreURIs="True" IgnoreAlphaNumericWords="True" IgnoreUppercaseWords="True"/>
	</RichTextBoxAdv:SfRichTextBoxAdv.SpellChecker>
</RichTextBoxAdv:SfRichTextBoxAdv>
```

## C#

```csharp
// Enable spell checking
richTextBoxAdv.SpellChecker.IsEnabled = true;

// Configure options
richTextBoxAdv.SpellChecker.IgnoreURIs = true;
richTextBoxAdv.SpellChecker.IgnoreAlphaNumericWords = true;
richTextBoxAdv.SpellChecker.IgnoreUppercaseWords = true;

// Disable
richTextBoxAdv.SpellChecker.IsEnabled = false;
```

---

## Adding custom dictionaries

- Register one or more custom dictionary files (plain `.dic` files).

- When at least one custom dictionary is defined, the Spelling Pane will allow adding misspelled words into the first custom dictionary.

### XAML

```xaml
<RichTextBoxAdv:SpellChecker IsEnabled="True" IgnoreURIs="True" IgnoreAlphaNumericWords="True" IgnoreUppercaseWords="True">
	<RichTextBoxAdv:SpellChecker.CustomDictionaries>
		<System:String>../../Assets/DefaultDictionary.dic</System:String>
		<System:String>../../Assets/CustomDictionary.dic</System:String>
	</RichTextBoxAdv:SpellChecker.CustomDictionaries>
</RichTextBoxAdv:SpellChecker>
```

**Placeholders**
- `../../Assets/DefaultDictionary.dic` → Replace with `{dictionaryPath}`
- `../../Assets/CustomDictionary.dic` → Replace with `{dictionaryPath}`

### Notes
- Misspelled words added via the UI are appended to the first custom dictionary in the collection.

- Provide valid paths to `.dic` files accessible at runtime.

---

## Multilingual spell check

Set the control `Language` to enable spell checking for that language (the platform language packs must be installed for the target language):

```xaml
<RichTextBoxAdv:SfRichTextBoxAdv x:Name="richTextBoxAdv" Language="fr">
	<RichTextBoxAdv:SfRichTextBoxAdv.SpellChecker>
		<RichTextBoxAdv:SpellChecker IsEnabled="True"/>
	</RichTextBoxAdv:SfRichTextBoxAdv.SpellChecker>
</RichTextBoxAdv:SfRichTextBoxAdv>
```

**Placeholders**
- `fr` → Replace with `{language}`

Note: language-specific .NET Framework language packs must be installed on the machine for correct dictionary support.

---

## Spelling pane (UI)

`SfRichTextBoxAdv` includes a built-in spelling pane for reviewing and correcting misspelled words. Show it with the `ShowSpellingPaneCommand`.

### XAML

```xaml
<Button Content="Show Spelling Pane" Command="RichTextBoxAdv:SfRichTextBoxAdv.ShowSpellingPaneCommand" CommandTarget="{Binding ElementName=richTextBoxAdv}" />

<syncfusion:SfRichTextBoxAdv x:Name="richTextBoxAdv" />
```

### C#

```csharp
SfRichTextBoxAdv.ShowSpellingPaneCommand.Execute(null, richTextBoxAdv);
```

---