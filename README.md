# Zero to Agent 🤖
### Building an AI Game Studio from Scratch — Publicly, in Real Time

> *One person. No CS degree. No prior agent experience.*
> *This is the unfiltered journey of learning to build AI agent systems by actually building one.*
> *Every error. Every fix. Every "wait, that's not really an agent" moment. All of it.*

---

## What This Is

This repository documents a real learning experiment: building a **multi-agent AI system capable of designing and creating a PC game** — from concept to playable — using Python and the Claude API.

Every module is a real session. Every mistake is committed to history.
This is not a tutorial written in hindsight by someone who already knew the answers.
**This is the answers being found in real time.**

---

## The Goal

Build a network of specialized AI agents that work together as a game studio:

| Agent | Role |
|---|---|
| 🎮 Game Designer | Concepts, mechanics, design documents |
| 💻 Coder | Writes and debugs actual game code |
| 🎨 Artist | Generates sprites, backgrounds, UI |
| 🔊 Audio | Sound effects and music |
| 🧪 QA | Tests logic, finds bugs |
| 🎬 Orchestrator | Manages the whole crew |

Final goal: describe a game idea in plain English → the agent network designs, codes, and illustrates it.

---

## The Journey

### ✅ Module 1 — What is an Agent? + Building the First One
**Status: Complete — May 18, 2026**

---

#### How it actually started

Before writing a single line of code, the first 40 minutes were spent on chaos management.

Turns out, before you can build anything, you need to know what accounts you already have, which emails they're on, and whether you accidentally created duplicates. Two ChatGPT accounts on different emails. A GitHub account that existed but was forgotten. $8 of OpenAI credits somewhere in the void.

The first real lesson wasn't about agents. It was:

> *"I have bad experience with this. I think I have multiple API keys with ChatGPT and somewhere I also have a GitHub account but no idea what and registered to which email address, which I have several of."*

So before any code: a project dashboard was built. One place tracking every account, every key, every tool. It sounds boring. It saved the project from collapsing on day one.

---

#### The prerequisites nobody mentions

Everyone's tutorials start with "install Python." Here's what they don't list:

- Python ✅ (already installed — version 3.12)
- VS Code — had to install it
- Git — **nobody mentioned this one**

The git omission hit at the exact moment it mattered most:

```
PS> git init
git : The term 'git' is not recognized as the name of a cmdlet,
function, script file, or operable program.
```

> *"Who would have thought that I need Git installed also... if only I had a powerful AI to tell me I need it."*

Noted. Git is now on the prerequisites list for anyone following along.

---

#### The first agent — and why it wasn't really one

First version of `agent.py` was a loop that sent messages to Claude with a system prompt and printed the replies. It worked. It responded. It remembered the conversation.

It was also immediately called out:

> *"OK to be honest this feels just like a chat through API, not an agent. I have done this before — let's move on so it would feel more like an agent system."*

Correct. A chatbot with a system prompt is not an agent.

**The real difference:** an agent has tools. It can take actions. It can change things outside the conversation. A chatbot talks. An agent does.

The code was rewritten. The agent was given one tool: `save_game_design()`. Now instead of just describing a game, it could write a file to disk. More importantly — it decided **when** to do it. No prompt like "now save the file." The agent determined the design was complete and called the tool on its own.

That inner decision loop — running autonomously until the task is done — is the core of what makes something an agent:

```python
while True:
    response = client.messages.create(...)

    if response.stop_reason == "tool_use":
        # agent decided to act — execute the tool, feed result back
        ...
    else:
        # agent decided it's done
        break
```

Even then, a fair question came up mid-run while watching it work:

> *"One AI is doing things... is that really an agent?"*

Yes — and that question cuts to the heart of it. The agent has a goal, not just a prompt. It decides when to act. It produces real-world effects — a file appears on disk. And it runs its own loop without a human triggering each step. That's agency. Minimal, but real.

---

#### The crashes, in order

**Crash 1 — Wrong model string**
```
anthropic.NotFoundError: Error code: 404
{'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}}
```
The model name in the code was outdated. This led to a real observation about AI and stale training data:

> *"As I told you in the beginning, I have learned over the year working with AIs — they rely as a first instinct on their training material, which might be 2-3 years old. They never check what is up to date at the moment and they never question whether their training material is still relevant."*

Correct. The right model string is `claude-sonnet-4-6`. Always verify version-sensitive details against current documentation — not against what the AI confidently tells you.

