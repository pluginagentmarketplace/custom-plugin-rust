# Rust Async Programming Complete Guide

## Understanding Async in Rust

Rust's async model is based on **futures** - values that represent computations that may complete in the future.

```rust
// This is a Future
async fn fetch_data() -> Data {
    // ...
}

// Calling it returns a Future, doesn't execute
let future = fetch_data();

// .await executes the future
let data = future.await;
```

## The Tokio Runtime

Tokio is the most popular async runtime for Rust.

### Basic Setup

```rust
// Simple setup
#[tokio::main]
async fn main() {
    println!("Hello async world!");
}

// Custom configuration
#[tokio::main(flavor = "multi_thread", worker_threads = 4)]
async fn main() {
    // ...
}
```

## Core Concepts

### 1. Spawning Tasks

```rust
// Fire and forget
tokio::spawn(async {
    process_background().await;
});

// Get the result
let handle = tokio::spawn(async {
    compute_something().await
});
let result = handle.await?;
```

### 2. Concurrent Execution

```rust
// Run futures concurrently, wait for all
let (a, b, c) = tokio::join!(
    fetch_user(id),
    fetch_orders(id),
    fetch_preferences(id)
);

// Race futures, first wins
tokio::select! {
    result = operation_a() => handle_a(result),
    result = operation_b() => handle_b(result),
    _ = tokio::time::sleep(Duration::from_secs(5)) => {
        println!("Timeout!");
    }
}
```

### 3. Channels

```rust
use tokio::sync::mpsc;

// Bounded channel (recommended)
let (tx, mut rx) = mpsc::channel::<Message>(100);

// Producer
tokio::spawn(async move {
    tx.send(Message::new()).await.ok();
});

// Consumer
while let Some(msg) = rx.recv().await {
    process(msg);
}
```

### 4. Synchronization

```rust
use tokio::sync::{Mutex, RwLock, Semaphore};

// Async Mutex
let data = Arc::new(Mutex::new(Vec::new()));
{
    let mut lock = data.lock().await;
    lock.push(item);
} // Lock released here

// Rate limiting with Semaphore
let semaphore = Arc::new(Semaphore::new(10));
let permit = semaphore.acquire().await?;
// Do work
drop(permit); // Release permit
```

## Common Patterns

### Pattern 1: Request-Response with oneshot

```rust
use tokio::sync::oneshot;

struct Request {
    data: String,
    response_tx: oneshot::Sender<Response>,
}

// Requester
let (tx, rx) = oneshot::channel();
actor_tx.send(Request { data, response_tx: tx }).await?;
let response = rx.await?;

// Actor
while let Some(req) = rx.recv().await {
    let response = process(req.data);
    req.response_tx.send(response).ok();
}
```

### Pattern 2: Graceful Shutdown

```rust
use tokio::signal;
use tokio::sync::broadcast;

let (shutdown_tx, _) = broadcast::channel(1);

// Main task
tokio::select! {
    _ = server.run() => {},
    _ = signal::ctrl_c() => {
        println!("Shutting down...");
        shutdown_tx.send(()).ok();
    }
}

// Worker task
let mut shutdown_rx = shutdown_tx.subscribe();
loop {
    tokio::select! {
        Some(work) = work_rx.recv() => process(work).await,
        _ = shutdown_rx.recv() => break,
    }
}
```

### Pattern 3: Connection Pool

```rust
use tokio::sync::Semaphore;

struct Pool {
    semaphore: Semaphore,
    connections: Mutex<Vec<Connection>>,
}

impl Pool {
    async fn get(&self) -> PooledConnection {
        let permit = self.semaphore.acquire().await.unwrap();
        let conn = self.connections.lock().await.pop().unwrap();
        PooledConnection { conn, permit, pool: self }
    }

    fn return_conn(&self, conn: Connection) {
        self.connections.lock().await.push(conn);
    }
}
```

### Pattern 4: Timeout with Retry

```rust
async fn fetch_with_retry<T, F, Fut>(
    mut f: F,
    max_retries: u32,
    timeout_duration: Duration,
) -> Result<T>
where
    F: FnMut() -> Fut,
    Fut: Future<Output = Result<T>>,
{
    for attempt in 0..max_retries {
        match tokio::time::timeout(timeout_duration, f()).await {
            Ok(Ok(result)) => return Ok(result),
            Ok(Err(e)) if attempt == max_retries - 1 => return Err(e),
            _ => {
                let backoff = Duration::from_millis(100 * 2_u64.pow(attempt));
                tokio::time::sleep(backoff).await;
            }
        }
    }
    unreachable!()
}
```

## Anti-Patterns to Avoid

### ❌ Blocking in Async

```rust
// BAD
async fn bad() {
    std::thread::sleep(Duration::from_secs(1)); // Blocks entire runtime!
}

// GOOD
async fn good() {
    tokio::time::sleep(Duration::from_secs(1)).await;
}
```

### ❌ CPU Work in Async

```rust
// BAD
async fn bad() {
    let result = heavy_computation(); // Blocks other tasks!
}

// GOOD
async fn good() {
    let result = tokio::task::spawn_blocking(|| {
        heavy_computation()
    }).await?;
}
```

### ❌ Holding Locks Across Await

```rust
// BAD - lock held across await point
async fn bad(data: Arc<Mutex<Vec<i32>>>) {
    let mut lock = data.lock().await;
    expensive_operation().await; // Lock still held!
    lock.push(1);
}

// GOOD - minimize lock scope
async fn good(data: Arc<Mutex<Vec<i32>>>) {
    let item = expensive_operation().await;
    data.lock().await.push(item);
}
```

## Testing Async Code

```rust
#[tokio::test]
async fn test_async_function() {
    let result = my_async_function().await;
    assert_eq!(result, expected);
}

#[tokio::test(flavor = "multi_thread", worker_threads = 2)]
async fn test_concurrent() {
    // Test with multi-threaded runtime
}
```

## Resources

- [Tokio Tutorial](https://tokio.rs/tokio/tutorial)
- [Async Book](https://rust-lang.github.io/async-book/)
- [Tokio API Docs](https://docs.rs/tokio)
