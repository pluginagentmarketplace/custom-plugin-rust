---
name: mobile-blockchain-specialized
description: Expert in Mobile Development (iOS, Android, React Native, Flutter), Blockchain, Game Development, Git, Full-Stack, QA, Product Management, Technical Writing, DevRel, and Cyber Security. Build modern applications and master specialized tech roles.
---

# Mobile, Blockchain & Specialized Roles

## Quick Start

### iOS Development with SwiftUI
```swift
import SwiftUI

struct User: Codable {
    let id: String
    let name: String
    let email: String
}

@main
struct ContentView: View {
    @StateObject var viewModel = UserViewModel()

    var body: some View {
        NavigationStack {
            List(viewModel.users) { user in
                VStack(alignment: .leading) {
                    Text(user.name).font(.headline)
                    Text(user.email).font(.caption).foregroundColor(.gray)
                }
            }
            .navigationTitle("Users")
            .task {
                await viewModel.fetchUsers()
            }
        }
    }
}

class UserViewModel: ObservableObject {
    @Published var users: [User] = []

    @MainActor
    func fetchUsers() async {
        do {
            let response = try await URLSession.shared
                .data(from: URL(string: "https://api.example.com/users")!)
            let decoded = try JSONDecoder().decode([User].self, from: response.0)
            self.users = decoded
        } catch {
            print("Error: \(error)")
        }
    }
}
```

### Android Development with Kotlin
```kotlin
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.lifecycle.viewmodel.compose.viewModel

data class User(
    val id: String,
    val name: String,
    val email: String
)

@Composable
fun UserList(viewModel: UserViewModel = viewModel()) {
    val users by viewModel.users.collectAsState()

    Scaffold(
        topBar = { TopAppBar(title = { Text("Users") }) }
    ) { padding ->
        LazyColumn(modifier = Modifier.padding(padding)) {
            items(users) { user ->
                UserItem(user)
            }
        }
    }

    LaunchedEffect(Unit) {
        viewModel.loadUsers()
    }
}

@Composable
fun UserItem(user: User) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(8.dp)
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(text = user.name, style = MaterialTheme.typography.headlineSmall)
            Text(text = user.email, style = MaterialTheme.typography.bodyMedium)
        }
    }
}

class UserViewModel : ViewModel() {
    private val _users = MutableStateFlow<List<User>>(emptyList())
    val users = _users.asStateFlow()

    fun loadUsers() {
        viewModelScope.launch {
            try {
                val response = Retrofit.create(ApiService::class.java).getUsers()
                _users.value = response
            } catch (e: Exception) {
                Log.e("UserViewModel", "Error loading users", e)
            }
        }
    }
}
```

### React Native Cross-Platform
```javascript
import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, StyleSheet, ActivityIndicator } from 'react-native';

export default function UserListScreen() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await fetch('https://api.example.com/users');
      const data = await response.json();
      setUsers(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <ActivityIndicator size="large" />;

  return (
    <View style={styles.container}>
      <FlatList
        data={users}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.userCard}>
            <Text style={styles.name}>{item.name}</Text>
            <Text style={styles.email}>{item.email}</Text>
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 10 },
  userCard: { padding: 15, borderBottomWidth: 1, borderBottomColor: '#eee' },
  name: { fontSize: 18, fontWeight: 'bold' },
  email: { fontSize: 14, color: 'gray' }
});
```

### Flutter Cross-Platform
```dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: UserListScreen(),
    );
  }
}

class UserListScreen extends StatefulWidget {
  @override
  State<UserListScreen> createState() => _UserListScreenState();
}

class _UserListScreenState extends State<UserListScreen> {
  late Future<List<User>> futureUsers;

  @override
  void initState() {
    super.initState();
    futureUsers = fetchUsers();
  }

  Future<List<User>> fetchUsers() async {
    final response = await http.get(Uri.parse('https://api.example.com/users'));

    if (response.statusCode == 200) {
      List jsonResponse = json.decode(response.body);
      return jsonResponse.map((user) => User.fromJson(user)).toList();
    } else {
      throw Exception('Failed to load users');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Users')),
      body: FutureBuilder<List<User>>(
        future: futureUsers,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemCount: snapshot.data!.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(snapshot.data![index].name),
                  subtitle: Text(snapshot.data![index].email),
                );
              },
            );
          }
          return Center(child: CircularProgressIndicator());
        },
      ),
    );
  }
}

class User {
  final String id;
  final String name;
  final String email;

  User({required this.id, required this.name, required this.email});

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id'],
      name: json['name'],
      email: json['email'],
    );
  }
}
```

