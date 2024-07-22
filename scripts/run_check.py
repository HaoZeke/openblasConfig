import argparse
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Run the bash check script.")
    parser.add_argument(
        "executable",
        type=Path,
        help="Path to the executable to be run.",
    )
    parser.add_argument(
        "suffix", help="Output file suffix Makefile_{suffix}.conf and config_{suffix}.h"
    )
    parser.add_argument("cid", help="Compiler ID, e.g. gcc, gfortran etc.")

    args = parser.parse_args()
    subprocess.run(
        [
            args.executable,
            f"Makefile_{args.suffix}.conf",
            f"config_{args.suffix}.h",
            args.cid,
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
