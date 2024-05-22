import csv
import sys

def create_map_csv(input_file):
    output_file = input_file.rsplit('.', 1)[0] + '_map.csv'

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the input file's header

        # Define the output header
        output_header = ["法人番号", "法人名", "法人名画像", "国内住所", "国内住所画像", "海外住所", "海外住所画像"]
        output_rows = [output_header]

        for row in reader:
            houjin_bangou = row[1]
            houjin_mei = row[6]

            houjin_mei_image_url = f"https://www.houjin-bangou.nta.go.jp/image?imageid={row[7]}" if row[7].isdigit() else ""

            kokunai_jusho = row[9] + row[10] + row[11]
            kokunai_jusho_image_url = f"https://www.houjin-bangou.nta.go.jp/image?imageid={row[12]}" if row[12].isdigit() else ""

            kaigai_jusho = row[16]
            kaigai_jusho_image_url = f"https://www.houjin-bangou.nta.go.jp/image?imageid={row[17]}" if row[17].isdigit() else ""

            output_row = [
                houjin_bangou,
                houjin_mei,
                houjin_mei_image_url,
                kokunai_jusho,
                kokunai_jusho_image_url,
                kaigai_jusho,
                kaigai_jusho_image_url
            ]
            output_rows.append(output_row)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_rows)

    print(f"Map CSV has been created: {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python houjin2map.py <input_csv_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    create_map_csv(input_file)

if __name__ == "__main__":
    main()
