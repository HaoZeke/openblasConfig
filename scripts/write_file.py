import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Write a set of strings to an output file."
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Path to the output file where the content will be written.",
    )
    parser.add_argument(
        "strings", nargs="+", help="Strings to write to the output file."
    )

    args = parser.parse_args()

    combined_content = "\n".join(args.strings)
    args.output_file.write_text(combined_content)
    print(f"Content written to {args.output_file}")


if __name__ == "__main__":
    main()
