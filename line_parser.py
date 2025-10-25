from .constants import *
from .inline_parser import parse_inline

def parse_line(line):
    stripped = line.strip()

    for i, prefix in enumerate(["###### ", "##### ", "#### ", "### ", "## ", "# "]):
        level = 6 - i
        if line.startswith(prefix):
            color = HEADER_COLORS[level - 1]
            text = parse_inline(line[len(prefix):].strip())
            if level == 1:
                return color + BOLD + UNDERLINE + text + UNDERLINE_ + BOLD_ + RESETCOLOR
            return color + BOLD + text + BOLD_ + RESETCOLOR

    if len(stripped) >= 3 and set(stripped).issubset(HLINE_CHARS) and len(set(stripped)) == 1:
        return "_" * columns

    if line.startswith(">> "):
        return QUOTE + "│ | " + parse_inline(line[3:]) + RESETCOLOR
    if line.startswith("> "):
        return QUOTE + "│ " + parse_inline(line[2:]) + RESETCOLOR

    indent = len(line) - len(stripped)
    level = indent // 2
    indent_str = "  " * level

    if any(stripped.startswith(f"{mark} [") for mark in ["-", "*"]):
        # robustly find the closing bracket for the checkbox and allow spacing
        close = stripped.find("]", 2)
        checkbox = stripped[2:close+1].strip().lower() if close != -1 else ""
        symbol = "☑" if checkbox == "[x]" else "☐"
        content = parse_inline(stripped[close+1:].strip() if close != -1 else stripped[6:].strip())
        return indent_str + LIST + symbol + " " + RESETCOLOR + content

    i = 0
    while i < len(stripped) and stripped[i].isdigit():
        i += 1
    if i > 0 and stripped[i:i+2] == ". ":
        number = stripped[:i]
        content = parse_inline(stripped[i+2:].strip())
        return indent_str + LIST + f"{number}. " + RESETCOLOR + content

    if stripped.startswith("- ") or stripped.startswith("* "):
        content = parse_inline(stripped[2:].strip())
        if content:
            return indent_str + LIST + "• " + RESETCOLOR + content

    return parse_inline(line)
