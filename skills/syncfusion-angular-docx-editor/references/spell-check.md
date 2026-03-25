# Spell Check Configuration

Implement spell checking in the Document Editor with multi-language support, custom dictionaries, contextual suggestions, and user-friendly correction options.

## Enable Spell Check

Activate spell checking on the DocumentEditorContainer component.

```typescript
<ejs-documenteditorcontainer 
  #document_editor 
  serviceUrl="https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/"
  [enableSpellCheck]="true" 
  [enableToolbar]="true" 
  (created)="onCreated()">
</ejs-documenteditorcontainer>
```

**Note:** Set `enableSpellCheck` property to `true`. Configure spell checker settings in the `created` event after the component initializes.

## Configure Spell Checker Settings

Customize spell checker behavior after component initialization through the `spellChecker` object.

### Language ID

Specify the language for spell checking using a language locale ID (LCID). Common values: `1033` (en-US), `1036` (fr-FR), `1031` (de-DE).

```typescript
this.container.documentEditor.spellChecker.languageID = 1033;
```

**Placeholders**
- `1033` → Replace with `{languageID}`

### Remove Underline

Hide the red squiggly underline that indicates misspelled words.

```typescript
this.container.documentEditor.spellChecker.removeUnderline = false;
```

**Placeholders**
- `false` → Replace with `{hideUnderline}`

### Allow Spell Check and Suggestion

Enable or disable correction suggestions for misspelled words.

```typescript
this.container.documentEditor.spellChecker.allowSpellCheckAndSuggestion = true;
```

**Note:** Default behavior provides both spell check and suggestions. Set to `false` to perform spell check only without suggestions.

### Enable Optimized Spell Check

Check only visible or modified pages incrementally instead of the entire document. This reduces server API calls and improves performance for large documents.

```typescript
this.container.documentEditor.spellChecker.enableOptimizedSpellCheck = true;
```


### Optimize Dictionary Performance

Pre-load dictionaries at application startup to eliminate runtime parsing overhead and support multiple languages in memory.

```csharp
List<DictionaryData> spellDictCollection = new List<DictionaryData>();
string personalDictPath = string.Empty;
int cacheCount = 2; // Hold 2 language dictionaries in memory

SpellChecker.InitializeDictionaries(spellDictCollection, personalDictPath, cacheCount);
```

**Placeholders**
- `2` → Replace with `{maxDictionariesToCache}`

**Note:** After initialization, use default `SpellChecker` constructor to leverage pre-loaded dictionaries and avoid reinitialization.

### Add Custom Words to Dictionary

Extend the dictionary by adding custom root words and their variations. This prevents domain-specific terms from being flagged as errors.

```csharp
SpellChecker spellChecker = new SpellChecker();
spellChecker.AddNewWord("en.dic", "en.aff", "construct",
    new string[] { "constructs", "reconstruct", "constructed", "constructive" });
```

**Placeholders**
- `"en.dic"` → Replace with `{dictionaryFile}`
- `"en.aff"` → Replace with `{affixFile}`
- `"construct"` → Replace with `{rootWord}`
- `["constructs", "reconstruct", ...]` → Replace with `{wordVariations}`

**Note:** Rules are generated automatically from the affix file. Custom words persist in the personal dictionary across sessions.


## Complete Setup Example

```typescript
import { Component, ViewChild, ViewEncapsulation } from '@angular/core';
import { ToolbarService, DocumentEditorContainerComponent } from '@syncfusion/ej2-angular-documenteditor';

@Component({
  selector: 'app-container',
  template: `<ejs-documenteditorcontainer 
    #document_editor 
    [enableSpellCheck]="true" 
    [enableToolbar]="true" 
    (created)="onCreated()">
  </ejs-documenteditorcontainer>`,
  encapsulation: ViewEncapsulation.None,
  providers: [ToolbarService]
})
export class AppComponent {
  @ViewChild('document_editor')
  public container?: DocumentEditorContainerComponent;

  public onCreated(): void {
    if (this.container) {
      this.container.documentEditor.spellChecker.languageID = 1033;
      this.container.documentEditor.spellChecker.removeUnderline = false;
      this.container.documentEditor.spellChecker.allowSpellCheckAndSuggestion = true;
    }
  }
}
```

## Context Menu Features

Right-click any misspelled word to access:
- **Suggestions** – Replace with a recommended spelling correction
- **Add to Dictionary** – Add the word permanently to prevent future errors
- **Ignore Once** – Skip this spelling error instance only
- **Ignore All** – Skip all instances of this word in the document
- **Spelling** – Open spell check dialog for comprehensive review

## Server-Side Configuration

### Setup ASP.NET Core Web API

**Step 1: Create a New ASP.NET Core Web API Project**

