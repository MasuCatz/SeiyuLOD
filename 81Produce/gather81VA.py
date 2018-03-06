#coding:utf-8

import requests
from bs4 import BeautifulSoup

def inputURL(url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text.encode(r.encoding),"html.parser")

    return soup

if __name__ == '__main__':

    #男性・女性の閲覧ページ
    VAListURL =["http://www.81produce.co.jp/acter/man/","http://www.81produce.co.jp/acter/lady/"]
    
    #各閲覧ページに対してリストを取得する
    for VAurl in VAListURL:

        s = inputURL(VAurl)

        for VAuri in s.find_all("dd"):
            
            #確認
            print(VAuri.a["href"])