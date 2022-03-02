import argparse
import tempfile
import venv
import os


if __name__ == "__main__":

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

    with tempfile.TemporaryDirectory() as tmp_dir:
        venv.create(tmp_dir, with_pip=True)
        os.system(f'{tmp_dir}/bin/pip install pyfiglet')
        os.system(f'{tmp_dir}/bin/python3 -m figdate{f" --format_str {args.format_str}" if args.format_str else ""}{f"--font {args.font}" if args.font else ""}')
