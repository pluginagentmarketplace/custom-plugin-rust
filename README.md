# 🦀 Rust Programming System

[![SASMP v1.3.0](https://img.shields.io/badge/SASMP-v1.3.0-blue.svg)](https://github.com/pluginagentmarketplace)
[![Rust](https://img.shields.io/badge/Rust-2024%20Edition-orange?logo=rust)](https://www.rust-lang.org)
[![Plugin Type](https://img.shields.io/badge/Type-Hybrid-purple.svg)](https://github.com/pluginagentmarketplace)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Complete Rust Programming System** - Learn AND Develop with expert AI agents. Master ownership, borrowing, async/await while building real projects.

## 🎯 Plugin Type: HYBRID

This plugin serves **two purposes**:

| Mode | Purpose | For Who |
|------|---------|---------|
| 🎓 **Learning** | Understand Rust concepts | Beginners, Students |
| 🔧 **Development** | Build real Rust projects | Developers, Engineers |

---

## 📊 Features Overview

| Category | Count | Items |
|----------|-------|-------|
| **Agents** | 7 | 3 Learning + 4 Development |
| **Skills** | 5 | 4 Learning + 1 Development |
| **Commands** | 8 | 2 Learning + 6 Development |

---

## 🎓 Learning Mode

### Learning Agents

| Agent | Expertise |
|-------|-----------|
| `rust-fundamentals-agent` | Ownership, borrowing, lifetimes |
| `rust-type-system-agent` | Traits, generics, pattern matching |
| `rust-async-agent` | Async/await, Tokio, concurrency |

### Learning Commands

```bash
/rust-learn ownership    # Interactive ownership lesson
/rust-learn traits       # Learn traits and generics
/rust-practice beginner  # Coding exercises
```

### Learning Skills

- **ownership-borrowing** - Memory safety fundamentals
- **error-handling** - Result, Option patterns
- **async-programming** - Async/await with Tokio
- **trait-generics** - Type system mastery

---

## 🔧 Development Mode

### Development Agents

| Agent | Purpose |
|-------|---------|
| `rust-tooling-agent` | Cargo, testing, CI/CD |
| `rust-web-agent` | Axum, Actix, REST APIs |
| `rust-project-agent` | Scaffolding, dependencies |
| `rust-debugger-agent` | Error fixing, optimization |

### Development Commands

| Command | Description |
|---------|-------------|
| `/rust-new` | Create new project with templates |
| `/rust-add` | Add dependencies |
| `/rust-build` | Build project (debug/release) |
| `/rust-test` | Run tests |
| `/rust-check` | Code analysis |
| `/rust-fix` | Auto-fix issues |

### Quick Start: Development

```bash
# Create a new CLI project
/rust-new my-cli cli

# Add dependencies
/rust-add clap --features derive
/rust-add tokio --features full

# Build and test
/rust-build release
/rust-test
```

### Project Templates

| Template | Includes |
|----------|----------|
| `cli` | clap, anyhow, tokio |
| `api` | axum, tokio, sqlx, serde |
| `lib` | thiserror, proptest |
| `workspace` | Multi-crate setup |

---

## 🗂️ Plugin Structure

```
custom-plugin-rust/
├── agents/
│   ├── rust-fundamentals-agent.md   # 🎓 Learning
│   ├── rust-type-system-agent.md    # 🎓 Learning
│   ├── rust-async-agent.md          # 🎓 Learning
│   ├── rust-tooling-agent.md        # 🔧 Development
│   ├── rust-web-agent.md            # 🔧 Development
│   ├── rust-project-agent.md        # 🔧 Development
│   └── rust-debugger-agent.md       # 🔧 Development
├── skills/
│   ├── ownership-borrowing/         # 🎓 Golden Format ✅
│   │   ├── SKILL.md
│   │   ├── assets/memory-diagrams.md
│   │   ├── scripts/ownership_checker.py
│   │   └── references/OWNERSHIP-GUIDE.md
│   ├── error-handling/              # 🎓 Golden Format ✅
│   │   ├── SKILL.md
│   │   ├── assets/error-patterns.yaml
│   │   ├── scripts/error_analyzer.py
│   │   └── references/ERROR-HANDLING-GUIDE.md
│   ├── async-programming/           # 🎓 Golden Format ✅
│   │   ├── SKILL.md
│   │   ├── assets/tokio-patterns.yaml
│   │   ├── scripts/async_analyzer.py
│   │   └── references/ASYNC-GUIDE.md
│   ├── trait-generics/              # 🎓 Golden Format ✅
│   │   ├── SKILL.md
│   │   ├── assets/trait-patterns.yaml
│   │   ├── scripts/trait_checker.py
│   │   └── references/TRAITS-GUIDE.md
│   └── cargo-ecosystem/             # 🔧 Golden Format ✅
│       ├── SKILL.md
│       ├── assets/cargo-commands.yaml
│       ├── scripts/project_analyzer.py
│       └── references/CARGO-GUIDE.md
├── commands/
│   ├── rust-learn.md                # 🎓 Learning
│   ├── rust-practice.md             # 🎓 Learning
│   ├── rust-new.md                  # 🔧 Development
│   ├── rust-add.md                  # 🔧 Development
│   ├── rust-build.md                # 🔧 Development
│   ├── rust-test.md                 # 🔧 Development
│   ├── rust-check.md                # 🔧 Development
│   └── rust-fix.md                  # 🔧 Development
├── hooks/
│   └── hooks.json
└── plugin.json
```

---

## 📚 Topics Covered

### Core Concepts (Learning)
- ✅ Ownership & Borrowing
- ✅ Lifetimes
- ✅ Traits & Generics
- ✅ Pattern Matching
- ✅ Error Handling (Result, Option)
- ✅ Async/Await

### Development Skills
- ✅ Project Scaffolding
- ✅ Dependency Management
- ✅ Build Optimization
- ✅ Testing Strategies
- ✅ Debugging Techniques
- ✅ Web Development (Axum)

---

## 🚀 Installation

```bash
# Via Claude Code plugin marketplace
/plugin install custom-plugin-rust
```

---

## 📖 Usage Examples

### Learning Flow
```bash
# 1. Start learning
/rust-learn ownership

# 2. Practice with exercises
/rust-practice beginner

# 3. Check understanding
/rust-practice intermediate
```

### Development Flow
```bash
# 1. Create project
/rust-new my-api api

# 2. Add dependencies
/rust-add serde --features derive
/rust-add sqlx --features postgres

# 3. Build and test
/rust-build
/rust-test

# 4. Fix issues
/rust-fix
```

### Hybrid Flow (Learn + Build)
```bash
# Learn a concept
/rust-learn async

# Apply in real project
/rust-new async-demo cli
/rust-add tokio --features full

# Get help when stuck
# (rust-debugger-agent activates on errors)
/rust-build
```

---

## 🔗 Related Resources

### Official Documentation
- [The Rust Book](https://doc.rust-lang.org/book/)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Tokio Tutorial](https://tokio.rs/tokio/tutorial)

### Research Documentation
Located in: `/Users/umitkacar/Documents/-project-18-rust/`

---

## 📊 Version History

| Version | Date | Type | Changes |
|---------|------|------|---------|
| 2.1.0 | 2025-12-29 | Hybrid | Added development agents & commands |
| 2.0.0 | 2025-12-29 | Learning | Rust-specific rewrite |
| 1.0.0 | 2024-11-18 | Generic | Initial template |

---

## License

MIT License - See [LICENSE](LICENSE) for details.

## Author

Plugin Agent Marketplace - [pluginagentmarketplace@gmail.com](mailto:pluginagentmarketplace@gmail.com)
