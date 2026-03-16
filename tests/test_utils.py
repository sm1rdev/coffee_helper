import sys
import pytest
from pathlib import Path

from coffee_helper.utils import get_args


def test_get_args(samples_dir, monkeypatch):
    file = samples_dir / "math.csv"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "prog",
            "--files", str(file),
            "--report", "median-coffee"
        ]
    )

    args = get_args()

    assert args.report == "median-coffee"
    assert args.files == [Path(file)]


def test_get_args_invalid(samples_dir, monkeypatch):
    file = samples_dir / "russian.csv"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "prog",
            "--files", str(file),
            "--report", "median-coffee"
        ]
    )

    with pytest.raises(SystemExit):
        args = get_args()
