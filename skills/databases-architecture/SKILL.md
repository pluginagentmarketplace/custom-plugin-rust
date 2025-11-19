---
name: databases-architecture-design
description: Master database design, optimization, and software architecture. Learn PostgreSQL, SQL, Redis, MongoDB, system design patterns, SOLID principles, and building scalable systems that can grow with demand.
---

# Databases & Architecture

## Quick Start

### SQL (PostgreSQL) Fundamentals
```sql
-- Create table with constraints
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created ON users(created_at);

-- Queries
SELECT u.id, u.name, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id, u.name
HAVING COUNT(p.id) > 0
ORDER BY post_count DESC;

-- Transactions with rollback
BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Window functions
SELECT
  user_id,
  amount,
  SUM(amount) OVER (PARTITION BY user_id ORDER BY date) as running_total
FROM transactions;
```

### PostgreSQL Advanced Features
```sql
-- JSON support
CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  data JSONB NOT NULL
);

SELECT data->>'user_id' as user_id
FROM events
WHERE data @> '{"type": "purchase"}'::jsonb;

-- Full-text search
CREATE TABLE articles (
  id SERIAL PRIMARY KEY,
  title TEXT,
  content TEXT,
  search_vector tsvector
);

INSERT INTO articles (title, content, search_vector)
VALUES ('AI Revolution', 'Article about AI',
        to_tsvector('english', 'AI Revolution'));

SELECT * FROM articles
WHERE search_vector @@ to_tsquery('english', 'AI');

-- Stored procedures
CREATE FUNCTION get_user_posts(p_user_id INT)
RETURNS TABLE(post_id INT, title TEXT) AS $$
BEGIN
  RETURN QUERY
  SELECT id, title FROM posts WHERE user_id = p_user_id;
END;
$$ LANGUAGE plpgsql;
```

### Redis - Caching & Data Structures
```python
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# String operations
r.set('user:1:name', 'John')
name = r.get('user:1:name')

# Key expiration (TTL)
r.setex('session:abc123', 3600, 'user_data')  # 1 hour

# Hash operations
r.hset('user:1', mapping={'name': 'John', 'email': 'john@example.com'})
user_data = r.hgetall('user:1')

# List operations (queue)
r.lpush('queue:jobs', 'job1', 'job2')
job = r.rpop('queue:jobs')

# Set operations
r.sadd('user:1:tags', 'python', 'devops')
tags = r.smembers('user:1:tags')

# Sorted set (leaderboard)
r.zadd('leaderboard', {'player1': 100, 'player2': 95})
r.zrevrange('leaderboard', 0, 10, withscores=True)

# Caching pattern
def get_user(user_id):
    # Check cache first
    cached = r.get(f'user:{user_id}')
    if cached:
        return json.loads(cached)

    # Get from database if not in cache
    user = db.fetch_user(user_id)
    r.setex(f'user:{user_id}', 3600, json.dumps(user))
    return user
```

### MongoDB - NoSQL Document Database
```javascript
// Connect to MongoDB
const mongoose = require('mongoose');
await mongoose.connect('mongodb://localhost/mydb');

// Define schema
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, unique: true },
  profile: {
    bio: String,
    avatar: String
  },
  posts: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Post' }],
  createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);

// CRUD operations
// Create
const user = new User({ name: 'John', email: 'john@example.com' });
await user.save();

// Read
const user = await User.findById(userId).populate('posts');
const users = await User.find({ name: /john/i });

// Update
await User.updateOne({ _id: userId }, { $set: { 'profile.bio': 'New bio' } });

// Delete
await User.deleteOne({ _id: userId });

// Aggregation pipeline
const result = await User.aggregate([
  { $match: { createdAt: { $gte: new Date('2024-01-01') } } },
  { $group: { _id: '$email', count: { $sum: 1 } } },
  { $sort: { count: -1 } }
]);
```

## Database Design Principles

### Normalization (SQL)
```sql
-- ❌ Not normalized (data duplication)
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_name VARCHAR(255),
  customer_email VARCHAR(255),
  product_name VARCHAR(255),
  product_price DECIMAL
);

-- ✅ Normalized (1st Normal Form)
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  price DECIMAL
);

CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT REFERENCES customers(id),
  product_id INT REFERENCES products(id)
);
```

