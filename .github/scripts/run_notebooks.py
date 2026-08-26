"""Execute a configured notebook suite without modifying source notebooks."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib


REPOSITORY = Path(__file__).resolve().parents[2]
CONFIGURATION = REPOSITORY / ".github" / "notebook-ci.toml"


def tracked_notebooks() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "*.ipynb"],
        cwd=REPOSITORY,
        check=True,
        capture_output=True,
    )
    return {
        name.decode().replace(os.sep, "/")
        for name in result.stdout.split(b"\0")
        if name
    }


def configured_suites() -> tuple[dict[str, list[str]], set[str]]:
    with CONFIGURATION.open("rb") as stream:
        configuration = tomllib.load(stream)

    suites = configuration["suites"]
    excluded = set(suites.pop("excluded"))
    return suites, excluded


def notebooks_for(suite_name: str) -> list[str]:
    tracked = tracked_notebooks()
    suites, excluded = configured_suites()
    configured = excluded | {name for suite in suites.values() for name in suite}

    unknown = configured - tracked
    if unknown:
        names = "\n  ".join(sorted(unknown))
        raise SystemExit(f"Notebook CI configuration contains untracked files:\n  {names}")

    if suite_name == "core":
        return sorted(tracked - configured)
    if suite_name not in suites:
        choices = ", ".join(["core", *sorted(suites)])
        raise SystemExit(f"Unknown suite {suite_name!r}; choose one of: {choices}")
    return suites[suite_name]


def execute(notebook_name: str, output_root: Path) -> bool:
    notebook = REPOSITORY / notebook_name
    output_directory = output_root / notebook.parent.relative_to(REPOSITORY)
    output_directory.mkdir(parents=True, exist_ok=True)

    print(f"::group::{notebook_name}", flush=True)
    result = subprocess.run(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            notebook.name,
            "--output",
            notebook.name,
            "--output-dir",
            str(output_directory),
            "--ExecutePreprocessor.timeout=600",
        ],
        cwd=notebook.parent,
    )
    print("::endgroup::", flush=True)

    if result.returncode:
        print(
            f"::error file={notebook_name}::Notebook execution failed",
            flush=True,
        )
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("suite", help="Notebook suite from notebook-ci.toml")
    arguments = parser.parse_args()

    notebooks = notebooks_for(arguments.suite)
    print(f"Executing {len(notebooks)} notebook(s) in {arguments.suite!r} suite")

    with tempfile.TemporaryDirectory(prefix="executed-notebooks-") as directory:
        failures = [
            notebook
            for notebook in notebooks
            if not execute(notebook, Path(directory))
        ]

    if failures:
        print("\nNotebook execution failures:")
        for notebook in failures:
            print(f"  - {notebook}")
        return 1

    print("All selected notebooks executed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
