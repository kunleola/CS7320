# Repository Guidelines for AI Agents

## Project Purpose

This repository contains lecture material, small code examples, and student exercises for an introductory artificial intelligence course based on *Artificial Intelligence: A Modern Approach*. Keep examples readable and focused on the AI concept being taught. Prefer straightforward implementations over abstractions, frameworks, or performance optimizations that obscure the algorithm.

## Repository Layout

- Topic directories such as `Agents/`, `Search/`, `Local_Search/`, `Games/`, `CSP/`, `Uncertainty/`, `Probabilistic_Reasoning/`, `ML/`, and `RL/` contain examples and exercises.
- `HOWTOs/` contains supporting Python and Jupyter tutorials.
- `Handouts/` and `slides/` contain course documents and presentation assets.
- Python notebooks (`.ipynb`) are the primary executable teaching material. Some notebooks have published `.html` counterparts.
- `RL/` also contains Quarto/R sources (`.qmd`) and generated HTML.
- Small `.py` files are helpers or reusable versions of algorithms demonstrated in notebooks.

Read the root `README.md` and the relevant topic's `README.md` before changing course content.

## Environment Setup

Use the Conda environment defined by `environment.yml`:

```bash
conda env create -f environment.yml
conda activate CS7320-AI
jupyter lab
```

The supported Python range is 3.11 through 3.12. Do not add a dependency unless it is needed by the course material; when adding one, update `environment.yml` and explain why.

Optional topic dependencies are separated under `environments/`: apply `gymnasium.yml` or `llm.yml` to the core `CS7320-AI` environment, and use the standalone `r.yml` environment for R/Quarto material. Keep notebook-level Colab installation cells commented out by default, version-bounded, and aligned with these files.

## Editing Guidelines

- Preserve the educational scope, terminology, and progression of the surrounding material.
- Match the local style of the file or notebook. Avoid broad formatting or cleanup changes unrelated to the task.
- Keep examples self-contained where practical and favor descriptive names and short explanatory comments.
- Preserve relative paths so notebooks work both locally and when opened from the repository.
- Do not expose assignment solutions. Files matching solution/working patterns are intentionally ignored by `.gitignore`.
- Do not edit generated HTML by hand when a corresponding `.ipynb`, `.qmd`, or `.Rmd` source exists. Change the source and regenerate the output when the task requires the published artifact to stay synchronized.
- Avoid committing transient files such as `.ipynb_checkpoints/`, `__pycache__/`, editor lock files, environment files, or notebook scratch outputs.
- Preserve the existing CC BY-SA licensing and attribution notices in course documents.

## Notebook Practices

- Keep notebook cells in a logical top-to-bottom execution order.
- Before finishing, restart the kernel and run all relevant cells when dependencies and runtime permit.
- Check for exceptions, stale results, excessive output, machine-specific paths, secrets, and nondeterministic behavior.
- Use a fixed random seed when reproducibility matters, while keeping genuinely stochastic demonstrations clearly labeled.
- Do not clear useful instructional output merely to reduce the diff.
- Notebook files are JSON: review the diff carefully and avoid metadata-only or unrelated output changes.

## Validation

There is no single repository-wide test command. Validate the smallest relevant scope:

- Python helpers: run the affected script or import it and exercise the changed behavior.
- Jupyter notebooks: execute the changed notebook from a fresh kernel where feasible.
- Quarto files: render the changed source with `quarto render path/to/file.qmd` when Quarto and its R dependencies are available.
- Markdown: verify links and paths, especially links used by GitHub Pages or Colab.

For a non-interactive notebook check, use a temporary output file so validation does not overwrite the source unintentionally:

```bash
jupyter nbconvert --to notebook --execute path/to/notebook.ipynb \
  --output /tmp/notebook.executed.ipynb
```

If full execution is impractical because of optional native dependencies, long training runs, interactive widgets, display requirements, or missing R packages, run the relevant cells or helper functions and report what was not verified.

## Change Hygiene

- Inspect `git status` before and after editing. The worktree may contain user changes; do not modify, discard, or overwrite unrelated work.
- Keep commits and diffs focused on one topic or correction.
- When changing shared helpers such as `tictactoe.py` or `maze_helper.py`, check all copies and consumers, but update only those that should intentionally remain aligned.
- Summarize changed files, behavioral or instructional impact, and validation performed when handing off work.
