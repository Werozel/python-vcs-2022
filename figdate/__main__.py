import locale
import argparse
from .figdate import date


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--format_str',
        type=str
    )
    arg_parser.add_argument(
        '--font',
        type=str
    )
    args = arg_parser.parse_args()

    if not args.format_str:
        print(date())
    elif not args.font:
        print(date(args.format_str))
    else:
        print(date(args.format_str, args.font))
