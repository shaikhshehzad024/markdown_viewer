import pytest

from markdown_viewer.inline_parser import parse_inline
from markdown_viewer import constants


def test_bold_and_italic():
    s = "This is **bold** and *italic*"
    out = parse_inline(s)
    assert constants.BOLD in out
    assert constants.BOLD_ in out
    assert constants.ITALIC in out
    assert "bold" in out
    assert "italic" in out


def test_escape_and_code():
    s = "Escaped \\*notitalic* and `code()`"
    out = parse_inline(s)
    # escaped star should remain literal
    assert "*notitalic*" in out
    # code should be wrapped with CODE/RESETCOLOR
    assert constants.CODE in out
    assert "code()" in out


def test_link_parsing():
    s = "Click [here](http://example.com)"
    out = parse_inline(s)
    # link label should be present and colored with LINK
    assert constants.LINK in out
    assert "here" in out
