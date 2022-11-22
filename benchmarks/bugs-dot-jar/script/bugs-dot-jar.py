import argparse

from info import info_args
from checkout import checkout_args, checkout_all_args
from compile import compile_args


def initParser():
    parser = argparse.ArgumentParser(
        prog="Bugs.jar", description='Bugs.jar CMD')

    bug_parser = argparse.ArgumentParser(add_help=False)
    bug_parser.add_argument(
        "--project", "-p", required=True, help="The project name")
    bug_parser.add_argument("--id", "-i", required=True, help="The commit ID")

    subparsers = parser.add_subparsers()

    checkout_parser = subparsers.add_parser(
        'checkout', help='Checkout a bug', parents=[bug_parser])
    checkout_parser.set_defaults(func=checkout_args)
    checkout_parser.add_argument("--destination", "-d", help="The destination")

    info_parser = subparsers.add_parser(
        'info', help='Info of a bug', parents=[bug_parser])
    info_parser.set_defaults(func=info_args)
    info_parser.add_argument(
        "--json", action='store_true', help="Export as JSON")

    compile_parser = subparsers.add_parser(
        'compile', help='Compile of a bug', parents=[bug_parser])
    compile_parser.set_defaults(func=compile_args)

    return parser.parse_args()


if __name__ == "__main__":
    args = initParser()
    args.func(args)
