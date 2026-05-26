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

### ✅ Module 2 — Giving Agents Multiple Tools
**Status: Complete — May 19, 2026**

---

#### The upgrade

Module 1's agent had one tool and one job. The question going into Module 2 was simple: what happens when you give an agent three tools and let it decide which ones to use, in what order, and how many times?

The agent was given:

| Tool | Purpose |
|---|---|
| `search_similar_games` | Find reference games to ground the design in reality |
| `estimate_dev_time` | Calculate how long features would take a solo developer |
| `save_game_design` | Save the completed document to disk |

Same game idea as Module 1 — Krenholm 1857. Different agent. Watch what changed.

---

#### What the agent actually did

This is the real terminal output, unedited:

```
[Agent using tool: search_similar_games]
[Input: {"genre": "construction management simulation",
         "mechanics": "resource management, building placement, worker assignment, historical setting"}]
[Result: Similar successful indie games in this space: Prison Architect, RimWorld, Dwarf Fortress.]

Designer: Great references! Prison Architect especially is a strong 2D construction management anchor.
Now let me draft the core features and estimate development time — these are independent steps I can run together.

[Agent using tool: estimate_dev_time]
[Input: {"features": ["2D grid-based building placement", "Worker hiring and assignment",
         "Resource supply chain", "Imperial quota system", "Worker morale and unrest",
         "Procedural map", "Day/night cycle", "Historical event cards",
         "Financial ledger", "Inspector visits", "Tech tree upgrade system"],
         "team_size": 1}]
[Result: Estimated development time: 24-36 weeks for core prototype.
Note: as a solo dev, budget 3x this estimate for polish and bugs.]

Designer: 24–36 weeks for the core is workable, but 3x polish is a serious warning.
Let me trim scope smartly — dropping procedural maps and day/night cycle — and re-estimate the leaner version.

[Agent using tool: estimate_dev_time]
[Input: {"features": ["2D grid-based building placement", "Worker hiring and assignment",
         "Resource supply chain", "Imperial quota system", "Worker morale and unrest",
         "Narva River water power (fixed map)", "Historical event cards",
         "Financial ledger", "Core building types", "Inspector visits"],
         "team_size": 1}]
[Result: Estimated development time: 20-30 weeks for core prototype.
Note: as a solo dev, budget 3x this estimate for polish and bugs.]

Designer: Solid — 20–30 weeks for core is a realistic solo MVP. Now let me compile everything into the final design document and save it.

[Agent using tool: save_game_design]
```

The agent called `estimate_dev_time` **twice.**

Nobody told it to do that. It saw the first result (24-36 weeks), decided that was too heavy, cut two features on its own judgment — procedural maps and the day/night cycle — and ran the tool again to verify the trimmed scope was better. Only then did it write and save the final document.

That re-estimation moment is the entire point of Module 2. The agent didn't just use tools — it **iterated** based on what the tools told it. That's judgment, not execution.

---

#### What changed in the output

The Module 2 design document is visibly richer than Module 1's. Because the agent researched reference games first, Prison Architect's visual clarity appears explicitly in the art direction. Because it ran scope estimation before writing, the document includes a realistic 20-30 week development roadmap and a dedicated "Intentionally Cut Features" section — things the agent decided to remove to keep the project shippable.

It didn't just design a game. It designed a *buildable* game.

[Read the full Krenholm 1857 design document →](krenholm_1857_design.md)

---

#### Also: PowerShell doesn't use &&

```
At line:1 char:11
+ git add . && git commit -m "Module 2 complete..."
+           ~~
The token '&&' is not a valid statement separator in this version.
```

On Windows PowerShell, run git commands one at a time. `&&` is a Linux/Mac thing. Every tutorial on the internet forgets this. Now you know.

---

#### What Module 2 actually taught

**Tool order is a decision, not an instruction.**
The agent searched for references before designing, estimated time before finalizing, and iterated when the first estimate was too high. Nobody specified that sequence. It reasoned its way to it from the tool descriptions alone. Writing good tool descriptions is therefore one of the most important skills in agent design.

**Agents iterate, not just execute.**
The double `estimate_dev_time` call is the clearest example yet of genuine agentic behavior. The agent observed a result, formed an opinion about it, took corrective action, and verified the correction. That loop — observe, evaluate, adjust — is what separates an agent from a script.

**Tools shape output quality.**
The same game idea produced a substantially better document in Module 2 than Module 1. Not because the model got smarter — but because it had more information to work with. Tools are how you feed an agent the context it needs to do better work.

---

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
