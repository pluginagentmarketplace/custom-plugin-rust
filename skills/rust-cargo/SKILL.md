---
name: rust-cargo
description: Cargo and Rust ecosystem - dependencies, workspaces, tools
sasmp_version: "1.3.0"
bonded_agent: rust-cargo
bond_type: PRIMARY_BOND
---

# Rust Cargo Skill

## Cargo Commands

```bash
# Create project
cargo new myproject
cargo new --lib mylib

# Build and run
cargo build
cargo build --release
cargo run
cargo run --release

# Testing
cargo test
cargo test test_name
cargo test -- --nocapture

# Other
cargo check      # Fast syntax check
cargo doc        # Generate docs
cargo doc --open # Open in browser
cargo clippy     # Linting
cargo fmt        # Format code
```

## Cargo.toml

```toml
[package]
name = "myproject"
version = "0.1.0"
edition = "2021"
authors = ["Name <email@example.com>"]
description = "My project"
license = "MIT"
repository = "https://github.com/user/project"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
reqwest = "0.11"

[dev-dependencies]
mockall = "0.11"

[build-dependencies]
cc = "1.0"

[features]
default = ["std"]
std = []
full = ["std", "extra"]

[[bin]]
name = "mybin"
path = "src/bin/mybin.rs"

[[example]]
name = "example1"
path = "examples/example1.rs"
```

## Workspaces

```toml
# root Cargo.toml
[workspace]
members = [
    "crate1",
    "crate2",
    "shared",
]

[workspace.dependencies]
serde = { version = "1.0", features = ["derive"] }
```

## Useful Tools

```bash
# Install tools
cargo install cargo-watch
cargo install cargo-edit
cargo install cargo-expand

# Usage
cargo watch -x run    # Auto-rebuild
cargo add serde       # Add dependency
cargo expand          # Expand macros
```

## Quick Reference

| Command | Purpose |
|---------|---------|
| cargo new | Create project |
| cargo build | Compile |
| cargo run | Build and run |
| cargo test | Run tests |
| cargo doc | Generate docs |
| cargo publish | Publish crate |

## Related
- rust-basics - Getting started
- rust-cargo agent
