# Spell Check

Enable real-time spelling verification in the Document Editor with multi-language support, custom dictionaries, and contextual correction suggestions.

## Enable Spell Check

Activate spell checking by setting `enableSpellChecker="true"` on the Document Editor component.

```cshtml
<ejs-documenteditorcontainer 
    id="container" 
    height="700px"
    serviceUrl="/api/DocumentEditor/"
    enableSpellCheck=true>
</ejs-documenteditorcontainer>

<script>
    var container;
    document.addEventListener('DOMContentLoaded', function () {
        container = document.getElementById('container').ej2_instances[0];
        container.documentEditor.spellChecker.languageID = 1033;
        container.documentEditor.spellChecker.removeUnderline = false;
        container.documentEditor.spellChecker.allowSpellCheckAndSuggestion = true;
    });
</script>
```

**Placeholders**
- `https://localhost:5001/api/documenteditor/` → Replace with `{serviceUrl}`

## Control Underline Display

Show or hide the red squiggly underline that indicates misspelled words.

```javascript
documentEditor.spellChecker.removeUnderline = false; // Show underline
```

## Enable Suggestions

Enable correction suggestions when spell checking detects errors.

```javascript
documentEditor.spellChecker.allowSpellCheckAndSuggestion = true;
```

## Configure Language

Set the language for spell checking using Language Locale ID (LCID).

```javascript
documentEditor.spellChecker.languageID = 1033; // en-US
```

**Placeholders**
- `1033` → Replace with `{languageID}` (1033=en-US, 1036=fr-FR, 1031=de-DE)



## Context Menu Actions

Right-click any misspelled word to access these options:
- **Suggestions** – Select a recommended spelling correction
- **Add to Dictionary** – Add the word permanently to the user's dictionary
- **Ignore Once** – Skip this instance without dictionary changes
- **Ignore All** – Skip all instances of this word in the current session
- **Spelling** – Open the spell check dialog for comprehensive review

## Server Architecture

The Document Editor client communicates with an ASP.NET Core Web API backend that hosts Syncfusion SpellChecker with Hunspell dictionaries. The server manages multi-language support, custom dictionaries, and performance optimization through dictionary caching.

### Server Endpoints

- **POST `/api/documenteditor/SpellCheck`** – Returns spelling errors and suggestions for text
- **POST `/api/documenteditor/SpellCheckByPage`** – Performs incremental page-by-page spell checking for optimized performance

### Server Setup

**Step 1: Create ASP.NET Core Web API Project**

```bash
dotnet new webapi -n SpellCheckServer
cd SpellCheckServer
```

**Step 2: Install Required NuGet Packages**

```bash
dotnet add package Syncfusion.EJ2.SpellChecker.AspNet.Core
dotnet add package Syncfusion.EJ2.WordEditor.AspNet.Core
dotnet add package Newtonsoft.Json
```

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
        public string SpellCheck([FromBody] SpellCheckJsonData spellChecker) 
        {  
            try  
            {  
                SpellChecker spellCheck = new SpellChecker();  
                spellCheck.GetSuggestions(spellChecker.LanguageID, spellChecker.TexttoCheck, spellChecker.CheckSpelling, spellChecker.CheckSuggestion, spellChecker.AddWord);  
                return Newtonsoft.Json.JsonConvert.SerializeObject(spellCheck);  
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
        public string SpellCheckByPage([FromBody] SpellCheckJsonData spellChecker)  
        {  
            try  
            {  
                SpellChecker spellCheck = new SpellChecker();  
                spellCheck.CheckSpelling(spellChecker.LanguageID, spellChecker.TexttoCheck);
                return Newtonsoft.Json.JsonConvert.SerializeObject(spellCheck);  
            }  
            catch  
            {  
                return "{\"SpellCollection\":[],\"HasSpellingError\":false,\"Suggestions\":null}";  
            }  
        }  

        public class SpellCheckJsonData  
        {  
            public int LanguageID { get; set; }  
            public string TexttoCheck { get; set; }  
            public bool CheckSpelling { get; set; }  
            public bool CheckSuggestion { get; set; }  
            public bool AddWord { get; set; }  
        } 

```

**Step 5: Configure Program.cs**

Initialize spell check dictionaries at application startup:

```csharp
using Syncfusion.EJ2.SpellChecker;
using Newtonsoft.Json;

var builder = WebApplication.CreateBuilder(args);

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

// Initialize dictionaries at startup for optimal performance
var env = app.Environment;
string dataPath = Path.Combine(env.ContentRootPath, "Data");

if (Directory.Exists(dataPath))
{
    var spellDictCollection = new List<DictionaryData>();
    string personalDictPath = Path.Combine(dataPath, "customDict.dic");

    spellDictCollection.Add(
        new DictionaryData(
            1033,
            Path.Combine(dataPath, "index.dic"),
            Path.Combine(dataPath, "index.aff")
        )
    );

    SpellChecker.InitializeDictionaries(spellDictCollection, personalDictPath, 2);
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

app.MapStaticAssets();
app.MapRazorPages()
   .WithStaticAssets();

app.Run();

```

**Step 6: Build and Run**

```bash
dotnet build
dotnet run
```

The API server will start at `https://localhost:5001` (or your configured port).