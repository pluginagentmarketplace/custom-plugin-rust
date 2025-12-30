#!/usr/bin/env python3
"""
Rust Async Code Analyzer
Analyzes Rust async code for common patterns and anti-patterns.
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List


@dataclass
class AsyncFinding:
    line_number: int
    pattern: str
    code: str
    message: str
    severity: str  # "good", "warning", "error"


def analyze_async_rust(content: str) -> List[AsyncFinding]:
    """Analyze Rust async code for patterns."""
    findings = []
    lines = content.split('\n')

    in_async_fn = False
    brace_depth = 0

    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        # Track async function context
        if 'async fn' in line:
            in_async_fn = True
            brace_depth = 0

        if in_async_fn:
            brace_depth += line.count('{') - line.count('}')
            if brace_depth <= 0:
                in_async_fn = False

        # Check for std::thread::sleep in async context
        if in_async_fn and 'thread::sleep' in line:
            findings.append(AsyncFinding(
                line_number=i,
                pattern="blocking_sleep",
                code=stripped[:60],
                message="Use tokio::time::sleep instead of std::thread::sleep in async context",
                severity="error"
            ))

        # Check for .await usage (positive)
        if '.await' in line:
            findings.append(AsyncFinding(
                line_number=i,
                pattern="await_point",
                code=stripped[:60],
                message="Await point found",
                severity="good"
            ))

        # Check for tokio::spawn (positive)
        if 'tokio::spawn' in line:
            findings.append(AsyncFinding(
                line_number=i,
                pattern="spawn_task",
                code=stripped[:60],
                message="Task spawning - ensure JoinHandle is handled",
                severity="good"
            ))

        # Check for spawn_blocking (positive)
        if 'spawn_blocking' in line:
            findings.append(AsyncFinding(
                line_number=i,
                pattern="spawn_blocking",
                code=stripped[:60],
                message="Good: Using spawn_blocking for blocking operations",
                severity="good"
            ))

        # Check for mutex lock in async
        if in_async_fn and '.lock()' in line and 'Mutex' not in line:
            if 'tokio::sync' not in content[:content.find(line)]:
                findings.append(AsyncFinding(
                    line_number=i,
                    pattern="sync_mutex",
                    code=stripped[:60],
                    message="Possible std::sync::Mutex in async - consider tokio::sync::Mutex",
                    severity="warning"
                ))

        # Check for join! macro (positive)
        if 'tokio::join!' in line or 'join!' in line:
            findings.append(AsyncFinding(
                line_number=i,
                pattern="concurrent_join",
                code=stripped[:60],
                message="Good: Using join! for concurrent execution",
                severity="good"
            ))

        # Check for select! macro (positive)
        if 'tokio::select!' in line or 'select!' in line:
            findings.append(AsyncFinding(
                line_number=i,
                pattern="select_macro",
                code=stripped[:60],
                message="Good: Using select! for racing futures",
                severity="good"
            ))

        # Check for timeout usage (positive)
        if 'timeout(' in line or 'timeout::' in line:
            findings.append(AsyncFinding(
                line_number=i,
                pattern="timeout",
                code=stripped[:60],
                message="Good: Using timeout for async operations",
                severity="good"
            ))

        # Check for unbounded channel
        if 'unbounded_channel' in line:
            findings.append(AsyncFinding(
                line_number=i,
                pattern="unbounded_channel",
                code=stripped[:60],
                message="Consider using bounded channel to prevent memory issues",
                severity="warning"
            ))

        # Check for block_on in async context
        if in_async_fn and 'block_on' in line:
            findings.append(AsyncFinding(
                line_number=i,
                pattern="nested_runtime",
                code=stripped[:60],
                message="Avoid block_on inside async context - causes deadlock",
                severity="error"
            ))

    return findings


def generate_report(findings: List[AsyncFinding], filename: str) -> str:
    """Generate markdown report."""
    report = [f"# Async Analysis: {filename}\n"]

    goods = [f for f in findings if f.severity == "good"]
    warnings = [f for f in findings if f.severity == "warning"]
    errors = [f for f in findings if f.severity == "error"]

    report.append("## Summary\n")
    report.append(f"- Good patterns: {len(goods)} 🟢")
    report.append(f"- Warnings: {len(warnings)} 🟡")
    report.append(f"- Errors: {len(errors)} 🔴\n")

    # Score
    score = 100 - (len(errors) * 15) - (len(warnings) * 5) + min(len(goods) * 2, 20)
    score = max(0, min(100, score))
    report.append(f"**Async Code Score: {score}/100**\n")

    if errors:
        report.append("## 🔴 Errors\n")
        for f in errors:
            report.append(f"**Line {f.line_number}:** {f.message}")
            report.append(f"```rust\n{f.code}\n```\n")

    if warnings:
        report.append("## 🟡 Warnings\n")
        for f in warnings:
            report.append(f"**Line {f.line_number}:** {f.message}")
            report.append(f"```rust\n{f.code}\n```\n")

    report.append("## Async Best Practices\n")
    report.append("1. Use `tokio::time::sleep`, not `std::thread::sleep`")
    report.append("2. Use `spawn_blocking` for CPU-intensive work")
    report.append("3. Use `tokio::sync::Mutex` instead of `std::sync::Mutex`")
    report.append("4. Always add timeouts to network operations")
    report.append("5. Use bounded channels to prevent memory leaks")
    report.append("6. Handle `JoinHandle` from spawned tasks\n")

    return '\n'.join(report)


def main():
    if len(sys.argv) < 2:
        print("Usage: async_analyzer.py <rust_file.rs>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if path.is_file():
        content = path.read_text()
        findings = analyze_async_rust(content)
        print(generate_report(findings, path.name))
    else:
        print(f"Error: {path} not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
