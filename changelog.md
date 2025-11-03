# GitHub Copilot Changelog

## 2025-11-03 Update

### 📋 Documentation Review

This update confirms that all major features documented in the October 2025 update remain current and accurate. The latest documentation scrape verified the following capabilities are fully operational:

#### ✅ Verified Core Features
- **Agent Mode**: Autonomous code editing with multi-step task completion continues to be available across VS Code, JetBrains IDEs, Visual Studio 17.14+, Xcode, and Eclipse
- **Copilot Free Plan**: No-subscription entry tier remains available for exploring core features
- **Image Support**: JPEG, PNG, GIF, and WEBP image attachments in chat continue to work with compatible AI models
- **GitHub Skills**: `@github` integration with dynamic skill selection and web search via `#web` variable
- **Custom Instructions**: AGENTS.md and repository-specific instruction files automatically integrated into chat context

#### 🎯 IDE Support Status
- **VS Code**: Full feature support including agent mode, image attachments, and Copilot Edits
- **JetBrains IDEs**: Complete integration with agent mode and edit mode capabilities
- **Visual Studio**: Agent mode available in 17.14+, with built-in extensions for 17.10+
- **Xcode**: Chat capabilities, agent mode, and file reference support
- **Eclipse**: Agent mode and MCP server integration support (requires version 2024-09+)
- **Windows Terminal Canary**: Terminal Chat interface operational

#### 🤖 AI Model Options Confirmed
- **Included Models**: GPT-4.1 (multiplier: 0) - no premium request consumption
- **Premium Models**: Claude Sonnet 3.5/3.7, Gemini 2.0 Flash/2.5 Pro available with varying multipliers
- **Model Selection**: Different models optimized for different question types and use cases

#### 💡 Usage & Billing Clarifications
- **Agent Mode Billing**: Only initial prompts count toward premium requests; follow-up actions and tool calls are not charged
- **Model Multipliers**: Each model has specific multipliers that determine premium request consumption
- **Free Tier**: Copilot Free provides limited features without premium model access

### 🔍 Documentation Completeness

All slash commands, chat variables, chat participants, and keyboard shortcuts previously documented remain accurate. No deprecated features were identified in this update cycle.

---

## 2025-10-16 Update

### ✨ New Features

#### Copilot Agent Mode
- **Autonomous Code Editing**: Agent mode now enables Copilot to autonomously edit your code and complete complex tasks
- **Multi-step Task Completion**: Copilot determines which files to change and iterates to remediate issues until tasks are complete
- **Terminal Integration**: Suggests and executes terminal commands as part of task completion
- **Smart Billing**: Only initial prompts count toward usage limits, not follow-up actions or tool calls

#### Enhanced Chat Participants
- **Automatic Inference**: Copilot Chat can now automatically infer relevant chat participants based on natural language prompts (currently in public preview)
- **Improved Discovery**: Advanced capabilities are now more discoverable without explicit participant specification
- **Copilot Extensions**: Install extensions from GitHub Marketplace or VS Code Marketplace for specialized chat participants
- **External Tool Integration**: Better integration with external tools through chat participants

#### Copilot Extensions Integration
- **Third-party Chat Participants**: Install Copilot Extensions that provide specialized chat participants
- **Marketplace Access**: Extensions available from both GitHub Marketplace and Visual Studio Code Marketplace
- **External Tool Integration**: Enhanced integration with external tools through chat participants
- **Domain-Specific Context**: Extensions provide specialized knowledge for specific domains and tools

#### Repository Custom Instructions & AGENTS.md Support
- **Custom Instructions Files**: Repositories can now include custom instruction files that are automatically added to all chat questions
- **AGENTS.md Support**: Special support for AGENTS.md files to provide agent-specific context and instructions
- **Automatic Integration**: Custom instructions improve response quality by providing project-specific context
- **Reference Links**: Custom instruction files are referenced in chat responses for transparency

### 🚀 Plan Updates

#### Copilot Free
- **No Subscription Required**: Explore core Copilot features without any paid plan
- **Entry Point**: Perfect for getting started with Copilot capabilities

#### Copilot Pro & Pro+
- **30-Day Free Trial**: One-time trial available for Copilot Pro
- **Enhanced Features**: Pro+ includes autonomous code changes and pull request creation
- **Student Access**: Students, teachers, and open source maintainers may qualify for free access

### 🔧 Platform Enhancements

#### IDE Support Improvements
- **VS Code Integration**: Enhanced chat panel with better file references and image support
- **JetBrains Support**: Improved authentication, chat functionality, and agent mode support
- **Visual Studio**: Better integration with latest versions (17.8+), built-in extensions for 17.10+
- **Eclipse Support**: Added agent mode functionality and enhanced chat capabilities
- **Xcode Integration**: Enhanced chat capabilities and better context handling

#### Mobile & Web Enhancements
- **GitHub Mobile**: Improved chat interface for mobile development workflows
- **Web Interface**: Better integration on GitHub website with enhanced chat features
- **Terminal Support**: Enhanced Windows Terminal Canary integration with Terminal Chat interface
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
- **AGENTS.md Support**: Special support for AGENTS.md files to provide agent-specific context
- **Better References**: Enhanced file reference system with attachment support and reference links
- **Context Variables**: Expanded set of chat variables including #solution for Visual Studio
- **Working Set Management**: Improved automatic file selection and context awareness

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
- **Smart Actions**: Improved context menu integration for quick access to common actions

#### Collaboration Features
- **Copilot Spaces**: Organize and share task-specific context for team collaboration
- **Knowledge Bases**: Create documentation collections for better context (Enterprise)
- **Pull Request Integration**: Automatic PR description generation

### 📊 Performance & Reliability

#### Usage Tracking
- **Premium Request Monitoring**: Clear tracking of premium request usage
- **Model Multipliers**: Different models have different usage multipliers
- **Billing Transparency**: Agent mode follow-up actions don't count toward usage

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

*This changelog is compiled from the latest GitHub Copilot documentation as of 2025-11-03. Features may be in various stages of rollout across different plans and platforms.*