### Denormalization (Performance)
```sql
-- Trade consistency for query speed
CREATE TABLE user_stats (
  user_id INT PRIMARY KEY,
  post_count INT,
  follower_count INT,
  updated_at TIMESTAMP
);

-- Update stats periodically with triggers or background jobs
CREATE TRIGGER update_user_stats
AFTER INSERT ON posts
BEGIN
  UPDATE user_stats
  SET post_count = post_count + 1
  WHERE user_id = NEW.user_id;
END;
```

## Learning Paths

### SQL (roadmap.sh/sql)
- SELECT queries
- JOINs and subqueries
- Aggregation
- Window functions
- Transactions

### PostgreSQL DBA (roadmap.sh/postgresql-dba)
- Installation and configuration
- Backup and recovery
- Performance tuning
- Replication
- Security management

### Redis (roadmap.sh/redis)
- Data structures
- Caching patterns
- Pub/Sub
- Transactions
- Persistence

### MongoDB (roadmap.sh/mongodb)
- Document model
- Indexing
- Aggregation
- Transactions
- Sharding

## Architecture Patterns

### Microservices Architecture
```
┌─────────────────────────────┐
│     API Gateway             │
└──────────────┬──────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
┌──────┐  ┌──────┐  ┌──────┐
│User  │  │Order │  │Payment│
│Service│  │Service│ │Service│
└──┬───┘  └──┬───┘  └──┬───┘
   │         │         │
  [DB]     [DB]      [DB]
```

### Event-Driven Architecture
```python
# Publisher
def create_order(order_data):
    order = Order.create(order_data)
    message_queue.publish('order.created', {'order_id': order.id})
    return order

# Subscriber
def on_order_created(event):
    order_id = event['order_id']
    send_confirmation_email(order_id)
    update_inventory(order_id)
    trigger_shipping(order_id)
```

### CQRS (Command Query Responsibility Segregation)
```
┌──────────────┐  ┌──────────────┐
│   Commands   │  │    Queries   │
│  (Write)     │  │    (Read)    │
└──────┬───────┘  └──────┬───────┘
       │                 │
    [Write DB]      [Read DB]
         └────────────┘
         (Event Stream)
```

## Design Patterns

### Singleton Pattern
```python
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = create_connection()
        return cls._instance

db = Database()
```

### Factory Pattern
```python
class RepositoryFactory:
    @staticmethod
    def create(type_: str):
        repositories = {
            'user': UserRepository,
            'product': ProductRepository,
            'order': OrderRepository,
        }
        return repositories[type_]()
```

### Observer Pattern
```python
class Observable:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)

class EmailObserver:
    def update(self, event):
        send_email(event)
```

## SOLID Principles

- **S**ingle Responsibility: One class, one reason to change
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subtypes must be substitutable
- **I**nterface Segregation: Many specific interfaces, not one general
- **D**ependency Inversion: Depend on abstractions, not concretions

## System Design

### Scalability Considerations
```
Scale Horizontally:
- Multiple database replicas
- Load balancing
- Sharding
- Caching layers

Scale Vertically:
- More CPU/Memory
- Faster disks
- Better network
```

### CAP Theorem
- **C**onsistency: All nodes have same data
- **A**vailability: System is always responsive
- **P**artition Tolerance: System works despite network failures

Choose 2 of 3 based on your requirements.

## Learning Paths

- **PostgreSQL DBA** (roadmap.sh/postgresql-dba)
- **SQL** (roadmap.sh/sql)
- **Redis** (roadmap.sh/redis)
- **MongoDB** (roadmap.sh/mongodb)
- **Software Design & Architecture** (roadmap.sh/software-design-architecture)
- **Software Architect** (roadmap.sh/software-architect)
- **System Design** (roadmap.sh/system-design)

## Resources

- [PostgreSQL Official Docs](https://www.postgresql.org/docs)
- [Redis Documentation](https://redis.io/documentation)
- [MongoDB Manual](https://docs.mongodb.com/manual)
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
