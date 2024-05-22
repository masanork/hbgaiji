import csv
import sys

def is_number(value):
    """Check if the value can be converted to a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def filter_and_save_rows(input_file, base_output_file):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # assuming the first row is the header

        gaiji_rows = [header]
        name_rows = [header]
        regional_rows = [header]
        foreign_rows = [header]

        for row in reader:
            if len(row) >= 18:  # Ensure the row has at least 18 columns
                if is_number(row[7]) or is_number(row[12]) or is_number(row[17]):
                    gaiji_rows.append(row)
                if is_number(row[7]):
                    name_rows.append(row)
                if is_number(row[12]):
                    regional_rows.append(row)
                if is_number(row[17]):
                    foreign_rows.append(row)

    save_to_csv(f"{base_output_file}_gaiji.csv", gaiji_rows)
    save_to_csv(f"{base_output_file}_name.csv", name_rows)
    save_to_csv(f"{base_output_file}_regional.csv", regional_rows)
    save_to_csv(f"{base_output_file}_foreign.csv", foreign_rows)

def save_to_csv(filename, rows):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

def main():
    if len(sys.argv) != 2:
        print("Usage: python houjin_gaiji_csv.py <input_csv_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    base_output_file = input_file.rsplit('.', 1)[0]
    filter_and_save_rows(input_file, base_output_file)
    print(f"Filtered rows have been saved to {base_output_file}_gaiji.csv, {base_output_file}_name.csv, {base_output_file}_regional.csv, and {base_output_file}_foreign.csv")

if __name__ == "__main__":
    main()
