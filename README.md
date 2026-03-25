# Syncfusion DOCX Editor SDK Skills

Skills are specialized instruction sets that teach AI assistants how to perform Word document editing tasks using platform-specific Syncfusion DOCX Editor SDK. These skills follow the [Agent Skills open standard](https://agentskills.io/) and include a `SKILL.md` manifest plus topic-level references to guide automated code generation.

## About This Repository

This repository contains **AI-ready skills** focused on DOCX Editor across multiple platforms (React, Blazor, WPF, UWP, Angular, ASP.NET Core). Each skill enables an AI to generate code snippets for the requirements.

## Included Platform-Specific DOCX Editor Skills

### Web Frameworks
- **Blazor DOCX Editor** -  Guidance for integrating the Blazor DOCX Editor into Blazor applications.
- **React DOCX Editor** - Integrate the React DOCX Editor into React applications for creating, editing, and more.
- **ASP.NET Core DOCX Editor** - Integrate the ASP.NET Core DOCX Editor into ASP.NET Core applications for creating, editing, and more.
- **Angular DOCX Editor** – Integrate the Angular DOCX Editor into Angular applications for creating, editing, and more.

### Desktop Frameworks
- **WPF DOCX Editor** - Examples and guidance for using DOCX Editor in WPF applications.
- **UWP DOCX Editor** - Examples and guidance for using DOCX Editor in UWP applications.

## Getting Started

### How to Integrate Skills

**Step 1: Checkout and copy the required skills**

Clone or download this repository and copy the skill folders you need (for example: `syncfusion-react-docx-editor`, `syncfusion-blazor-docx-editor`, `syncfusion-uwp-docx-editor`, `syncfusion-wpf-docx-editor`, `syncfusion-angular-docx-editor`, `syncfusion-aspnetcore-docx-editor`) from the `skills/` directory.

**Step 2: Install the skills**

Place the copied skill folders in your workspace following this structure:

```
your-workspace/
├── .github/skills/ or .claude/skills/ or .codestudio/skills/
│   ├── syncfusion-angular-docx-editor
│   │   └── SKILL.md
│   ├── syncfusion-aspnetcore-docx-editor/
│   │   └── SKILL.md
│   ├── syncfusion-blazor-docx-editor/
│   │   └── SKILL.md
│   ├── syncfusion-react-docx-editor/
│   │   └── SKILL.md
│   ├── syncfusion-uwp-docx-editor/
│   │   └── SKILL.md
│   ├── syncfusion-wpf-docx-editor/
│   │   └── SKILL.md
└── your-project-files...
```

Each skill directory must contain a `SKILL.md` file that defines the skill's behavior and example prompts.

**Step 3: Use the skills**

Two common ways to use skills:

1. **Automatic loading** — Describe your DOCX Editor task naturally and the AI agent will load the most relevant skill. Example:

	```
	Create DOCX Editor 
	Add a button to delete all the comments.

	```

2. **Slash commands** — Type `/` in the GitHub Copilot or Syncfusion Code Studio chat to mention available skills. For example:

	```
	/syncfusion-react-docx-editor Create DOCX Editor and enable track changes.
	```

When a skill is loaded, the AI agent gains specialized knowledge of the DOCX Editor SDK and can generate platform-specific code or step-by-step integration instructions.

## How it works

Each skill supports code generation that produces ready-to-use platform-specific code snippets you can insert into your application files (for example, `App.ts`, `Home.razor`, `App.tsx`, or `index.html`). This accelerates adding features such as text formatting, tables, images, headers/footers, track changes, and more.

**Trigger keywords:** `create`, `initialize`, `show me code`, `generate`, `how to`, `example code`

## References & Resources

- [Syncfusion DOCX Editor Overview](https://help.syncfusion.com/document-processing/word/word-processor/overview)
- [Syncfusion React DOCX Editor Documentation](https://help.syncfusion.com/document-processing/word/word-processor/react/overview)
- [Syncfusion Blazor Core Editor Overview](https://help.syncfusion.com/document-processing/word/word-processor/blazor/overview)
- [Syncfusion ASP.NET Core Editor Overview](https://help.syncfusion.com/document-processing/word/word-processor/asp-net-core/overview)
- [Syncfusion Angular DOCX Editor Documentation](https://help.syncfusion.com/document-processing/word/word-processor/angular/overview)
- [Syncfusion UWP DOCX Editor Documentation](https://help.syncfusion.com/document-processing/word/word-processor/uwp/overview)
- [Syncfusion WPF DOCX Editor Documentation](https://help.syncfusion.com/document-processing/word/word-processor/wpf/overview)
- [Syncfusion Community License](https://www.syncfusion.com/products/communitylicense)

## License

Syncfusion DOCX Editor SDK require a [commercial license](https://www.syncfusion.com/document-sdk) for production use. A [free Community License](https://www.syncfusion.com/products/communitylicense) is also available for individual developers and small businesses.

