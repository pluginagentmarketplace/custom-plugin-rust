# Rust Traits and Generics Complete Guide

## What are Traits?

Traits define shared behavior. They're similar to interfaces in other languages but more powerful.

```rust
trait Animal {
    fn name(&self) -> String;
    fn speak(&self);

    // Default implementation
    fn describe(&self) -> String {
        format!("{} says:", self.name())
    }
}
```

## Implementing Traits

```rust
struct Dog {
    name: String,
}

impl Animal for Dog {
    fn name(&self) -> String {
        self.name.clone()
    }

    fn speak(&self) {
        println!("Woof!");
    }
}
```

## Deriving Traits

Common traits can be auto-implemented:

```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash, Default)]
struct User {
    id: u64,
    name: String,
}
```

### Derivable Traits

| Trait | Purpose | When to Use |
|-------|---------|-------------|
| `Debug` | Debug formatting | Always (for {:?}) |
| `Clone` | Deep copy | When copies needed |
| `Copy` | Bitwise copy | Small, stack-only types |
| `PartialEq` | Equality (==) | When comparing values |
| `Eq` | Total equality | When no NaN-like values |
| `PartialOrd` | Ordering (<, >) | When sorting |
| `Ord` | Total ordering | When total order exists |
| `Hash` | Hashing | For HashMap/HashSet keys |
| `Default` | Default value | Types with sensible defaults |

## Generics

### Generic Functions

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
```

### Generic Structs

```rust
struct Point<T> {
    x: T,
    y: T,
}

// Different types for x and y
struct Point2<T, U> {
    x: T,
    y: U,
}
```

### Generic Impl Blocks

```rust
impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

// Specialized impl for specific types
impl Point<f64> {
    fn distance_from_origin(&self) -> f64 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

## Trait Bounds

### Basic Bounds

```rust
// T must implement Display
fn print<T: std::fmt::Display>(value: T) {
    println!("{}", value);
}

// Multiple bounds
fn print_debug<T: Display + Debug>(value: T) {
    println!("{} ({:?})", value, value);
}
```

### Where Clauses

```rust
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
    // ...
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
```

## Common Trait Patterns

### The From/Into Pattern

```rust
struct Celsius(f64);
struct Fahrenheit(f64);

impl From<Celsius> for Fahrenheit {
    fn from(c: Celsius) -> Self {
        Fahrenheit(c.0 * 9.0 / 5.0 + 32.0)
    }
}

// Usage
let c = Celsius(100.0);
let f: Fahrenheit = c.into();  // Auto-implemented
let f = Fahrenheit::from(c);   // Explicit
```

### The TryFrom Pattern

```rust
impl TryFrom<i32> for PositiveInt {
    type Error = &'static str;

    fn try_from(value: i32) -> Result<Self, Self::Error> {
        if value > 0 {
            Ok(PositiveInt(value))
        } else {
            Err("Value must be positive")
        }
    }
}
```

### The Newtype Pattern

```rust
// Wrap existing type to implement foreign traits
struct Wrapper(Vec<String>);

impl fmt::Display for Wrapper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}
```

### The Extension Trait Pattern

```rust
// Add methods to types you don't own
trait VecExt<T> {
    fn push_if_not_empty(&mut self, item: T);
}

impl<T> VecExt<T> for Vec<T> {
    fn push_if_not_empty(&mut self, item: T) {
        if !self.is_empty() {
            self.push(item);
        }
    }
}
```

## Trait Objects (Dynamic Dispatch)

```rust
// Trait object with dyn
fn speak_all(animals: Vec<Box<dyn Animal>>) {
    for animal in animals {
        animal.speak();
    }
}

// As parameter
fn process(animal: &dyn Animal) {
    animal.speak();
}
```

### Object Safety

A trait is object-safe if:
1. No `Self` in method signatures (except self)
2. No generic methods
3. No associated constants

```rust
// NOT object-safe (returns Self)
trait Clone {
    fn clone(&self) -> Self;
}

// Object-safe
trait Drawable {
    fn draw(&self);
}
```

## Supertraits

```rust
trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        println!("* {} *", self);  // Uses Display
    }
}
```

## Blanket Implementations

```rust
// Implement trait for all types that satisfy bound
impl<T: Display> ToString for T {
    fn to_string(&self) -> String {
        format!("{}", self)
    }
}
```

## Operator Overloading

```rust
use std::ops::Add;

#[derive(Debug, Clone, Copy)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

// Usage
let p1 = Point { x: 1, y: 2 };
let p2 = Point { x: 3, y: 4 };
let p3 = p1 + p2;  // Point { x: 4, y: 6 }
```

## Best Practices

1. **Prefer static dispatch** (generics) when possible
2. **Use `dyn` for heterogeneous collections**
3. **Derive standard traits** unless manual impl needed
4. **Document trait requirements** clearly
5. **Use `where` clauses** for complex bounds
6. **Consider `#[must_use]`** for important returns

## Resources

- [Rust Book Ch.10: Generics](https://doc.rust-lang.org/book/ch10-00-generics.html)
- [Rust Book Ch.17: Trait Objects](https://doc.rust-lang.org/book/ch17-02-trait-objects.html)
- [Rust Reference: Traits](https://doc.rust-lang.org/reference/items/traits.html)
