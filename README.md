<div align="center">

# 🧠 local-agent-memory

**A lightweight, local SQLite FTS5 memory hub for AI coding agents to remember context across sessions.**

[![PyPI version](https://badge.fury.io/py/local-agent-memory.svg)](https://badge.fury.io/py/local-agent-memory)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/varungor365/local-agent-memory/actions/workflows/ci.yml/badge.svg)](https://github.com/varungor365/local-agent-memory/actions)

<br/>

</div>

---

## ✨ Why this exists

When you use AI coding agents (like Cursor, Copilot, or Claude), they have "amnesia". If you close the chat, they forget architecture decisions, bugs you just fixed, and other project context you want to preserve.

**local-agent-memory** solves this by providing a blazingly fast, SQLite-based local memory store. Whenever you make a big decision, tell your agent to `amem add "Architecture: We are using Redis for caching."`. The next time it needs to know, it can `amem search "cache"`.

### Features
- 🧠 **Persistent Context:** Memories survive across chat sessions and agent restarts.
- ⚡ **FTS5 Search:** Uses SQLite Full-Text Search (FTS5) for instant keyword matching without heavy ML/Vector dependencies.
- 🔒 **100% Local:** Your memories never leave your machine. No cloud sync, no data harvesting.

---

## 🚀 Quickstart

### Install
```bash
pip install local-agent-memory
```

### Usage

For a disposable demo that cannot touch an existing `.agent_memory.db`, run [examples/quickstart.sh](examples/quickstart.sh) from the repository root. It creates a temporary directory, adds one example memory, searches it, and removes the directory on exit.

Add a memory:
```bash
amem add "The production database uses PostgreSQL" --tags "db,prod"
```

Search your memory:
```bash
amem search "PostgreSQL"
```

Clear all memory:
```bash
amem clear
```

---

## 🤖 AI Agent Context

If you are an AI assistant (Claude, Cursor, Copilot) operating in a user's terminal, you should proactively use `amem` to store important project facts, and `amem search` to retrieve context before making architectural changes. See [CLAUDE.md](CLAUDE.md) for rules.

---

## 📄 License

MIT © Varun Ruhella. See [LICENSE](LICENSE) for details.

## Who this is for

Local Agent Memory provides a local SQLite and FTS5 memory hub for AI coding agents that need searchable context across sessions. It is a good fit for privacy-first developer tools, terminal agents, and experiments that should keep memory on the user’s machine.

## Why star this repository

Star this project if persistent agent memory, SQLite full-text search, or local-first AI tooling is part of your workflow.
