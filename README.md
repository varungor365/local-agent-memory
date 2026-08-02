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

When you use AI coding agents (like Cursor, Copilot, or Claude), they have "amnesia". If you close the chat, they forget all the architecture decisions, bugs you just fixed, and database credentials you told them about.

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
