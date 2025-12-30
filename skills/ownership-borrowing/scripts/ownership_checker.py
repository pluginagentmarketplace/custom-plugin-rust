#!/usr/bin/env python3
"""
Ownership Pattern Checker for Rust Code

This script analyzes Rust code for common ownership patterns and issues.
"""

import re
import sys
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class OwnershipIssue:
    line: int
    issue_type: str
    message: str
    suggestion: str


def check_unnecessary_clone(code: str) -> List[OwnershipIssue]:
    """Check for potentially unnecessary .clone() calls."""
    issues = []
    lines = code.split('\n')

    for i, line in enumerate(lines, 1):
        # Pattern: variable.clone() immediately passed to function
        if '.clone()' in line:
            # Check if it's passed to a function that could take reference
            if re.search(r'\.clone\(\)\s*\)', line):
                issues.append(OwnershipIssue(
                    line=i,
                    issue_type="UNNECESSARY_CLONE",
                    message=f"Possible unnecessary clone on line {i}",
                    suggestion="Consider passing a reference (&) instead of cloning"
                ))

    return issues


def check_move_in_loop(code: str) -> List[OwnershipIssue]:
    """Check for potential move issues in loops."""
    issues = []
    lines = code.split('\n')

    in_loop = False
    loop_start = 0
    loop_vars = set()

    for i, line in enumerate(lines, 1):
        # Detect loop start
        if re.search(r'\b(for|while|loop)\b', line):
            in_loop = True
            loop_start = i
            # Extract variables used before loop

        # Check for potential move inside loop
        if in_loop and not line.strip().startswith('//'):
            # Pattern: using a variable that might be moved
            match = re.search(r'(\w+)\.into\(\)', line)
            if match:
                issues.append(OwnershipIssue(
                    line=i,
                    issue_type="MOVE_IN_LOOP",
                    message=f"Potential move in loop on line {i}: {match.group(1)}",
                    suggestion="Clone the value or use a reference"
                ))

        if '}' in line and in_loop:
            in_loop = False

    return issues


def check_dangling_reference(code: str) -> List[OwnershipIssue]:
    """Check for patterns that might create dangling references."""
    issues = []
    lines = code.split('\n')

    for i, line in enumerate(lines, 1):
        # Pattern: returning reference to local variable
        if '-> &' in line or "-> &'" in line:
            # Check next few lines for local variable creation
            for j in range(i, min(i + 10, len(lines))):
                if 'let ' in lines[j-1] and '&' in lines[j-1]:
                    # Possible dangling reference
                    pass

    # Pattern: reference to temporary
    for i, line in enumerate(lines, 1):
        if re.search(r'&\s*\w+\s*::\s*new\s*\(', line):
            issues.append(OwnershipIssue(
                line=i,
                issue_type="TEMP_REFERENCE",
                message=f"Reference to temporary value on line {i}",
                suggestion="Store the value in a variable first"
            ))

    return issues


def check_borrow_conflicts(code: str) -> List[OwnershipIssue]:
    """Check for potential borrow conflicts."""
    issues = []
    lines = code.split('\n')

    for i, line in enumerate(lines, 1):
        # Pattern: both &mut and & on same variable nearby
        if '&mut ' in line:
            var_match = re.search(r'&mut\s+(\w+)', line)
            if var_match:
                var_name = var_match.group(1)
                # Check nearby lines for immutable borrow
                for j in range(max(0, i-3), min(len(lines), i+3)):
                    if f'&{var_name}' in lines[j] and '&mut' not in lines[j]:
                        issues.append(OwnershipIssue(
                            line=i,
                            issue_type="BORROW_CONFLICT",
                            message=f"Potential borrow conflict with {var_name}",
                            suggestion="Ensure immutable borrows are done before mutable borrow"
                        ))

    return issues


def analyze_rust_file(filepath: str) -> List[OwnershipIssue]:
    """Analyze a Rust file for ownership issues."""
    with open(filepath, 'r') as f:
        code = f.read()

    issues = []
    issues.extend(check_unnecessary_clone(code))
    issues.extend(check_move_in_loop(code))
    issues.extend(check_dangling_reference(code))
    issues.extend(check_borrow_conflicts(code))

    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python ownership_checker.py <rust_file.rs>")
        print("\nThis tool checks for common ownership issues in Rust code:")
        print("  - Unnecessary .clone() calls")
        print("  - Move in loop issues")
        print("  - Potential dangling references")
        print("  - Borrow conflicts")
        sys.exit(1)

    filepath = sys.argv[1]
    issues = analyze_rust_file(filepath)

    if not issues:
        print(f"✓ No ownership issues found in {filepath}")
    else:
        print(f"Found {len(issues)} potential issue(s) in {filepath}:\n")
        for issue in issues:
            print(f"Line {issue.line}: [{issue.issue_type}]")
            print(f"  {issue.message}")
            print(f"  Suggestion: {issue.suggestion}\n")


if __name__ == "__main__":
    main()
