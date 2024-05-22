import re
import sys
import os

def convert_image_urls(kml_string):
    def replace_image_url(match):
        field_name = match.group(1)
        image_url = match.group(2)
        if image_url:
            return f'<b>{field_name}:</b> <br>\n<img src="{image_url}" alt="{field_name}"><br>'
        else:
            return f'<b>{field_name}:</b> <br>'

    patterns = [
        (r'(法人名画像): (.*?)<br>', replace_image_url),
        (r'(国内住所画像): (.*?)<br>', replace_image_url),
        (r'(海外住所画像): (.*?)<br>', replace_image_url),
    ]

    for pattern, replacement in patterns:
        kml_string = re.sub(pattern, replacement, kml_string, flags=re.DOTALL)

    return kml_string

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("使用法: python script.py input.kml")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + "_img.kml"

    # KMLファイルの文字列を読み込む
    with open(input_file, 'r') as file:
        kml_string = file.read()

    # 画像URLを変換する
    converted_kml = convert_image_urls(kml_string)

    # 変換後のKMLを新しいファイルに書き込む
    with open(output_file, 'w') as file:
        file.write(converted_kml)
