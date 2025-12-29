---
name: rust-structs
description: Rust structs - definition, methods, and associated functions
sasmp_version: "1.3.0"
bonded_agent: rust-types
bond_type: PRIMARY_BOND
---

# Rust Structs Skill

## Struct Types

```rust
// Named struct
struct User {
    username: String,
    email: String,
    active: bool,
    sign_in_count: u64,
}

// Tuple struct
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

// Unit struct
struct AlwaysEqual;
```

## Creating Instances

```rust
let user = User {
    username: String::from("john"),
    email: String::from("john@example.com"),
    active: true,
    sign_in_count: 1,
};

// Field init shorthand
fn build_user(email: String, username: String) -> User {
    User {
        email,     // Same as email: email
        username,  // Same as username: username
        active: true,
        sign_in_count: 1,
    }
}

// Struct update syntax
let user2 = User {
    email: String::from("another@example.com"),
    ..user  // Rest from user
};
```

## Methods and Associated Functions

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    // Associated function (constructor)
    fn new(width: u32, height: u32) -> Self {
        Self { width, height }
    }

    fn square(size: u32) -> Self {
        Self { width: size, height: size }
    }

    // Method (takes &self)
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

    // Mutable method
    fn set_width(&mut self, width: u32) {
        self.width = width;
    }

    // Consuming method
    fn into_square(self) -> Rectangle {
        Rectangle::square(self.width.max(self.height))
    }
}

// Usage
let rect = Rectangle::new(30, 50);
println!("Area: {}", rect.area());
```

## Derive Macros

```rust
#[derive(Debug, Clone, PartialEq, Default)]
struct Point {
    x: f64,
    y: f64,
}

let p1 = Point { x: 1.0, y: 2.0 };
let p2 = p1.clone();
println!("{:?}", p1);  // Debug
assert_eq!(p1, p2);    // PartialEq
let p3 = Point::default();  // Default
```

## Quick Reference

| Derive | Provides |
|--------|----------|
| Debug | {:?} formatting |
| Clone | .clone() method |
| Copy | Implicit copy |
| PartialEq | == comparison |
| Default | Default::default() |
| Hash | Hash trait |

## Related
- rust-enums - Enums
- rust-traits - Custom traits