```bash
dotnet new webapi -n SpellCheckServer
cd SpellCheckServer
```

**Step 2: Install Required NuGet Packages**

```bash
dotnet add package Syncfusion.EJ2.WordEditor.AspNet.Core
dotnet add package Syncfusion.EJ2.SpellChecker.AspNet.Core
dotnet add package Newtonsoft.Json
```

**Step 3: Configure Dictionary Files**

1. Create a `Data` folder in project root
2. Download Hunspell dictionaries from [wooorm/dictionaries](https://github.com/wooorm/dictionaries):
   - `.dic` file (dictionary)
   - `.aff` file (affix/rules)
   - `customDict.dic` file (personal dictionary)

3. Create `Data/spellcheck.json`:

```json
[
  {
    "LanguadeID": 1033,
    "DictionaryPath": "index.dic",
    "AffixPath": "index.aff",
    "PersonalDictPath": "customDict.dic"
  }
]
```

4. Update `.csproj` to copy dictionary files to output:

```xml
<ItemGroup>
  <None Update="Data\**\*">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </None>
</ItemGroup>
```

**Step 4: Create DocumentEditorController**

Create `Controllers/DocumentEditorController.cs`:

```csharp
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using Syncfusion.EJ2.SpellChecker;

namespace SpellCheckServer.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class DocumentEditorController : ControllerBase
    {
        [HttpPost]
        [Route("SpellCheck")]
        [EnableCors("AllowAllOrigins")]
        public string SpellCheck([FromBody] SpellCheckJsonData spellChecker)
        {
            try
            {
                SpellChecker spellCheck = new SpellChecker();
                spellCheck.GetSuggestions(
                    spellChecker.LanguageID,
                    spellChecker.TexttoCheck,
                    spellChecker.CheckSpelling,
                    spellChecker.CheckSuggestion,
                    spellChecker.AddWord
                );
                return JsonConvert.SerializeObject(spellCheck);
            }
            catch
            {
                return "{\"SpellCollection\":[],\"HasSpellingError\":false,\"Suggestions\":null}";
            }
        }

        [HttpPost]
        [Route("SpellCheckByPage")]
        [EnableCors("AllowAllOrigins")]
        public string SpellCheckByPage([FromBody] SpellCheckJsonData spellChecker)
        {
            try
            {
                SpellChecker spellCheck = new SpellChecker();
                spellCheck.CheckSpelling(spellChecker.LanguageID, spellChecker.TexttoCheck);
                return JsonConvert.SerializeObject(spellCheck);
            }
            catch
            {
                return "{\"SpellCollection\":[],\"HasSpellingError\":false,\"Suggestions\":null}";
            }
        }

        public class SpellCheckJsonData
        {
            public int LanguageID { get; set; }
            public string TexttoCheck { get; set; }
            public bool CheckSpelling { get; set; }
            public bool CheckSuggestion { get; set; }
            public bool AddWord { get; set; }
        }
    }
}
```

**Step 5: Configure Program.cs**

```csharp
using Newtonsoft.Json;
using Syncfusion.EJ2.SpellChecker;

var builder = WebApplication.CreateBuilder(args);
var env = builder.Environment;

// Add services
builder.Services.AddControllers().AddNewtonsoftJson();
builder.Services.AddMemoryCache();
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAllOrigins", policy =>
    {
        policy.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader();
    });
});
builder.Services.AddResponseCompression();

var app = builder.Build();

// Initialize spell checker dictionaries
string dictionaryPath = Path.Combine(env.ContentRootPath, "Data");
string jsonFileName = Path.Combine(dictionaryPath, "spellcheck.json");

if (File.Exists(jsonFileName))
{
    string jsonContent = File.ReadAllText(jsonFileName);
    List<DictionaryData> dictionaries = JsonConvert.DeserializeObject<List<DictionaryData>>(jsonContent);
    List<DictionaryData> spellDictCollection = new();

    foreach (var dict in dictionaries)
    {
        spellDictCollection.Add(new DictionaryData(
            dict.LanguadeID,
            Path.Combine(dictionaryPath, dict.DictionaryPath),
            Path.Combine(dictionaryPath, dict.AffixPath)
        ));
    }

    string personalDictPath = Path.Combine(dictionaryPath, "customDict.dic");
    int cacheCount = 2;
    SpellChecker.InitializeDictionaries(spellDictCollection, personalDictPath, cacheCount);
}

app.UseCors("AllowAllOrigins");
app.UseResponseCompression();
app.MapControllers();

app.Run();
```

**Step 6: Build and Run**

```bash
dotnet build
dotnet run
```

**Note:** Default address is `http://localhost:5000`. Update your Angular client's service URL to match.
