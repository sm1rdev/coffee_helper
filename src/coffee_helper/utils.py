from argparse import ArgumentParser, Namespace, ArgumentTypeError
from pathlib import Path


def check_path(path_str: str):
    path = Path(path_str)
    if not path.exists() or not path.is_file():
        raise ArgumentTypeError(f"File not found: {path_str}")
    return path


def get_args() -> Namespace:
    args_parser: ArgumentParser = ArgumentParser()

    args_parser.add_argument(
        "--files", nargs="+", type=check_path, required=True, help="Enter paths to files"
    )
    args_parser.add_argument(
        "--report", type=str, required=True, help="Enter name of report"
    )

    args: Namespace = args_parser.parse_args()

    return args
