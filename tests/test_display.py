from markdown_viewer.display import load_file


def test_load_file(tmp_path):
    p = tmp_path / "sample.md"
    content = "# Hello\nThis is a test"
    p.write_text(content, encoding="utf-8")
    out = load_file(str(p))
    assert "Hello" in out
    assert "This is a test" in out
