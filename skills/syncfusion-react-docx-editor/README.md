# Syncfusion<sup>®</sup> React DOCX Editor Skill

## Overview

Build MS Word–like document editor applications in React using the Syncfusion DOCX Editor. This skill provides AI-guided code generation and integration support for the React document editor component, enabling editing, formatting, import/export capabilities, and more.

See **[SKILL.md](SKILL.md)** for the full intent-routing guide and rules.

---

## Key Capabilities

- **Document Editing:** Create, edit, and view Word documents.
- **Protection:** Apply read-only mode, allow comments, allow form filling, enforce tracked changes,and define editable ranges.
- **Review:** Enable track changes (revisions) and accept/reject changes.
- **Comments:** Add comments, replies, and author metadata.
- **Find and replace:** Perform programmatic find and replace operations for automation.
- **Form Fields:** Insert and fill text fields, check boxes, and dropdown form fields.

---

## Getting Started

### How to Integrate Skills

**Step 1: Checkout and copy the required skills**

Clone or download the DOCX-Editor-SDK-Skills repository and copy the **syncfusion-react-docx-editor** skill from the `skills/` directory.

**Step 2: Install the skill**

Place the copied skill folder in your workspace following this structure:

```
your-workspace/
├── .github/skills/ or .claude/skills/ or .codestudio/skills/
│   └── syncfusion-react-docx-editor/
│       ├── SKILL.md
│       └── references/
├── your-project-files...
└── src/
    └── App.jsx
```

**Step 3: Verify and manage your skills**

Type `/skills` in the GitHub Copilot or Code Studio chat to quickly access the Configure Skills menu and manage your installed skills.

**Step 4: Use skills in VS Code**

There are two ways to use skills:

1. **Slash commands** - Type `/` in the GitHub Copilot chat to see available skills. For example:
   ```
   /syncfusion-react-docx-editor Create a Document Editor with built-in toolbar options
   ```

2. **Automatic loading** - Simply describe your task naturally, and your AI Agent automatically loads the relevant skill:
   ```
   Create a React document editor with a built-in toolbar that allows users to open, edit, and save documents
   ```

When a skill is loaded, AI Agent gains specialized knowledge of the Syncfusion React DOCX Editor and can help you generate code snippets or build complete document editor features.

---

## Prerequisites

### Runnable React Project

To integrate the Syncfusion DOCX Editor component directly into your project files, you need a working React application. If you don't have one yet, follow the [Getting Started guide](https://help.syncfusion.com/document-processing/word/word-processor/react/getting-started) to set up a new React project with Create React App or Vite.

**Alternative Options:**
- **No project needed:** You can request code snippets directly in the chat window for learning or reference purposes
- **Separate file generation:** Code can be saved to the skill's output folder (`syncfusion-react-docx-editor/output/`) as standalone files

---

## Example Prompts

- "Show me code to create a Document Editor component"
- "Create a Document Editor with Read‑Only restriction mode"

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **License watermark appears** | Verify that your license key is properly configured. See [Licensing](https://help.syncfusion.com/document-processing/licensing/overview). |
| **Style/Theme not applied** | Import CSS files in correct order. Ensure theme CSS matches desired theme name. |
| **Document loading issue** |  The document fails to load due to an unreachable or incorrect service URL. See [Link](https://help.syncfusion.com/document-processing/word/word-processor/react/troubleshooting/document-loading-issue-with-404-error)|

---

## Resources

- [Documentation](https://help.syncfusion.com/document-processing/word/word-processor/react/overview)
- [API Reference](https://ej2.syncfusion.com/react/documentation/api/document-editor-container/index-default)
- [Online Demo](https://document.syncfusion.com/demos/docx-editor/react/#/tailwind3/document-editor/default)

---

## License

Syncfusion React DOCX Editor SDK require a [commercial license](https://www.syncfusion.com/docx-editor-sdk/react-docx-editor) for production use. A [free Community License](https://www.syncfusion.com/products/communitylicense) is also available for individual developers and small businesses.
