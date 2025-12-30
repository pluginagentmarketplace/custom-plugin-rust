---
description: Review and analyze Rust code
allowed-tools: Read, Bash, Grep, Glob
---

# /rust-check Command

Analyze Rust code for common issues and best practices.

## Usage

```
/rust-check [path]
```

## Checks Performed

### Ownership & Borrowing
- Unnecessary clones
- Potential dangling references
- Borrow conflicts

### Error Handling
- Unwrap in production code
- Missing error context
- Silent error ignoring

### Performance
- Unnecessary allocations
- Missing iterator optimizations
- Redundant copies

### Style
- Naming conventions
- Documentation completeness
- Code organization

## Example

```
/rust-check src/main.rs
```

## Output

```
[Line 42] CLONE: Unnecessary clone - consider borrowing
[Line 67] UNWRAP: Use ? or handle error explicitly
[Line 89] PERF: Consider using iter() instead of into_iter()
```

## Related

- `cargo clippy` - Official linter
- `cargo fmt` - Code formatting
