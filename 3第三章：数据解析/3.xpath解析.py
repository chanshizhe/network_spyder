# -*- coding:utf-8 -*-
# @TIME : 2021/3/11 17:34
# @Author : MYH
# @File : 3.xpath解析.py
# @Software : PyCharm
# @需求 : 爬取58二手房中的房源信息

import requests
from lxml import etree

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url = 'https://bj.58.com/ershoufang/?PGTID=0d100000-0000-1940-eb91-7ce95e438d90&ClickID=4'
    page_text = requests.get(url=url, headers=headers).text

    # 数据解析
    tree = etree.HTML(page_text)
    title_list = tree.xpath('//section[@class="list"]/div/a/div[@class="property-content"]/div[@class="property-content-detail"]/div[@class="property-content-title"]/h3/text()')

    fp = open('./58.txt', 'w', encoding='utf-8')
    for title in title_list:
        fp.write(title+'\n')

    print('over')
