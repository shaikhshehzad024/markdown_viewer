def is_table_line(line):
    return '|' in line and line.strip().startswith("|")

def parse_table(lines, start):
    table_lines = []
    i = start
    while i < len(lines) and is_table_line(lines[i]):
        table_lines.append(lines[i].strip())
        i += 1

    rows = [list(map(str.strip, row.strip('|').split('|'))) for row in table_lines]
    col_widths = [max(len(row[i]) if i < len(row) else 0 for row in rows) for i in range(len(rows[0]))]

    def format_row(row, border="│"):
        return border + border.join(
            f" {row[i].ljust(col_widths[i])} " if i < len(row) else " " * (col_widths[i] + 2)
            for i in range(len(col_widths))
        ) + border

    top = "┌" + "┬".join("─" * (w + 2) for w in col_widths) + "┐"
    header = format_row(rows[0])
    separator = "├" + "┼".join("─" * (w + 2) for w in col_widths) + "┤"
    body = [format_row(row) for row in rows[2:] if row != rows[1]]
    bottom = "└" + "┴".join("─" * (w + 2) for w in col_widths) + "┘"

    return "\n".join([top, header, separator] + body + [bottom]), i
