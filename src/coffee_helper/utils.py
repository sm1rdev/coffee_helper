from argparse import ArgumentParser, Namespace, ArgumentTypeError
from pathlib import Path


def check_path(path_str: str) -> Path:
    """
    Validates that the given path exists and is a file.

    Args:
        path_str (str): File path as a string.

    Raises:
        ArgumentTypeError: If the file does not exist or is not a file.

    Returns:
        Path: Path object for the valid file.
    """

    path = Path(path_str)
    if not path.exists() or not path.is_file():
        raise ArgumentTypeError(f"File not found: {path_str}")
    return path


def get_args() -> Namespace:
    """
    Parses command-line arguments using argparse.

    Returns:
        Namespace: Parsed command-line arguments with:
            - files: list of CSV files
            - report: name of report
    """

    args_parser: ArgumentParser = ArgumentParser()

    args_parser.add_argument(
        "--files", nargs="+", type=check_path, required=True, help="Enter paths to files"
    )
    args_parser.add_argument(
        "--report", type=str, required=True, help="Enter name of report"
    )

    args: Namespace = args_parser.parse_args()

    return args
