# Syncfusion<sup>®</sup> UWP DOCX Editor Skill

## Overview

Build a WYSIWYG rich text editor in UWP using the Syncfusion DOCX Editor. This skill provides AI-guided code generation and integration support for the UWP RichTextBox component, enabling editing, formatting, import/export capabilities, and more.

See **[SKILL.md](SKILL.md)** for the full intent-routing guide and rules.

---

## Key Capabilities

- **Document Editing:** View and edit rich text content, including text, images, tables, and comments.
- **Formatting and Styles:** Apply text, paragraph, list, hyperlink, and style formatting.
- **Comments:** Add and manage comments in the document.
- **Find and Replace:** Perform programmatic find-and-replace operations for automation.
- **Import/Export:** Import and export Word, RTF, HTML, and text formats.
- **Localization:** Localize UI text into different languages.

---

## Getting Started

### How to Integrate Skills

**Step 1: Checkout and copy the required skills**

Clone or download the DOCX-Editor-SDK-Skills repository and copy the **syncfusion-uwp-docx-editor** skill from the `skills/` directory.

**Step 2: Install the skill**

Place the copied skill folders in your workspace following this structure:

```
your-workspace/
├── .github/skills/          # or .claude/skills/ or .codestudio/skills/
│   └── syncfusion-uwp-docx-editor/
│       └── SKILL.md
├── Docxeditor/              # UWP projects
│   ├── MainPage.xaml
│   ├── MainPage.xaml.cs
│   └── ...
└── Docxeditor.sln          # Solution file
```

**Step 3: Verify and manage your skills**

Type `/skills` in the GitHub Copilot or Code Studio chat to quickly access the Configure Skills menu and manage your installed skills.

**Step 4: Use skills in VS Code**

There are two ways to use skills:

1. **Slash commands** - Type `/` in the GitHub Copilot chat to see available skills. For example:
   ```
   /syncfusion-uwp-docx-editor Create a UWP page with SfRichTextBoxAdv to insert and format a table
   ```

2. **Automatic loading** - Simply describe your task naturally, and your AI Agent automatically loads the relevant skill:
   ```
   Create a UWP document editor using SfRichTextBoxAdv with a radial menu that allows users to open, edit, and save documents
   ```
   
When a skill is loaded, AI Agent gains specialized knowledge of Syncfusion UWP DOCX Editor and can help you generate code for your UWP project efficiently.

### Prerequisites

### Runnable UWP project 

To integrate the Syncfusion UWP DOCX Editor component directly into your project files, you need a working UWP project. If you don't have one yet, follow the [Getting Started guide](https://help.syncfusion.com/document-processing/word/word-processor/uwp/getting-started) to set up a new UWP project.

**Alternative Options:**
- **No project needed:** You can request code snippets directly in the chat window for learning or reference purposes
- **Separate file generation:** Code can be saved to the skill's output folder (`syncfusion-uwp-docx-editor/output/`) as standalone files

## Example Prompts

*Use these when you want C# code snippets for your UWP project.*

- "Show me how to enable the radial menu in SfRichTextBoxAdv for text formatting"  
- "Generate code to insert and format a table in a UWP document editor"  
- "Add comments to selected text in SfRichTextBoxAdv"  
- "Show me how to perform find and replace in a UWP document"  
- "Generate code to load and save Word, RTF, and HTML documents"   

---
## Troubleshooting

| Issue | Solution |
|-------|----------|
| License Watermark | Add key to `SyncfusionLicense.txt` or use env var `SYNCFUSION_LICENSE_KEY` |
| Missing NuGet package | `dotnet add package Syncfusion.SfRichTextBoxAdv.UWP`|
| Document Not Loading | Check file path and ensure the format is supported |

---

## Resources

- [Syncfusion UWP DOCX Editor Documentation](https://help.syncfusion.com/document-processing/word/word-processor/uwp/overview)
- [API Reference](https://help.syncfusion.com/cr/uwp/Syncfusion.UI.Xaml.RichTextBoxAdv.html)
- [Demo & Examples](https://github.com/syncfusion/uwp-demos)

---

## License

Syncfusion UWP DOCX Editor requires a commercial license for production use. A [free community license](https://www.syncfusion.com/products/communitylicense) is available for qualifying organizations.