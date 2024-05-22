import csv
import sys
import os

def csv_to_kml(csv_file, kml_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダー行をスキップ
        data = list(reader)

    with open(kml_file, 'w', encoding='utf-8') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        file.write('  <Document>\n')

        for row in data:
            file.write('    <Placemark>\n')
            file.write(f'      <name>{row[1]}</name>\n')
            file.write(f'      <address>{row[3]}</address>\n')
            file.write('      <description><![CDATA[\n')
            file.write(f'        <b>法人番号:</b> {row[0]}<br>\n')

            if row[2]:
                file.write('        <b>法人名画像:</b> <br>\n')
                file.write(f'        <img src="{row[2]}" alt="法人名画像"><br>\n')

            file.write(f'        <b>国内住所:</b> {row[3]}<br>\n')

            if row[4]:
                file.write('        <b>国内住所画像:</b> <br>\n')
                file.write(f'        <img src="{row[4]}" alt="国内住所画像"><br>\n')

            if row[5]:
                file.write(f'        <b>海外住所:</b> {row[5]}<br>\n')

            if row[6]:
                file.write('        <b>海外住所画像:</b> <br>\n')
                file.write(f'        <img src="{row[6]}" alt="海外住所画像"><br>\n')

            file.write('      ]]></description>\n')
            file.write('      <styleUrl>#icon-1899-0288D1-labelson</styleUrl>\n')
            file.write('      <ExtendedData>\n')
            file.write('        <Data name="法人番号">\n')
            file.write(f'          <value>{row[0]}</value>\n')
            file.write('        </Data>\n')

            if row[2]:
                file.write('        <Data name="法人名画像">\n')
                file.write(f'          <value>{row[2]}</value>\n')
                file.write('        </Data>\n')

            file.write('        <Data name="国内住所">\n')
            file.write(f'          <value>{row[3]}</value>\n')
            file.write('        </Data>\n')

            if row[4]:
                file.write('        <Data name="国内住所画像">\n')
                file.write(f'          <value>{row[4]}</value>\n')
                file.write('        </Data>\n')

            if row[5]:
                file.write('        <Data name="海外住所">\n')
                file.write(f'          <value>{row[5]}</value>\n')
                file.write('        </Data>\n')

            if row[6]:
                file.write('        <Data name="海外住所画像">\n')
                file.write(f'          <value>{row[6]}</value>\n')
                file.write('        </Data>\n')

            file.write('      </ExtendedData>\n')
            file.write('    </Placemark>\n')

        file.write('  </Document>\n')
        file.write('</kml>\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用法: python script.py input.csv")
        sys.exit(1)

    csv_file = sys.argv[1]
    kml_file = os.path.splitext(csv_file)[0] + ".kml"

    csv_to_kml(csv_file, kml_file)
