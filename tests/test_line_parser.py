from markdown_viewer.line_parser import parse_line
from markdown_viewer import constants


def test_headers():
    out = parse_line("# Top")
    assert constants.UNDERLINE in out or constants.BOLD in out
    assert "Top" in out


def test_horizontal_rule():
    # create a line of dashes -> should return underscores equal to columns
    line = "-" * 5 + "\n"
    # the implementation checks stripped length and chars; emulate a valid hr
    hr = "---\n"
    out = parse_line(hr)
    assert out == "_" * constants.columns


def test_quotes_and_lists():
    assert "│ " in parse_line("> a quote")
    assert "│ | " in parse_line(">> nested")

    assert "☐" in parse_line("- [ ] task")
    assert "☑" in parse_line("- [x] done")

    assert "• " in parse_line("- bullet")
    assert "1. " in parse_line("1. first")
