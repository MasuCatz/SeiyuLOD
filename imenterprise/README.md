# 声優情報取得プログラム(アイムエンタープライズ)

=====

## 概要
アイムエンタープライズに所属する声優のサンプルボイスを取得しjson形式で出力するプログラム

## 説明
言語：Python3

使用ライブラリ：BeautifulSoup4

・imenterpriseVA.txt：あらかじめ作成した声優のWebページのURLをまとめたもの

・imenterprise.py：声優のWebページ上に記載されているサンプルボイスにあたるURLを抽出し、json形式へ変換

・imenterprise_All.html:事務所に所属する全声優のWebページが記載されているURL

①：imenterpriseVA.txt・imenterprise.pyの2ファイルを同じディレクトリに配置。

②：imenterprise.pyを実行で"アイムエンタープライズ.json"というファイルが出力される。

## ライセンス
MIT

## Author

Maskapara