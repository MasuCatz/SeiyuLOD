#coding:utf-8

import json
import time
import requests
from bs4 import BeautifulSoup

def inputURL(url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text.encode(r.encoding),"html.parser")

    return soup

if __name__ == '__main__':   

    #声優リストファイルのオープン処理
    f = open("osawaVA.txt","r")

    #声優リストの1行毎のデータ(URI)
    vaList = f.readlines()

    #全体の辞書
    dataDic2={}

    #声優毎のループ
    for currentURI in vaList:

        #大沢事務所の各声優のWebページ
        seiyuPage = currentURI

        #声優のスープ作成
        soupData = inputURL(currentURI)

        #確認
        print(soupData)
        
        #名前取得用(もっと楽に作りたい)
        nameSearch = []

        #名前取得
        for vaName in soupData.find_all("h2"):
            nameSearch.append(vaName.get_text())

        #名前
        #改行・全角スペース削除
        nameVA = nameSearch[1].replace("\n","")
        nameVA = nameVA.replace("\r","")
        nameVA = nameVA.replace("\u3000","")

        #ループ変数
        i = 1

        # 各音声とURLの辞書(声優単位)
        dataDic = {}                

        #声優個人の音声ファイルの数だけループ
        for jar in soupData.find_all("param",attrs={"name":"FlashVars"}):

            # URI部分取得
            getURI = (seiyuPage + "/../" + jar["value"][5:]).replace("\n","")

            #音声キーワード
            keyS = "音声" + str(i)

            #音声の連番号とURIの辞書
            tempDic={keyS:getURI}

            #声優個人の音声・URIの辞書に追加
            dataDic.update(tempDic)

            # ループ変数更新
            i = i + 1

        #声優個人の名前と声優データの辞書生成
        tempDic2={nameVA:dataDic}

        #全体辞書dataDic2に追加
        if len(dataDic) > 0:
            dataDic2.update(tempDic2)
        
        time.sleep(3)
    
    #ファイル閉め
    f.close

    #確認
    print(json.dumps(dataDic2,indent=4,ensure_ascii=False))

    #生成
    fw = open("osawaVA.json","w")
    json.dump(dataDic2,fw,indent=4,ensure_ascii=False)