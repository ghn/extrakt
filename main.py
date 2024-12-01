import argparse
import os
from extrakt.base import extract_all


def main():
    parser = argparse.ArgumentParser(description="Extract data from your GPX files")

    parser.add_argument(
        "-f", "--file", type=str, required=True, help="GPX file location"
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default=os.getcwd(),
        help="The output directory. Will generate the files in current directory if not specified",
    )

    args = parser.parse_args()

    data_files = extract_all(args.file, args.output_dir)
    print("Data has been extracted in:")
    print(f"  {data_files['data_file']}")
    print(f"  {data_files['map_file']}")


if __name__ == "__main__":
    main()
