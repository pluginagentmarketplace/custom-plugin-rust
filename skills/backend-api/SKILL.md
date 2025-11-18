---
name: backend-api-development
description: Master backend development, API design, server architecture, database integration, authentication, microservices, and production patterns. Includes Node.js, GraphQL, Spring Boot, ASP.NET Core, and PHP frameworks.
---

# Backend & API Development

## Quick Start

Modern backend development requires understanding multiple layers of architecture and design:

### Node.js with Express
```javascript
const express = require('express');
const app = express();

// Middleware
app.use(express.json());
app.use(require('cors')());

// Routes
app.get('/api/users/:id', async (req, res) => {
  try {
    const user = await User.findById(req.params.id);
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(3000);
```

### GraphQL Server
```javascript
const { ApolloServer, gql } = require('apollo-server-express');

const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post]
  }

  type Query {
    user(id: ID!): User
    users: [User]
  }

  type Mutation {
    createUser(input: CreateUserInput!): User
  }
`;

const resolvers = {
  Query: {
    user: (_, { id }) => User.findById(id),
    users: () => User.find(),
  },
  Mutation: {
    createUser: (_, { input }) => User.create(input),
  },
};
```

### Spring Boot (Java)
```java
@RestController
@RequestMapping("/api/users")
public class UserController {

  @Autowired
  private UserService userService;

  @GetMapping("/{id}")
  public ResponseEntity<UserDTO> getUser(@PathVariable String id) {
    User user = userService.findById(id);
    return ResponseEntity.ok(mapToDTO(user));
  }

  @PostMapping
  public ResponseEntity<UserDTO> createUser(@RequestBody CreateUserRequest req) {
    User user = userService.create(req);
    return ResponseEntity.status(201).body(mapToDTO(user));
  }
}
```

### ASP.NET Core
```csharp
[ApiController]
[Route("api/[controller]")]
public class UsersController : ControllerBase {

  private readonly IUserService _userService;

  public UsersController(IUserService userService) {
    _userService = userService;
  }

  [HttpGet("{id}")]
  public async Task<ActionResult<UserDto>> GetUser(string id) {
    var user = await _userService.GetUserAsync(id);
    if (user == null)
      return NotFound();
    return Ok(user);
  }

  [HttpPost]
  public async Task<ActionResult<UserDto>> CreateUser(CreateUserDto dto) {
    var user = await _userService.CreateUserAsync(dto);
    return CreatedAtAction(nameof(GetUser), new { id = user.Id }, user);
  }
}
```

### RESTful API Design
```
GET    /api/users              - List all users
GET    /api/users/{id}         - Get single user
POST   /api/users              - Create new user
PUT    /api/users/{id}         - Update user
PATCH  /api/users/{id}         - Partial update
DELETE /api/users/{id}         - Delete user
```

### Authentication with JWT
```javascript
const jwt = require('jsonwebtoken');

// Generate token
function generateToken(user) {
  return jwt.sign(
    { id: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  );
}

// Verify middleware
function verifyToken(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
}

app.get('/api/protected', verifyToken, (req, res) => {
  res.json({ user: req.user });
});
```

### Error Handling
```javascript
class AppError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
  }
}

// Global error handler
app.use((error, req, res, next) => {
  const statusCode = error.statusCode || 500;
  const message = error.message || 'Internal Server Error';

  res.status(statusCode).json({
    status: 'error',
    statusCode,
    message,
    ...(process.env.NODE_ENV === 'development' && { stack: error.stack }),
  });
});
```

### Database Integration with ORM
```javascript
// Sequelize (Node.js)
const user = await User.create({
  name: 'John',
  email: 'john@example.com',
});

// Typeorm (Node.js/TypeScript)
@Entity()
export class User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column()
  name: string;

  @Column({ unique: true })
  email: string;

  @OneToMany(() => Post, post => post.user)
  posts: Post[];
}
```

## Learning Paths

### Backend Fundamentals
1. **Node.js** (roadmap.sh/nodejs)
   - Event-driven architecture
   - NPM/yarn ecosystem
   - Asynchronous patterns

2. **REST API Design** (roadmap.sh/api-design)
   - HTTP methods
   - Status codes
   - Versioning strategies

3. **GraphQL** (roadmap.sh/graphql)
   - Schema design
   - Query and mutation resolvers
   - Subscriptions

4. **Spring Boot** (roadmap.sh/spring-boot)
   - Dependency injection
   - JPA/Hibernate
   - Spring Security

5. **ASP.NET Core** (roadmap.sh/aspnet-core)
   - Middleware pipeline
   - Dependency injection
   - Entity Framework

6. **PHP** (roadmap.sh/php)
   - Modern PHP (8.0+)
   - Laravel/Symfony frameworks
   - PSR standards

### Advanced Topics

- **Microservices Architecture**
  - Service discovery
  - API gateways
  - Event streaming (Kafka, RabbitMQ)

- **Caching Strategies**
  - Redis usage
  - Cache invalidation
  - Cache-aside patterns

- **Testing & Quality**
  - Unit testing
  - Integration testing
  - Test coverage

## Deployment & DevOps

```yaml
# Docker for backend
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
```

## Performance Optimization

- **Database Optimization**
  - Indexing strategies
  - Query optimization
  - Connection pooling

- **Caching**
  - Response caching
  - Database query caching
  - CDN usage

- **Monitoring**
  - Request logging
  - Performance metrics
  - Error tracking

## Security Best Practices

- [ ] Input validation
- [ ] SQL injection prevention
- [ ] CORS configuration
- [ ] Rate limiting
- [ ] HTTPS enforcement
- [ ] Secure headers (HSTS, CSP)
- [ ] Authentication & authorization
- [ ] Secrets management
- [ ] Regular dependency updates
- [ ] Security audits

## Key Frameworks Summary

| Framework | Language | Best For | Popularity |
|-----------|----------|----------|------------|
| Express | Node.js | Lightweight APIs | ⭐⭐⭐⭐⭐ |
| NestJS | TypeScript | Enterprise apps | ⭐⭐⭐⭐ |
| Spring Boot | Java | Large systems | ⭐⭐⭐⭐⭐ |
| ASP.NET Core | C# | Enterprise | ⭐⭐⭐⭐ |
| Laravel | PHP | Web apps | ⭐⭐⭐⭐ |

## Resources

- [REST API Best Practices](https://restfulapi.net)
- [GraphQL Official Docs](https://graphql.org)
- [OpenAPI/Swagger](https://swagger.io)