**Crash 2 — Windows commands**
```
echo. : The term 'echo.' is not recognized as the name of a cmdlet
```
The instructions used Mac/Linux shell commands. Windows PowerShell is different.
`echo. > .env` becomes `New-Item .env`. Simple fix. Annoying to hit.

**Crash 3 — Windows file encoding**
```
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f3ed'
```
The agent generated a design document with emojis. Windows default file encoding (`cp1252`) can't handle them. Fix was one parameter:

```python
open(filename, 'w', encoding='utf-8')
```

One word. Forty minutes of confusion if you don't know where to look.

**Crash 4 — The API key in git history**

This one is a rite of passage.

`.env` was committed before `.gitignore` was properly set up. The push to GitHub was blocked:

```
remote: - GITHUB PUSH PROTECTION
remote:   Push cannot contain secrets
remote:   —— Anthropic API Key ————————————————
remote:     locations:
remote:       - commit: c88d8121691dd0ba3a72eefe18deab3513d0a27b
remote:         path: .env:1
```

GitHub's secret scanner caught it before it went public. The API key was immediately rotated on console.anthropic.com. The repo was deleted and recreated clean.

**The rule:** when an API key touches git history — even for one second — rotate it immediately. Don't think about it. Just rotate it.

---

#### The first real result

On the very first run of the working agent, it was given a vague prompt about an Estonian factory.

It produced **Krenholm: Rise of the Mill** — a historically grounded 2D construction management game set in 1857 Imperial Russia, based on the real construction of what became the largest textile factory in Europe. Three interlocking game loops. Full win/lose conditions. Art direction. Scope estimates. A historical hook that ties the game back to real Estonian history.

The agent designed all of it. Then saved it to disk. Without being asked.

[Read the full Krenholm design document →](krenholm_-_rise_of_the_mill_design.md)

---

#### What Module 1 actually taught

**Tool use is the line between chatbot and agent.**
The moment a model can call a function and receive a result back, behavior changes fundamentally. It stops being a conversation and starts being a system with agency.

**The agent loop is the core mechanic.**
Reason → Act → Observe → Reason again. That loop running autonomously — without a human triggering each step — is what all agentic systems are built on. Everything in later modules is this loop, made more complex.

**Conversation history is manual.**
There is no magic memory. Every message, tool call, and result gets appended to a list and sent with every request. The model appears to remember because you send it everything that happened. Understanding this is essential for understanding why agents behave the way they do — and why they sometimes don't.

**AI is confidently wrong about version-specific details.**
Model strings, library versions, OS-specific commands — these change faster than training data. Treat any version-specific output from an AI as a first draft that needs verification, not a final answer.

**The boring setup work is load-bearing.**
Account management, `.gitignore`, `.env` files, encoding parameters — none of it is interesting. All of it will end your session early if you skip it.

---

### 🔒 Module 2 — Giving Agents Multiple Tools
*Coming next — when an agent can choose between tools, behavior starts feeling genuinely autonomous*

### 🔒 Module 3 — Two Agents Talking
### 🔒 Module 4 — CrewAI: First Real Crew
### 🔒 Module 5 — Game Designer + Coder Agents
### 🔒 Module 6 — Art Agent (Image Generation)
### 🔒 Module 7 — Full Pipeline → Playable Game

---

## The Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Language |
| Claude Sonnet 4.6 | Agent brain (Anthropic API) |
| `anthropic` Python SDK | API client |
| `python-dotenv` | Secret management |
| VS Code + GitHub | Editor and version control |
| CrewAI *(coming)* | Multi-agent orchestration |
| Pygame *(coming)* | Game engine |

---

## Running the Code

```bash
# Clone the repo
git clone https://github.com/quietaidev-collab/zero-to-agent.git
cd zero-to-agent

# Install dependencies
pip install anthropic python-dotenv

# Create a .env file with your API key
# ANTHROPIC_API_KEY=your-key-here
# Get one at console.anthropic.com

# Run the Game Designer agent
python agent.py
```

Describe a game idea. Watch it design and save a document without being asked.

---

## About

Built in Tallinn, Estonia 🇪🇪
Started May 18, 2026

By someone who decided that not knowing how to do something was a reason to start, not a reason to wait.

---

*If Krenholm's workers could build the largest textile factory in Europe with hand tools and determination in 1857, building an AI game studio with Python in 2026 seems reasonable.*
