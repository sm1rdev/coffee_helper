import pytest
from pathlib import Path

from coffee_helper.reader import read_files


def test_reader(samples_dir: Path):
    rows: list[dict] = read_files([samples_dir / "math.csv"])
    assert rows[0]["student"] == "Алексей Смирнов"
    assert rows[0]["coffee_spent"] == "450"
