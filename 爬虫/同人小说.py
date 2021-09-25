# -*- coding = utf-8 -*-
# @TIME : 2020/9/19 16:22
# @Author : MYH
# @File : 同人小说.py
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
    url1 = "http://book.zongheng.com/store/c0/c0/b0/u0/p"
    url2 = "/v9/s9/t0/u0/i0/ALL.html"
    datalist = getData()

    savepath = "同人小说.xls"
    saveData(datalist, savepath)

findLink = re.compile((r'<a href="(.*?)" target='))
findType = re.compile(r'target="_blank">(.*?)</a>')
findjianjie = re.compile(r'(?s)<div class="bookintro">(.*?)</div>')
findzhangjie = re.compile(r'最新章节：(.*?)</a>')
findtime = re.compile(r'(?s)更新时间(.*?)</span>')


def getData():
    datalist = []

    url1 = "http://book.zongheng.com/store/c0/c0/b0/u0/p"
    url2 = "/v9/s9/t0/u0/i1/ALL.html"
    for i in range(100):
        url = url1 +str(i)+url2
        html = askURL(url)

        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="bookinfo"):
            #print(item)
            # for i in range(150):
            data = []
            item = str(item)

            link = re.findall(findLink,item)[0]
            data.append(link)

            name = re.findall(findType,item)[0]
            data.append(name)

            author = re.findall(findType,item)[1]
            data.append(author)

            type = re.findall(findType,item)[2]
            data.append(type)

            # time = re.findall(findtime,item)[0]
            # data.append(time)

            # jianjie = re.findall(findjianjie,item)[0]
            # data.append(jianjie)

            zhangjie = re.findall(findzhangjie,item)[0]
            data.append(zhangjie)

            #print(data)
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
    sheet = book.add_sheet("同人小说",cell_overwrite_ok=True)
    col = ('链接','书名','作者','类型','章节')
    for i in range(0,5):
        sheet.write(0,i,col[i])
    for i in range(0,5000):
        print("第%d条" %(i+1))
        data = datalist[i]
        #print(data)
        for j in range(0,5):
            sheet.write(i+1, j, data[j])

    book.save('同人小说.xls')



if __name__ == "__main__":
    main()