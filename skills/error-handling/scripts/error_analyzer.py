#!/usr/bin/env python3
"""
Rust Error Handling Analyzer
Analyzes Rust code for error handling patterns and suggests improvements.
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple, Optional


class ErrorPattern(Enum):
    UNWRAP = "unwrap"
    EXPECT = "expect"
    QUESTION_MARK = "question_mark"
    MATCH_RESULT = "match_result"
    MAP_ERR = "map_err"
    OK_OR = "ok_or"
    PANIC = "panic"
    UNREACHABLE = "unreachable"


@dataclass
class Finding:
    line_number: int
    pattern: ErrorPattern
    code_snippet: str
    suggestion: str
    severity: str  # "info", "warning", "error"


def analyze_rust_file(content: str) -> List[Finding]:
    """Analyze Rust code for error handling patterns."""
    findings = []
    lines = content.split('\n')

    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        # Check for .unwrap() usage
        if '.unwrap()' in line and not stripped.startswith('//'):
            findings.append(Finding(
                line_number=i,
                pattern=ErrorPattern.UNWRAP,
                code_snippet=stripped[:80],
                suggestion="Consider using `?` operator or `unwrap_or_default()` for safer error handling",
                severity="warning"
            ))

        # Check for .expect() usage
        if re.search(r'\.expect\s*\(', line) and not stripped.startswith('//'):
            findings.append(Finding(
                line_number=i,
                pattern=ErrorPattern.EXPECT,
                code_snippet=stripped[:80],
                suggestion="Good: expect() provides context. Ensure message is descriptive.",
                severity="info"
            ))

        # Check for ? operator (positive pattern)
        if re.search(r'\?\s*[;}\)]', line):
            findings.append(Finding(
                line_number=i,
                pattern=ErrorPattern.QUESTION_MARK,
                code_snippet=stripped[:80],
                suggestion="Good: Using ? operator for error propagation",
                severity="info"
            ))

        # Check for panic!() macro
        if 'panic!' in line and not stripped.startswith('//'):
            findings.append(Finding(
                line_number=i,
                pattern=ErrorPattern.PANIC,
                code_snippet=stripped[:80],
                suggestion="Consider returning Result<T, E> instead of panicking",
                severity="error"
            ))

        # Check for map_err usage (positive pattern)
        if '.map_err(' in line:
            findings.append(Finding(
                line_number=i,
                pattern=ErrorPattern.MAP_ERR,
                code_snippet=stripped[:80],
                suggestion="Good: Converting error types with map_err",
                severity="info"
            ))

        # Check for ok_or usage
        if '.ok_or(' in line or '.ok_or_else(' in line:
            findings.append(Finding(
                line_number=i,
                pattern=ErrorPattern.OK_OR,
                code_snippet=stripped[:80],
                suggestion="Good: Converting Option to Result",
                severity="info"
            ))

    return findings


def generate_report(findings: List[Finding], filename: str) -> str:
    """Generate a markdown report of findings."""
    report = [f"# Error Handling Analysis: {filename}\n"]

    # Summary
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]
    infos = [f for f in findings if f.severity == "info"]

    report.append("## Summary\n")
    report.append(f"- Errors: {len(errors)}")
    report.append(f"- Warnings: {len(warnings)}")
    report.append(f"- Info: {len(infos)}\n")

    # Score
    score = 100 - (len(errors) * 10) - (len(warnings) * 5)
    score = max(0, score)
    report.append(f"**Error Handling Score: {score}/100**\n")

    # Detailed findings
    if findings:
        report.append("## Findings\n")
        for f in findings:
            icon = {"error": "🔴", "warning": "🟡", "info": "🟢"}[f.severity]
            report.append(f"### {icon} Line {f.line_number}: {f.pattern.value}\n")
            report.append(f"```rust\n{f.code_snippet}\n```")
            report.append(f"**Suggestion:** {f.suggestion}\n")

    # Recommendations
    report.append("## Best Practices\n")
    report.append("1. Prefer `?` operator over `.unwrap()`")
    report.append("2. Use `.expect()` with descriptive messages")
    report.append("3. Define custom error types with `thiserror`")
    report.append("4. Use `anyhow` for application-level errors")
    report.append("5. Handle all error cases explicitly\n")

    return '\n'.join(report)


def main():
    if len(sys.argv) < 2:
        print("Usage: error_analyzer.py <rust_file.rs>")
        print("       error_analyzer.py <directory>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if path.is_file():
        content = path.read_text()
        findings = analyze_rust_file(content)
        report = generate_report(findings, path.name)
        print(report)
    elif path.is_dir():
        all_findings = []
        for rust_file in path.rglob("*.rs"):
            content = rust_file.read_text()
            findings = analyze_rust_file(content)
            all_findings.extend(findings)
        report = generate_report(all_findings, str(path))
        print(report)
    else:
        print(f"Error: {path} not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
