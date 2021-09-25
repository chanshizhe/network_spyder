
from bs4 import BeautifulSoup
import xlwt
import xlrd
import requests
import re


def getData():
    book = xlrd.open_workbook('./xhs.xlsx')
    sheet1 = book.sheets()[0]
    nrows = sheet1.nrows

    datalist = []

    for rows in range(0, nrows):
        data = []
        url_id = sheet1.row_values(rows)[0]
        url_base = 'https://www.xiaohongshu.com/discovery/item/'
        url = url_base+url_id
        data.append(url)

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'xhsTrackerId=e043f316-14f4-4112-c1a3-78800d033479; xhs_spid.5dde=50bcd5a2ecec833f.1586698129.1.1586698148.1586698129.c00103d5-f5d0-4cdf-9298-9ce1d78b7523; xhsSEM=07877214-c251-415d-a13c-b075db26cbb6; timestamp2=20210922d919f98798c3291594ea65ad; timestamp2.sig=X1Fe0pp06X1EJ1U24r1YjLaF_a0SYlhPMCtQUdJIJfA; xhsTracker=url=user-profile&searchengine=baidu; extra_exp_ids=gif_exp1,ques_clt2',
            'dnt': '1',
            'pragma': 'no-cache',
            'referer': 'https://www.xiaohongshu.com/discovery/item/61445e10000000000102f442',
            'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
            'x-b3-traceid': 'b290c01e18a4917c',
            'x-s': '1lcCZBci125pZgAW1iaBsBUU0j1LZ2MGZgkBZYTp1gF3',
            'x-t': '1632388036688'
        }

        page = requests.get(url=url, headers=headers)
        page.encoding = 'utf-8'
        page_text = page.text

        soup = BeautifulSoup(page_text,'lxml')

        # print(soup)

        title_all = soup.title
        # print(title)

        ex = '<title>(.*?)_'
        title = re.findall(ex, str(title_all), re.S)[0]
        # print(img_src_list[0])
        data.append(title)
        # print(data)

        datalist.append(data)

    return datalist, nrows

def saveData(datalist, savepath,nrows):
    print("saving...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("数据", cell_overwrite_ok=True)
    col = ('链接','名字','超链接')
    for i in range(0,3):
        sheet.write(0,i,col[i])
    for i in range(0, nrows):
        print("第%d条" % (i + 1))
        data = datalist[i]
        # print(data)
        for j in range(0, 3):
            if j<=1:
                sheet.write(i + 1, j, data[j])
            else:
                sheet.write(i+1, j, xlwt.Formula('HYPERLINK("%s","%s")'%(data[0],data[1])))

    book.save('小红书数据.xls')



if __name__ == "__main__":
    datalist, nrows = getData()


    savepath = "./小红书数据.xls"
    saveData(datalist, savepath, nrows)


