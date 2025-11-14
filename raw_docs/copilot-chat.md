GitHub Copilot
/
How-tos
/
Chat with Copilot
/
Chat in IDE
Asking GitHub Copilot questions in your IDE
Use Copilot Chat in your editor to give you code suggestions, explain code, generate unit tests, and suggest code fixes.
Tool navigation
Visual Studio Code
JetBrains IDEs
Visual Studio
Eclipse
Xcode
In this article
Introduction
Prerequisites
Submitting prompts
Using keywords in your prompt
Using GitHub skills for Copilot
Using Model Context Protocol (MCP) servers
AI models for Copilot Chat
Additional ways to access Copilot Chat
Copilot Chat chat modes
Using images in Copilot Chat
Sharing feedback
Further reading
Prerequisites
Submitting prompts
Using keywords in your prompt
Using GitHub skills for Copilot (preview)
Using Model Context Protocol (MCP) servers
AI models for Copilot Chat
Additional ways to access Copilot Chat
Copilot Edits
Using images in Copilot Chat
Sharing feedback
Further reading
Prerequisites
Submitting prompts
Using keywords in your prompt
Using GitHub skills for Copilot
Using Model Context Protocol (MCP) servers
AI models for Copilot Chat
Additional ways to access Copilot Chat
Copilot Edits
Sharing feedback
Further reading
Prerequisites
Submitting prompts
Using Model Context Protocol (MCP) servers
AI models for Copilot Chat
Using keywords in your prompt
Copilot agent mode
File references
Chat management
Sharing feedback
Further reading
Prerequisites
Submitting prompts
Using keywords in your prompt
Using Model Context Protocol (MCP) servers
AI models for Copilot Chat
Copilot agent mode
Further reading
Introduction
This guide describes how to use Copilot Chat to ask questions about software development in your IDE. You can ask general questions about software development, or specific questions about the code in your project. For more information, see
About GitHub Copilot Chat
.
Prerequisites
Access to GitHub Copilot
. See
What is GitHub Copilot?
.
Latest version of Visual Studio Code
. See the
Visual Studio Code download page
.
Sign in to GitHub in Visual Studio Code
. If you experience authentication issues, see
Troubleshooting common issues with GitHub Copilot
.
If you have access to GitHub Copilot via your organization, you won't be able to use GitHub Copilot Chat if your organization owner has disabled chat. See
Managing policies and features for GitHub Copilot in your organization
.
Submitting prompts
You can ask Copilot Chat to give you code suggestions, explain code, generate unit tests, and suggest code fixes.
To open the chat view, click the
icon in the title bar of Visual Studio Code. If the
icon is not displayed, right-click the title bar and make sure that
Command Center
is selected.
Enter a prompt in the prompt box, or click one of the suggested prompts. For an introduction to the kinds of prompts you can use, see
Getting started with prompts for GitHub Copilot Chat
.
Evaluate Copilot's response, and make a follow-up request if needed.
The response may contain text, code blocks, buttons, images, URIs, and file trees. The response often includes interactive elements. For example, the response may include a menu to insert a code block, or a button to invoke a Visual Studio Code command.
To see the files that Copilot Chat used to generate the response, select the
Used
n
references
dropdown at the top of the response. The references may include a link to a custom instructions file for your repository. This file contains additional information that is automatically added to all of your chat questions to improve the quality of the responses. For more information, see
Adding repository custom instructions for GitHub Copilot
.
Using keywords in your prompt
You can use special keywords to help Copilot understand your prompt. For examples, see
Getting started with prompts for GitHub Copilot Chat
.
Chat participants
Chat participants are like domain experts who have a specialty that they can help you with.
Copilot Chat can infer relevant chat participants based on your natural language prompt, improving discovery of advanced capabilities without you having to explicitly specify the participant you want to use in your prompt.
Note
Automatic inference for chat participants is currently in public preview and is subject to change.
Alternatively, you can manually specify a chat participant to scope your prompt to a specific domain. To do this, type
@
in the chat prompt box, followed by a chat participant name.
For a list of available chat participants, type
@
in the chat prompt box. See also
GitHub Copilot Chat cheat sheet
or
Chat participants
in the Visual Studio Code documentation.
Slash commands
Use slash commands to avoid writing complex prompts for common scenarios. To use a slash command, type
/
in the chat prompt box, followed by a command.
To see all available slash commands, type
/
in the chat prompt box. See also
GitHub Copilot Chat cheat sheet
or
Slash commands
in the Visual Studio Code documentation.
Chat variables
Use chat variables to include specific context in your prompt. To use a chat variable, type
#
in the chat prompt box, followed by a chat variable.
To see all available chat variables, type
#
in the chat prompt box. See also
GitHub Copilot Chat cheat sheet
or
Chat variables
in the Visual Studio Code documentation.
Using GitHub skills for Copilot
Copilot's GitHub-specific skills expand the type of information Copilot can provide. To access these skills in Copilot Chat, include
@github
in your question.
When you add
@github
to a question, Copilot dynamically selects an appropriate skill, based on the content of your question. You can also explicitly ask Copilot Chat to use a particular skill. You can do this in two ways:
Use natural language to ask Copilot Chat to use a skill. For example,
@github Search the web to find the latest GPT model from OpenAI.
To specifically invoke a web search you can include the
#web
variable in your question. For example,
@github #web What is the latest LTS of Node.js?
You can generate a list of currently available skills by asking Copilot:
@github What skills are available?
Using Model Context Protocol (MCP) servers
You can use MCP to extend the capabilities of Copilot Chat by integrating it with a wide range of existing tools and services. For additional information, see
About Model Context Protocol (MCP)
.
AI models for Copilot Chat
You can change the model Copilot uses to generate responses to chat prompts. You may find that different models perform better, or provide more useful responses, depending on the type of questions you ask. Options include premium models with advanced capabilities.  See
Changing the AI model for GitHub Copilot Chat
.
Additional ways to access Copilot Chat
In addition to submitting prompts through the chat view, you can submit prompts in other ways:
Quick chat:
To open the quick chat dropdown, enter
⇧
+
⌥
+
⌘
+
L
(Mac) /
Ctrl
+
Shift
+
Alt
+
L
(Windows/Linux).
Inline:
To start an inline chat directly in the editor or integrated terminal, enter
Command
+
i
(Mac) /
Ctrl
+
i
(Windows/Linux).
Smart actions:
To submit prompts via the context menu, right click in your editor, select
Copilot
in the menu that appears, then select one of the actions. Smart actions can also be accessed via the sparkle icon that sometimes appears when you select a line of code.
See
inline chat
,
quick chat
, and
chat smart actions
in the Visual Studio Code documentation for more details.
Copilot Chat chat modes
You can use Copilot Chat in the following modes:
Ask mode
: to get answers to coding questions and get Copilot to provide code suggestions.
Edit mode
: to get Copilot to make controlled edits to multiple files.
Agent mode
: to get Copilot to autonomously accomplish a set task.
Plan mode
: to get Copilot to create detailed implementation plans to ensure all requirements are met.
To switch between modes, use the agents dropdown at the bottom of the chat view.
Ask mode
Ask mode is optimized for answering questions about your codebase, coding, and general technology concepts. Use ask mode when you want to understand how something works, explore ideas, or get help with coding tasks. For larger changes across multiple files or more complex coding tasks, consider using edit mode or agent mode.
Using ask mode
If the chat view is not already displayed, select
Open Chat
from the Copilot Chat menu.
At the bottom of the chat view, select
Ask
from the agents dropdown.
Type a prompt in the prompt box and press
Enter
.
Edit mode
Edit mode is only available in Visual Studio Code and JetBrains IDEs.
Use edit mode when you want more granular control over the edits that Copilot proposes. In edit mode, you choose which files Copilot can make changes to, provide context to Copilot with each iteration, and decide whether or not to accept the suggested edits after each turn.
Edit mode is best suited to use cases where:
You want to make a quick, specific update to a defined set of files.
You want full control over the number of LLM requests Copilot uses.
Using edit mode
If the chat view is not already displayed, select
Open Chat
from the Copilot Chat menu.
At the bottom of the chat view, select
Edit
from the agents dropdown.
Optionally, add relevant files to the
working set
to indicate to GitHub Copilot which files you want to work on.
Submit a prompt. In response to your prompt, Copilot Edits determines which files in your
working set
to change and adds a short description of the change.
Review the changes and
Apply
or
Discard
the edits for each file.
For more detailed instructions, see
Copilot Edits
in the Visual Studio Code documentation.
Agent mode
Use agent mode when you have a specific task in mind and want to enable Copilot to autonomously edit your code. In agent mode, Copilot determines which files to make changes to, offers code changes and terminal commands to complete the task, and iterates to remediate issues until the original task is complete.
Agent mode is best suited to use cases where:
Your task is complex, and involves multiple steps, iterations, and error handling.
You want Copilot to determine the necessary steps to take to complete the task.
The task requires Copilot to integrate with external applications, such as an MCP server.
Using agent mode
If the chat view is not already displayed, select
Open Chat
from the Copilot Chat menu.
At the bottom of the chat view, select
Agent
from the agents dropdown.
Submit a prompt. In response to your prompt, Copilot streams the edits in the editor, updates the working set, and if necessary, suggests terminal commands to run.
Review the changes. If Copilot suggested terminal commands, confirm whether or not Copilot can run them. In response, Copilot iterates and performs additional actions to complete the task in your original prompt.
You can also directly
open agent mode in VS Code
.
For more information, see
Copilot Edits
in the Visual Studio Code documentation.
When you use Copilot agent mode, each prompt you enter counts as one premium request, multiplied by the model’s multiplier. For example, if you're using the included model—which has a multiplier of 0—your prompts won’t consume any premium requests. Copilot may take several follow-up actions to complete your task, but these follow-up actions do
not
count toward your premium request usage. Only the prompts you enter are billed—tool calls or background steps taken by the agent are not charged.
The total number of premium requests you use depends on how many prompts you enter and which model you select. See
Requests in GitHub Copilot
.
Plan mode
Note
Plan mode in VS Code is currently in public preview and subject to change.
Plan mode helps you to create detailed implementation plans before executing them. This ensures that all requirements are considered and addressed before any code changes are made. The plan agent does not make any code changes until the plan is reviewed and approved by you. Once approved, you can hand off the plan to the default agent or save it for further refinement, review, or team discussions.
The plan agent is designed to:
Research the task comprehensively using read-only tools and codebase analysis to identify requirements and constraints.
Break down the task into manageable, actionable steps and include open questions about ambiguous requirements.
Present a concise plan draft, based on a standardized plan format, for user review and iteration.
Using plan mode
If the chat view is not already displayed, select
Open Chat
from the Copilot Chat menu.
At the bottom of the chat view, select
Plan
from the agents dropdown.
Enter a task for which you want to create a plan, then press
Enter
.
The plan agent provides a high-level summary and a breakdown of steps, including any open questions for clarification.
Review the plan and answer any questions the agent has asked.
You can iterate multiple times to clarify requirements, adjust scope, or answer questions.
Once the plan is finalized, choose to save it or hand it off to an implementation agent to start coding, by using the corresponding controls.
For more information, see
Planning in VS Code chat
in the Visual Studio Code documentation.
Using images in Copilot Chat
Note
If you're using a Copilot Business or Copilot Enterprise plan, the organization or enterprise that provides your plan must enable the
Editor preview features
setting. See
Managing policies and features for GitHub Copilot in your organization
or
Managing policies and features for GitHub Copilot in your enterprise
.
You can attach images to your chat prompts and then ask Copilot about the images. For example, you can attach:
A screenshot of a code snippet and ask Copilot to explain the code.
A mockup of the user interface for an application and ask Copilot to generate the code.
A flowchart and ask Copilot to describe the processes shown in the image.
A screenshot of a web page and ask Copilot to generate HTML for a similar page.
Note
The following types of image file are supported: JPEG (
.jpg
,
.jpeg
), PNG (
.png
), GIF (
.gif
), or WEBP (
.webp
).
Attaching images to your chat prompt
If you see the AI model picker at the bottom right of the chat view, select one of the models that supports adding images to prompts:
Do one of the following:
Copy an image and paste it into the chat view.
Drag and drop one or more image file from your operating system's file explorer—or from the Explorer in VS Code—into the chat view.
Right-click an image file in the VS Code Explorer and click
Copilot
then
Add File to Chat
.
Type your prompt into the chat view to accompany the image. For example,
explain this diagram
,
describe each of these images in detail
,
what does this error message mean
.
Sharing feedback
To indicate whether a response was helpful, use the thumbs up and thumbs down icons that appear next to the response.
To leave feedback about the GitHub Copilot Chat extension, open an issue in the
microsoft/vscode-copilot-release
repository.
Further reading
Prompt engineering for GitHub Copilot Chat
Using Copilot Chat in VS Code
and
Getting started with GitHub Copilot Chat in VS Code
in the Visual Studio Code documentation
Asking GitHub Copilot questions in GitHub
Responsible use of GitHub Copilot Chat in your IDE
GitHub Terms for Additional Products and Features
GitHub Copilot Trust Center
GitHub Copilot FAQ
Prerequisites
Access to GitHub Copilot
. See
What is GitHub Copilot?
.
Visual Studio 2022 version 17.8 or later
. See
Install Visual Studio
in the Visual Studio documentation.
For Visual Studio 17.8 and 17.9:
GitHub Copilot extension
. See
Install GitHub Copilot in Visual Studio
in the Visual Studio documentation.
GitHub Copilot Chat extension
. See
Install GitHub Copilot in Visual Studio
in the Visual Studio documentation.
Visual Studio 17.10 and later have the GitHub Copilot and GitHub Copilot Chat extensions built in. You don't need to install them separately.
Sign in to GitHub in Visual Studio
. If you experience authentication issues, see
Troubleshooting common issues with GitHub Copilot
.
If you have access to GitHub Copilot via your organization, you won't be able to use GitHub Copilot Chat if your organization owner has disabled chat. See
Managing policies and features for GitHub Copilot in your organization
.
Submitting prompts
You can ask Copilot Chat to give you code suggestions, explain code, generate unit tests, and suggest code fixes.
In the Visual Studio menu bar, click
View
, then click
GitHub Copilot Chat
.
In the Copilot Chat window, enter a prompt, then press
Enter
. For example prompts, see
Getting started with prompts for GitHub Copilot Chat
.
Evaluate Copilot's response, and submit a follow up prompt if needed.
The response often includes interactive elements. For example, the response may include buttons to copy, insert, or preview the result of a code block.
To see the files that Copilot Chat used to generate the response, click the
References
link below the response. The references may include a link to a custom instructions file for your repository. This file contains additional information that is automatically added to all of your chat questions to improve the quality of the responses. For more information, see
Adding repository custom instructions for GitHub Copilot
.
Using keywords in your prompt
You can use special keywords to help Copilot understand your prompt.
Slash commands
Use slash commands to avoid writing complex prompts for common scenarios. To use a slash command, type
/
in the chat prompt box, followed by a command.
To see all available slash commands, type
/
in the chat prompt box. See also
GitHub Copilot Chat cheat sheet
or
Slash commands
in the Visual Studio documentation.
References
By default, Copilot Chat will reference the file that you have open or the code that you have selected. You can also use
#
followed by a file name, file name and line numbers, or
solution
to reference a specific file, lines, or solution.
See also
GitHub Copilot Chat cheat sheet
or
Reference
in the Visual Studio documentation.
Using GitHub skills for Copilot (preview)
Note
The
@github
chat participant is currently in preview, and only available in
Visual Studio 2022 Preview 2
onwards.
Copilot's GitHub-specific skills expand the type of information Copilot can provide. To access these skills in Copilot Chat in Visual Studio, include
@github
in your question.
When you add
@github
to a question, Copilot dynamically selects an appropriate skill, based on the content of your question. You can also explicitly ask Copilot Chat to use a particular skill. For example,
@github Search the web to find the latest GPT4 model from OpenAI.
You can generate a list of currently available skills by asking Copilot:
@github What skills are available?
Using Model Context Protocol (MCP) servers
You can use MCP to extend the capabilities of Copilot Chat by integrating it with a wide range of existing tools and services. For additional information, see
About Model Context Protocol (MCP)
.
AI models for Copilot Chat
You can change the model Copilot uses to generate responses to chat prompts. You may find that different models perform better, or provide more useful responses, depending on the type of questions you ask. Options include premium models with advanced capabilities.  See
Changing the AI model for GitHub Copilot Chat
.
Additional ways to access Copilot Chat
In addition to submitting prompts through the chat window, you can submit prompts inline. To start an inline chat, right click in your editor window and select
Ask Copilot
.
See
Ask questions in the inline chat view
in the Visual Studio documentation for more details.
Copilot Edits
Note
This feature is currently in public preview and subject to change.
Available in Visual Studio 17.14 and later.
Copilot Edits lets you make changes across multiple files from a single Copilot Chat prompt
Use agent mode when you have a specific task in mind and want to enable Copilot to autonomously edit your code. In agent mode, Copilot determines which files to make changes to, offers code changes and terminal commands to complete the task, and iterates to remediate issues until the original task is complete.
Using agent mode
In the Visual Studio menu bar, click
View
, then click
GitHub Copilot Chat
.
At the bottom of the chat panel, select
Agent
from the agents dropdown.
Submit a prompt. In response to your prompt, Copilot streams the edits in the editor, updates the working set, and if necessary, suggests terminal commands to run.
Review the changes. If Copilot suggested terminal commands, confirm whether or not Copilot can run them. In response, Copilot iterates and performs additional actions to complete the task in your original prompt.
When you use Copilot agent mode, each prompt you enter counts as one premium request, multiplied by the model’s multiplier. For example, if you're using the included model—which has a multiplier of 0—your prompts won’t consume any premium requests. Copilot may take several follow-up actions to complete your task, but these follow-up actions do
not
count toward your premium request usage. Only the prompts you enter are billed—tool calls or background steps taken by the agent are not charged.
Using images in Copilot Chat
Note
If you're using a Copilot Business or Copilot Enterprise plan, the organization or enterprise that provides your plan must enable the
Editor preview features
setting. See
Managing policies and features for GitHub Copilot in your organization
or
Managing policies and features for GitHub Copilot in your enterprise
.
You can attach images to your chat prompts and then ask Copilot about the images. For example, you can attach:
A screenshot of a code snippet and ask Copilot to explain the code.
A mockup of the user interface for an application and ask Copilot to generate the code.
A flowchart and ask Copilot to describe the processes shown in the image.
A screenshot of a web page and ask Copilot to generate HTML for a similar page.
Note
The following types of image file are supported: JPEG (
.jpg
,
.jpeg
), PNG (
.png
), GIF (
.gif
), or WEBP (
.webp
).
Attaching images to your chat prompt
If you see the AI model picker at the bottom right of the chat view, select one of the models that supports adding images to prompts:
Do one of the following:
Copy an image and paste it into the chat view.
Click the paperclip icon at the bottom right of the chat view, click
Upload Image
, browse to the image file you want to attach, select it and click
Open
.
You can add multiple images if required.
Type your prompt into the chat view to accompany the image. For example,
explain this image
, or
describe each of these images in detail
.
Sharing feedback
To share feedback about Copilot Chat, you can use the
Send feedback
button in Visual Studio. For more information on providing feedback for Visual Studio, see the
Visual Studio Feedback
documentation.
In the top right corner of the Visual Studio window, click the
Send feedback
button.
Choose the option that best describes your feedback.
To report a bug, click
Report a problem
.
To request a feature, click
Suggest a feature
.
Further reading
Prompt engineering for GitHub Copilot Chat
Using GitHub Copilot Chat in Visual Studio in the Microsoft Learn documentation
Tips to improve GitHub Copilot Chat results in the Microsoft Learn documentation
Asking GitHub Copilot questions in GitHub
Responsible use of GitHub Copilot Chat in your IDE
GitHub Terms for Additional Products and Features
GitHub Copilot Trust Center
GitHub Copilot FAQ
Prerequisites
Access to GitHub Copilot
. See
What is GitHub Copilot?
.
Compatible JetBrains IDE
. GitHub Copilot is compatible with the following IDEs:
IntelliJ IDEA (Ultimate, Community, Educational)
Android Studio
AppCode
CLion
Code With Me Guest
DataGrip
DataSpell
GoLand
JetBrains Client
MPS
PhpStorm
PyCharm (Professional, Community, Educational)
Rider
RubyMine
RustRover
WebStorm
Writerside
See the
JetBrains IDEs
tool finder to download.
Latest version of the GitHub Copilot extension
. See the
GitHub Copilot plugin
in the JetBrains Marketplace. For installation instructions, see
Installing the GitHub Copilot extension in your environment
.
Sign in to GitHub in your JetBrains IDE
. For authentication instructions, see
Installing the GitHub Copilot extension in your environment
.
If you have access to GitHub Copilot via your organization, you won't be able to use GitHub Copilot Chat if your organization owner has disabled chat. See
Managing policies and features for GitHub Copilot in your organization
.
Submitting prompts
You can ask Copilot Chat to give you code suggestions, explain code, generate unit tests, and suggest code fixes.
Open the Copilot Chat window by clicking the
GitHub Copilot Chat
icon at the right side of the JetBrains IDE window.
Enter a prompt in the prompt box. For example prompts, see
Getting started with prompts for GitHub Copilot Chat
.
Evaluate Copilot's response, and submit a follow up prompt if needed.
The response often includes interactive elements. For example, the response may include buttons to copy or insert a code block.
To see the files that Copilot Chat used to generate the response, click the
References
link below the response. The references may include a link to a custom instructions file for your repository. This file contains additional information that is automatically added to all of your chat questions to improve the quality of the responses. For more information, see
Adding repository custom instructions for GitHub Copilot
.
Using keywords in your prompt
You can use special keywords to help Copilot understand your prompt.
Chat participants
Chat participants are like domain experts who have a specialty that they can help you with. You can use a chat participant to scope your prompt to a specific domain. To do this, type
@
in the chat prompt box, followed by a chat participant name.
For a list of available chat participants, type
@
in the chat prompt box. See also
GitHub Copilot Chat cheat sheet
.
Extending Copilot Chat
GitHub Copilot Extensions integrate the power of external tools into Copilot Chat, helping you reduce context switching and receive responses with domain-specific context. You can install Copilot Extensions from the GitHub Marketplace or build private ones within your organization, then type
@
in a chat window to see a list of your available extensions. To use an extension, select the extension from the list or type the full slug name, then type your prompt.
Slash commands
Use slash commands to avoid writing complex prompts for common scenarios. To use a slash command, type
/
in the chat prompt box, followed by a command.
To see all available slash commands, type
/
in the chat prompt box. See also
GitHub Copilot Chat cheat sheet
.
File references
By default, Copilot Chat will reference the file that you have open or the code that you have selected. You can also tell Copilot Chat which files to reference by dragging a file into the chat prompt box. Alternatively, you can right click on a file, select
GitHub Copilot
, then select
Reference File in Chat
.
Using GitHub skills for Copilot
Copilot's GitHub-specific skills expand the type of information Copilot can provide. To access these skills in Copilot Chat, include
@github
in your question.
When you add
@github
to a question, Copilot dynamically selects an appropriate skill, based on the content of your question. You can also explicitly ask Copilot Chat to use a particular skill. You can do this in two ways:
Use natural language to ask Copilot Chat to use a skill. For example,
@github Search the web to find the latest GPT model from OpenAI.
To specifically invoke a web search you can include the
#web
variable in your question. For example,
@github #web What is the latest LTS of Node.js?
You can generate a list of currently available skills by asking Copilot:
@github What skills are available?
Using Model Context Protocol (MCP) servers
You can use MCP to extend the capabilities of Copilot Chat by integrating it with a wide range of existing tools and services. For additional information, see
About Model Context Protocol (MCP)
.
AI models for Copilot Chat
You can change the model Copilot uses to generate responses to chat prompts. You may find that different models perform better, or provide more useful responses, depending on the type of questions you ask. Options include premium models with advanced capabilities.  See
Changing the AI model for GitHub Copilot Chat
.
Additional ways to access Copilot Chat
Built-in requests
. In addition to submitting prompts through the chat window, you can submit built-in requests by right clicking in a file, selecting
GitHub Copilot
, then selecting one of the options.
Inline
. You can submit a chat prompt inline, and scope it to a highlighted code block or your current file.
To start an inline chat, right click on a code block or anywhere in your current file, hover over
GitHub Copilot
, then select
Copilot: Inline Chat
, or enter
Ctrl
+
Shift
+
I
.
Copilot Edits
Use Copilot Edits to make changes across multiple files directly from a single Copilot Chat prompt. Copilot Edits has the following modes:
Edit mode
lets Copilot make controlled edits to multiple files.
Agent mode
lets Copilot autonomously accomplish a set task.
Edit mode
Edit mode is only available in Visual Studio Code and JetBrains IDEs.
Use edit mode when you want more granular control over the edits that Copilot proposes. In edit mode, you choose which files Copilot can make changes to, provide context to Copilot with each iteration, and decide whether or not to accept the suggested edits after each turn.
Edit mode is best suited to use cases where:
You want to make a quick, specific update to a defined set of files.
You want full control over the number of LLM requests Copilot uses.
Using edit mode
To start an edit session, click
Copilot
in the menu bar, then select
Open GitHub Copilot Chat
.
At the top of the chat panel, click
Copilot Edits
.
Add relevant files to the
working set
to indicate to GitHub Copilot which files you want to work on. You can add all open files by clicking
Add all open files
or individually search for single files.
Submit a prompt. In response to your prompt, Copilot Edits determines which files in your
working set
to change and adds a short description of the change.
Review the changes and
Accept
or
Discard
the edits for each file.
Agent mode
Use agent mode when you have a specific task in mind and want to enable Copilot to autonomously edit your code. In agent mode, Copilot determines which files to make changes to, offers code changes and terminal commands to complete the task, and iterates to remediate issues until the original task is complete.
Agent mode is best suited to use cases where:
Your task is complex, and involves multiple steps, iterations, and error handling.
You want Copilot to determine the necessary steps to take to complete the task.
The task requires Copilot to integrate with external applications, such as an MCP server.
Using agent mode
To start an edit session using agent mode, click
Copilot
in the menu bar, then select
Open GitHub Copilot Chat
.
At the top of the chat panel, click the
Agent
tab.
Submit a prompt. In response to your prompt, Copilot streams the edits in the editor, updates the working set, and if necessary, suggests terminal commands to run.
Review the changes. If Copilot suggested terminal commands, confirm whether or not Copilot can run them. In response, Copilot iterates and performs additional actions to complete the task in your original prompt.
When you use Copilot agent mode, each prompt you enter counts as one premium request, multiplied by the model’s multiplier. For example, if you're using the included model—which has a multiplier of 0—your prompts won’t consume any premium requests. Copilot may take several follow-up actions to complete your task, but these follow-up actions do
not
count toward your premium request usage. Only the prompts you enter are billed—tool calls or background steps taken by the agent are not charged.
The total number of premium requests you use depends on how many prompts you enter and which model you select. See
Requests in GitHub Copilot
.
Sharing feedback
To share feedback about Copilot Chat, you can use the
share feedback
link in JetBrains.
At the right side of the JetBrains IDE window, click the
Copilot Chat
icon to open the Copilot Chat window.
At the top of the Copilot Chat window, click the
share feedback
link.
Further reading
Prompt engineering for GitHub Copilot Chat
Asking GitHub Copilot questions in GitHub
Responsible use of GitHub Copilot Chat in your IDE
GitHub Pre-release License Terms
GitHub Terms for Additional Products and Features
GitHub Copilot Trust Center
GitHub Copilot FAQ
Prerequisites
Access to GitHub Copilot
. See
What is GitHub Copilot?
.
Latest version of the GitHub Copilot extension
. For installation instructions, see
Installing the GitHub Copilot extension in your environment
.
Sign in to GitHub in Xcode
. If you experience authentication issues, see
Troubleshooting common issues with GitHub Copilot
.
If you have access to GitHub Copilot via your organization, you won't be able to use GitHub Copilot Chat if your organization owner has disabled chat. See
Managing policies and features for GitHub Copilot in your organization
.
Submitting prompts
You can ask Copilot Chat to give you code suggestions, explain code, generate unit tests, and suggest code fixes.
To open the chat view, click
Editor
in the menu bar, then click
GitHub Copilot
then
Open Chat
. Copilot Chat opens in a new window.
Enter a prompt in the prompt box. For example prompts, see
Getting started with prompts for GitHub Copilot Chat
.
Evaluate Copilot's response, and submit a follow up prompt if needed.
The response often includes interactive elements. For example, the response may include buttons to copy or insert a code block.
To see the files that Copilot Chat used to generate the response, click the
References
link below the response. The references may include a link to a custom instructions file for your repository. This file contains additional information that is automatically added to all of your chat questions to improve the quality of the responses. For more information, see
Adding repository custom instructions for GitHub Copilot
.
Using Model Context Protocol (MCP) servers
You can use MCP to extend the capabilities of Copilot Chat by integrating it with a wide range of existing tools and services. For additional information, see
About Model Context Protocol (MCP)
.
AI models for Copilot Chat
You can change the model Copilot uses to generate responses to chat prompts. You may find that different models perform better, or provide more useful responses, depending on the type of questions you ask. Options include premium models with advanced capabilities.  See
Changing the AI model for GitHub Copilot Chat
.
Using keywords in your prompt
You can use special keywords to help Copilot understand your prompt.
Slash commands
Use slash commands to avoid writing complex prompts for common scenarios. To use a slash command, type
/
in the chat prompt box, followed by a command.
To see all available slash commands, type
/
in the chat prompt box. For more information, see
GitHub Copilot Chat cheat sheet
.
Copilot agent mode
Use agent mode when you have a specific task in mind and want to enable Copilot to autonomously edit your code. In agent mode, Copilot determines which files to make changes to, offers code changes and terminal commands to complete the task, and iterates to remediate issues until the original task is complete.
Agent mode is best suited to use cases where:
Your task is complex, and involves multiple steps, iterations, and error handling.
You want Copilot to determine the necessary steps to take to complete the task.
The task requires Copilot to integrate with external applications, such as an MCP server.
Using agent mode
To open the chat view, click
Copilot
in the menu bar, then click
Open Chat
.
At the bottom of the chat panel, select
Agent
from the agents dropdown.
Optionally, add relevant files to the
working set
view to indicate to Copilot which files you want to work on.
Submit a prompt. In response to your prompt, Copilot streams the edits in the editor, updates the working set, and if necessary, suggests terminal commands to run.
Review the changes. If Copilot suggested terminal commands, confirm whether or not Copilot can run them. In response, Copilot iterates and performs additional actions to complete the task in your original prompt.
When you use Copilot agent mode, each prompt you enter counts as one premium request, multiplied by the model’s multiplier. For example, if you're using the included model—which has a multiplier of 0—your prompts won’t consume any premium requests. Copilot may take several follow-up actions to complete your task, but these follow-up actions do
not
count toward your premium request usage. Only the prompts you enter are billed—tool calls or background steps taken by the agent are not charged.
The total number of premium requests you use depends on how many prompts you enter and which model you select. See
Requests in GitHub Copilot
.
File references
By default, Copilot Chat will reference the file that you have open or the code that you have selected. To attach a specific file as reference, click
in the chat prompt box.
Chat management
You can open a conversation thread for each Xcode IDE to keep discussions organized across different contexts. You can also revisit previous conversations and reference past suggestions through the chat history.
Sharing feedback
To indicate whether a response was helpful, use
or
that appear next to the response.
Further reading
Prompt engineering for GitHub Copilot Chat
Asking GitHub Copilot questions in GitHub
Responsible use of GitHub Copilot Chat in your IDE
GitHub Pre-release License Terms
GitHub Terms for Additional Products and Features
GitHub Copilot Trust Center
GitHub Copilot FAQ
Prerequisites
Access to Copilot
. See
What is GitHub Copilot?
.
Compatible version of Eclipse
. To use the GitHub Copilot extension, you must have Eclipse version 2024-09 or above. See the
Eclipse download page
.
If you are a member of an organization or enterprise with a Copilot Business or Copilot Enterprise plan, the "MCP servers in Copilot" policy must be enabled in order to use MCP with Copilot.
Latest version of the GitHub Copilot extension
. Download this from the
Eclipse Marketplace
. For more information, see
Installing the GitHub Copilot extension in your environment
.
Sign in to GitHub in Eclipse
. If you experience authentication issues, see
Troubleshooting common issues with GitHub Copilot
.
If you have access to GitHub Copilot via your organization, you won't be able to use GitHub Copilot Chat if your organization owner has disabled chat. See
Managing policies and features for GitHub Copilot in your organization
.
Submitting prompts
You can ask Copilot Chat to give you code suggestions, explain code, generate unit tests, and suggest code fixes.
To open the Copilot Chat panel, click the Copilot icon (
) in the status bar at the bottom of Eclipse, then click
Open Chat
.
Enter a prompt in the prompt box, then press
Enter
.
For an introduction to the kinds of prompts you can use, see
Getting started with prompts for GitHub Copilot Chat
.
Evaluate Copilot's response, and make a follow up request if needed.
Using keywords in your prompt
You can use special keywords to help Copilot understand your prompt. For examples, see
Getting started with prompts for GitHub Copilot Chat
.
Slash commands
Use slash commands to avoid writing complex prompts for common scenarios. To use a slash command, type
/
in the chat prompt box, followed by a command. For example, use
/explain
to ask Copilot to explain the code in the file currently displayed in the editor.
To see all available slash commands, type
/
in the chat prompt box.
Using Model Context Protocol (MCP) servers
You can use MCP to extend the capabilities of Copilot Chat by integrating it with a wide range of existing tools and services. For additional information, see
About Model Context Protocol (MCP)
.
AI models for Copilot Chat
You can change the model Copilot uses to generate responses to chat prompts. You may find that different models perform better, or provide more useful responses, depending on the type of questions you ask. Options include premium models with advanced capabilities.  See
Changing the AI model for GitHub Copilot Chat
.
Copilot agent mode
Use agent mode when you have a specific task in mind and want to enable Copilot to autonomously edit your code. In agent mode, Copilot determines which files to make changes to, offers code changes and terminal commands to complete the task, and iterates to remediate issues until the original task is complete.
Agent mode is best suited to use cases where:
Your task is complex, and involves multiple steps, iterations, and error handling.
You want Copilot to determine the necessary steps to take to complete the task.
The task requires Copilot to integrate with external applications, such as an MCP server.
Using agent mode
To open the Copilot Chat panel, click the Copilot icon (
) in the status bar at the bottom of Eclipse, then click
Open Chat
.
At the bottom of the chat panel, select
Agent
from the agents dropdown.
Submit a prompt. In response to your prompt, Copilot streams the edits in the editor, updates the working set, and if necessary, suggests terminal commands to run.
Review the changes. If Copilot suggested terminal commands, confirm whether or not Copilot can run them. In response, Copilot iterates and performs additional actions to complete the task in your original prompt.
When you use Copilot agent mode, each prompt you enter counts as one premium request, multiplied by the model’s multiplier. For example, if you're using the included model—which has a multiplier of 0—your prompts won’t consume any premium requests. Copilot may take several follow-up actions to complete your task, but these follow-up actions do
not
count toward your premium request usage. Only the prompts you enter are billed—tool calls or background steps taken by the agent are not charged.
The total number of premium requests you use depends on how many prompts you enter and which model you select. See
Requests in GitHub Copilot
.
Further reading
Prompt engineering for GitHub Copilot Chat
Asking GitHub Copilot questions in GitHub
Responsible use of GitHub Copilot Chat in your IDE
GitHub Terms for Additional Products and Features
GitHub Copilot Trust Center
GitHub Copilot FAQ