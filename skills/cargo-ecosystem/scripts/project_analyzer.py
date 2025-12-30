#!/usr/bin/env python3
"""
Rust Project Analyzer
Analyzes Cargo.toml and project structure for best practices.
"""

import re
import sys
import tomllib
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class ProjectInfo:
    name: str
    version: str
    edition: str
    authors: List[str]
    description: Optional[str]
    license: Optional[str]
    repository: Optional[str]


@dataclass
class Dependency:
    name: str
    version: str
    features: List[str]
    dev: bool
    optional: bool


@dataclass
class Suggestion:
    category: str
    message: str
    priority: str  # "high", "medium", "low"


def parse_cargo_toml(path: Path) -> tuple:
    """Parse Cargo.toml and extract information."""
    content = path.read_text()
    data = tomllib.loads(content)

    # Extract project info
    package = data.get('package', {})
    info = ProjectInfo(
        name=package.get('name', 'unknown'),
        version=package.get('version', '0.0.0'),
        edition=package.get('edition', '2021'),
        authors=package.get('authors', []),
        description=package.get('description'),
        license=package.get('license'),
        repository=package.get('repository'),
    )

    # Extract dependencies
    deps = []
    for section, is_dev in [('dependencies', False), ('dev-dependencies', True)]:
        for name, spec in data.get(section, {}).items():
            if isinstance(spec, str):
                deps.append(Dependency(name, spec, [], is_dev, False))
            elif isinstance(spec, dict):
                deps.append(Dependency(
                    name=name,
                    version=spec.get('version', '*'),
                    features=spec.get('features', []),
                    dev=is_dev,
                    optional=spec.get('optional', False),
                ))

    return info, deps, data


def analyze_project(info: ProjectInfo, deps: List[Dependency], data: dict) -> List[Suggestion]:
    """Generate suggestions for the project."""
    suggestions = []

    # Check edition
    if info.edition != '2021':
        suggestions.append(Suggestion(
            category="Edition",
            message=f"Consider upgrading to edition 2021 (current: {info.edition})",
            priority="medium"
        ))

    # Check metadata
    if not info.description:
        suggestions.append(Suggestion(
            category="Metadata",
            message="Add 'description' to [package] for crates.io",
            priority="low"
        ))

    if not info.license:
        suggestions.append(Suggestion(
            category="Metadata",
            message="Add 'license' to [package] (e.g., 'MIT' or 'Apache-2.0')",
            priority="medium"
        ))

    if not info.repository:
        suggestions.append(Suggestion(
            category="Metadata",
            message="Add 'repository' URL to [package]",
            priority="low"
        ))

    # Check for common dependencies
    dep_names = {d.name for d in deps}

    # Error handling
    if 'thiserror' not in dep_names and 'anyhow' not in dep_names:
        suggestions.append(Suggestion(
            category="Dependencies",
            message="Consider adding 'thiserror' or 'anyhow' for error handling",
            priority="low"
        ))

    # Serialization
    if 'serde' in dep_names:
        serde_dep = next(d for d in deps if d.name == 'serde')
        if 'derive' not in serde_dep.features:
            suggestions.append(Suggestion(
                category="Dependencies",
                message="Consider enabling 'derive' feature for serde",
                priority="low"
            ))

    # Async runtime
    async_deps = {'tokio', 'async-std', 'smol'}
    if async_deps & dep_names:
        if 'tokio' in dep_names:
            tokio_dep = next(d for d in deps if d.name == 'tokio')
            if not tokio_dep.features:
                suggestions.append(Suggestion(
                    category="Dependencies",
                    message="Specify tokio features (e.g., 'full', 'rt-multi-thread', 'macros')",
                    priority="medium"
                ))

    # Check profiles
    profiles = data.get('profile', {})
    if 'release' not in profiles:
        suggestions.append(Suggestion(
            category="Profiles",
            message="Consider adding [profile.release] with lto = true for smaller binaries",
            priority="low"
        ))

    # Check for dev-dependencies
    dev_deps = {d.name for d in deps if d.dev}
    if 'criterion' not in dev_deps and 'divan' not in dev_deps:
        suggestions.append(Suggestion(
            category="Testing",
            message="Consider adding 'criterion' or 'divan' for benchmarking",
            priority="low"
        ))

    return suggestions


