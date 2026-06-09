# Syncfusion<sup>®</sup> WPF DOCX Editor Skill

## Overview

Build a WYSIWYG rich text editor in WPF using the Syncfusion DOCX Editor. This skill provides AI-guided code generation and integration support for the WPF RichTextBox component, enabling editing, formatting, import/export capabilities, and more.

See **[SKILL.md](SKILL.md)** for the full intent-routing guide and rules.

---

## Key Capabilities

- **Document Editing:** View and edit rich text content, including text, images, tables, and comments.
- **Formatting and Styles:** Apply text, paragraph, list, hyperlink, and style formatting.
- **Comments:** Add and manage comments in the document.
- **Find and Replace:** Perform programmatic find-and-replace operations for automation.
- **Spell Check:** Perform spell-checking on text content.
- **Import/Export:** Import and export Word, RTF, HTML, XAML, and text formats.

---

## Getting Started

### How to Integrate Skills

**Step 1: Checkout and copy the required skills**

Clone or download the DOCX-Editor-SDK-Skills repository and copy the **syncfusion-wpf-docx-editor** skill from the `skills/` directory.

**Step 2: Install the skill**

Place the copied skill folders in your workspace following this structure:

```
your-workspace/
├── .github/skills/          # or .claude/skills/ or .codestudio/skills/
│   └── syncfusion-wpf-docx-editor/
│       └── SKILL.md
├── Docxeditor/              # WPF projects
│   ├── MainWindow.xaml
│   ├── MainWindow.xaml.cs
│   └── ...
└── Docxeditor.sln          # Solution file
```

**Step 3: Verify and manage your skills**

Type `/skills` in the GitHub Copilot or Code Studio chat to quickly access the Configure Skills menu and manage your installed skills.

**Step 4: Use skills in VS Code**

There are two ways to use skills:

1. **Slash commands** - Type `/` in the GitHub Copilot chat to see available skills. For example:
   ```
   /syncfusion-wpf-docx-editor Create a WPF window with SfRichTextBoxAdv to insert and format a table
   ```

2. **Automatic loading** - Simply describe your task naturally, and your AI Agent automatically loads the relevant skill:
   ```
   Create a WPF document editor using SfRichTextRibbon and SfRichTextBoxAdv that allows users to open, edit, and save documents
   ```

When a skill is loaded, AI Agent gains specialized knowledge of Syncfusion WPF DOCX Editor and can help you generate code for your WPF project efficiently.

### Prerequisites

### Runnable WPF project 

To integrate the Syncfusion WPF DOCX Editor component directly into your project files, you need a working WPF project. If you don't have one yet, follow the [Getting Started guide](https://help.syncfusion.com/document-processing/word/word-processor/wpf/getting-started) to set up a new WPF project.

**Alternative Options:**
- **No project needed:** You can request code snippets directly in the chat window for learning or reference purposes
- **Separate file generation:** Code can be saved to the skill's output folder (`syncfusion-wpf-docx-editor/output/`) as standalone files

## Example Prompts

*Use these when you want C# code snippets for your WPF project.*

* "Create a WPF application with SfRichTextBoxAdv for editing and formatting documents"
* "Show me how to integrate SfRichTextRibbon with SfRichTextBoxAdv"
* "Generate code to apply paragraph styles and bullet lists to selected text"
* "Show me how to perform find and replace in a WPF document editor"
* "Enable spell check support in SfRichTextBoxAdv"
* "Show me how to load and save documents in Word and HTML formats"

---
## Troubleshooting

| Issue | Solution |
|-------|----------|
| License Watermark | Add key to `SyncfusionLicense.txt` or use env var `SYNCFUSION_LICENSE_KEY` |
| Missing NuGet package | `dotnet add package Syncfusion.SfRichTextBoxAdv.WPF`|
| `SfRichTextRibbon` backstage not opening | Ensure the window inherits `RibbonWindow`, not `Window` |

---

## Resources

- [Syncfusion WPF DOCX Editor Documentation](https://help.syncfusion.com/document-processing/word/word-processor/wpf/overview)
- [API Reference](https://help.syncfusion.com/cr/wpf/Syncfusion.Windows.Controls.RichTextBoxAdv.html)
- [Demo & Examples](https://github.com/syncfusion/docx-editor-sdk-wpf-demos)

---

## License

Syncfusion WPF DOCX Editor SDK requires a commercial license for production use. A [free community license](https://www.syncfusion.com/products/communitylicense) is available for qualifying organizations.