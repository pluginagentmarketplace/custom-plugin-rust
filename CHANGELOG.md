# Changelog

## [2.2.0] - 2024-12-30

### Production-Grade Upgrade
- **8 agents** (added rust-devops-agent with full Docker/CI/CD content)
- **12 skills** all production-ready with troubleshooting sections:
  - rust-testing: Unit tests, mocking, property testing
  - rust-cli: clap, colored output, progress bars
  - rust-macros: Declarative and procedural macros
  - rust-concurrency: Threads, channels, Rayon
  - rust-performance: Profiling, benchmarking, optimization
  - rust-docker: Multi-stage builds, scratch images
  - rust-wasm: wasm-pack, wasm-bindgen, browser integration
- Fixed ghost references (skills now bond to correct agents)
- All skills include troubleshooting tables
- Updated plugin.json with complete 8 agents + 12 skills

### Integrity Verified
- Zero broken links (agent ↔ skill references)
- Zero orphan skills
- Zero ghost triggers
- All bonded_agent references valid

## [2.0.0] - 2024-12-29

### Complete Rewrite
- 8 specialized Rust agents
- 12 Golden Format skills
- 4 practical commands
- SASMP v1.3.0 compliance
- Replaced generic "Developer Learning System" with Rust-specific content
