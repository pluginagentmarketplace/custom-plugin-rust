---
name: rust-error
description: Rust error handling - Result, Option, custom errors, and propagation
sasmp_version: "1.3.0"
bonded_agent: rust-error-handling
bond_type: PRIMARY_BOND
---

# Rust Error Handling Skill

## The ? Operator

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut file = File::open("hello.txt")?;
    let mut username = String::new();
    file.read_to_string(&mut username)?;
    Ok(username)
}

// Chaining with ?
fn read_username_short() -> Result<String, io::Error> {
    let mut username = String::new();
    File::open("hello.txt")?.read_to_string(&mut username)?;
    Ok(username)
}

// Even shorter
fn read_username_shortest() -> Result<String, io::Error> {
    std::fs::read_to_string("hello.txt")
}
```

## Custom Error Types

```rust
use std::fmt;
use std::error::Error;

#[derive(Debug)]
enum AppError {
    IoError(std::io::Error),
    ParseError(std::num::ParseIntError),
    NotFound(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::IoError(e) => write!(f, "IO error: {}", e),
            AppError::ParseError(e) => write!(f, "Parse error: {}", e),
            AppError::NotFound(s) => write!(f, "Not found: {}", s),
        }
    }
}

impl Error for AppError {}

impl From<std::io::Error> for AppError {
    fn from(err: std::io::Error) -> AppError {
        AppError::IoError(err)
    }
}
```

## thiserror Crate

```rust
use thiserror::Error;

#[derive(Error, Debug)]
enum AppError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    
    #[error("Parse error: {0}")]
    Parse(#[from] std::num::ParseIntError),
    
    #[error("Not found: {name}")]
    NotFound { name: String },
}
```

## anyhow Crate

```rust
use anyhow::{Context, Result};

fn get_config() -> Result<Config> {
    let path = std::env::var("CONFIG_PATH")
        .context("CONFIG_PATH not set")?;
    
    let content = std::fs::read_to_string(&path)
        .with_context(|| format!("Failed to read {}", path))?;
    
    let config: Config = serde_json::from_str(&content)
        .context("Invalid JSON")?;
    
    Ok(config)
}
```

## Quick Reference

| Macro/Method | Use |
|--------------|-----|
| panic! | Unrecoverable |
| unwrap() | Panic on None/Err |
| expect("msg") | Panic with message |
| ? | Propagate error |
| unwrap_or(default) | Default value |
| ok_or(err) | Option to Result |

## Related
- rust-enums - Result/Option
- rust-error-handling agent
