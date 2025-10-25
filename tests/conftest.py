import sys
from pathlib import Path

# Ensure project root (parent of tests/) is on sys.path so test imports find modules
# We need to add the parent of the project root so `import markdown_viewer` works
PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_PARENT = PROJECT_ROOT.parent
if str(PROJECT_PARENT) not in sys.path:
    sys.path.insert(0, str(PROJECT_PARENT))

import importlib
# ensure package is importable during tests
importlib.import_module(PROJECT_ROOT.name)
