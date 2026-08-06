# 🧠 No Cold Starts

A small handoff system for AI-assisted projects, so a new agent can pick up
where the last one left off.

## 📖 Contents

- [🚧 Why this exists](#-why-this-exists)
- [🏗️ How it works](#-how-it-works)
- [🚀 Getting started](#-getting-started)
- [🗂️ What lives here](#-what-lives-here)
- [🔁 An example project](#-an-example-project)

## 🚧 Why this exists

### How it started

I built No Cold Starts while upgrading my website with AI. As the work grew, I
kept running into the same problems.

### What kept going wrong

- The thread became huge, and useful decisions were hard to find.
- The context window filled up, so earlier details started dropping away.
- Switching sessions or agents meant explaining the project all over again.
- Git showed me what changed, but not why we chose it or what came next.

### What I built instead

I did not need another transcript. I needed a few small files that captured the
useful parts: where things stood, what we had decided, what was blocked, and
what to do next.

That personal handoff system became No Cold Starts. It is a reusable way to
give the next AI agent the context it actually needs.

In practice, it gives you:

- A quick answer to “Where are we, and what happens next?”
- The reasoning behind decisions, not just the final code.
- A clean handoff when you switch agents, tools, or sessions.
- A private project notebook that stays separate from the codebase.

## 🏗️ How it works

### What it is

No Cold Starts is a set of Markdown files for AI handoffs. Think of it as a
lightweight Jira, scaffolded like a starter app.

### What bootstrap does

`bootstrap.py` asks for the project name, description, and repository directory,
then fills in the starting files. That is all it does. There is no server, AI
connection, or background process.

### What happens next

After setup, you and your agents keep it current by following `AGENTS.md` and
recording outcomes, decisions, blockers, and next steps.

## 🚀 Getting started

1. Clone this repo or download it as a zip
2. Run `python3 bootstrap.py` from your terminal
3. The script will guide you through setup and tell you what to do next.

## 🗂️ What lives here

| File | What it is for |
| --- | --- |
| `README.md` | Start here. This one is for humans. |
| `AGENTS.md` | How AI agents should work in the workspace. |
| `.ai/CURRENT.md` | Where the project stands right now. |
| `.ai/ROADMAP.md` | Where the project is heading. |
| `.ai/initiatives/` | Plans that are active or already completed. |
| `.ai/decisions/` | Why important choices were made. |
| `.ai/README.md` | How the workspace state fits together. |
| `bootstrap.py` | The small setup script you run once. |

## 🔁 An example project

Say you need to upgrade Next.js or React in an existing web app. The journey
looks like this:

1. **Set the goal**

   Start an agent from the workspace and say: “Upgrade the website's Next.js
   version.”

2. **Write down the plan**

   The agent inspects the code and saves the plan in
   `.ai/initiatives/active/nextjs-upgrade/PLAN.md`. `.ai/CURRENT.md` records
   what it is working on now.

3. **Complete one piece of work**

   The agent changes and tests the code in the codebase. The plan and project
   context stay in this workspace.

4. **Prepare the handoff**

   Ask: “Prepare a handoff according to `AGENTS.md`. Record what was completed,
   verified, blocked, decided, and what should happen next.”

   The agent updates the plan, `.ai/CURRENT.md`, and `.ai/decisions/` when a
   decision is worth keeping.

5. **Switch agents without starting over**

   The next agent reads those files, checks them against Git, and continues
   from the next task instead of rebuilding the story from an old thread.

Repeat the loop whenever a task is finished or a thread starts getting heavy.
A short, distilled handoff is often more useful than carrying an ever-growing
conversation forward.
