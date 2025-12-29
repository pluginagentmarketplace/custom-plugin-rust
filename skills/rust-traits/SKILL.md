---
name: rust-traits
description: Rust traits - definition, implementation, bounds, and trait objects
sasmp_version: "1.3.0"
bonded_agent: rust-types
bond_type: PRIMARY_BOND
---

# Rust Traits Skill

## Trait Definition

```rust
trait Summary {
    fn summarize(&self) -> String;
    
    // Default implementation
    fn default_summary(&self) -> String {
        String::from("(Read more...)")
    }
}

struct Article {
    title: String,
    content: String,
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{}: {}", self.title, &self.content[..50])
    }
}
```

## Trait Bounds

```rust
// Function with trait bound
fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

// Trait bound syntax
fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}

// Multiple bounds
fn notify(item: &(impl Summary + Display)) { }
fn notify<T: Summary + Display>(item: &T) { }

// Where clause
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
    // ...
}
```

## Common Traits

```rust
// Display - user-facing output
use std::fmt;
impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

// From/Into - conversions
impl From<(i32, i32)> for Point {
    fn from((x, y): (i32, i32)) -> Self {
        Point { x, y }
    }
}
let p: Point = (1, 2).into();

// Iterator
impl Iterator for Counter {
    type Item = u32;
    fn next(&mut self) -> Option<Self::Item> {
        self.count += 1;
        if self.count < 6 { Some(self.count) } else { None }
    }
}
```

## Trait Objects

```rust
// Dynamic dispatch
trait Draw {
    fn draw(&self);
}

struct Screen {
    components: Vec<Box<dyn Draw>>,
}

impl Screen {
    fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

## Quick Reference

| Trait | Purpose |
|-------|---------|
| Clone | Deep copy |
| Copy | Implicit copy |
| Debug | {:?} format |
| Display | {} format |
| Default | Default values |
| Iterator | Iteration |
| From/Into | Conversions |

## Related
- rust-generics - Generic programming
- rust-types agent
