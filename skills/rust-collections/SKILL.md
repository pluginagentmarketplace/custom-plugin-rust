---
name: rust-collections
description: Rust collections - Vec, HashMap, HashSet, and iterators
sasmp_version: "1.3.0"
bonded_agent: rust-fundamentals
bond_type: SECONDARY_BOND
---

# Rust Collections Skill

## Vec<T>

```rust
// Creation
let v: Vec<i32> = Vec::new();
let v = vec![1, 2, 3];
let v = Vec::with_capacity(10);

// Operations
v.push(4);
v.pop();
v.len();
v.is_empty();
v.insert(0, 0);
v.remove(0);

// Access
let third = &v[2];
let third = v.get(2);  // Option<&T>

// Iteration
for i in &v { }
for i in &mut v { }
for i in v { }  // Consumes vec
```

## HashMap<K, V>

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

// From iterators
let teams = vec!["Blue", "Yellow"];
let initial_scores = vec![10, 50];
let scores: HashMap<_, _> = teams.into_iter().zip(initial_scores.into_iter()).collect();

// Access
let score = scores.get("Blue");  // Option<&V>
scores.entry("Red").or_insert(25);

// Iteration
for (key, value) in &scores { }
```

## Iterators

```rust
let v = vec![1, 2, 3, 4, 5];

// Iterator methods
v.iter().map(|x| x + 1);
v.iter().filter(|&x| x % 2 == 0);
v.iter().fold(0, |acc, x| acc + x);
v.iter().sum::<i32>();
v.iter().collect::<Vec<_>>();

// Chaining
let result: Vec<i32> = v.iter()
    .filter(|&x| x % 2 == 0)
    .map(|x| x * 2)
    .collect();

// More methods
v.iter().any(|&x| x > 3);
v.iter().all(|&x| x > 0);
v.iter().find(|&&x| x > 3);
v.iter().position(|&x| x > 3);
v.iter().take(3);
v.iter().skip(2);
v.iter().enumerate();
v.iter().zip(other.iter());
```

## Quick Reference

| Collection | Use Case |
|------------|----------|
| Vec | Dynamic array |
| HashMap | Key-value store |
| HashSet | Unique values |
| VecDeque | Double-ended queue |
| BTreeMap | Sorted map |
| LinkedList | Linked list |

## Related
- rust-basics - Fundamentals
- rust-traits - Iterator trait
