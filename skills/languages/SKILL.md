---
name: programming-languages-core
description: Master programming fundamentals, algorithms, data structures, and multiple languages. Covers Python, Java, Go, Rust, C++, Kotlin, Bash, and computer science essentials for every developer.
---

# Programming Languages & Core CS

## Quick Start

### Python - Versatile & Readable
```python
# Data structures
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers if x % 2 == 0]

# Functions
def process_data(data, transform=None):
    """Process data with optional transform."""
    if transform:
        return [transform(x) for x in data]
    return data

# Classes
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"
```

### Java - Object-Oriented & Typed
```java
public class User {
  private String name;
  private int age;

  public User(String name, int age) {
    this.name = name;
    this.age = age;
  }

  public String getName() {
    return name;
  }

  // Collections
  List<User> users = new ArrayList<>();
  users.stream()
    .filter(u -> u.age > 18)
    .map(User::getName)
    .forEach(System.out::println);
}
```

### Go - Concurrent & Fast
```go
package main

import "fmt"

// Goroutines for concurrency
func fetchData(url string, ch chan string) {
    // fetch and send result
    ch <- result
}

func main() {
    ch := make(chan string)
    go fetchData("url1", ch)
    go fetchData("url2", ch)

    result1 := <-ch
    result2 := <-ch
    fmt.Println(result1, result2)
}
```

### Rust - Memory Safety & Performance
```rust
// Ownership system
fn main() {
    let mut s = String::from("hello");
    s.push_str(" world");
    println!("{}", s);

    // Pattern matching
    match result {
        Ok(value) => println!("{}", value),
        Err(e) => eprintln!("Error: {}", e),
    }
}

// Iterators
let sum: i32 = (1..10)
    .filter(|x| x % 2 == 0)
    .map(|x| x * 2)
    .sum();
```

### C++ - Performance-Critical Systems
```cpp
#include <vector>
#include <algorithm>

class Vector {
private:
    std::vector<int> data;
public:
    void push(int value) {
        data.push_back(value);
    }

    // Move semantics
    Vector(Vector&& other) noexcept
        : data(std::move(other.data)) {}
};
```

### Kotlin - Pragmatic JVM Language
```kotlin
// Data class
data class User(val name: String, val age: Int)

// Extension functions
fun <T> List<T>.second(): T = this[1]

// Coroutines
suspend fun fetchUser(id: Int): User {
    return withContext(Dispatchers.IO) {
        // async operation
    }
}
```

### Bash/Shell - System Automation
```bash
#!/bin/bash

# Variables and expansions
readonly CONFIG_DIR="${HOME}/.config"

# Functions
backup_files() {
    local source=$1
    local dest=$2
    cp -r "$source" "$dest"
}

# Conditionals and loops
for file in *.log; do
    [[ -f "$file" ]] && rm "$file"
done

# Command substitution
files=$(find . -name "*.rs" | wc -l)
echo "Found $files Rust files"
```

## Algorithms & Complexity

### Big O Analysis
```
O(1)   - Constant time: direct access
O(log n) - Logarithmic: binary search
O(n)   - Linear: simple loop
O(n log n) - Log-linear: efficient sorting
O(n²)  - Quadratic: nested loops
O(2ⁿ)  - Exponential: rarely acceptable
O(n!)  - Factorial: avoid at all costs
```

### Common Algorithms

#### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
```

#### Quick Sort
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
```

## Data Structures

### Linked List
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
```

### Binary Tree
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# In-order traversal
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)
```

### Hash Map
```python
# Dictionary in Python
cache = {}
cache['key'] = 'value'
value = cache.get('key', 'default')
```

## Learning Paths

### Python (roadmap.sh/python)
- Fundamentals & syntax
- Data structures
- OOP & design patterns
- Web frameworks (Django, Flask)
- Data science & ML libraries

### Java (roadmap.sh/java)
- Core concepts & syntax
- OOP & design patterns
- Collections framework
- Concurrency & threading
- Spring ecosystem

### Go (roadmap.sh/golang)
- Goroutines & channels
- Interfaces
- Package management
- HTTP servers
- Microservices

### Rust (roadmap.sh/rust) ⭐ Featured
- Ownership & borrowing
- Pattern matching
- Error handling
- Memory safety
- Systems programming

### C++ (roadmap.sh/cpp)
- Standard library
- Memory management
- Templates
- Modern C++ (17, 20)
- Performance optimization

### Kotlin (roadmap.sh/kotlin)
- JVM fundamentals
- Extension functions
- Coroutines
- Null safety
- Interoperability

### Bash/Shell (roadmap.sh/shell-bash)
- Script basics
- Variables & expansions
- Functions
- Error handling
- System administration

## Computer Science Fundamentals (roadmap.sh/computer-science)

- **Algorithms** (roadmap.sh/datastructures-and-algorithms)
- **Data Structures**
- **Complexity Analysis**
- **Problem-Solving**
- **Coding Patterns**

## Language Comparison

| Language | Type | Performance | Learning | Use Case |
|----------|------|-------------|----------|----------|
| Python | Dynamic | Medium | Easy | Data science, scripting |
| Java | Static | Fast | Medium | Enterprise systems |
| Go | Static | Fast | Easy | Microservices, cloud |
| Rust | Static | Fastest | Hard | Systems, WebAssembly |
| C++ | Static | Fastest | Hard | Performance critical |
| Kotlin | Static | Fast | Easy | Android, JVM |
| Bash | Scripting | Slow | Easy | System automation |

## Interview Preparation

Key topics to master:
- [ ] Two-pointer techniques
- [ ] Sliding window
- [ ] Dynamic programming
- [ ] Graph algorithms (DFS, BFS)
- [ ] Tree traversals
- [ ] Hash tables
- [ ] Sorting algorithms
- [ ] Search algorithms

## Resources

- [LeetCode](https://leetcode.com) - Algorithm practice
- [HackerRank](https://hackerrank.com) - Coding challenges
- [GeeksforGeeks](https://geeksforgeeks.org) - DSA tutorials
- Language-specific docs
