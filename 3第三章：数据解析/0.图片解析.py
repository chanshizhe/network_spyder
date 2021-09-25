# -*- coding:utf-8 -*-
# @TIME : 2021/3/10 14:38
# @Author : MYH
# @File : 1.正则解析.py
# @Software : PyCharm
# @需求 : 爬取糗事百科中糗图板块下所有的糗图图片

import requests

if __name__ == "__main__":
    # 如何爬取图片
    url = 'https://pic.qiushibaike.com/system/pictures/12413/124132664/medium/LBBZ8DUMBG0M6JEZ.jpg'
    # content属性返回二进制形式的图片数据
    # .text(字符串)  .content(二进制)  .json(对象)
    img = requests.get(url=url).content

    with open('./qiutu.jpg', 'wb') as fp:
        fp.write(img)