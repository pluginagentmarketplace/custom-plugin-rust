---
name: rust-generics
description: Rust generics - functions, structs, and associated types
sasmp_version: "1.3.0"
bonded_agent: rust-types
bond_type: PRIMARY_BOND
---

# Rust Generics Skill

## Generic Functions

```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}

// Multiple type parameters
fn swap<T, U>(pair: (T, U)) -> (U, T) {
    (pair.1, pair.0)
}
```

## Generic Structs

```rust
struct Point<T> {
    x: T,
    y: T,
}

struct Point2<T, U> {
    x: T,
    y: U,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

// Specific implementation
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

## Associated Types

```rust
trait Iterator {
    type Item;  // Associated type
    fn next(&mut self) -> Option<Self::Item>;
}

impl Iterator for Counter {
    type Item = u32;
    fn next(&mut self) -> Option<Self::Item> {
        // ...
    }
}

// vs Generic trait
trait Container<T> {
    fn contains(&self, item: &T) -> bool;
}
```

## Const Generics

```rust
struct ArrayWrapper<T, const N: usize> {
    data: [T; N],
}

impl<T, const N: usize> ArrayWrapper<T, N> {
    fn new(data: [T; N]) -> Self {
        Self { data }
    }
}

let arr = ArrayWrapper::new([1, 2, 3, 4, 5]);
```

## PhantomData

```rust
use std::marker::PhantomData;

struct Wrapper<T> {
    value: u64,
    _marker: PhantomData<T>,  // Zero-sized type marker
}
```

## Quick Reference

| Concept | Syntax |
|---------|--------|
| Generic function | `fn foo<T>(x: T)` |
| Generic struct | `struct Foo<T>` |
| Bounds | `T: Trait` |
| Associated type | `type Item;` |
| Const generic | `const N: usize` |

## Related
- rust-traits - Trait bounds
- rust-types agent
