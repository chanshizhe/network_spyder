# -*- coding:utf-8 -*-
# @TIME : 2021/3/10 15:27
# @Author : MYH
# @File : 2.bs4解析基础.py
# @Software : PyCharm
# @需求 : 爬取三国演义小说所有的章节标题和内容

from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

    page = requests.get(url=url,headers=headers)
    page.encoding = 'utf-8'
    page_text = page.text

    # 在首页中解析出章节的标题和详情页的url
    # 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    # print(soup)
    # 解析章节标题和详情页url
    li_list = soup.select('.book-mulu > ul > li')

    fp = open('./三国.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.text
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析章节内容
        detail_page = requests.get(url=detail_url, headers=headers)
        detail_page.encoding = 'utf-8'
        detail_page_text = detail_page.text
        # 解析出详情页中相关的章节内容
        soup_detail = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = soup_detail.find('div', class_='chapter_content')
        content = div_tag.text

        fp.write(title+'：'+content+'\n')
        print(title,'爬取成功')




