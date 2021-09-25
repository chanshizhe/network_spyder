# -*- coding:utf-8 -*-
# @TIME : 2021/3/2 17:27
# @Author : MYH
# @File : 04.豆瓣电影爬取.py
# @Software : PyCharm
# @需求 : 爬取豆瓣电影排行榜

import requests
import json

if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',# 从库中的第几部电影取
        'limit': '60',# 一次请求取出的个数
    }

    response = requests.get(url=url, params=params, headers=headers)
    list_data = response.json()

    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print('over.')
