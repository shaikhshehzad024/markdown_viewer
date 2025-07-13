from .constants import *
from .line_parser import parse_line
from .inline_parser import parse_inline
from .table_parser import is_table_line, parse_table

def display_markdown_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            line = lines[i]
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""

            if line.strip() and len(next_line) >= 2 and all(c == '-' for c in next_line):
                print(HEADER_COLORS[0] + BOLD + parse_inline(line.strip()) + BOLD_ + RESETCOLOR)
                i += 2
                continue
            elif len(next_line) >= 2 and all(c == '=' for c in next_line):
                print(HEADER_COLORS[1] + BOLD + UNDERLINE + parse_inline(line.strip()) + UNDERLINE_ + BOLD_ + RESETCOLOR)
                i += 2
                continue

            if is_table_line(line):
                table, i = parse_table(lines, i)
                print(table)
                continue

            print(parse_line(line))
            i += 1

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# display.py

def load_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
