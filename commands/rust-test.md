---
description: Run tests in Rust project
allowed-tools: Read, Bash
---

# /rust-test Command

Run tests in your Rust project.

## Usage

```
/rust-test [filter] [options]
```

## Options

| Option | Description |
|--------|-------------|
| `--lib` | Run library tests only |
| `--doc` | Run documentation tests |
| `--ignored` | Run ignored tests |
| `--release` | Run tests in release mode |
| `--nocapture` | Show println! output |

## Examples

```bash
# Run all tests
/rust-test

# Run specific test
/rust-test test_user_creation

# Run tests matching pattern
/rust-test user

# Run with output visible
/rust-test --nocapture

# Run ignored tests
/rust-test --ignored

# Run doc tests only
/rust-test --doc
```

## Test Types

### Unit Tests
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }
}
```

### Integration Tests
```
tests/
└── integration_test.rs
```

### Doc Tests
```rust
/// Adds two numbers.
///
/// # Examples
///
/// ```
/// let result = my_lib::add(2, 2);
/// assert_eq!(result, 4);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

## Output

- Test results (pass/fail)
- Execution time
- Failed test details
- Coverage summary (if enabled)

## Related

- `/rust-build` - Build project
- `/rust-check` - Analyze code
