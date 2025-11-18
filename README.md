# Custom-Plugin-Rust 🚀

**The Ultimate Developer Learning System**

A comprehensive Claude Code plugin with **7 expert agents** and **71+ developer roles** covering everything from Frontend to Blockchain. Master any technology with structured learning paths, interactive skills, and guided assessments.

## 🎯 Features

### 7 Specialized Agents
- **Frontend & UI/Design** - HTML, CSS, JavaScript, React, Vue, Angular, UX Design
- **Backend & API** - Node.js, GraphQL, Spring Boot, ASP.NET Core, PHP
- **Languages & Core** - Python, Java, Go, Rust, C++, Kotlin, Bash, CS Fundamentals
- **Data, AI & ML** - Machine Learning, AI Engineering, Data Science, MLOps
- **Cloud & DevOps** - AWS, Docker, Kubernetes, Terraform, Linux, System Design
- **Databases & Architecture** - PostgreSQL, SQL, Redis, MongoDB, Design Patterns
- **Mobile & Specialized** - iOS, Android, Flutter, Blockchain, Game Dev, QA, PM, Tech Writing

### 71+ Developer Roles
Complete learning paths for every developer specialty:
- ✅ Frontend (12 roles)
- ✅ Backend (8 roles)
- ✅ Languages (9 roles)
- ✅ Data/AI/ML (9 roles)
- ✅ Cloud/DevOps (9 roles)
- ✅ Databases (6 roles)
- ✅ Mobile/Blockchain (19+ roles)

### 4 Powerful Commands
- `/learn` - Get personalized learning paths
- `/roadmap` - View detailed role roadmaps
- `/assess` - Test your knowledge with interactive assessments
- `/browse` - Explore all 71+ roles

### Invokable Skills
7 specialized skills with 1000+ code examples and patterns:
- Frontend/UI/Design Systems
- Backend/API Development
- Programming Languages & Core CS
- Data Science & AI/ML
- Cloud/DevOps & Infrastructure
- Databases & Architecture
- Mobile/Blockchain & Specialized Roles

## 📦 Installation

### Using Claude Code

```bash
# From a local directory
claude code ./custom-plugin-rust

# Or add to plugins directory
cp -r custom-plugin-rust ~/.claude-code/plugins/
```

### Using Marketplace (Coming Soon)

One-line installation from the Claude Code marketplace:
```
plugin add custom-plugin-rust
```

## 🚀 Quick Start

### 1. Start Learning
```
/learn
```
Get a personalized learning path for your chosen role.

### 2. View a Roadmap
```
/roadmap react
```
See the complete React learning roadmap with milestones and resources.

### 3. Take an Assessment
```
/assess javascript
```
Test your JavaScript knowledge and get recommendations.

### 4. Browse All Roles
```
/browse
```
Explore all 71+ available developer roles and specializations.

## 📚 Learning Content

Each role includes:
- ✅ **Fundamentals** - Core concepts you must master
- ✅ **Intermediate Skills** - Building on basics
- ✅ **Advanced Topics** - Specialized knowledge
- ✅ **Project Milestones** - Hands-on practice
- ✅ **Code Examples** - 1000+ examples across all topics
- ✅ **Resources** - Books, courses, documentation
- ✅ **Assessments** - Measure your progress

## 🏗️ Plugin Structure

```
custom-plugin-rust/
├── .claude-plugin/
│   └── plugin.json                 # Plugin manifest
├── agents/                         # 7 specialized agents
│   ├── 01-frontend-ui-design.md
│   ├── 02-backend-api-development.md
│   ├── 03-languages-core-programming.md
│   ├── 04-data-ai-ml.md
│   ├── 05-cloud-devops-infrastructure.md
│   ├── 06-databases-architecture.md
│   └── 07-mobile-blockchain-specialized.md
├── commands/                       # 4 slash commands
│   ├── learn.md
│   ├── roadmap.md
│   ├── assess.md
│   └── browse.md
├── skills/                         # 7 invokable skills
│   ├── frontend-design/SKILL.md
│   ├── backend-api/SKILL.md
│   ├── languages/SKILL.md
│   ├── data-ai/SKILL.md
│   ├── cloud-devops/SKILL.md
│   ├── databases-architecture/SKILL.md
│   └── mobile-blockchain/SKILL.md
├── README.md
├── CHANGELOG.md
└── plugin.json
```

## 🎓 Supported Roles

