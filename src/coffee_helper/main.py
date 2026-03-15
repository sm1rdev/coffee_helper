from argparse import Namespace

from coffee_helper.reader import read_files
from coffee_helper.utils import get_args


def main() -> None:
    args: Namespace = get_args()
    rows: list[dict] = read_files(args.files)


if __name__ == "__main__":
    main()
