# -*- coding:utf-8 -*-
# @TIME : 2021/3/2 18:18
# @Author : MYH
# @File : 05.肯德基餐厅位置信息爬取.py
# @Software : PyCharm
# @需求 : 爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数

import requests

if __name__ == "__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    params = {
        'cname':'',
        'pid':'',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10',
    }

    response = requests.post(url=url, params=params, headers=headers)

    text_data = response.text

    print(text_data)
