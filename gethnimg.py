import csv
import logging
import os
import sys
from datetime import datetime

import requests

PROGRAM_NAME = "法人番号検索サイト外字画像取得"
VERSION = "0.1.0"


def setup_logging():
    log_filename = f"gethnimg-{datetime.now().strftime('%Y%m%d')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_filename), logging.StreamHandler(sys.stdout)],
    )
    return log_filename


def download_image(image_url, save_path):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        logging.info(f"Downloaded {save_path} with HTTP status {response.status_code}")
        return True, response.status_code
    except requests.RequestException as e:
        logging.error(f"Failed to download {image_url} to {save_path}: {e}")
        if e.response is not None:
            return False, e.response.status_code
        else:
            return False, None


def count_rows_with_numbers(rows, start_index):
    count_name = 0
    count_regional = 0
    count_foreign = 0

    for i, row in enumerate(rows):
        if i == 0:  # Skip header
            continue
        if i < start_index:
            continue

        if len(row) > 7 and row[7].isdigit():
            count_name += 1
        if len(row) > 12 and row[12].isdigit():
            count_regional += 1
        if len(row) > 17 and row[17].isdigit():
            count_foreign += 1

    logging.info(
        f"Count - name: {count_name}, regional: {count_regional}, foreign: {count_foreign}"
    )
    print(
        f"Count - name: {count_name}, regional: {count_regional}, foreign: {count_foreign}"
    )


def main(csv_file, start_index=0, count_only=False):
    log_filename = setup_logging()
    total_count = 0
    success_count = 0
    error_count = 0

    with open(csv_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        total_count = len(rows) - 1  # Excluding header row

        if count_only:
            count_rows_with_numbers(rows, start_index)
            return

        for i, row in enumerate(rows):
            if i == 0:  # Skip header
                continue
            if i < start_index:
                continue

            number = None
            folder = None
            if len(row) > 7 and row[7].isdigit():
                number = row[7]
                folder = "name"
            elif len(row) > 12 and row[12].isdigit():
                number = row[12]
                folder = "regional"
            elif len(row) > 17 and row[17].isdigit():
                number = row[17]
                folder = "foreign"

            if number and folder:
                image_url = (
                    f"https://www.houjin-bangou.nta.go.jp/image?imageid={number}"
                )
                save_path = os.path.join(folder, f"{number}.jpg")
                os.makedirs(os.path.dirname(save_path), exist_ok=True)

                success, status_code = download_image(image_url, save_path)
                if success:
                    success_count += 1
                else:
                    error_count += 1

            logging.info(
                f"Processed {i}/{total_count} rows. Successful: {success_count}, Errors: {error_count}"
            )

    # Final log summary
    logging.info(
        f"Download completed. Total rows: {total_count}, Successful downloads: {success_count}, Errors: {error_count}"
    )
    logging.info(f"Log file saved to {log_filename}")


def print_help():
    help_text = f"""
Usage: python {sys.argv[0]} <csv_file> [start_index] [options]

Options:
  -h, --help       Show this help message and exit
  -v, --version    Show program's name and version number
  -c, --count      Count rows with numbers in specific columns and exit

Arguments:
  csv_file         Path to the CSV file to process
  start_index      Row index to start processing from (default is 0)
"""
    print(help_text)


def print_version():
    print(f"{PROGRAM_NAME} version {VERSION}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()
        sys.exit(0)

    if "-v" in sys.argv or "--version" in sys.argv:
        print_version()
        sys.exit(0)

    count_only = "-c" in sys.argv or "--count" in sys.argv

    csv_file = sys.argv[1]
    start_index = 0
    if len(sys.argv) > 2 and sys.argv[2].isdigit():
        start_index = int(sys.argv[2])

    main(csv_file, start_index, count_only)
