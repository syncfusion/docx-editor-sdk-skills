# Spell Check

Configure and manage spell checking functionality with multi-language support, custom dictionaries, and context menu corrections.

## Enable Spell Check

Activate spell checking by setting `enableSpellCheck={true}` on the DocumentEditorComponent:

```ts
<template>
  <ejs-documenteditor 
    ref="documenteditor" 
    id="container" 
    height="370px"
    :enableSpellCheck="true">
  </ejs-documenteditor>
</template>

<script>
export default {
  mounted() {
    // Component is ready for spell check configuration
  }
}
</script>
```

## Set Language ID

Map spell checking to a specific language using the language locale ID (LCID):

```ts
// Common language IDs: 1033 = en-US, 1036 = fr-FR, 1031 = de-DE
this.$refs.documenteditor.ej2Instances.spellChecker.languageID = 1033;
```

**Placeholders**
- `1033` → Replace with `{languageID}` (LCID: 1033 = en-US, 1036 = fr-FR, 1031 = de-DE, etc.)

## Remove Underline

Hide the red squiggly underline under misspelled words:

```ts
this.$refs.documenteditor.ej2Instances.spellChecker.removeUnderline = false;
```

> **Note:** Set to `true` to hide underlines; set to `false` (default) to show them.

## Enable Spell Check and Suggestions

Toggle whether to provide correction suggestions alongside spell checking:

```ts
// Enable both spell check and suggestions (recommended)
this.$refs.documenteditor.ej2Instances.spellChecker.allowSpellCheckAndSuggestion = true;

// Or disable suggestions and check only
this.$refs.documenteditor.ej2Instances.spellChecker.allowSpellCheckAndSuggestion = false;
```

## Enable Optimized Spell Check

Check only visible or modified pages incrementally instead of the entire document to reduce server API calls:

```ts
this.$refs.documenteditor.ej2Instances.spellChecker.enableOptimizedSpellCheck = true;
```

> **Note:** Improves performance for large documents by deferring spell check to visible regions.

## Context Menu Corrections

Right-click on a misspelled word to access:

- **Suggestions** – Replace with a recommended correction
- **Add to Dictionary** – Permanently add the word to avoid future flags
- **Ignore Once** – Skip this occurrence only
- **Ignore All** – Skip all occurrences in the current session
- **Spelling** – Open the spell check dialog for comprehensive review

## Configure Dictionary Cache

Pre-load and cache multiple language dictionaries at application startup to reduce parsing overhead:

```csharp
// Server-side (C#/.NET)
List<DictionaryData> spellDictCollection = new List<DictionaryData>();
string personalDictPath = string.Empty;
int cacheCount = 2; // Hold up to 2 language dictionaries in memory

SpellChecker.InitializeDictionaries(spellDictCollection, personalDictPath, cacheCount);
```

> **Note:** After initialization, instantiate `SpellChecker()` without parameters to use pre-loaded dictionaries.

## Add Custom Words to Dictionary

Extend the dictionary by adding domain-specific terms and their variations:

```csharp
// Server-side (C#/.NET)
SpellChecker spellChecker = new SpellChecker();
spellChecker.AddNewWord("en.dic", "en.aff", "{rootWord}", 
    new string[] { "{possibleWord1}", "{possibleWord2}", "{possibleWord3}" });
```

**Placeholders**
- `"en.dic"` → Replace with `{dictionaryFileName}`
- `"en.aff"` → Replace with `{affixFileName}`
- `"{rootWord}"` → Replace with the base word to add (e.g., "construct")
- `{ "{possibleWord1}", "{possibleWord2}", "{possibleWord3}" }` → Replace with `{possibleWordArray}`

> **Note:** Custom words persist in the personal dictionary across sessions.

## Server-Side Setup

### Create a New ASP.NET Core Web API Project

```bash
dotnet new webapi -n SpellCheckServer
cd SpellCheckServer
```

### Install Required NuGet Packages

Server-side dependencies:

```bash
dotnet add package Syncfusion.EJ2.WordEditor.AspNet.Core
dotnet add package Syncfusion.EJ2.SpellChecker.AspNet.Core
dotnet add package Newtonsoft.Json
```

### Download and Setup Dictionary Files

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

**Placeholders**
- `1033` → Replace with `{languageID}` (LCID for target language)
- `"index.dic"` → Replace with `{dictionaryFileName}`
- `"index.aff"` → Replace with `{affixFileName}`
- `"customDict.dic"` → Replace with `{personalDictionaryFileName}`

### Update Project File for Dictionary Copying

