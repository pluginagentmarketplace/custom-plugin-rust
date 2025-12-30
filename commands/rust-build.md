---
description: Build and compile Rust project
allowed-tools: Read, Bash
---

# /rust-build Command

Build your Rust project with various options.

## Usage

```
/rust-build [mode] [options]
```

## Modes

| Mode | Description |
|------|-------------|
| `debug` | Fast compilation, no optimizations (default) |
| `release` | Optimized build for production |
| `check` | Fast syntax/type check without building |

## Options

| Option | Description |
|--------|-------------|
| `--target` | Cross-compile for target platform |
| `--features` | Enable specific features |
| `--all` | Build all workspace members |

## Examples

```bash
# Debug build
/rust-build

# Release build
/rust-build release

# Quick check
/rust-build check

# Cross-compile
/rust-build release --target x86_64-unknown-linux-musl

# With features
/rust-build release --features full
```

## Build Profiles

### Debug (default)
- Fast compilation
- Debug symbols included
- No optimizations
- Good for development

### Release
- Slower compilation
- Full optimizations
- Smaller binary
- Good for production

## Error Handling

If build fails:
1. Shows compiler errors
2. Suggests fixes based on error codes
3. Links to Rust error documentation

## Related

- `/rust-check` - Analyze code
- `/rust-test` - Run tests
- `/rust-fix` - Fix issues
