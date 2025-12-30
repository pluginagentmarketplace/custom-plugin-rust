---
description: Create a new Rust project with best-practice structure
allowed-tools: Read, Write, Bash
---

# /rust-new Command

Create a new Rust project with production-ready structure.

## Usage

```
/rust-new <project-name> [template]
```

## Templates

| Template | Description |
|----------|-------------|
| `cli` | Command-line application with clap |
| `api` | REST API with Axum |
| `lib` | Reusable library |
| `workspace` | Multi-crate workspace |

## Examples

```bash
# Simple binary
/rust-new my-app

# CLI application
/rust-new my-cli cli

# Web API
/rust-new my-api api

# Library
/rust-new my-lib lib

# Workspace
/rust-new my-project workspace
```

## Generated Structure

### CLI Template
```
my-cli/
├── Cargo.toml          # With clap, anyhow, tokio
├── src/
│   ├── main.rs         # Entry point with clap setup
│   ├── cli.rs          # CLI argument definitions
│   └── commands/
│       └── mod.rs
├── tests/
│   └── cli_tests.rs
└── README.md
```

### API Template
```
my-api/
├── Cargo.toml          # With axum, tokio, sqlx, serde
├── src/
│   ├── main.rs         # Server setup
│   ├── routes/
│   │   └── mod.rs
│   ├── handlers/
│   │   └── mod.rs
│   ├── models/
│   │   └── mod.rs
│   └── error.rs
├── tests/
│   └── api_tests.rs
└── README.md
```

## What Gets Created

1. **Cargo.toml** with appropriate dependencies
2. **src/** with template-specific structure
3. **.gitignore** for Rust projects
4. **README.md** with project description
5. **rustfmt.toml** for consistent formatting
6. **.github/workflows/** for CI (optional)

## Related

- `/rust-add` - Add dependencies
- `/rust-build` - Build project
