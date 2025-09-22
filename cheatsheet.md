# GitHub Copilot Chat Cheatsheet

## Quick Setup

### Initial Setup
1. Sign up for GitHub Copilot (Free plan available)
2. Install the Copilot extension in your IDE
3. Sign in to GitHub in your IDE
4. Start chatting with Copilot!

### Access Methods
- **Chat Panel**: Click the Copilot icon in your IDE
- **Quick Chat**: `Ctrl+Shift+Alt+L` (Windows/Linux) or `⇧⌥⌘L` (Mac)
- **Inline Chat**: `Ctrl+I` (Windows/Linux) or `⌘I` (Mac)
- **Context Menu**: Right-click in editor and select Copilot options
- **Smart Actions**: Access via sparkle icon when selecting code lines

## Slash Commands

Slash commands help you avoid writing complex prompts for common scenarios.

### How to Use
Type `/` in the chat prompt box to see all available commands.

### Common Commands
- `/explain` - Explain the code in the current file or selection
- `/fix` - Suggest fixes for problems in the selected code
- `/tests` - Generate unit tests for the selected code
- `/doc` - Add documentation comments to the selected code
- `/optimize` - Suggest performance improvements

**Note**: More slash commands are available - type `/` in the chat prompt box to see the complete list.

### Usage Example
```
/explain
```
↳ Asks Copilot to explain the code currently displayed in the editor

## Chat Variables

Chat variables include specific context in your prompts.

### How to Use
Type `#` in the chat prompt box to see all available variables.

### Common Variables
- `#selection` - Currently selected code
- `#file` - The current file
- `#editor` - Visible portion of the current editor
- `#web` - Enable web search for current information
- `#solution` - Reference the entire solution (Visual Studio)

**Note**: More chat variables are available - type `#` in the chat prompt box to see the complete list.

### Usage Example
```
How can I improve this code? #selection
```
↳ Asks for improvements on the currently selected code

## Chat Participants

Chat participants are like domain experts with specialized knowledge.

### How to Use
- **Automatic Inference**: Copilot can automatically infer relevant participants based on your natural language prompt
- **Manual Selection**: Type `@` in the chat prompt box to see available participants

### GitHub Skills
- `@github` - Access GitHub-specific capabilities and skills
- `@github #web` - Search the web for latest information
- **Dynamic Selection**: Copilot automatically selects appropriate skills based on your question content
- **Natural Language Integration**: Use natural language to invoke specific skills

### Copilot Extensions
- Install extensions from GitHub Marketplace or VS Code Marketplace
- Provide specialized chat participants for external tool integration
- Access via `@` followed by extension name
- **Automatic Inference**: Copilot can automatically infer relevant participants based on natural language prompts (public preview)

### Usage Examples
```
@github What skills are available?
```
```
@github #web What is the latest LTS of Node.js?
```
```
@github Search the web to find the latest GPT model from OpenAI.
```

**Note**: Automatic participant inference is currently in public preview and subject to change.

## Agent Mode

**Feature**: Copilot Edits with autonomous code editing and task completion capabilities.

### Copilot Edits Modes
- **Edit Mode**: Controlled edits to multiple files with granular control
- **Agent Mode**: Autonomous task completion with iterative problem solving

### When to Use Agent Mode
- Complex tasks involving multiple steps, iterations, and error handling
- Want Copilot to determine necessary steps automatically
- Tasks requiring integration with external applications (MCP servers)
- Multi-file editing and refactoring tasks

### How to Enable Agent Mode
1. Open Copilot Chat panel
2. Select "Agent" from the mode dropdown
3. Submit your task prompt
4. Review and confirm suggested changes and terminal commands
5. Let Copilot iterate to complete the task

### Agent Mode Benefits
- **Autonomous Editing**: Streams edits directly in the editor
- **Working Set Management**: Updates working set automatically
- **Terminal Integration**: Suggests and executes terminal commands
- **Iterative Completion**: Continues until task is fully complete
- **Smart Billing**: Only initial prompts count toward usage limits, not follow-up actions or tool calls
- **Multi-Model Support**: Works with different AI models with varying multipliers

### Available In
- Visual Studio Code
- JetBrains IDEs
- Visual Studio (17.14+)

## Pro Tips

### Effective Prompting
1. Be specific about what you want
2. Include relevant context using variables
3. Use slash commands for common tasks
4. Reference specific files or code sections

### Model Selection
- **Multiple AI Models**: Choose from GPT-4.1, Claude Sonnet 3.5/3.7, Gemini 2.0 Flash/2.5 Pro
- **Premium Models**: Advanced capabilities available with premium models
- **Performance Optimization**: Different models excel at different question types
- **Usage Multipliers**: Different models have different usage multipliers for billing

### Image Support in Chat
- **Supported Formats**: JPEG, PNG, GIF, WEBP
- **Usage**: Attach images via copy/paste, drag-and-drop, or attachment button
- **Compatible Models**: GPT-4.1, Claude Sonnet 3.5/3.7, Gemini 2.0/2.5
- **Use Cases**: Screenshot explanations, UI mockups, flowchart descriptions, web page analysis

### Custom Instructions & Repository Context
- **Repository Instructions**: Add custom instruction files to your repository
- **Automatic Inclusion**: Instructions are automatically added to all chat questions
- **Referenced in Responses**: Custom instruction files may be linked in response references
- **Context Enhancement**: Help Copilot understand your project's specific context and requirements

### File References
- Attach specific files using the attachment button
- Default references include open files and selections
- Provides better context for more accurate responses

## Keyboard Shortcuts

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Quick Chat | `Ctrl+Shift+Alt+L` | `⇧⌥⌘L` |
| Inline Chat | `Ctrl+I` | `⌘I` |
| Accept Suggestion | `Tab` | `Tab` |
| Reject Suggestion | `Esc` | `Esc` |

## Troubleshooting

### Common Issues
1. **Authentication Problems**: Check GitHub sign-in status
2. **No Suggestions**: Verify Copilot subscription is active
3. **Chat Disabled**: Check organization policies if using enterprise
4. **Slow Responses**: Try different AI model or check connection

### Getting Help
- Use thumbs up/down icons to rate responses
- Report issues to microsoft/vscode-copilot-release repository
- Check GitHub Copilot Trust Center for policies
- Review FAQ in GitHub documentation

---

*Last updated: 2025-09-22 based on latest Copilot documentation*