# Spell Checker

Implement spell checking in the Document Editor with multi-language support, custom dictionaries, contextual suggestions, and user-friendly correction options.

## Enable Spell Check

To activate spell checking, set `enableSpellCheck: true` on the DocumentEditorContainer and inject the `SpellChecker` module:

```ts
import { DocumentEditorContainer, Toolbar, SpellChecker } from '@syncfusion/ej2-documenteditor';

DocumentEditorContainer.Inject(Toolbar);

let container: DocumentEditorContainer = new DocumentEditorContainer({
    enableToolbar: true,
    enableSpellCheck: true,
    height: '590px'
});

container.appendTo('#container');

// Accessing spell checker instance
let spellChecker: SpellChecker = container.documentEditor.spellChecker;

// Set language ID to map dictionary on server side
spellChecker.languageID = 1033; // en-US

// Allow suggestions for misspelled words
spellChecker.allowSpellCheckAndSuggestion = true;
```

## Disable Spell Check

Spell check is disabled by default. To disable it explicitly, set `enableSpellCheck: false` or omit the property entirely.

```ts
let container: DocumentEditorContainer = new DocumentEditorContainer({
    enableToolbar: true,
    enableSpellCheck: false
});
```

## Configure Spell Checker Settings

Customize spell checker behavior after component initialization through the `documentEditor.spellChecker` object:

### Language ID

Specify the language for spell checking using a language locale ID (LCID). Common values: `1033` (en-US), `1036` (fr-FR), `1031` (de-DE):

```ts
documentEditor.spellChecker.languageID = 1033; // en-US
```

### Remove Underline

Hide the red squiggly underline that indicates misspelled words:

```ts
documentEditor.spellChecker.removeUnderline = true;
```

### Allow Spell Check and Suggestion

Enable or disable correction suggestions for misspelled words:

```ts
// With suggestions (recommended)
documentEditor.spellChecker.allowSpellCheckAndSuggestion = true;

// Without suggestions (error detection only)
documentEditor.spellChecker.allowSpellCheckAndSuggestion = false;
```

### Enable Optimized Spell Check

Check only visible/modified pages incrementally instead of the entire document. This reduces server API calls and improves performance, especially for large documents:

```ts
documentEditor.spellChecker.enableOptimizedSpellCheck = true;
```


## Optimize Dictionary Performance

Pre-load dictionaries at application startup to eliminate runtime parsing overhead. Set a cache limit to hold multiple language dictionaries in memory:

```csharp
List<DictionaryData> spellDictCollection = new List<DictionaryData>();
string personalDictPath = string.Empty;
int cacheCount = 2; // Keep 2 language dictionaries in memory

SpellChecker.InitializeDictionaries(spellDictCollection, personalDictPath, cacheCount);
```

After initialization, instantiate `SpellChecker` without parameters to use pre-loaded dictionaries:

```csharp
[HttpPost]
public string SpellCheck([FromBody] SpellCheckJsonData spellCheckData)
{
  try
  {
    SpellChecker spellCheck = new SpellChecker(); // Uses pre-initialized dictionaries
    spellCheck.GetSuggestions(
      spellCheckData.LanguageID,
      spellCheckData.TexttoCheck,
      spellCheckData.CheckSpelling,
      spellCheckData.CheckSuggestion,
      spellCheckData.AddWord
    );
    return JsonConvert.SerializeObject(spellCheck);
  }
  catch
  {
    return "{\"SpellCollection\":[],\"HasSpellingError\":false,\"Suggestions\":null}";
  }
}
```

## Add Custom Words to Dictionary

Extend the dictionary by adding custom root words and their variations. This is a server-side operation that allows you to prevent domain-specific terms from being flagged as spelling errors:

```csharp
SpellChecker spellChecker = new SpellChecker();
spellChecker.AddNewWord("en.dic", "en.aff", "construct", 
    new string[] { "constructs", "reconstruct", "constructed", "constructive" });
```

**Note:** Custom words are added to the personal dictionary and persist across spell check sessions.

## Context Menu Features

Right-click any misspelled word to access these quick-action options:

- **Suggestions** – Replace with a recommended spelling correction from the suggestions list
- **Add to Dictionary** – Add the word permanently to the user's dictionary to bypass future checks
- **Ignore Once** – Skip this spelling error instance without modifying the dictionary
- **Ignore All** – Skip all instances of this word throughout the entire document in the current session
- **Spelling** – Open the spell check dialog for comprehensive manual review and correction of all errors

## Placeholders

`1033` → Replace with `{languageID}` (LCID: 1033 = en-US, 1036 = fr-FR, etc.)

`en.dic` → Replace with `{dictionaryFileName}`

`en.aff` → Replace with `{affixFileName}`

`construct` → Replace with `{rootWord}`

`["constructs", "reconstruct", "constructed", "constructive"]` → Replace with `{possibleWordArray}`

---

## Server Layer (ASP.NET Core Web API)

