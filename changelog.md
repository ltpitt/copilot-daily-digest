# GitHub Copilot Changelog

## 2025-09-22 Update

### ✨ New Features

#### Copilot Edits with Enhanced Modes
- **Edit Mode**: Make controlled edits to multiple files with granular control over LLM requests and file selection
- **Agent Mode**: Autonomous task completion with iterative problem solving and terminal command integration
- **Multi-File Editing**: Make changes across multiple files from a single chat prompt
- **Working Set Management**: Automatic file selection and context management

#### Enhanced Chat Participants
- **Automatic Inference**: Copilot Chat can automatically infer relevant chat participants based on natural language prompts (public preview)
- **Improved Discovery**: Advanced capabilities are more discoverable without explicit participant specification  
- **Copilot Extensions**: Install extensions from GitHub Marketplace or VS Code Marketplace for specialized chat participants
- **External Tool Integration**: Better integration with external tools through extensions

#### GitHub Skills for Copilot
- **@github Integration**: Access GitHub-specific skills through chat
- **Dynamic Skill Selection**: Copilot automatically selects appropriate skills based on questions
- **Web Search**: Use `#web` variable for latest information searches
- **Skill Discovery**: Query available skills with `@github What skills are available?`
- **Natural Language Integration**: Use natural language to invoke specific skills

#### Enhanced Image Support in Chat
- **Multi-Format Support**: Support for JPEG, PNG, GIF, and WEBP image formats
- **Visual Code Assistance**: Attach screenshots, UI mockups, flowcharts, and web pages
- **Compatible Models**: Works with GPT-4.1, Claude Sonnet 3.5/3.7, and Gemini 2.0 Flash/2.5 Pro
- **Multiple Attachment Methods**: Copy/paste, drag-and-drop, or attachment button
- **Enterprise Controls**: Requires "Editor preview features" setting for Business/Enterprise plans

### 🚀 Plan Updates

#### Copilot Free
- **No Subscription Required**: Explore core Copilot features without any paid plan  
- **Entry Point**: Perfect for getting started with Copilot capabilities

#### Copilot Pro & Pro+
- **30-Day Free Trial**: One-time trial available for Copilot Pro
- **Enhanced Features**: Pro+ includes autonomous code changes and pull request creation (Pro+, Business, and Enterprise only)
- **Student Access**: Students, teachers, and open source maintainers may qualify for free access

### 🔧 Platform Enhancements

#### IDE Support Improvements
- **VS Code Integration**: Enhanced chat panel with Copilot Edits, better file references and image support
- **JetBrains Support**: Improved authentication, chat functionality, and Copilot Edits support
- **Visual Studio**: Better integration with latest versions (17.14+ for agent mode), built-in extensions
- **Eclipse Support**: Added agent mode functionality and enhanced chat capabilities
- **Xcode Integration**: Enhanced chat capabilities and better context handling

#### Mobile & Web Enhancements
- **GitHub Mobile**: Improved chat interface for mobile development workflows
- **Web Interface**: Better integration on GitHub website with enhanced chat features
- **Terminal Support**: Enhanced Windows Terminal Canary integration with Terminal Chat interface for command line assistance
- **Cross-Platform**: Consistent experience across all supported platforms

### 📱 New Capabilities

#### GitHub Skills for Copilot
- **@github Integration**: Access GitHub-specific skills through chat
- **Dynamic Skill Selection**: Copilot automatically selects appropriate skills based on questions
- **Web Search**: Use `#web` variable for latest information searches
- **Skill Discovery**: Query available skills with `@github What skills are available?`
- **Natural Language Integration**: Use natural language to invoke specific skills

#### Image Support in Chat
- **Multi-Format Support**: Support for JPEG, PNG, GIF, and WEBP image formats
- **Visual Code Assistance**: Attach screenshots, UI mockups, flowcharts, and web pages
- **Compatible Models**: Works with GPT-4.1, Claude Sonnet 3.5/3.7, and Gemini 2.0/2.5
- **Multiple Attachment Methods**: Copy/paste, drag-and-drop, or attachment button
- **Enterprise Controls**: Requires "Editor preview features" setting for Business/Enterprise plans

#### Enhanced AI Model Selection
- **GPT-4.1**: Default model with comprehensive capabilities
- **Claude Sonnet 3.5/3.7**: Advanced reasoning and code understanding  
- **Gemini 2.0 Flash/2.5 Pro**: Fast responses and advanced capabilities
- **Usage Multipliers**: Different models have different billing multipliers
- **Model-Specific Features**: Some features like image support require specific models

#### Improved Context Handling
- **Custom Instructions**: Repository-specific instructions automatically included in chat questions
- **Better References**: Enhanced file reference system with attachment support and reference links
- **Context Variables**: Expanded set of chat variables including #solution for Visual Studio
- **Working Set Management**: Improved automatic file selection and context awareness for Copilot Edits

### 🎨 User Experience Improvements

#### Chat Interface Enhancements
- **Smart Actions**: Improved context menu integration for quick access
- **Inline Chat**: Better inline chat experience directly in editor
- **Quick Chat**: Enhanced quick chat dropdown functionality
- **Response Formatting**: Better handling of code blocks, buttons, and interactive elements

#### Model Selection
- **Multiple AI Models**: Access to different models for various use cases
- **Premium Models**: Advanced capabilities available with premium models
- **Performance Optimization**: Different models perform better for different question types

### 🛠️ Developer Experience

#### Better Prompting
- **Slash Command Expansion**: Complete set of slash commands available - type `/` to see all options
- **Variable System**: Enhanced chat variables including #selection, #file, #editor, #web, #solution
- **Keyword Support**: Special keywords to help Copilot understand prompts better
- **Smart Actions**: Improved context menu integration with sparkle icon for quick access to common actions

#### Collaboration Features
- **Copilot Spaces**: Organize and share task-specific context for team collaboration
- **Knowledge Bases**: Create documentation collections for better context (Enterprise)
- **Pull Request Integration**: Automatic PR description generation

### 📊 Performance & Reliability

#### Usage Tracking
- **Premium Request Monitoring**: Clear tracking of premium request usage
- **Model Multipliers**: Different models have different usage multipliers
- **Copilot Edits Billing**: Agent mode follow-up actions don't count toward usage - only initial prompts are billed

#### Authentication & Security
- **Improved Auth**: Better authentication flow across all platforms
- **Organization Controls**: Enhanced policy management for enterprise users
- **Trust Center**: Comprehensive security and privacy documentation

---

## Previous Notable Updates

### Enhanced Documentation
- Comprehensive prompt engineering guides
- Platform-specific setup instructions
- Troubleshooting and FAQ improvements

### Accessibility Improvements
- Better keyboard navigation
- Screen reader compatibility
- High contrast theme support

### API & Integration
- GitHub CLI integration improvements
- REST API enhancements for enterprise users
- Webhook support for organization management

---

## Coming Soon 🔮

- Enhanced agent mode capabilities
- More third-party integrations
- Advanced code review features
- Expanded language support

---

*This changelog is compiled from the latest GitHub Copilot documentation as of 2025-09-22. Features may be in various stages of rollout across different plans and platforms.*