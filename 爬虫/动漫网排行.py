# -*- coding = utf-8 -*-
# @TIME : 2020/9/10 15:46
# @Author : MYH
# @File : 动漫网排行.py
# @Software : PyCharm


import os
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup  #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error  #指定url获取网页数据
import xlwt     #进行Excel操作
import math

def main():
    url = "http://www.dongmanwang.com/top/"
    datalist = getData()
    savepath = "动漫网分类排行.xls"
    saveData(datalist, savepath)

findLink = re.compile(r'href="(.*?)"')
findName = re.compile(r'target="_blank">(.*?)</a>')
findRank = re.compile(r'<em class="ui-border-em">(.*?)</em>')
findTitle = re.compile(r'<h3>(.*?)</h3>')


def getData():
    datalist = []
    url = "http://www.dongmanwang.com/top/"
    html = askURL(url)

    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="maxBox lb mb5 newp"):
        for i in range(42):
            for j in range(15):
                data = []
                item = str(item)
                #print(item)
                title = re.findall(findTitle, item)[math.floor(i)]
                data.append(title)
                link = re.findall(findLink,item)[15*i+j]
                link = "http://www.dongmanwang.com"+link
                data.append(link)
                name = re.findall(findName,item)[15*i+j]
                data.append(name)
                # print(link)
                # print(name)
                # print(rank)
                datalist.append(data)
    #print(datalist)
    # for i in range(100):
    #     data = datalist[i]
    #     print(data)

    return datalist


def askURL(url):
    head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }

    request = urllib.request.Request(url,headers=head)
    html=""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
        #print(html)
    except:
        print("error")

    return html

def saveData(datalist, savepath):
    print("saving...")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("动漫网分类",cell_overwrite_ok=True)
    col = ('分类','连接','名字')
    for i in range(0,3):
        sheet.write(0,i,col[i])
    for i in range(0,630):
        print("第%d条" %(i+1))
        data = datalist[i]
            #print(data)
        for j in range(0,3):
            sheet.write(i+1, j, data[j])

    book.save('动漫网分类排行.xls')



if __name__ == "__main__":
    main()