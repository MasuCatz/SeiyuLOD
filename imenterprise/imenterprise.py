#coding:utf-8

import json
import time
import requests
from bs4 import BeautifulSoup

#urlのスープ作成
def inputURL(url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text.encode(r.encoding),"html.parser")

    return soup

if __name__ == "__main__":

    f = open("imenterpriseVA.txt","r")
    vaList = f.readlines()

    #事務所の全体辞書
    DicImenterprise = {}

    #各声優のWebページを入力していく
    for currentVA in vaList:

        currentVA_str = str(currentVA)

        #不適切文字列の処理
        currentVA_str = currentVA_str.rstrip("\n")
        
        s = inputURL(currentVA_str)
        s = inputURL("http://www.imenterprise.jp/data.php?id=80")

        #文字列処理 + 名前取得
        name = s.find("tr",attrs={"class":"table01"}).contents[3].string    
        name = str(name)
        name = name.strip()
        name = name.replace(" ","")

        #mp3部分取得
        strHtml = str(s)
        mp3URI = "http://www.imenterprise.jp" + "/" + strHtml[strHtml.find("mp3:") + 6: strHtml.find(".mp3") + 4]

        #声優単位の辞書
        vaData = {"サンプルボイス:" : mp3URI}
        vaDic = {name : vaData}

        print(vaDic)

        #声優の音声データがある場合のみに全体の辞書に追加
        if len(vaData) > 0:
            DicImenterprise.update(vaDic)

        #時間処理
        time.sleep(3)

    #ファイル〆
    f.close

    #確認
    print(json.dumps(DicImenterprise,indent = 4,ensure_ascii=False))

    #json生成
    fw = open("アイムエンタープライズ.json","w")
    json.dump(DicImenterprise,fw,indent = 4,ensure_ascii=False)

    #一部の声優名が化けてるWebページの問題?