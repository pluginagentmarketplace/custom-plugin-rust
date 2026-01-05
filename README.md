<div align="center">

<!-- Animated Typing Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=Rust+Development+Assistant;8+Agents+%7C+12+Skills;Claude+Code+Plugin" alt="Rust Development Assistant" />

<br/>

<!-- Badge Row 1: Status Badges -->
[![Version](https://img.shields.io/badge/Version-2.2.0-blue?style=for-the-badge)](https://github.com/pluginagentmarketplace/custom-plugin-rust/releases)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)
[![SASMP](https://img.shields.io/badge/SASMP-v1.3.0-blueviolet?style=for-the-badge)](#)

<!-- Badge Row 2: Content Badges -->
[![Agents](https://img.shields.io/badge/Agents-8-orange?style=flat-square&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/Skills-12-purple?style=flat-square&logo=lightning)](#-skills)
[![Commands](https://img.shields.io/badge/Commands-4-green?style=flat-square&logo=terminal)](#-commands)

<br/>

<!-- Quick CTA Row -->
[📦 **Install Now**](#-quick-start) · [🤖 **Explore Agents**](#-agents) · [📖 **Documentation**](#-documentation) · [⭐ **Star this repo**](https://github.com/pluginagentmarketplace/custom-plugin-rust)

---

### What is this?

> **Rust Development Assistant** is a Claude Code plugin with **8 agents** and **12 skills** for Rust development. Master ownership, borrowing, async/await, WebAssembly, and systems programming with expert AI agents.

</div>

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Agents](#-agents)
- [Skills](#-skills)
- [Commands](#-commands)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

---

## 🚀 Quick Start

### Prerequisites

- Claude Code CLI v2.0.27+
- Active Claude subscription

### Installation (Choose One)

<details open>
<summary><strong>Option 1: From Marketplace (Recommended)</strong></summary>

```bash
# Step 1️⃣ Add the marketplace
/plugin marketplace add pluginagentmarketplace/custom-plugin-rust

# Step 2️⃣ Install the plugin
/plugin install rust-development-assistant@pluginagentmarketplace-rust

# Step 3️⃣ Restart Claude Code
# Close and reopen your terminal/IDE
```

</details>

<details>
<summary><strong>Option 2: Local Installation</strong></summary>

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-rust.git
cd custom-plugin-rust

# Load locally
/plugin load .

# Restart Claude Code
```

</details>

### ✅ Verify Installation

After restart, you should see these agents:

```
rust-development-assistant:rust-fundamentals-agent
rust-development-assistant:rust-type-system-agent
rust-development-assistant:rust-async-agent
rust-development-assistant:rust-tooling-agent
rust-development-assistant:rust-web-agent
rust-development-assistant:rust-project-agent
rust-development-assistant:rust-debugger-agent
rust-development-assistant:08-rust-devops
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **8 Agents** | Specialized AI agents for Rust tasks |
| 🛠️ **12 Skills** | Reusable capabilities with Golden Format |
| ⌨️ **4 Commands** | Quick slash commands |
| 🔄 **SASMP v1.3.0** | Full protocol compliance |
| 🦀 **Systems Focus** | Ownership, borrowing, async, WASM |

---

## 🤖 Agents

### 8 Specialized Agents

| # | Agent | Purpose |
|---|-------|---------|
| 1 | **rust-fundamentals-agent** | Ownership, borrowing, lifetimes basics |
| 2 | **rust-type-system-agent** | Traits, generics, pattern matching |
| 3 | **rust-async-agent** | Async/await, Tokio, concurrency |
| 4 | **rust-tooling-agent** | Cargo, testing, CI/CD |
| 5 | **rust-web-agent** | Axum, Actix, REST APIs |
| 6 | **rust-project-agent** | Scaffolding, dependencies |
| 7 | **rust-debugger-agent** | Error fixing, optimization |
| 8 | **08-rust-devops** | Docker, deployment, infrastructure |

---

## 🛠️ Skills

### Available Skills

| Skill | Description | Invoke |
|-------|-------------|--------|
| `ownership-borrowing` | Memory safety fundamentals | `Skill("rust-development-assistant:ownership-borrowing")` |
| `error-handling` | Result, Option patterns | `Skill("rust-development-assistant:error-handling")` |
| `async-programming` | Async/await with Tokio | `Skill("rust-development-assistant:async-programming")` |
| `trait-generics` | Type system mastery | `Skill("rust-development-assistant:trait-generics")` |
| `cargo-ecosystem` | Cargo and dependencies | `Skill("rust-development-assistant:cargo-ecosystem")` |
| `rust-docker` | Containerization patterns | `Skill("rust-development-assistant:rust-docker")` |
| `rust-wasm` | WebAssembly compilation | `Skill("rust-development-assistant:rust-wasm")` |
| `rust-cli` | CLI application development | `Skill("rust-development-assistant:rust-cli")` |
| `rust-testing` | Testing strategies | `Skill("rust-development-assistant:rust-testing")` |
| `rust-performance` | Optimization techniques | `Skill("rust-development-assistant:rust-performance")` |
| `rust-concurrency` | Thread-safe patterns | `Skill("rust-development-assistant:rust-concurrency")` |
| `rust-macros` | Procedural and declarative macros | `Skill("rust-development-assistant:rust-macros")` |

---

## ⌨️ Commands

| Command | Description |
|---------|-------------|
| `/rust-learn` | Interactive Rust learning lessons |
| `/rust-practice` | Coding exercises by difficulty |
| `/rust-check` | Code analysis and quality checks |
| `/rust-new` | Create new Rust project with templates |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [LICENSE](LICENSE) | License information |

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

```
custom-plugin-rust/
├── 📁 .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── 📁 agents/              # 8 agents
├── 📁 skills/              # 12 skills (Golden Format)
├── 📁 commands/            # 4 commands
├── 📁 hooks/
├── 📄 README.md
├── 📄 CHANGELOG.md
└── 📄 LICENSE
```

</details>

---

## 📅 Metadata

| Field | Value |
|-------|-------|
| **Version** | 2.2.0 |
| **Last Updated** | 2025-12-31 |
| **Status** | Production Ready |
| **SASMP** | v1.3.0 |
| **Agents** | 8 |
| **Skills** | 12 |
| **Commands** | 4 |

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

1. Fork the repository
2. Create your feature branch
3. Follow the Golden Format for new skills
4. Submit a pull request

---

## ⚠️ Security

> **Important:** This repository contains third-party code and dependencies.
>
> - ✅ Always review code before using in production
> - ✅ Check dependencies for known vulnerabilities
> - ✅ Follow security best practices
> - ✅ Report security issues privately via [Issues](../../issues)

---

## 📝 License

Copyright © 2025 **Dr. Umit Kacar** & **Muhsin Elcicek**

Custom License - See [LICENSE](LICENSE) for details.

---

## 👥 Contributors

<table>
<tr>
<td align="center">
<strong>Dr. Umit Kacar</strong><br/>
Senior AI Researcher & Engineer
</td>
<td align="center">
<strong>Muhsin Elcicek</strong><br/>
Senior Software Architect
</td>
</tr>
</table>

---

<div align="center">

**Made with ❤️ for the Claude Code Community**

[![GitHub](https://img.shields.io/badge/GitHub-pluginagentmarketplace-black?style=for-the-badge&logo=github)](https://github.com/pluginagentmarketplace)

</div>
