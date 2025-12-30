---
description: Automatically fix Rust code issues
allowed-tools: Read, Write, Edit, Bash
---

# /rust-fix Command

Automatically fix common Rust code issues.

## Usage

```
/rust-fix [type]
```

## Fix Types

| Type | Description |
|------|-------------|
| `lint` | Fix clippy warnings |
| `format` | Apply rustfmt formatting |
| `compiler` | Apply compiler suggestions |
| `all` | Run all fixes (default) |

## Examples

```bash
# Fix all issues
/rust-fix

# Fix clippy warnings only
/rust-fix lint

# Format code only
/rust-fix format

# Apply compiler suggestions
/rust-fix compiler
```

## What Gets Fixed

### Clippy Fixes
- Unused imports
- Redundant clones
- Unnecessary type annotations
- Inefficient patterns

### Format Fixes
- Indentation
- Line length
- Brace style
- Import ordering

### Compiler Fixes
- Deprecated syntax
- Edition migration
- Suggested refactors

## Commands Run

```bash
# Clippy with auto-fix
cargo clippy --fix --allow-dirty

# Format
cargo fmt

# Compiler suggestions
cargo fix --allow-dirty
```

## Safety

- Creates backup before major changes
- Shows diff of changes
- Asks for confirmation on destructive fixes

## Related

- `/rust-check` - Analyze without fixing
- `/rust-build` - Build project
