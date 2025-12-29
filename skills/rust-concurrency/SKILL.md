---
name: rust-concurrency
description: Rust concurrency - threads, channels, Mutex, Arc
sasmp_version: "1.3.0"
bonded_agent: rust-concurrency
bond_type: PRIMARY_BOND
---

# Rust Concurrency Skill

## Threads

```rust
use std::thread;
use std::time::Duration;

// Spawn thread
let handle = thread::spawn(|| {
    for i in 1..10 {
        println!("Thread: {}", i);
        thread::sleep(Duration::from_millis(1));
    }
});

handle.join().unwrap();

// Move closure
let v = vec![1, 2, 3];
let handle = thread::spawn(move || {
    println!("{:?}", v);
});
```

## Channels

```rust
use std::sync::mpsc;

// Create channel
let (tx, rx) = mpsc::channel();

// Send
thread::spawn(move || {
    tx.send(String::from("hello")).unwrap();
});

// Receive
let received = rx.recv().unwrap();

// Multiple producers
let tx1 = tx.clone();

// Iterate over received
for received in rx {
    println!("{}", received);
}
```

## Mutex

```rust
use std::sync::Mutex;

let m = Mutex::new(5);

{
    let mut num = m.lock().unwrap();
    *num = 6;
}  // Lock released here

// Arc + Mutex for shared state
use std::sync::Arc;

let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];

for _ in 0..10 {
    let counter = Arc::clone(&counter);
    let handle = thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    });
    handles.push(handle);
}

for handle in handles {
    handle.join().unwrap();
}
```

## Quick Reference

| Type | Use Case |
|------|----------|
| thread::spawn | Create thread |
| channel | Message passing |
| Mutex | Mutual exclusion |
| RwLock | Read-write lock |
| Arc | Thread-safe Rc |
| Barrier | Synchronize threads |

## Related
- rust-async - Async/await
- rust-concurrency agent
