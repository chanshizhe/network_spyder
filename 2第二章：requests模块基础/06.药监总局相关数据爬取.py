# -*- coding:utf-8 -*-
# @TIME : 2021/3/2 18:27
# @Author : MYH
# @File : 06.药监总局相关数据爬取.py
# @Software : PyCharm
# @需求 : 爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据http://scxk.nmpa.gov.cn:81/xk/

import requests
import json

if __name__ == "__main__":

    id_list = []
    allData = []

    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    for page in range(1, 6):
        page = str(page)
        params = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':'',
        }

        json_ids = requests.post(url=url, params=params, headers=headers).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    # print(id_list)

    url_2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        params_2 = {
            'id':id
        }
        detail_json = requests.post(url=url_2, params=params_2, headers=headers).json()
        # print(detail_json)
        allData.append(detail_json)

    fp = open('./allData.json', 'w', encoding='utf-8')
    json.dump(allData, fp=fp, ensure_ascii=False)

    print('over.')
