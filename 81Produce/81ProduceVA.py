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

if __name__ == '__main__':   
    
    f = open("81VA.txt","r")
    vaList = f.readlines()    

    #81プロデュース全体の声優辞書
    Dic81={}

    fva = open("81VAList.csv","a")

    #各声優のWebページを入力する
    for currentVA in vaList:

        #不適切な文字列の削除処理
        currentVA = currentVA.replace("\n","")
        currentVA = currentVA.replace("\r","")
        currentVA = currentVA.replace("\u3000","")

        #声優単位でのwebページ
        s = inputURL(currentVA)

        #確認(指定したページと異なるスープが出来る?)
        print(s)

        #声優名取得
        nameVA = str(s.find("div",attrs={"id":"pan"}).contents[0])
        nameVA = nameVA[:-1]

        #不適切な文字列の削除処理
        nameVA = nameVA.replace("\n","")
        nameVA = nameVA.replace("/r","")
        nameVA = nameVA.replace("\u3000","")

        #音声名
        nameSS = []
        for nameS in s.find_all("img",attrs={"border":"0"}):
            
            #"サンプルボイス"を含むものだけnameSSに追加
            if "サンプルボイス" in nameS["alt"]:
                nameSS.append(nameS["alt"])
        
        #音声URI部分取得 + 声優データ辞書作成
        makeDataCount = 0

        #声優毎の辞書データ
        vaData={}

        #音声データ数だけループ
        for sURI in s.find_all("audio"):
            #確認
            #print(sURI["src"])

            #URI補完生成
            vaURI = "http://www.81produce.co.jp/" + sURI["src"]
            
            #文字列整理
            vaURI = vaURI.replace("\n","")
            vaURI = vaURI.replace("\r","")
            vaURI = vaURI.replace("\u3000","")

            vaData.update({nameSS[makeDataCount]:vaURI})
            makeDataCount = makeDataCount + 1

        #声優単位の辞書
        vaND={nameVA:vaData}

        #声優の音声データがある場合のみに全体の辞書に追加
        if len(vaData) > 0:
            Dic81.update(vaND)
        
        #確認
        print(vaData)

        fva.write(nameVA + "," + currentVA + "\n")

        time.sleep(3)

    #ファイル〆
    f.close
    fva.close

    #確認
    print(json.dumps(Dic81,indent=4,ensure_ascii=False))

    #生成
    #fw = open("81プロデュース.json","w")
    #json.dump(Dic81,fw,indent=4,ensure_ascii=False)