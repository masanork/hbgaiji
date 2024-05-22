import csv
import sys

def filter_us_rows(input_file):
    output_file = input_file.rsplit('.', 1)[0] + '_us.csv'
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        # Collect rows that contain a full-width underscore (＿)
        us_rows = [header]
        for row in reader:
            if any('＿' in cell for cell in row):
                us_rows.append(row)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(us_rows)

    print(f"Filtered rows with full-width underscores have been saved to {output_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python csv_us.py <input_csv_file1> <input_csv_file2> ...")
        sys.exit(1)

    input_files = sys.argv[1:]
    for input_file in input_files:
        filter_us_rows(input_file)

if __name__ == "__main__":
    main()