Add to `.csproj` to copy dictionary files to output directory during build:

```xml
<ItemGroup>
  <None Update="Data\**\*">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </None>
</ItemGroup>
```

> **Note:** .NET does not copy `.dic` and `.aff` files by default; this configuration ensures they are available at runtime.

### Initialize Dictionaries in Program.cs

Configure spell check at application startup to cache dictionaries and reduce latency:

```csharp
using Newtonsoft.Json;
using Syncfusion.EJ2.SpellChecker;

public class Program 
{ 
    internal static string path; 

    public static void Main(string[] args) 
    { 
        var builder = WebApplication.CreateBuilder(args); 
        var MyAllowSpecificOrigins = "AllowAllOrigins"; 
        var configuration = builder.Configuration; 
        var env = builder.Environment; 

        builder.Services.AddControllers()
            .AddNewtonsoftJson(options => 
            { 
                options.SerializerSettings.ContractResolver = new DefaultContractResolver(); 
            }); 

        builder.Services.AddMemoryCache(); 
        builder.Services.AddCors(options => 
        { 
            options.AddPolicy(MyAllowSpecificOrigins, policy => 
            { 
                policy.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader(); 
            }); 
        }); 

        builder.Services.Configure<GzipCompressionProviderOptions>(options => 
        { 
            options.Level = System.IO.Compression.CompressionLevel.Optimal; 
        }); 

        builder.Services.AddResponseCompression(); 

        var app = builder.Build(); 
        path = configuration["SPELLCHECK_DICTIONARY_PATH"]; 
        string jsonFileName = configuration["SPELLCHECK_JSON_FILENAME"]; 
        int cacheCount = int.TryParse(configuration["SPELLCHECK_CACHE_COUNT"], out int result) ? result : 1;

        path = string.IsNullOrEmpty(path) 
            ? Path.Combine(env.ContentRootPath, "Data") 
            : Path.Combine(env.ContentRootPath, path); 

        jsonFileName = string.IsNullOrEmpty(jsonFileName) 
            ? Path.Combine(path, "spellcheck.json") 
            : Path.Combine(path, jsonFileName); 

        if (File.Exists(jsonFileName)) 
        { 
            string jsonImport = File.ReadAllText(jsonFileName); 
            List<DictionaryData> spellChecks = JsonConvert.DeserializeObject<List<DictionaryData>>(jsonImport);
            List<DictionaryData> spellDictCollection = new List<DictionaryData>(); 
            string personalDictPath = string.Empty; 

            foreach (var spellCheck in spellChecks) 
            { 
                spellDictCollection.Add(new DictionaryData(
                    spellCheck.LanguadeID, 
                    Path.Combine(path, spellCheck.DictionaryPath), 
                    Path.Combine(path, spellCheck.AffixPath)
                )); 
                personalDictPath = Path.Combine(path, spellCheck.PersonalDictPath); 
            } 

            SpellChecker.InitializeDictionaries(spellDictCollection, personalDictPath, cacheCount); 
        }

        app.UseRouting();
        app.UseCors(MyAllowSpecificOrigins);
        app.UseEndpoints(endpoints => endpoints.MapControllers());
        app.Run();
    }
}
```

### Implement Spell Check Endpoints

Create `Controllers/DocumentEditorController.cs` with spell check endpoints:

```csharp
using Newtonsoft.Json;
using Syncfusion.EJ2.SpellChecker;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Cors;

[Route("api/[controller]")]
[ApiController]
[EnableCors("AllowAllOrigins")]
public class DocumentEditorController : ControllerBase
{
    [HttpPost]
    [Route("SpellCheck")]
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

**Placeholders**
- `"api/[controller]"` → Replace with `{apiRoute}` (default maps to api/documenteditor)
- Route names `"SpellCheck"`, `"SpellCheckByPage"` → Use as-is or replace with `{endpointName}`

### Build and Run

Build and start the server:

```bash
dotnet build
dotnet run
```

Default location: `http://localhost:5000/api/documenteditor/SpellCheck`

> **Important:** Update your Vue client's `serviceUrl` configuration to match your server's base URL (e.g., `http://localhost:5000/api/documenteditor/` for local development or your production URL for deployment).

### File Changes

- `Program.cs` → Initialize spell check dictionaries at startup
- `Data/spellcheck.json` → Configure dictionary paths and language IDs
- `Controllers/DocumentEditorController.cs` → Implement `SpellCheck` and `SpellCheckByPage` endpoints
- `Data/*.dic` and `Data/*.aff` → Copy Hunspell dictionary files to output directory