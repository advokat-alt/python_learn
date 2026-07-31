# python_learn

A collection of small, standalone Python learning scripts. Scripts use only the
Python standard library.

## Cursor Cloud specific instructions

- Runtime: Python 3.12 is preinstalled (`python3`). Use `python3`, not `python`
  (there is no `python` alias). `pip3` is available.
- Dependencies: there is no dependency manifest (no `requirements.txt`,
  `pyproject.toml`, etc.) and no third-party packages are required. There is
  nothing to install for standard development.
- No build step, no test suite, and no lint configuration exist in this repo.
- Running scripts: execute a file directly, e.g. `python3 weather_condition.py`.
- Gotcha: some scripts read from stdin via `input()`. To run them
  non-interactively (e.g. in CI or a headless session), pipe the input, e.g.
  `echo "sunny" | python3 weather_condition.py`.
