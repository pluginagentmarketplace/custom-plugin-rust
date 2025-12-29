---
name: rust-basics
description: Rust basics - variables, types, functions, and control flow
sasmp_version: "1.3.0"
bonded_agent: rust-fundamentals
bond_type: PRIMARY_BOND
---

# Rust Basics Skill

## Overview

Master Rust fundamentals - variables, types, functions, and control flow.

## Installation

```bash
# Install rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Check version
rustc --version
cargo --version

# Update
rustup update
```

## Variables

```rust
// Immutable by default
let x = 5;

// Mutable with mut
let mut y = 10;
y = 20;

// Constants (must be type annotated)
const MAX_POINTS: u32 = 100_000;

// Shadowing
let x = 5;
let x = x + 1;  // x is now 6
let x = "hello";  // Different type OK with shadowing
```

## Data Types

```rust
// Scalar types
let integer: i32 = 42;
let float: f64 = 3.14;
let boolean: bool = true;
let character: char = 'R';

// Compound types
let tuple: (i32, f64, u8) = (500, 6.4, 1);
let (x, y, z) = tuple;  // Destructuring
let first = tuple.0;    // Index access

let array: [i32; 5] = [1, 2, 3, 4, 5];
let first = array[0];
let same = [3; 5];  // [3, 3, 3, 3, 3]
```

## Functions

```rust
fn main() {
    greet("World");
    let sum = add(5, 3);
}

fn greet(name: &str) {
    println!("Hello, {}!", name);
}

fn add(a: i32, b: i32) -> i32 {
    a + b  // Expression, no semicolon = return value
}

// Early return
fn check(n: i32) -> bool {
    if n < 0 {
        return false;
    }
    true
}
```

## Control Flow

```rust
// if expression
let number = 6;
let result = if number % 2 == 0 { "even" } else { "odd" };

// loop
let mut counter = 0;
let result = loop {
    counter += 1;
    if counter == 10 {
        break counter * 2;  // Returns value
    }
};

// while
while counter > 0 {
    counter -= 1;
}

// for
for element in [1, 2, 3, 4, 5] {
    println!("{}", element);
}

for i in 0..5 {  // Range: 0, 1, 2, 3, 4
    println!("{}", i);
}

for i in (1..=5).rev() {  // Inclusive, reversed: 5, 4, 3, 2, 1
    println!("{}", i);
}
```

## Quick Reference

| Type | Size | Range |
|------|------|-------|
| i8/u8 | 1 byte | -128..127 / 0..255 |
| i32/u32 | 4 bytes | Default integer |
| i64/u64 | 8 bytes | Large integers |
| f32/f64 | 4/8 bytes | Floats (f64 default) |
| bool | 1 byte | true/false |
| char | 4 bytes | Unicode scalar |

## Related
- rust-ownership - Memory safety
- rust-fundamentals agent
