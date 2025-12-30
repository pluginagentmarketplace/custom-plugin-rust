#!/usr/bin/env python3
"""
Rust Trait Implementation Checker
Analyzes Rust code for trait implementations and suggests improvements.
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Set


@dataclass
class TraitInfo:
    name: str
    line_number: int
    type_name: str
    is_derived: bool


@dataclass
class Suggestion:
    line_number: int
    type_name: str
    message: str
    priority: str  # "high", "medium", "low"


def find_structs_and_enums(content: str) -> List[tuple]:
    """Find all struct and enum definitions."""
    types = []
    lines = content.split('\n')

    for i, line in enumerate(lines, 1):
        # Match struct definitions
        struct_match = re.match(r'\s*(?:pub\s+)?struct\s+(\w+)', line)
        if struct_match:
            types.append((i, 'struct', struct_match.group(1)))

        # Match enum definitions
        enum_match = re.match(r'\s*(?:pub\s+)?enum\s+(\w+)', line)
        if enum_match:
            types.append((i, 'enum', enum_match.group(1)))

    return types


def find_derives(content: str) -> Dict[str, Set[str]]:
    """Find all derive macros and their associated types."""
    derives = {}
    lines = content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check for derive attribute
        derive_match = re.search(r'#\[derive\((.*?)\)\]', line)
        if derive_match:
            traits = [t.strip() for t in derive_match.group(1).split(',')]

            # Find the type this applies to
            j = i + 1
            while j < len(lines):
                type_match = re.match(r'\s*(?:pub\s+)?(?:struct|enum)\s+(\w+)', lines[j])
                if type_match:
                    type_name = type_match.group(1)
                    derives[type_name] = set(traits)
                    break
                if lines[j].strip() and not lines[j].strip().startswith('#'):
                    break
                j += 1

        i += 1

    return derives


def find_impl_blocks(content: str) -> List[TraitInfo]:
    """Find all impl blocks for traits."""
    impls = []
    lines = content.split('\n')

    for i, line in enumerate(lines, 1):
        # Match impl blocks: impl Trait for Type
        impl_match = re.match(r'\s*impl(?:<.*?>)?\s+(\w+)\s+for\s+(\w+)', line)
        if impl_match:
            impls.append(TraitInfo(
                name=impl_match.group(1),
                line_number=i,
                type_name=impl_match.group(2),
                is_derived=False
            ))

    return impls


def generate_suggestions(types: List[tuple], derives: Dict[str, Set[str]], impls: List[TraitInfo]) -> List[Suggestion]:
    """Generate suggestions for missing trait implementations."""
    suggestions = []

    # Common traits that should usually be derived
    recommended_derives = {
        'Debug': ('high', 'All types should implement Debug for debugging'),
        'Clone': ('medium', 'Consider if type should be cloneable'),
    }

    # Pairs of traits
    trait_pairs = {
        'PartialEq': ('Eq', 'If PartialEq is derived, consider deriving Eq too'),
        'PartialOrd': ('Ord', 'If PartialOrd is derived, consider deriving Ord too'),
    }

    # Hash requires Eq
    hash_requirement = 'If using Hash (for HashMap/HashSet), also need PartialEq + Eq'

    impl_traits = {(i.type_name, i.name) for i in impls}

    for line_num, type_kind, type_name in types:
        type_derives = derives.get(type_name, set())

        # Check for Debug
        if 'Debug' not in type_derives and (type_name, 'Debug') not in impl_traits:
            suggestions.append(Suggestion(
                line_number=line_num,
                type_name=type_name,
                message=f"Missing Debug trait - add #[derive(Debug)] to {type_name}",
                priority="high"
            ))

        # Check trait pairs
        for trait, (paired, message) in trait_pairs.items():
            if trait in type_derives and paired not in type_derives:
                suggestions.append(Suggestion(
                    line_number=line_num,
                    type_name=type_name,
                    message=f"{type_name}: {message}",
                    priority="low"
                ))

        # Check Hash requirements
        if 'Hash' in type_derives:
            if 'PartialEq' not in type_derives or 'Eq' not in type_derives:
                suggestions.append(Suggestion(
                    line_number=line_num,
                    type_name=type_name,
                    message=f"{type_name}: {hash_requirement}",
                    priority="high"
                ))

    return suggestions


def generate_report(content: str, filename: str) -> str:
    """Generate analysis report."""
    types = find_structs_and_enums(content)
    derives = find_derives(content)
    impls = find_impl_blocks(content)
    suggestions = generate_suggestions(types, derives, impls)

    report = [f"# Trait Analysis: {filename}\n"]

    # Summary
    report.append("## Types Found\n")
    for line_num, type_kind, name in types:
        derived = derives.get(name, set())
        derived_str = ', '.join(sorted(derived)) if derived else 'none'
        report.append(f"- **{name}** ({type_kind}, line {line_num})")
        report.append(f"  - Derived: {derived_str}")

    report.append(f"\n## Trait Implementations: {len(impls)}\n")
    for impl in impls:
        report.append(f"- `impl {impl.name} for {impl.type_name}` (line {impl.line_number})")

    if suggestions:
        report.append("\n## Suggestions\n")
        high = [s for s in suggestions if s.priority == "high"]
        medium = [s for s in suggestions if s.priority == "medium"]
        low = [s for s in suggestions if s.priority == "low"]

        if high:
            report.append("### 🔴 High Priority")
            for s in high:
                report.append(f"- Line {s.line_number}: {s.message}")

        if medium:
            report.append("\n### 🟡 Medium Priority")
            for s in medium:
                report.append(f"- Line {s.line_number}: {s.message}")

        if low:
            report.append("\n### 🟢 Low Priority")
            for s in low:
                report.append(f"- Line {s.line_number}: {s.message}")

    report.append("\n## Best Practices\n")
    report.append("1. Always derive `Debug` for all types")
    report.append("2. Derive `Clone` unless type holds non-cloneable resources")
    report.append("3. If `PartialEq`, consider `Eq` (unless NaN-like values)")
    report.append("4. `Hash` requires `Eq` for correctness")
    report.append("5. Use `#[derive(Default)]` for types with sensible defaults")

    return '\n'.join(report)


def main():
    if len(sys.argv) < 2:
        print("Usage: trait_checker.py <rust_file.rs>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if path.is_file():
        content = path.read_text()
        print(generate_report(content, path.name))
    else:
        print(f"Error: {path} not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