**Architecture Overview:**
- Hosts Syncfusion SpellChecker with [Hunspell](https://github.com/wooorm/dictionaries) dictionaries (.aff/.dic files)
- Supports optional personal dictionaries for domain-specific terminology
- Pre-caches multiple language dictionaries at startup to reduce latency

**Key Features:**
- **Multi-Language:** Uses `languageID` (LCID) to select the appropriate dictionary automatically
- **Error Detection:** Analyzes text to identify misspelled words using Hunspell algorithms
- **Suggestions:** Generates ranked correction suggestions based on edit distance
- **Performance:** Page-by-page checking via `enableOptimizedSpellCheck` reduces server requests
- **Caching:** Pre-loaded dictionaries and reused suggestions minimize response time

### Spell Check Server-Side Setup

**Step 1: Create a New ASP.NET Core Web API Project**

Initialize a new ASP.NET Core Web API project using one of these methods:
- Visual Studio (File → New → Project → ASP.NET Core Web API)
- Visual Studio Code with .NET extension
- Command line: `dotnet new webapi -n SpellCheckServer`   

**Step 2: Install Required NuGet Packages** 

Add these NuGet packages to enable spell checking capabilities: 

- [Syncfusion.EJ2.WordEditor.AspNet.Core](https://www.nuget.org/packages/Syncfusion.EJ2.WordEditor.AspNet.Core/) – Word document processing
- [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json) – JSON parsing/Serilaizing
- [Syncfusion.EJ2.SpellChecker.AspNet.Core](https://www.nuget.org/packages/Syncfusion.EJ2.SpellChecker.AspNet.Core/) – Spell checking engine
 

**Step 3: Configure Dictionary Files**

Set up language dictionaries for spell checking:

1. **Create a Data folder** in your project root
2. **Download Hunspell dictionaries** from [wooorm/dictionaries](https://github.com/wooorm/dictionaries):
   - **.dic** – Valid words dictionary
   - **.aff** – Affix rules for word derivations
   - **customDict.dic** – (Optional) Personal dictionary for domain-specific terms
   
   Example: Download `en/index.dic` and `en/index.aff` for English spell checking.

3. **Create spellcheck.json** configuration file in the Data folder:

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

**Important:** Dictionary files must be copied to the output directory during build.

By default, .NET does **not** copy `.dic` and `.aff` files to the `bin` output directory during the build process. This causes the application to fail at runtime when attempting to locate these files.

To resolve this, add the following configuration to your project file (`.csproj`):

```xml
<ItemGroup>
  <None Update="Data\**\*">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </None>
</ItemGroup>
```

This ensures all files in the `Data` folder are copied to the output directory and remain up-to-date when the source files change.

**Step 4: Add Spell Check Controller** 

Create a controller file named **DocumentEditorController.cs** in the Controllers folder:

1. Apply the route attribute `[Route("api/[controller]")]` to the class (automatically maps to `api/documenteditor`)
2. Implement the `SpellCheck` and `SpellCheckByPage` endpoints below
3. Avoid adding unnecessary code

The spell checker implementation is provided in `Syncfusion.EJ2.SpellChecker`. Import the required namespace before implementing the endpoints:

```csharp
using Newtonsoft.Json;
using Syncfusion.EJ2.SpellChecker;

        [AcceptVerbs("Post")]  
        [HttpPost]  
        [EnableCors("AllowAllOrigins")]  
        [Route("SpellCheck")]  
        public string SpellCheck([FromBody] SpellCheckJsonData spellChecker) 
        {  
            try  
            {  
                SpellChecker spellCheck = new SpellChecker();  
                spellCheck.GetSuggestions(spellChecker.LanguageID, spellChecker.TexttoCheck, spellChecker.CheckSpelling, spellChecker.CheckSuggestion, spellChecker.AddWord);  
                return Newtonsoft.Json.JsonConvert.SerializeObject(spellCheck);  
            }  
            catch  
            {  
                return "{\"SpellCollection\":[],\"HasSpellingError\":false,\"Suggestions\":null}";  
            }  
        }

        [AcceptVerbs("Post")]  
        [HttpPost]  
        [EnableCors("AllowAllOrigins")]  
        [Route("SpellCheckByPage")]  
        public string SpellCheckByPage([FromBody] SpellCheckJsonData spellChecker)  
        {  
            try  
            {  
                SpellChecker spellCheck = new SpellChecker();  
                spellCheck.CheckSpelling(spellChecker.LanguageID, spellChecker.TexttoCheck);
                return Newtonsoft.Json.JsonConvert.SerializeObject(spellCheck);  
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

```

**Step 5: Configure the Spell Check Service** 

Update **Program.cs** to initialize dictionaries at application startup.

```csharp
using Syncfusion.EJ2.SpellChecker;
using Newtonsoft.Json;

var builder = WebApplication.CreateBuilder(args);
var env = builder.Environment;

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddControllers();
builder.Services.AddMemoryCache();


builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAllOrigins", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});



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

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();


app.UseRouting();                  

app.UseCors("AllowAllOrigins");    

app.UseAuthorization();            

app.MapControllers();   


app.MapRazorPages();

app.Run();
```

**Step 6: Build and Run the Web API** 

Build and run the server locally to test spell check functionality:

```bash
dotnet build
dotnet run
```

The Web API will be available at `http://localhost:5000/api/documenteditor/` (or another configured port). 

**Important**: Update your JavaScript client's `serviceUrl` to match your server's base URL (e.g., `http://localhost:5000/api/documenteditor/` if running locally, or your production URL for deployment).
