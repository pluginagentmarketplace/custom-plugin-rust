# Memory Layout Diagrams

## String Memory Layout

```
Stack                              Heap
┌───────────────────┐              ┌─────────────────────┐
│ String            │              │                     │
├───────────────────┤              │  h  e  l  l  o      │
│ ptr ──────────────────────────▶  │                     │
│ len: 5            │              └─────────────────────┘
│ capacity: 5       │
└───────────────────┘
```

## Move Semantics

```
BEFORE MOVE:
┌─────────────────┐
│ s1              │     ┌─────────────────┐
│ ptr ────────────────▶ │ "hello"         │
│ len: 5          │     └─────────────────┘
│ capacity: 5     │
└─────────────────┘

AFTER: let s2 = s1;
┌─────────────────┐
│ s1 (INVALID)    │
│ ─ ─ ─ ─ ─ ─ ─   │
└─────────────────┘

┌─────────────────┐
│ s2              │     ┌─────────────────┐
│ ptr ────────────────▶ │ "hello"         │
│ len: 5          │     └─────────────────┘
│ capacity: 5     │
└─────────────────┘
```

## Clone vs Move

```
CLONE: let s2 = s1.clone();

┌─────────────────┐     ┌─────────────────┐
│ s1              │     │ "hello"         │
│ ptr ────────────────▶ │                 │
│ len: 5          │     └─────────────────┘
│ capacity: 5     │
└─────────────────┘

┌─────────────────┐     ┌─────────────────┐
│ s2              │     │ "hello"         │
│ ptr ────────────────▶ │ (copy)          │
│ len: 5          │     └─────────────────┘
│ capacity: 5     │
└─────────────────┘

Both s1 and s2 are valid!
```

## Borrowing Diagram

```
IMMUTABLE BORROW: let r = &s;

┌─────────────────┐
│ s (owner)       │     ┌─────────────────┐
│ ptr ────────────────▶ │ "hello"         │
│ len: 5          │     └─────────────────┘
└─────────────────┘           ▲
                              │
┌─────────────────┐           │
│ r (&s)          │───────────┘
│ (reference)     │
└─────────────────┘

s retains ownership
r can READ but not modify
```

## Mutable Borrow

```
MUTABLE BORROW: let r = &mut s;

┌─────────────────┐
│ s (owner)       │     ┌─────────────────┐
│ ptr ────────────────▶ │ "hello"         │
│ len: 5          │     └─────────────────┘
└─────────────────┘           ▲
     [LOCKED]                 │
                              │
┌─────────────────┐           │
│ r (&mut s)      │───────────┘
│ (mut reference) │
└─────────────────┘

s cannot be used while r exists
r can READ and MODIFY
```

## Lifetime Scope

```
fn main() {
    let s1 = String::from("hello");  // ─┐ 's1 lifetime
                                      //  │
    {                                 //  │
        let s2 = String::from("hi");  // ─┼─┐ 's2 lifetime
        let r = longest(&s1, &s2);    //  │ │
        println!("{}", r);            //  │ │
    }                                 //  │ │ s2 dropped
                                      //  │ ◀─┘
    println!("{}", s1);               //  │
}                                     // ─┘ s1 dropped
```
