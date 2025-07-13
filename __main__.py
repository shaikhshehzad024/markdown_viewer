import sys
from .display import display_markdown_from_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m markdown_viewer <filename.md>")
    else:
        display_markdown_from_file(sys.argv[1])
