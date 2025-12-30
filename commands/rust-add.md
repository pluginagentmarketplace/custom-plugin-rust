---
description: Add dependencies to Rust project
allowed-tools: Read, Write, Bash
---

# /rust-add Command

Add crate dependencies to your Rust project.

## Usage

```
/rust-add <crate-name> [--features <features>] [--dev]
```

## Options

| Option | Description |
|--------|-------------|
| `--features` | Enable specific features |
| `--dev` | Add as dev dependency |
| `--build` | Add as build dependency |

## Examples

```bash
# Add crate
/rust-add serde

# Add with features
/rust-add serde --features derive

# Add dev dependency
/rust-add criterion --dev

# Add multiple
/rust-add tokio axum serde
```

## Common Crate Bundles

### Web API Bundle
```bash
/rust-add axum tokio serde serde_json sqlx tracing
```

### CLI Bundle
```bash
/rust-add clap anyhow tokio
```

### Testing Bundle
```bash
/rust-add criterion proptest mockall --dev
```

## What Happens

1. Runs `cargo add <crate>`
2. Updates Cargo.toml
3. Shows added dependency info
4. Suggests common companion crates

## Related

- `/rust-new` - Create project
- `/rust-build` - Build project
