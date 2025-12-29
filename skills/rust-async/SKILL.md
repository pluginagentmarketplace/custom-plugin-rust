---
name: rust-async
description: Rust async programming - async/await, futures, tokio
sasmp_version: "1.3.0"
bonded_agent: rust-async
bond_type: PRIMARY_BOND
---

# Rust Async Skill

## async/await Basics

```rust
async fn hello() -> String {
    String::from("Hello, async!")
}

async fn greet() {
    let msg = hello().await;
    println!("{}", msg);
}

// Async block
let future = async {
    let x = foo().await;
    let y = bar().await;
    x + y
};
```

## tokio Runtime

```rust
use tokio;

#[tokio::main]
async fn main() {
    let result = some_async_function().await;
}

// Manual runtime
let rt = tokio::runtime::Runtime::new().unwrap();
rt.block_on(async {
    // async code
});

// Spawn tasks
tokio::spawn(async {
    // Runs concurrently
});
```

## Concurrent Execution

```rust
use tokio::join;

// Run concurrently
let (a, b, c) = join!(
    fetch_a(),
    fetch_b(),
    fetch_c()
);

// Select first completed
use tokio::select;
select! {
    val = future1 => { }
    val = future2 => { }
}
```

## HTTP Client Example

```rust
use reqwest;

#[tokio::main]
async fn main() -> Result<(), reqwest::Error> {
    let body = reqwest::get("https://api.example.com")
        .await?
        .text()
        .await?;
    
    println!("{}", body);
    Ok(())
}
```

## Quick Reference

| Concept | Description |
|---------|-------------|
| async fn | Async function |
| .await | Wait for future |
| tokio::spawn | Spawn task |
| join! | Concurrent execution |
| select! | Race futures |

## Related
- rust-concurrency - Threads
- rust-async agent
