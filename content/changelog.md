# GitHub Copilot Changelog

## 2025-12-08 Update

### 🎯 New Feature: Model Picker for Coding Agent

**Model Selection for Coding Agent** (December 8, 2025)
- Copilot Pro and Pro+ subscribers can now select which AI model to use when starting a coding agent task
- Available when starting tasks from agents tab, agents panel, or other entry points
- Provides more control over agent capabilities and performance characteristics
- Gives users flexibility to choose models best suited for specific tasks
- **Source**: [GitHub Changelog](https://github.blog/changelog/2025-12-08-model-picker-for-copilot-coding-agent-for-copilot-pro-and-pro-subscribers)

### 📋 Additional Updates

### 📋 Additional Updates

#### Documentation Verification

This update confirms that all major features documented in the November 2025 updates remain current and fully operational. The latest documentation scrape verified the following capabilities:

#### ✅ Verified Core Features & Capabilities

**Copilot Free Tier**
- No-subscription entry tier remains available for exploring core Copilot features
- Provides access to basic code suggestions and limited chat capabilities
- Perfect starting point for new users to experience Copilot

**Chat Modes Available Across IDEs**
- **Ask Mode**: Optimized for answering questions about code and exploring ideas
- **Edit Mode**: Controlled multi-file editing (VS Code, JetBrains)
- **Agent Mode**: Autonomous code editing with multi-step task completion
- **Plan Mode**: Implementation planning before execution (public preview)

**Subagents**
- Delegate complex tasks to isolated agents with their own context window
- Automatic delegation based on prompt analysis
- Direct invocation for specific tasks
- Requires custom agents configured in environment

**Chat Interface Features**
- **Slash Commands**: Quick commands for common scenarios (type `/` to see all)
- **Chat Variables**: Include specific context (type `#` to see all options)
- **Chat Participants**: Domain experts with specialized knowledge (type `@` for list)
- **GitHub Skills**: `@github` integration with dynamic skill selection
- **Web Search**: Use `#web` variable for latest information

**IDE Support Status**
- **Visual Studio Code**: Full support including all chat modes, inline chat, quick chat
- **JetBrains IDEs**: Complete integration with agent mode, edit mode, and subagents
- **Visual Studio**: Agent mode in 17.14+, Copilot Edits support
- **Xcode**: Agent mode, plan mode, subagents, and chat management
- **Eclipse**: Agent mode, plan mode, subagents, and MCP integration (version 2024-09+)
- **Windows Terminal Canary**: Terminal Chat interface

**AI Model Options**
- **Included Model**: GPT-4.1 (multiplier: 0) - no premium request consumption
- **Premium Models**: Claude Sonnet 3.5/3.7, Gemini 2.0 Flash/2.5 Pro
- **Model Selection**: Different models optimized for different question types
- **Image Support**: JPEG, PNG, GIF, WEBP attachments with compatible models

**Advanced Features**
- **Custom Instructions**: Repository-specific instruction files automatically included in chat
- **AGENTS.md Support**: Special support for agent-specific context and instructions
- **Model Context Protocol (MCP)**: Extend Copilot Chat with external tools and services
- **Copilot Extensions**: Third-party chat participants from GitHub and VS Code Marketplace

#### 💡 Usage & Billing Confirmed

**Agent Mode Billing**
- Only initial prompts count toward premium requests
- Follow-up actions and tool calls are not charged
- Model multipliers determine premium request consumption
- Included model (GPT-4.1) has multiplier of 0

**Plan Options**
- **Copilot Free**: Core features with no paid plan required
- **Copilot Pro**: Full access with generous usage limits (30-day free trial available)
- **Copilot Pro+**: Advanced features including autonomous code changes
- **Copilot Business/Enterprise**: Organization-level features and controls

#### 🎯 Access Methods & Interfaces

**Where to Use Copilot**
- IDEs: VS Code, JetBrains, Visual Studio, Xcode, Eclipse
- GitHub Mobile: Chat interface for mobile workflows
- Windows Terminal Canary: Terminal Chat interface
- Command Line: GitHub CLI integration
- GitHub Website: Direct web-based access

**Chat Access Methods**
- Chat Panel: Primary interface for extended conversations
- Quick Chat: Keyboard shortcuts for rapid questions
- Inline Chat: Direct editor integration for contextual help
- Smart Actions: Context menu integration for quick access

### 🔍 Documentation Completeness

All previously documented features remain accurate and operational. The documentation confirms:
- Complete list of slash commands available via `/` in chat
- Full set of chat variables accessible via `#` in chat
- Chat participants can be invoked via `@` or automatic inference
- Keyboard shortcuts remain consistent across platforms
- Plan mode, subagents, and agent mode working as documented

---

## 2025-11-28 Update

### ✨ New Features

#### Subagents
- **Isolated Task Delegation**: Delegate complex tasks to isolated agents with their own context window
- **Automatic Delegation**: Copilot automatically selects appropriate subagents based on your prompt
- **Direct Invocation**: Explicitly call subagents for specific tasks like testing or refactoring
- **Tool Reference**: Use `#runSubagent` in prompts for targeted delegation
- **Requires Custom Agents**: Subagents work with custom agent configurations
- **Available In**: VS Code, JetBrains IDEs, Xcode, Eclipse

#### Plan Mode (Public Preview)
- **Implementation Planning**: Create detailed plans before executing code changes
- **Research Phase**: Comprehensive research using read-only tools and codebase analysis
- **Actionable Steps**: Break down tasks into manageable, actionable steps
- **Open Questions**: Plans include questions about ambiguous requirements
- **Plan Handoff**: Approve plans and hand off to agent mode for implementation
- **Save for Later**: Export plans as Markdown for team review and discussions

### 🔧 IDE Support Enhancements

#### All Chat Modes Now Available
- **Ask Mode**: Question answering and code exploration
- **Edit Mode**: Controlled multi-file editing (VS Code, JetBrains)
- **Agent Mode**: Autonomous task completion with iteration
- **Plan Mode**: Implementation planning before execution

#### Platform-Specific Updates
- **Xcode**: Full agent mode, plan mode, and subagent support
- **Eclipse**: Agent mode, plan mode, subagents, and MCP integration
- **Visual Studio**: Agent mode in 17.14+ with Copilot Edits
- **JetBrains**: Complete edit mode and agent mode with subagent support

### 📋 Documentation Verification

This update confirms all features from previous updates remain operational:

- ✅ **Agent Mode**: Multi-step autonomous task completion across all supported IDEs
- ✅ **Copilot Free Plan**: No-subscription entry tier for core features
- ✅ **Image Support**: JPEG, PNG, GIF, WEBP attachments with compatible AI models
- ✅ **GitHub Skills**: `@github` integration with dynamic skill selection and `#web` search
- ✅ **Custom Instructions**: AGENTS.md and repository-specific instruction files
- ✅ **MCP Integration**: Model Context Protocol support for external tool integration
- ✅ **Multiple AI Models**: GPT-4.1 (included), Claude Sonnet 3.5/3.7, Gemini 2.0/2.5 (premium)

---

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

*This changelog is compiled from the latest GitHub Copilot documentation as of 2025-12-08. Features may be in various stages of rollout across different plans and platforms.*