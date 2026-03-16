import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def samples_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "samples"