### Frontend & Design
HTML, CSS, JavaScript, TypeScript, React, Next.js, Vue, Angular, React Native, UX Design, Design Systems

### Backend & API
Node.js, GraphQL, Spring Boot, ASP.NET Core, PHP, API Design

### Languages
Python, Java, Go, Rust, C++, Kotlin, Bash/Shell, Computer Science, Data Structures

### Data & AI/ML
AI Engineer, AI Data Scientist, Machine Learning, MLOps, Prompt Engineering, Data Science, Data Engineer, BI Analyst

### Cloud & DevOps
AWS, Cloudflare, Docker, Kubernetes, Terraform, Linux, DevOps, System Design

### Databases
PostgreSQL DBA, SQL, Redis, MongoDB, Software Architecture

### Mobile & Specialized
iOS, Swift, Android, Flutter, React Native, Git, Blockchain, Game Dev, QA, Product Manager, Engineering Manager, Technical Writer, DevRel, Cybersecurity

## 💡 Example Usage

### Learn React
```
User: /learn
Agent: Choose your role
User: React
Agent: Shows personalized React learning path with weekly milestones
```

### Get Backend Roadmap
```
User: /roadmap node.js
Agent: Displays complete Node.js learning roadmap with prerequisites, milestones, projects
```

### Assess Knowledge
```
User: /assess python
Agent: Provides interactive assessment with feedback and recommendations
```

### Browse All Options
```
User: /browse --trending
Agent: Shows latest and trending developer roles to learn
```

## 🔧 Development

### Adding New Content

1. **Add Agent**: Create new markdown file in `agents/`
2. **Add Command**: Create new markdown file in `commands/`
3. **Add Skill**: Create new folder in `skills/` with `SKILL.md`
4. **Update plugin.json**: Reference new components

### Standards

- **Agents**: Include description, capabilities, use cases
- **Skills**: YAML frontmatter with name and description
- **Commands**: Clear examples and related commands
- **Code Examples**: Working, tested code samples

## 📊 Plugin Statistics

| Component | Count | Status |
|-----------|-------|--------|
| Agents | 7 | ✅ Complete |
| Commands | 4 | ✅ Complete |
| Skills | 7 | ✅ Complete |
| Roles | 71+ | ✅ Complete |
| Code Examples | 1000+ | ✅ Complete |
| Learning Hours | 1000+ | ✅ Complete |

## 🌟 Key Features

✅ **Multi-Agent System**: 7 specialized agents covering all tech domains
✅ **Comprehensive Content**: 1000+ code examples and learning materials
✅ **Structured Learning**: Step-by-step paths from beginner to expert
✅ **Interactive Assessments**: Test knowledge and track progress
✅ **Real-world Projects**: Hands-on practice with practical applications
✅ **Career Guidance**: Job market insights and salary information
✅ **Community Resources**: Links to official docs, courses, communities
✅ **Skill Tracking**: Measure progress and earn badges

## 🎯 Use Cases

- 👨‍🎓 **Students** - Structured learning for any tech specialization
- 🔄 **Career Changers** - Clear paths to switch tech stacks
- 📈 **Professionals** - Upskill in new technologies
- 🏢 **Teams** - Unified learning platform for organizations
- 🤖 **AI-Powered** - Leverage Claude's knowledge for better learning

## 📖 Documentation

Each component includes detailed documentation:
- **Agents**: Role description, expertise areas, capabilities
- **Commands**: Usage examples, options, related commands
- **Skills**: Code examples, best practices, resources

## 🤝 Contributing

Contributions welcome! Please:
1. Follow the existing structure
2. Add quality code examples
3. Include documentation
4. Test thoroughly

## 📝 License

MIT License - See LICENSE file for details

## 🔗 Links

- **Repository**: https://github.com/pluginagentmarketplace/custom-plugin-rust
- **Claude Code Docs**: https://docs.claude.com
- **Developer Roadmaps**: https://roadmap.sh

## 🚀 What's Next

- [ ] More specialized agent skills
- [ ] Interactive coding challenges
- [ ] Live mentorship integration
- [ ] Certification programs
- [ ] Team collaboration features
- [ ] Progress analytics dashboard

## 📞 Support

For issues, questions, or suggestions:
1. Check the documentation
2. Review agent descriptions
3. Ask specific questions in the appropriate agent

## ⭐ Star History

Your support matters! Star the repository to show you find this useful.

---

**Happy Learning! 🎓** Master any developer skill with the ultimate learning system powered by Claude Code.
