markdown_viewer
=================

This is a small package to render markdown to a terminal-friendly formatted output.

Quick start — run the package

Because this project is a package with relative imports, run it from the parent directory using -m. Example:

```bash
# from the parent directory of the package (one level up)
cd /home/shehzad/dev
python -m markdown_viewer /home/shehzad/dev/markdown_viewer/example.md
```

You can substitute any markdown file path for the last argument.

How to run tests

Activate your virtualenv (if used) and run pytest from the project root or parent directory:

```bash
# optional: activate virtualenv
source /home/shehzad/.local/share/virtualenvs/backend-_5hcRy06/bin/activate

# run tests (from project folder or its parent)
cd /home/shehzad/dev/markdown_viewer
pytest -q
```

Notes

- Running `python -m markdown_viewer <file>` from the package parent is required because the package uses relative imports.
- If you see `ModuleNotFoundError: No module named 'markdown_viewer'`, ensure you're running from the package parent or add the parent to PYTHONPATH:

```bash
export PYTHONPATH=/home/shehzad/dev:$PYTHONPATH
python -m markdown_viewer /path/to/your.md
```
