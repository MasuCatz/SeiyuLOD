#coding:utf-8

import json
import time
import requests
from bs4 import BeautifulSoup

#1〜1622

def inputURL(url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text.encode(r.encoding),"html.parser")

    return soup

if __name__ == '__main__':

    soupData = inputURL("http://neoapo.com/characters/search/1/?mode=d")

    gatherA = []

    #gatherA = soupData.find_all("div",attrs={"class":"article_list"})
    gatherA = soupData.find("div",attrs={"class":"article_list"}).find_all("a")

    for tagA in gatherA:
        print(tagA["href"])
        time.sleep(3)

    # for tagA in soupData.find_all("div",attrs={"class":"article_list"}):
    #     #gatherA.append(tagA.get_text().find_all("a"))
    #     print(tagA.find_all("a",attrs={"name":""}))
    #     time.sleep(3)