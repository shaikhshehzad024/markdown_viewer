from markdown_viewer.table_parser import is_table_line, parse_table


def test_is_table_line():
    assert is_table_line("| a | b |\n")
    assert not is_table_line("a | b\n")


def test_parse_table_simple():
    lines = [
        "| Name | Age |\n",
        "|------|-----|\n",
        "| Alice | 30 |\n",
        "| Bob | 25 |\n",
    ]
    table_str, new_i = parse_table(lines, 0)
    # basic structure and contents
    assert "┌" in table_str and "└" in table_str
    assert "Name" in table_str
    assert "Age" in table_str
    # new_i should be past the table lines
    assert new_i == 4
