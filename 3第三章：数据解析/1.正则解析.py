# -*- coding:utf-8 -*-
# @TIME : 2021/3/10 14:46
# @Author : MYH
# @File : 1.正则解析.py
# @Software : PyCharm
# @需求 : 爬取糗事百科中糗图板块下所有的糗图图片

import requests
import re
import os

if __name__ == "__main__":
    # 创建一个文件夹保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')

    headers = {
        'User-Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.72Safari / 537.36Edg / 89.0.774.45'
    }
    # 设置一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'

    for pageNum in range(1,14):
        new_url = format(url%pageNum)

        # 使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url, headers=headers).text

        # 使用聚焦爬虫将页面中所有的糗图进行解析、提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt=".*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)

        for src in img_src_list:
            src = 'https:'+src
            # 请求到了图片的二进制数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            # 指定存储的路径
            img_path = './qiutuLibs/'+img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name,'下载成功')
