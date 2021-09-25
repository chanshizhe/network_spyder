# -*- coding:utf-8 -*-
# @TIME : 2021/3/2 16:30
# @Author : MYH
# @File : 02.requests实战之网页采集器.py
# @Software : PyCharm
# 需求：爬取搜狗指定词条对应的搜索结果页面

# 反爬机制：UA伪装
# UA：User-Agent（请求载体的身份标识）
# 门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，则说明该请求是一个正常的请求
# 如果检测到请求的载体身份标识不是基于某一款浏览器的，则表示该请求为不正常的请求（爬虫），则服务器端可能拒绝该次请求

import requests

if __name__ == "__main__":

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url = 'https://www.sogou.com/web?'
    # 处理url携带的参数:封装到字典中
    kw = input('enter a work:')
    param = {
        'query':kw
    }

    # 对指定url发起请求，对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text

    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName,'保存成功。')
