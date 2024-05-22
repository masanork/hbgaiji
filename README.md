法人番号検索サイト全件CSVファイル関連ツール
===

ファイル構成
---

- houjin_gaiji_csv.py: 外字CSVファイル分割ツール
- houjin2map.py: 地図用CSV変換ツール
- csv_us.py: 縮退不可能文字の代替「＿」を含む行の抽出
- csv2kml.py: 地図用CSVをGoogle MyMapのKML形式に変換
- gethning.py: 外字画像ファイル取得ツール

外字KMLファイルの作成方法
---

$ python houjin_gaiji_csv.py 00_zenkoku_all_YYYYMMDD.csv
$ python houjin2map.py 00_zenkoku_all_YYYYMMDD_*
$ python csv_us.py 00_zenkoku_all_YYYYMMDD_*
$ python csv2kml.py 00_zenkoku_all_YYYYMMDD_gaiji_us.csv
00_zenkoku_all_YYYYMMDD_gaiji_us.kml
