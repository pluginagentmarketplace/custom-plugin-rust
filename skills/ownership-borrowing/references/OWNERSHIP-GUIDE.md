# Complete Ownership Guide

## Understanding Ownership

### Why Ownership?

Rust's ownership system enables:
- **Memory safety** without garbage collection
- **Thread safety** without data races
- **Zero-cost abstractions** for resource management

### Stack vs Heap

| Stack | Heap |
|-------|------|
| Fixed size, known at compile time | Dynamic size |
| Fast allocation | Slower allocation |
| Automatic cleanup | Manual or ownership-based cleanup |
| `i32`, `f64`, `bool`, `char` | `String`, `Vec<T>`, `Box<T>` |

### Copy Types

Types that implement `Copy` are automatically copied:

```rust
let x: i32 = 5;
let y = x;  // Copy, both valid
println!("{} {}", x, y);

// Copy types include:
// - All integer types (i8, i16, i32, i64, i128, u8, u16, u32, u64, u128)
// - Boolean (bool)
// - Floating point (f32, f64)
// - Character (char)
// - Tuples of Copy types: (i32, i32)
```

### Move Types

Types that don't implement `Copy` are moved:

```rust
let s1 = String::from("hello");
let s2 = s1;  // Move, s1 invalid
// println!("{}", s1);  // ERROR!
println!("{}", s2);  // OK
```

## Borrowing Rules

### Rule 1: Multiple Immutable Borrows OK

```rust
let s = String::from("hello");
let r1 = &s;
let r2 = &s;
let r3 = &s;
println!("{} {} {}", r1, r2, r3);  // OK
```

### Rule 2: Only One Mutable Borrow

```rust
let mut s = String::from("hello");
let r1 = &mut s;
// let r2 = &mut s;  // ERROR: second mutable borrow
r1.push_str(" world");
```

### Rule 3: No Mixing Mutable and Immutable

```rust
let mut s = String::from("hello");
let r1 = &s;     // immutable borrow
// let r2 = &mut s;  // ERROR: can't borrow as mutable
println!("{}", r1);
```

### Non-Lexical Lifetimes (NLL)

```rust
let mut s = String::from("hello");

let r1 = &s;
let r2 = &s;
println!("{} {}", r1, r2);
// r1 and r2 no longer used

let r3 = &mut s;  // OK! r1 and r2 are "done"
r3.push_str(" world");
```

## Common Patterns

### 1. Taking Ownership and Returning

```rust
fn process(s: String) -> String {
    format!("{} processed", s)
}

let s = String::from("data");
let s = process(s);  // Ownership transferred and returned
```

### 2. Borrowing for Read-Only

```rust
fn analyze(data: &[i32]) -> i32 {
    data.iter().sum()
}

let numbers = vec![1, 2, 3, 4, 5];
let sum = analyze(&numbers);
println!("Sum: {}, Numbers: {:?}", sum, numbers);  // numbers still valid
```

### 3. Mutable Borrowing for Modification

```rust
fn append_world(s: &mut String) {
    s.push_str(" world");
}

let mut greeting = String::from("hello");
append_world(&mut greeting);
println!("{}", greeting);  // "hello world"
```

### 4. Clone When You Need Both

```rust
fn process(s: String) -> String {
    format!("{} done", s)
}

let original = String::from("data");
let result = process(original.clone());
println!("Original: {}, Result: {}", original, result);
```

## Error Solutions

### E0382: Value borrowed after move

```rust
// Error
let s = String::from("hello");
let s2 = s;
println!("{}", s);  // Error: s moved

// Solutions:
// 1. Clone
let s2 = s.clone();

// 2. Use reference
let s2 = &s;

// 3. Restructure to not need both
```

### E0502: Cannot borrow as mutable

```rust
// Error
let mut v = vec![1, 2, 3];
let first = &v[0];
v.push(4);  // Error: v borrowed immutably
println!("{}", first);

// Solution: Complete immutable use first
let mut v = vec![1, 2, 3];
let first = v[0];  // Copy the value
v.push(4);
println!("{}", first);
```

### E0499: Cannot borrow as mutable more than once

```rust
// Error
let mut s = String::from("hello");
let r1 = &mut s;
let r2 = &mut s;  // Error

// Solution: Use one at a time
let mut s = String::from("hello");
{
    let r1 = &mut s;
    r1.push_str(" world");
}  // r1 goes out of scope
let r2 = &mut s;  // OK now
```

## Lifetime Basics

### Function Lifetime Annotations

```rust
// The returned reference lives as long as the shortest input
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Struct Lifetime Annotations

```rust
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    fn level(&self) -> i32 {
        3
    }

    // Lifetime elision: &self lifetime returned
    fn announce_and_return(&self, announcement: &str) -> &str {
        println!("Attention: {}", announcement);
        self.part
    }
}
```

### Lifetime Elision Rules

1. Each input reference gets its own lifetime
2. If exactly one input lifetime, it's assigned to all outputs
3. If `&self` or `&mut self`, self's lifetime is assigned to outputs

## Best Practices

1. **Prefer borrowing over ownership** when you don't need to own
2. **Use `&str` instead of `String`** for function parameters when possible
3. **Clone sparingly** - it's a code smell if overused
4. **Let the compiler guide you** - error messages are helpful
5. **Use NLL** - structure code to minimize borrow scopes
