# -*- coding:utf-8 -*-
# @TIME : 2021/3/2 16:38
# @Author : MYH
# @File : 03.requests实战之破解百度翻译.py
# @Software : PyCharm
# @需求 : 破解百度翻译

# post请求，携带了参数
# 响应数据是一组json数据

import requests
import json

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    # post请求参数处理
    word = input('enter a word:')
    data = {
        'kw':word
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据：json()方法返回的是obj
    # 只有确认响应数据是json类型，才可以使用json方法
    dic_obj = response.json()

    fileName = word+'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('over')

