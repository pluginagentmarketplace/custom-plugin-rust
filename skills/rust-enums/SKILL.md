---
name: rust-enums
description: Rust enums - variants, pattern matching, Option, and Result
sasmp_version: "1.3.0"
bonded_agent: rust-types
bond_type: PRIMARY_BOND
---

# Rust Enums Skill

## Enum Definition

```rust
// Simple enum
enum Direction {
    North,
    South,
    East,
    West,
}

// Enum with data
enum Message {
    Quit,                       // No data
    Move { x: i32, y: i32 },   // Named fields
    Write(String),              // String
    ChangeColor(i32, i32, i32), // Tuple
}

// Enum with impl
impl Message {
    fn call(&self) {
        match self {
            Message::Quit => println!("Quit"),
            Message::Write(text) => println!("{}", text),
            _ => println!("Other"),
        }
    }
}
```

## Pattern Matching

```rust
fn process_message(msg: Message) {
    match msg {
        Message::Quit => {
            println!("Quitting");
        }
        Message::Move { x, y } => {
            println!("Move to ({}, {})", x, y);
        }
        Message::Write(text) => {
            println!("Text: {}", text);
        }
        Message::ChangeColor(r, g, b) => {
            println!("Color: #{:02x}{:02x}{:02x}", r, g, b);
        }
    }
}

// Match guards
match value {
    Some(x) if x < 5 => println!("less than five"),
    Some(x) => println!("{}", x),
    None => println!("nothing"),
}

// Binding with @
match value {
    Some(n @ 1..=5) => println!("1-5: {}", n),
    Some(n) => println!("other: {}", n),
    None => (),
}
```

## Option<T>

```rust
enum Option<T> {
    Some(T),
    None,
}

let some_number: Option<i32> = Some(5);
let no_number: Option<i32> = None;

// Methods
some_number.unwrap();           // Panics if None
some_number.unwrap_or(0);       // Default value
some_number.expect("error");    // Custom panic message

// if let
if let Some(n) = some_number {
    println!("Number: {}", n);
}

// Combinators
some_number.map(|n| n * 2);           // Option<i32>
some_number.and_then(|n| Some(n * 2)); // Flat map
some_number.filter(|&n| n > 0);       // Filter
some_number.ok_or("error");           // Option -> Result
```

## Result<T, E>

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}

fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Division by zero"))
    } else {
        Ok(a / b)
    }
}

// Usage
match divide(10.0, 2.0) {
    Ok(result) => println!("Result: {}", result),
    Err(e) => println!("Error: {}", e),
}

// Combinators
result.map(|v| v * 2);
result.map_err(|e| format!("Error: {}", e));
result.and_then(|v| divide(v, 2.0));
result.ok();  // Result -> Option
```

## Quick Reference

| Pattern | Usage |
|---------|-------|
| if let | Single pattern match |
| while let | Loop on pattern |
| match | Exhaustive matching |
| @ | Bind while matching |
| _ | Wildcard pattern |
| .. | Ignore rest |

## Related
- rust-error - Error handling
- rust-traits - Trait objects