def check_project_structure(root: Path) -> List[Suggestion]:
    """Check project directory structure."""
    suggestions = []

    # Check for standard directories
    standard_dirs = ['src', 'tests', 'examples', 'benches']
    for dir_name in standard_dirs:
        dir_path = root / dir_name
        if dir_name == 'src' and not dir_path.exists():
            suggestions.append(Suggestion(
                category="Structure",
                message="Missing 'src' directory",
                priority="high"
            ))
        elif dir_name == 'tests' and not dir_path.exists():
            suggestions.append(Suggestion(
                category="Structure",
                message="Consider adding 'tests' directory for integration tests",
                priority="low"
            ))

    # Check for common files
    if not (root / 'README.md').exists():
        suggestions.append(Suggestion(
            category="Documentation",
            message="Add README.md for project documentation",
            priority="medium"
        ))

    if not (root / '.gitignore').exists():
        suggestions.append(Suggestion(
            category="Git",
            message="Add .gitignore (should include /target)",
            priority="medium"
        ))

    if not (root / 'LICENSE').exists() and not (root / 'LICENSE.md').exists():
        suggestions.append(Suggestion(
            category="Legal",
            message="Add LICENSE file",
            priority="medium"
        ))

    return suggestions


def generate_report(root: Path) -> str:
    """Generate full analysis report."""
    cargo_toml = root / 'Cargo.toml'

    if not cargo_toml.exists():
        return "Error: Cargo.toml not found"

    info, deps, data = parse_cargo_toml(cargo_toml)
    toml_suggestions = analyze_project(info, deps, data)
    struct_suggestions = check_project_structure(root)
    all_suggestions = toml_suggestions + struct_suggestions

    report = [f"# Project Analysis: {info.name}\n"]

    # Project Info
    report.append("## Project Information\n")
    report.append(f"- **Name:** {info.name}")
    report.append(f"- **Version:** {info.version}")
    report.append(f"- **Edition:** {info.edition}")
    report.append(f"- **License:** {info.license or 'Not specified'}")
    report.append(f"- **Description:** {info.description or 'Not specified'}\n")

    # Dependencies
    report.append(f"## Dependencies ({len(deps)} total)\n")
    regular = [d for d in deps if not d.dev]
    dev = [d for d in deps if d.dev]

    if regular:
        report.append("### Runtime Dependencies")
        for d in regular:
            features = f" (features: {', '.join(d.features)})" if d.features else ""
            optional = " [optional]" if d.optional else ""
            report.append(f"- `{d.name}` {d.version}{features}{optional}")

    if dev:
        report.append("\n### Dev Dependencies")
        for d in dev:
            features = f" (features: {', '.join(d.features)})" if d.features else ""
            report.append(f"- `{d.name}` {d.version}{features}")

    # Suggestions
    if all_suggestions:
        report.append("\n## Suggestions\n")

        high = [s for s in all_suggestions if s.priority == "high"]
        medium = [s for s in all_suggestions if s.priority == "medium"]
        low = [s for s in all_suggestions if s.priority == "low"]

        if high:
            report.append("### 🔴 High Priority")
            for s in high:
                report.append(f"- **[{s.category}]** {s.message}")

        if medium:
            report.append("\n### 🟡 Medium Priority")
            for s in medium:
                report.append(f"- **[{s.category}]** {s.message}")

        if low:
            report.append("\n### 🟢 Low Priority")
            for s in low:
                report.append(f"- **[{s.category}]** {s.message}")

    # Score
    score = 100 - (len(high) * 15) - (len(medium) * 5) - (len(low) * 2)
    score = max(0, score)
    report.append(f"\n## Project Health Score: {score}/100\n")

    return '\n'.join(report)


def main():
    if len(sys.argv) < 2:
        path = Path('.')
    else:
        path = Path(sys.argv[1])

    if path.is_file():
        path = path.parent

    print(generate_report(path))


if __name__ == "__main__":
    main()
