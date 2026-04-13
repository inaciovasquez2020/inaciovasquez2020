from pathlib import Path

def test_program_map_2026_04_12() -> None:
    s = Path("docs/program/PROGRAM_MAP_2026_04_12.md").read_text()
    assert "## Closed Non-Clay" in s
    assert "cslib-fmt (EV0V3/TIFF scope-closed)" in s
    assert "Clay repositories are strengthening artifacts, not current closure targets." in s
    assert "The program closes non-Clay artifacts first and presents Clay work as frontier-strengthening evidence." in s
