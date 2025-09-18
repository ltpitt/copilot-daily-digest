# GitHub Copilot Changelog

## 2025-09-18 Update

### ✨ New Features

#### Copilot Agent Mode
- **Autonomous Code Editing**: Agent mode now enables Copilot to autonomously edit your code and complete complex tasks
- **Multi-step Task Completion**: Copilot determines which files to change and iterates to remediate issues until tasks are complete
- **Terminal Integration**: Suggests and executes terminal commands as part of task completion
- **Smart Billing**: Only initial prompts count toward usage limits, not follow-up actions or tool calls

#### Enhanced Chat Participants
- **Automatic Inference**: Copilot Chat can now automatically infer relevant chat participants based on natural language prompts
- **Improved Discovery**: Advanced capabilities are now more discoverable without explicit participant specification
- **Preview Status**: Currently in public preview and subject to change

#### Copilot Extensions Integration
- **Third-party Chat Participants**: Install Copilot Extensions that provide specialized chat participants
- **Marketplace Access**: Extensions available from both GitHub Marketplace and Visual Studio Code Marketplace
- **External Tool Integration**: Better integration with external tools through chat participants

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
- **VS Code Integration**: Enhanced chat panel with better file references
- **JetBrains Support**: Improved authentication and chat functionality
- **Visual Studio**: Better integration with latest versions (17.8+)
- **Eclipse Support**: Added agent mode functionality
- **Xcode Integration**: Enhanced chat capabilities

#### Mobile & Web Enhancements
- **GitHub Mobile**: Improved chat interface for mobile development
- **Web Interface**: Better integration on GitHub website
- **Terminal Support**: Enhanced Windows Terminal Canary integration

### 📱 New Capabilities

#### GitHub Skills for Copilot
- **@github Integration**: Access GitHub-specific skills through chat
- **Dynamic Skill Selection**: Copilot automatically selects appropriate skills based on questions
- **Web Search**: Use `#web` variable for latest information searches
- **Skill Discovery**: Query available skills with `@github What skills are available?`

#### Improved Context Handling
- **Custom Instructions**: Repository-specific instructions automatically included in chat questions
- **Better References**: Enhanced file reference system with attachment support
- **Context Variables**: Expanded set of chat variables for better prompt context

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
- **Slash Command Expansion**: More slash commands available for common scenarios
- **Variable System**: Enhanced chat variables for specific context inclusion
- **Keyword Support**: Special keywords to help Copilot understand prompts better

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

*This changelog is compiled from the latest GitHub Copilot documentation as of 2025-09-18. Features may be in various stages of rollout across different plans and platforms.*