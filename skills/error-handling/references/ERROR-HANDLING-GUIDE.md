# Rust Error Handling Complete Guide

## Overview

Rust has no exceptions. Instead, it uses the `Result<T, E>` type for recoverable errors and `panic!` for unrecoverable errors.

## The Result Type

```rust
enum Result<T, E> {
    Ok(T),    // Success case
    Err(E),   // Error case
}
```

## The Option Type

```rust
enum Option<T> {
    Some(T),  // Value exists
    None,     // No value
}
```

## Error Handling Patterns

### Pattern 1: The ? Operator (Recommended)

```rust
fn read_config() -> Result<Config, ConfigError> {
    let file = File::open("config.toml")?;  // Returns early on error
    let content = read_to_string(file)?;     // Returns early on error
    let config = parse_config(&content)?;    // Returns early on error
    Ok(config)
}
```

### Pattern 2: Match Expression

```rust
fn process(value: Option<i32>) -> String {
    match value {
        Some(n) if n > 0 => format!("Positive: {}", n),
        Some(n) => format!("Non-positive: {}", n),
        None => String::from("No value"),
    }
}
```

### Pattern 3: Combinators

```rust
// Map - transform the success value
let doubled = result.map(|x| x * 2);

// Map_err - transform the error
let converted = result.map_err(|e| MyError::from(e));

// And_then - chain operations
let chained = result.and_then(|x| validate(x));

// Unwrap_or - provide default
let value = option.unwrap_or(42);

// Unwrap_or_else - lazy default
let value = option.unwrap_or_else(|| expensive_default());
```

## Custom Error Types

### Using thiserror (Library Errors)

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum DataError {
    #[error("Database connection failed: {0}")]
    Connection(#[from] diesel::ConnectionError),

    #[error("Record not found: {id}")]
    NotFound { id: i32 },

    #[error("Validation failed: {0}")]
    Validation(String),

    #[error(transparent)]
    Other(#[from] anyhow::Error),
}
```

### Using anyhow (Application Errors)

```rust
use anyhow::{Context, Result, bail, ensure};

fn load_config(path: &str) -> Result<Config> {
    let content = fs::read_to_string(path)
        .context("Failed to read config file")?;

    let config: Config = toml::from_str(&content)
        .context("Failed to parse config file")?;

    ensure!(config.port > 0, "Port must be positive");

    if config.debug && config.production {
        bail!("Cannot enable debug in production");
    }

    Ok(config)
}
```

## Converting Between Option and Result

```rust
// Option -> Result
let result: Result<i32, &str> = option.ok_or("value was None");
let result: Result<i32, Error> = option.ok_or_else(|| Error::new());

// Result -> Option
let option: Option<i32> = result.ok();   // Discards error
let option: Option<Error> = result.err(); // Discards success
```

## Error Propagation Strategies

### Strategy 1: Bubble Up

```rust
fn outer() -> Result<(), Error> {
    inner()?;  // Propagate error
    Ok(())
}
```

### Strategy 2: Convert and Bubble

```rust
fn outer() -> Result<(), MyError> {
    inner().map_err(|e| MyError::from(e))?;
    Ok(())
}
```

### Strategy 3: Handle and Continue

```rust
fn process_items(items: Vec<Item>) -> Vec<Result<Output, Error>> {
    items.into_iter()
        .map(|item| process_one(item))
        .collect()
}
```

### Strategy 4: Collect Results

```rust
fn process_all(items: Vec<Item>) -> Result<Vec<Output>, Error> {
    items.into_iter()
        .map(|item| process_one(item))
        .collect()  // Fails on first error
}
```

## Best Practices

1. **Never use `.unwrap()` in library code**
2. **Use `.expect()` only when panic is acceptable**
3. **Prefer `?` over explicit `match`**
4. **Define custom error types for libraries**
5. **Use `anyhow` for applications**
6. **Add context to errors with `.context()`**
7. **Log errors at appropriate levels**
8. **Test error paths, not just happy paths**

## Anti-Patterns to Avoid

```rust
// ❌ DON'T: Silent error swallowing
let _ = might_fail();

// ❌ DON'T: Panicking on recoverable errors
let config = load_config().unwrap();

// ❌ DON'T: Returning String as error type
fn process() -> Result<Data, String>

// ❌ DON'T: Ignoring Result
might_fail();  // Warning: unused Result

// ✅ DO: Handle or propagate
let config = load_config()?;
let config = load_config().unwrap_or_default();
if let Err(e) = might_fail() { log::error!("{}", e); }
```

## Resources

- [Rust Book Ch.9: Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- [thiserror crate](https://docs.rs/thiserror)
- [anyhow crate](https://docs.rs/anyhow)
- [Error Handling in Rust](https://blog.burntsushi.net/rust-error-handling/)
