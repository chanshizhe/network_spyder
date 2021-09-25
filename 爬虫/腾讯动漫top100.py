# -*- coding = utf-8 -*-
# @TIME : 2020/9/10 9:29
# @Author : MYH
# @File : 腾讯动漫.py
# @Software : PyCharm


import os
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup  #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error  #指定url获取网页数据
import xlwt     #进行Excel操作

def main():
    url = "https://ac.qq.com/Rank/comicRank/type/top"
    datalist = getData()
    savepath = "腾讯动漫top100.xls"
    saveData(datalist, savepath)

findLink = re.compile(r'href="(.*?)"')
findName = re.compile(r'title="(.*?)">')
findRank = re.compile(r'<em class="ui-border-em">(.*?)</em>')


def getData():
    datalist = []
    url = "https://ac.qq.com/Rank/comicRank/type/top"
    html = askURL(url)

    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('ul', class_="rank-ul"):
        # print(item)
        # print(123)
        for i in range(20):
            data = []
            item = str(item)
            link = re.findall(findLink,item)[i]
            link = "https://ac.qq.com"+link
            data.append(link)
            name = re.findall(findName,item)[i]
            data.append(name)
            rank = re.findall(findRank,item)[i]
            data.append(rank)
            # print("https://ac.qq.com"+link)
            # print(name)
            # print(rank)
            datalist.append(data)

    # for i in range(100):
    #     data = datalist[i]
    #     print(data)

    return datalist


def askURL(url):
    head = {
    "User-Agent":"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.132 Safari / 537.36"
    }

    request = urllib.request.Request(url,headers=head)
    html=""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except:
        print("error")

    return html

def saveData(datalist, savepath):
    print("saving...")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("腾讯动漫top100",cell_overwrite_ok=True)
    col = ('链接','名字','排名')
    for i in range(0,3):
        sheet.write(0,i,col[i])
    for i in range(0,5):
        for k in range(0,20):
            print("第%d条" %(i*20+k+1))
            data = datalist[i*20+k]
            #print(data)
            for j in range(0,3):
                sheet.write(i*20+k+1, j, data[j])

    book.save('腾讯动漫top100.xls')



if __name__ == "__main__":
    main()