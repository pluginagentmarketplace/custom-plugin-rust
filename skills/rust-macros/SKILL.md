---
name: rust-macros
description: Rust macros - declarative and procedural macros
sasmp_version: "1.3.0"
bonded_agent: rust-advanced
bond_type: PRIMARY_BOND
---

# Rust Macros Skill

## Declarative Macros (macro_rules!)

```rust
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
}

say_hello!();

// With parameters
macro_rules! create_function {
    ($func_name:ident) => {
        fn $func_name() {
            println!("Called {:?}()", stringify!($func_name));
        }
    };
}

create_function!(foo);
foo();

// Pattern matching
macro_rules! vec_of_strings {
    ($($x:expr),*) => {
        vec![$($x.to_string()),*]
    };
}

let v = vec_of_strings!["a", "b", "c"];
```

## Fragment Types

| Fragment | Matches |
|----------|---------|
| item | Function, struct, etc. |
| block | Block {} |
| stmt | Statement |
| expr | Expression |
| pat | Pattern |
| ty | Type |
| ident | Identifier |
| path | Path |
| tt | Token tree |
| literal | Literal |

## Procedural Macros

```rust
// In proc-macro crate
use proc_macro::TokenStream;

#[proc_macro_derive(MyTrait)]
pub fn my_trait_derive(input: TokenStream) -> TokenStream {
    // Implementation
}

// Attribute macro
#[proc_macro_attribute]
pub fn my_attribute(attr: TokenStream, item: TokenStream) -> TokenStream {
    item
}

// Function-like macro
#[proc_macro]
pub fn my_macro(input: TokenStream) -> TokenStream {
    input
}
```

## Common Macros

```rust
println!("Value: {}", x);
format!("Hello, {}!", name);
vec![1, 2, 3];
panic!("Error!");
assert!(condition);
assert_eq!(a, b);
dbg!(expression);
todo!();
unimplemented!();
```

## Quick Reference

| Type | Usage |
|------|-------|
| macro_rules! | Declarative |
| #[derive] | Derive macro |
| #[attribute] | Attribute macro |
| proc_macro! | Function macro |

## Related
- rust-advanced agent
- rust-traits - Derive macros
