# -*- coding = utf-8 -*-
# @TIME : 2020/9/21 11:33
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
    urlbase = "https://ac.qq.com/Comic/index/state/pink"
    datalist = getData()
    savepath = "腾讯动漫.xls"
    saveData(datalist, savepath)

findLink = re.compile(r'<a href="(.*?)"')
findName = re.compile(r'title="(.*?)">')
findType = re.compile(r'target="_blank">(.*?)</span>')
findFire = re.compile(r'<em>(.*?)</em>')


def getData():
    datalist = []
    urlbase = "https://ac.qq.com/Comic/index/state/pink/page/"
    for i in range(178):
        url=urlbase + str(i)
        html = askURL(url)

        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="ret-works-info"):
            # print(item)
            # print(123)
            data = []
            item = str(item)
            link = re.findall(findLink,item)[0]
            link = "https://ac.qq.com"+link
            data.append(link)

            name = re.findall(findName,item)[0]
            data.append(name)

            type1 = re.findall(findType,item)[0]
            data.append(type1)
            type2 = "玄幻"
            if i != 85 and i !=138 and i != 171 and i != 174:
                type2 = re.findall(findType,item)[1]
            data.append(type2)

            fire = re.findall(findFire,item)[0]
            data.append(fire)
            # print("https://ac.qq.com"+link)
            # print(name)
            # print(rank)
            datalist.append(data)
        print(i+1)
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
    sheet = book.add_sheet("腾讯动漫",cell_overwrite_ok=True)
    col = ('链接','名字','类型1','类型2','人气')
    for i in range(0,5):
        sheet.write(0,i,col[i])
    for i in range(0,2136):
        print("第%d条" %(i+1))
        data = datalist[i]
        #print(data)
        for j in range(0,5):
            sheet.write(i+1, j, data[j])

    book.save('腾讯动漫.xls')



if __name__ == "__main__":
    main()