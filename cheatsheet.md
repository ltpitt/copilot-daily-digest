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

### Usage Example
```
How can I improve this code? #selection
```
↳ Asks for improvements on the currently selected code

## Chat Participants

Domain experts that provide specialized help.

### How to Use
Type `@` in the chat prompt box to see available participants.

### GitHub Skills
- `@github` - Access GitHub-specific capabilities
- `@github #web` - Search the web for latest information

### Usage Examples
```
@github What skills are available?
```
```
@github #web What is the latest LTS of Node.js?
```

## Agent Mode

**New Feature**: Autonomous code editing and task completion.

### When to Use Agent Mode
- Complex tasks involving multiple steps
- Want Copilot to determine necessary steps automatically
- Need integration with external applications (MCP servers)
- Iterative problem solving with error handling

### How to Enable
1. Open Copilot Chat panel
2. Select "Agent" from the mode dropdown
3. Submit your task prompt
4. Review and confirm suggested changes and terminal commands

### Agent Mode Benefits
- Streams edits directly in the editor
- Updates working set automatically
- Suggests and runs terminal commands
- Iterates to fix issues until task completion
- Only initial prompts count toward usage limits

## Pro Tips

### Effective Prompting
1. Be specific about what you want
2. Include relevant context using variables
3. Use slash commands for common tasks
4. Reference specific files or code sections

### Model Selection
- Different AI models available for different use cases
- Premium models offer advanced capabilities
- Choose based on your question type and needs

### Custom Instructions & AGENTS.md Support
- **Repository Instructions**: Add custom instructions files to your repository
- **Automatic Inclusion**: Instructions are automatically added to all chat questions
- **AGENTS.md Support**: Special support for AGENTS.md files in repositories
- **Context Enhancement**: Help Copilot understand your project's specific context and requirements
- **Referenced in Responses**: Custom instruction files may be linked in response references

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

*Last updated: 2025-09-18 based on latest Copilot documentation*