### Blockchain Smart Contract (Solidity)
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SimpleToken {
    mapping(address => uint256) public balances;
    uint256 public totalSupply;
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 18;

    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * 10 ** uint256(decimals);
        balances[msg.sender] = totalSupply;
    }

    function transfer(address to, uint256 value) public returns (bool) {
        require(to != address(0), "Invalid address");
        require(balances[msg.sender] >= value, "Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }

    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }
}
```

### Git Workflow
```bash
# Feature branch workflow
git checkout -b feature/user-authentication
git add .
git commit -m "feat: add user login form"
git push origin feature/user-authentication

# Create pull request on GitHub

# After review, merge
git checkout main
git pull origin main
git merge feature/user-authentication
git push origin main

# Clean up
git branch -d feature/user-authentication
git push origin --delete feature/user-authentication

# Semantic commit messages
# feat: new feature
# fix: bug fix
# docs: documentation
# style: formatting
# refactor: code restructuring
# test: adding tests
# chore: build/dependencies
```

## Learning Paths

### Mobile Development

#### iOS (roadmap.sh/ios)
- Swift basics
- UIKit vs SwiftUI
- Networking
- Core Data
- App Store deployment

#### Swift/SwiftUI (roadmap.sh/swift-ui)
- SwiftUI fundamentals
- State management
- Navigation
- Animations
- Async/await

#### Android (roadmap.sh/android)
- Kotlin basics
- Jetpack Compose
- Room database
- Firebase
- Play Store deployment

#### React Native (roadmap.sh/react-native)
- Components and navigation
- State management (Redux/Context)
- Native modules
- Performance optimization

#### Flutter (roadmap.sh/flutter)
- Dart language
- Widget composition
- State management (Provider)
- Firebase integration
- Cross-platform optimization

### Blockchain (roadmap.sh/blockchain)
```python
# Web3.py for Ethereum interaction
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR-PROJECT-ID'))

# Check connection
print(w3.is_connected())

# Get account balance
balance = w3.eth.get_balance('0x...')
print(w3.from_wei(balance, 'ether'))

# Deploy contract
contract = w3.eth.contract(abi=ABI, bytecode=BYTECODE)
tx_hash = contract.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
```

### Game Development

#### Game Engines
- **Unity** - Cross-platform (C#)
- **Unreal Engine** - High-performance (C++)
- **Godot** - Open-source (GDScript)

#### Game Developer (roadmap.sh/game-developer)
- Game loops and rendering
- Physics simulation
- Input handling
- Asset management

### Specialized Roles

#### QA Testing (roadmap.sh/qa)
```python
# Automated testing example
import pytest
from selenium import webdriver

def test_user_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    username = driver.find_element("id", "username")
    password = driver.find_element("id", "password")

    username.send_keys("testuser")
    password.send_keys("password123")
    driver.find_element("id", "login-btn").click()

    assert driver.current_url == "https://example.com/dashboard"
```

#### Product Manager (roadmap.sh/product-manager)
- User research
- Requirements definition
- Product roadmap
- Metrics and KPIs
- Stakeholder management

#### Engineering Manager (roadmap.sh/engineering-manager)
- Team leadership
- Performance reviews
- Career development
- Project planning
- Technical decision-making

#### Technical Writer (roadmap.sh/technical-writer)
```markdown
# API Documentation

## Authentication

All API requests require an authentication token in the `Authorization` header:

\`\`\`
Authorization: Bearer YOUR_TOKEN
\`\`\`

## Endpoints

### Get User
\`\`\`
GET /api/users/{id}
\`\`\`

**Response:**
\`\`\`json
{
  "id": "123",
  "name": "John Doe",
  "email": "john@example.com"
}
\`\`\`
```

#### DevRel Engineer (roadmap.sh/devrel)
- Community building
- Technical advocacy
- Developer documentation
- Conference speaking
- Content creation

#### Cyber Security (roadmap.sh/cyber-security)
- Network security
- Cryptography
- Vulnerability assessment
- Penetration testing
- Security incident response

## Full-Stack Development (roadmap.sh/full-stack)

```javascript
// Full-stack example: Node.js + React

// Backend (Node.js/Express)
app.get('/api/users', async (req, res) => {
  const users = await User.find();
  res.json(users);
});

// Frontend (React)
function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/api/users')
      .then(r => r.json())
      .then(setUsers);
  }, []);

  return (
    <ul>
      {users.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}
```

## Resources

- [iOS Dev](https://developer.apple.com)
- [Android Dev](https://developer.android.com)
- [React Native Docs](https://reactnative.dev)
- [Flutter Docs](https://flutter.dev)
- [Ethereum Dev](https://ethereum.org/developers)
- [Git Docs](https://git-scm.com/doc)
