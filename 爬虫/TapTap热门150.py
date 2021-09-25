# -*- coding = utf-8 -*-
# @TIME : 2020/9/11 11:27
# @Author : MYH
# @File : TapTap热门150.py
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
    url = "http://127.0.0.1:5000/1"
    datalist = getData()

    savepath = "TapTap热门150.xls"
    saveData(datalist, savepath)

findLink = re.compile(r'href="(.*?)"')
findName = re.compile(r'title="(.*?)"/>')
findRank = re.compile(r'<span class="top-card-order-text orange">(.*?)</span>')
findType = re.compile(r'">(.*?)</a>')
findStore = re.compile(r'">厂商:\xa0(.*?)</a>')
findStar = re.compile(r'<span>(.*?)</span>')
findJianjie= re.compile(r'</div class="myh">(.*?)</p><div class="card-tags">')


def getData():
    datalist = []
    url = "http://127.0.0.1:5000/1"
    html = askURL(url)

    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="taptap-top-card"):
        print(item)
        # for i in range(150):
        data = []
        item = str(item)

        # rank = re.findall(findRank,item)[0]
        # data.append(rank)

        link = re.findall(findLink,item)[0]
        #link = "https://ac.qq.com"+link
        data.append(link)

        name = re.findall(findName,item)[0]
        data.append(name)

        star = re.findall(findStar,item)[0]
        data.append(star)

        store = re.findall(findStore,item)[0]
        data.append(store)

        type1 = re.findall(findType,item)[1]
        data.append(type1)
        type2 = re.findall(findType,item)[2]
        data.append(type2)
        type3 = re.findall(findType,item)[3]
        data.append(type3)
        type4 = re.findall(findType,item)[4]
        data.append(type4)
        #
        # jianjie = re.findall(findJianjie,item)[0]
        # data.append(jianjie)

        print(data)
        # print(link)
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
        # print(html)
    except:
        print("error")

    return html

def saveData(datalist, savepath):
    print("saving...")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("TapTap150",cell_overwrite_ok=True)
    col = ('链接','名称','评分','厂商','类型1','类型2','类型3','类型4','简介')
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,150):
        print("第%d条" %(i+1))
        data = datalist[i]
        print(data)
        for j in range(0,8):
            sheet.write(i+1, j, data[j])

    book.save('TapTap150.xls')



if __name__ == "__main__":
    main()