# Cargo and Rust Ecosystem Complete Guide

## What is Cargo?

Cargo is Rust's build system and package manager. It handles:
- Building your code
- Downloading dependencies
- Building dependencies
- Running tests
- Generating documentation

## Cargo.toml Structure

```toml
[package]
name = "my-project"
version = "0.1.0"
edition = "2021"
authors = ["Your Name <you@example.com>"]
description = "A brief description"
license = "MIT"
repository = "https://github.com/user/repo"
readme = "README.md"
keywords = ["keyword1", "keyword2"]
categories = ["category"]

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }

[dev-dependencies]
criterion = "0.5"

[build-dependencies]
cc = "1.0"

[features]
default = ["std"]
std = []
async = ["tokio"]

[[bin]]
name = "my-binary"
path = "src/bin/main.rs"

[[example]]
name = "demo"
path = "examples/demo.rs"

[profile.release]
opt-level = 3
lto = true
codegen-units = 1
```

## Essential Cargo Commands

### Building

```bash
# Debug build
cargo build

# Release build (optimized)
cargo build --release

# Check without building (faster)
cargo check

# Build specific target
cargo build --bin my-binary
cargo build --lib
```

### Running

```bash
# Run default binary
cargo run

# Run with release optimizations
cargo run --release

# Run specific binary
cargo run --bin other-binary

# Pass arguments
cargo run -- arg1 arg2

# Run example
cargo run --example demo
```

### Testing

```bash
# Run all tests
cargo test

# Run specific test
cargo test test_function_name

# Run tests matching pattern
cargo test pattern

# Show output
cargo test -- --nocapture

# Run ignored tests
cargo test -- --ignored

# Run only unit tests
cargo test --lib

# Run only integration tests
cargo test --test integration_test_name

# Run doc tests
cargo test --doc
```

### Documentation

```bash
# Generate and open docs
cargo doc --open

# Include private items
cargo doc --document-private-items

# Don't document dependencies
cargo doc --no-deps
```

### Dependency Management

```bash
# Add dependency
cargo add serde
cargo add serde --features derive
cargo add tokio --features "full"

# Add dev dependency
cargo add --dev criterion

# Remove dependency
cargo remove serde

# Update dependencies
cargo update
cargo update -p specific-crate

# Show dependency tree
cargo tree
cargo tree -d  # duplicates only
cargo tree -i serde  # inverted (who uses serde?)
```

## Popular Crates by Category

### Serialization
```toml
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
toml = "0.8"
```

### Async Runtime
```toml
tokio = { version = "1", features = ["full"] }
# or
async-std = "1"
```

### Web Frameworks
```toml
# Modern and ergonomic
axum = "0.7"

# High performance
actix-web = "4"

# Minimal
warp = "0.3"
```

### HTTP Clients
```toml
reqwest = { version = "0.11", features = ["json"] }
```

### CLI Tools
```toml
clap = { version = "4", features = ["derive"] }
```

### Error Handling
```toml
# For libraries
thiserror = "1.0"

# For applications
anyhow = "1.0"
```

### Logging
```toml
tracing = "0.1"
tracing-subscriber = "0.3"
```

### Database
```toml
# SQL
sqlx = { version = "0.7", features = ["runtime-tokio", "postgres"] }

# ORM
diesel = { version = "2.1", features = ["postgres"] }
```

### Testing
```toml
[dev-dependencies]
criterion = "0.5"  # Benchmarking
mockall = "0.11"   # Mocking
proptest = "1.0"   # Property testing
```

## Workspaces

For multi-package projects:

```toml
# root Cargo.toml
[workspace]
members = [
    "crates/core",
    "crates/cli",
    "crates/web",
]
resolver = "2"

[workspace.package]
version = "0.1.0"
edition = "2021"
license = "MIT"

[workspace.dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
```

```toml
# crates/core/Cargo.toml
[package]
name = "my-core"
version.workspace = true
edition.workspace = true

[dependencies]
serde.workspace = true
```

## Cargo Profiles

```toml
# Development (default)
[profile.dev]
opt-level = 0
debug = true

# Release
[profile.release]
opt-level = 3
lto = true
codegen-units = 1
panic = "abort"

# Testing
[profile.test]
opt-level = 0
debug = true

# Benchmarking
[profile.bench]
opt-level = 3
debug = false
```

## Features

```toml
[features]
default = ["std"]
std = []
async = ["dep:tokio"]
full = ["std", "async", "serde"]

[dependencies]
tokio = { version = "1", optional = true }
serde = { version = "1", optional = true }
```

Usage:
```bash
cargo build --features async
cargo build --features "async,serde"
cargo build --all-features
cargo build --no-default-features
```

## Useful Cargo Extensions

```bash
# Install extensions
cargo install cargo-watch
cargo install cargo-edit
cargo install cargo-audit
cargo install cargo-outdated
cargo install cargo-bloat
cargo install cargo-expand

# Usage
cargo watch -x check           # Auto-rebuild on changes
cargo audit                    # Security vulnerability check
cargo outdated                 # Check for updates
cargo bloat --release          # Analyze binary size
cargo expand                   # Expand macros
```

## CI/CD Configuration

```bash
# Typical CI workflow
cargo fmt --check
cargo clippy -- -D warnings
cargo test
cargo doc --no-deps
cargo build --release
```

## Best Practices

1. **Always specify versions** - Use `crate = "1.2"` not `crate = "*"`
2. **Use workspace dependencies** - Share versions across packages
3. **Enable LTO for release** - Smaller, faster binaries
4. **Run clippy regularly** - Catch common mistakes
5. **Use cargo-audit** - Check for security issues
6. **Pin Cargo.lock** - Commit for binaries, don't commit for libraries
7. **Use features wisely** - Don't enable unused features

## Resources

- [Cargo Book](https://doc.rust-lang.org/cargo/)
- [crates.io](https://crates.io/)
- [lib.rs](https://lib.rs/) - Better crate search
- [Blessed.rs](https://blessed.rs/) - Recommended crates
