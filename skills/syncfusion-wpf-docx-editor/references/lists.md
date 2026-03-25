# Lists in WPF DOCX Editor

List formatting support in the Syncfusion WPF DOCX Editor allows creating and managing bulleted and numbered lists within documents.


---

## Apply Bullet

```csharp
// Initializes a new abstract list instance.
AbstractListAdv abstractListAdv = new AbstractListAdv(null);
abstractListAdv.AbstractListId = 1;

// Defines new ListLevel instance.
ListLevelAdv listLevel = new ListLevelAdv(abstractListAdv);
listLevel.ParagraphFormat.LeftIndent = 24d;
listLevel.FollowCharacter = FollowCharacterType.Tab;
listLevel.ListLevelPattern = ListLevelPattern.Bullet;
listLevel.ParagraphFormat.AfterSpacing = 8d;
listLevel.NumberFormat = "\uf0b7";
listLevel.CharacterFormat.FontFamily = new FontFamily("Symbol");

// Adds list level to abstract list.
abstractListAdv.Levels.Add(listLevel);

// Adds abstract list to the document.
richTextBoxAdv.Document.AbstractLists.Add(abstractListAdv);

// Creates a new list instance.
ListAdv listAdv = new ListAdv(null);
listAdv.ListId = 1;
listAdv.AbstractListId = 1;

// Adds list to the document.
richTextBoxAdv.Document.Lists.Add(listAdv);

// Add list item 1
ParagraphAdv paragraphAdv = new ParagraphAdv();
SpanAdv spanAdv = new SpanAdv() { Text = "List Item 1" };
paragraphAdv.Inlines.Add(spanAdv);
richTextBoxAdv.Document.Sections[0].Blocks.Add(paragraphAdv);

paragraphAdv.ParagraphFormat.ListFormat.ListId = 1;
paragraphAdv.ParagraphFormat.ListFormat.ListLevelNumber = 0;
```

**Placeholders**
- `1` (AbstractListId) → Replace with `{abstractListId}`
- `1` (ListId) → Replace with `{listId}`
- `"\uf0b7"` → Replace with `{bulletCharacter}`

---

## Define various bullet type list

- Bulleted list by setting list level pattern as Bullet. You can define various bullets by defining the bullet character. 

- The following code sample demonstrates how to define dot, square and arrow bullet.

### C#
```csharp
// Defines Bulleted List.
listLevel.ListLevelPattern = ListLevelPattern.Bullet;

// Defining Dot Bullet
listLevel.NumberFormat = "\uf0b7";
listLevel.CharacterFormat.FontFamily = new FontFamily("Symbol");

// Defines Square bullet.
listLevel.NumberFormat = "\uf0a7";
listLevel.CharacterFormat.FontFamily = new FontFamily("Wingdings");

// Defines Arrow Bullet.
listLevel.NumberFormat = "\u27a4";
listLevel.CharacterFormat.FontFamily = new FontFamily("Symbol");
```

**Placeholders**
- `ListLevelPattern.Bullet` → Replace with `{listLevelPattern}`
- `"\uf0b7"` / `"\uf0a7"` / `"\u27a4"` → Replace with `{numberFormat}`
- `"Symbol"` / `"Wingdings"` → Replace with `{fontFamily}`

---

## Apply Numbering

```csharp
// Initializes a new abstract list instance.
AbstractListAdv abstractListAdv = new AbstractListAdv(null);
abstractListAdv.AbstractListId = 1;

// Defines new ListLevel instance.
ListLevelAdv listLevel = new ListLevelAdv(abstractListAdv);
listLevel.ParagraphFormat.LeftIndent = 48d;
listLevel.ParagraphFormat.FirstLineIndent = 24d;
listLevel.FollowCharacter = FollowCharacterType.Tab;
listLevel.ListLevelPattern = ListLevelPattern.Number;
listLevel.NumberFormat = "%1.";
listLevel.RestartLevel = 0;
listLevel.StartAt = 1;

// Adds list level to abstract list.
abstractListAdv.Levels.Add(listLevel);

// Adds abstract list to the document.
richTextBoxAdv.Document.AbstractLists.Add(abstractListAdv);

// Creates a new list instance.
ListAdv listAdv = new ListAdv(null);
listAdv.ListId = 1;
// Sets the abstract list Id for this list.
listAdv.AbstractListId = 1;

// Adds list to the document.
richTextBoxAdv.Document.Lists.Add(listAdv);

// Add list item 1
ParagraphAdv paragraphAdv = new ParagraphAdv();
SpanAdv spanAdv = new SpanAdv() { Text = "List Item 1" };
paragraphAdv.Inlines.Add(spanAdv);
richTextBoxAdv.Document.Sections[0].Blocks.Add(paragraphAdv);

// Defines the list format for the paragraph.
paragraphAdv.ParagraphFormat.ListFormat.ListId = 1;
paragraphAdv.ParagraphFormat.ListFormat.ListLevelNumber = 0;
```

**Placeholders**
- `ListLevelPattern.Number` → Replace with `{listLevelPattern}`
- `"%1."` → Replace with `{numberFormat}`
- `1` (StartAt) → Replace with `{startAt}`
- `1` (ListId) → Replace with `{listId}`
---

## Numerical list - Number formats

```csharp
// Defines the number format for the list level.
/* Note
* The percent sign (%) followed by any number from 1 through 9 represents the number style from the respective list level. 
* For example, if you wanted the format for the first level to be "Article I." "Article II," and so on, the string for the NumberFormat property would be "Article %1." and the ListLevelPattern property would be set to ListLevelPattern.UpRoman.
*/
listLevel.NumberFormat = "Article %1.";
listLevel.ListLevelPattern = ListLevelPattern.UpRoman;
```

**Placeholders**
- `"Article %1."` → Replace with `{numberFormatPattern}`
- `ListLevelPattern.UpRoman` → Replace with `{numberStyle}`

---

## Editing List

- The list applied to the current selection can be retrieved and modified as required. 

- After updating the list properties, the modified list must be reassigned to the current selection for the changes to take effect.
### C#
```csharp
// Gets the current list for the selection content.
ListAdv listAdv = richTextBoxAdv.Selection.ParagraphFormat.GetList();

//Make changes to the ListAdv

// Applies list for the Selection content.
richTextBoxAdv.Selection.ParagraphFormat.SetList(listAdv);
```

---
