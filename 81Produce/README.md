# 声優情報取得プログラム(81プロデュース)

=====

## 概要
81プロデュースに所属する声優のサンプルボイスを取得しjson形式で出力するプログラム

## 説明
言語：Python3

使用ライブラリ：BeautifulSoup4

・81VAList.csv：あらかじめ作成した声優名と声優毎のURLまとめ

・81VA.txt：声優のWebページのURLをまとめたもの

・81Produce.py:声優のWebページ上に記載されているサンプルボイスにあたるURLを抽出し、json形式に変換

①：81VA.txt・81Produce.pyの2ファイルを同ディレクトリに配置。

②：81Produce.pyを実行で"81プロデュース.json"というファイルが出力される。

## ライセンス
MIT

## Author

Maskapara