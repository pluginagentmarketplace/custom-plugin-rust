---
name: rust-ownership
description: Rust ownership - borrowing, references, and lifetimes
sasmp_version: "1.3.0"
bonded_agent: rust-ownership
bond_type: PRIMARY_BOND
---

# Rust Ownership Skill

## Overview

Master Rust's unique ownership system - the key to memory safety without garbage collection.

## Ownership Rules

1. Each value has exactly one owner
2. When owner goes out of scope, value is dropped
3. Ownership can be transferred (moved)

```rust
// Move semantics
let s1 = String::from("hello");
let s2 = s1;  // s1 is moved to s2, s1 is invalid

// Copy types (stack-only)
let x = 5;
let y = x;  // Copy, both valid

// Clone for heap data
let s1 = String::from("hello");
let s2 = s1.clone();  // Deep copy, both valid
```

## References and Borrowing

```rust
// Immutable reference (borrow)
fn calculate_length(s: &String) -> usize {
    s.len()
}

let s = String::from("hello");
let len = calculate_length(&s);  // s is still valid

// Mutable reference
fn append_world(s: &mut String) {
    s.push_str(" world");
}

let mut s = String::from("hello");
append_world(&mut s);
```

## Borrowing Rules

1. At any time: ONE mutable reference OR any number of immutable references
2. References must always be valid

```rust
let mut s = String::from("hello");

// Multiple immutable references OK
let r1 = &s;
let r2 = &s;
println!("{} {}", r1, r2);

// Mutable reference after immutable done
let r3 = &mut s;  // OK, r1 and r2 no longer used

// ERROR: Can't have mutable while immutable exists
let r1 = &s;
let r2 = &mut s;  // Error!
println!("{}", r1);
```

## Lifetimes

```rust
// Lifetime annotation
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// Struct with lifetime
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
    
    fn announce(&self, announcement: &str) -> &str {
        println!("Attention: {}", announcement);
        self.part
    }
}

// Static lifetime
let s: &'static str = "I live forever";
```

## Lifetime Elision Rules

```rust
// These are equivalent:
fn first_word(s: &str) -> &str { ... }
fn first_word<'a>(s: &'a str) -> &'a str { ... }

// Elision rules:
// 1. Each reference parameter gets its own lifetime
// 2. If exactly one input lifetime, it's assigned to all outputs
// 3. If &self or &mut self, self's lifetime is assigned to outputs
```

## Common Patterns

```rust
// Slice reference
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[..i];
        }
    }
    &s[..]
}

// Cow (Clone on Write)
use std::borrow::Cow;
fn process(input: &str) -> Cow<str> {
    if input.contains("bad") {
        Cow::Owned(input.replace("bad", "good"))
    } else {
        Cow::Borrowed(input)
    }
}
```

## Quick Reference

| Concept | Syntax | Meaning |
|---------|--------|---------|
| Move | `let s2 = s1` | s1 invalid |
| Borrow | `&s` | Immutable reference |
| Mutable borrow | `&mut s` | Mutable reference |
| Lifetime | `'a` | Reference validity |
| Static | `'static` | Lives entire program |

## Related
- rust-basics - Fundamentals
- rust-ownership agent
