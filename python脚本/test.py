#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from urllib import request as ur
import re
import csv

def get_html(url):
    # 请求站点获得一个HTTPResponse对象
    response = ur.urlopen(url)
    # 网页内容
    html = response.read().decode('utf-8')
    #print(html)
    return html

def deal_with(data):

    pattern = re.compile('<li>\s+<time\sdatetime="(\d{4})-(\d{2})-(\d{2}).*?</time>\s+<a\shref=".*?>(.*?)</a></li>',re.S)
    items = re.findall(pattern, data)
    #print(items[:5])
    return items[:5]

def write_data(items):
    headers = ['日期','标题']
    # python-latest-news.csv
    # 用utf-8 会导致中文乱码
    with open('python-latest-news.csv','w+',encoding='utf-8',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        rows=[]
        for cnt in items:
            datetime = cnt[0]+"-"+cnt[1]+"-"+cnt[2]
            news = cnt[-1]
            #print(news)
            row = [datetime,news]
            rows.append(row)
        #print(rows)
        f_csv.writerows(rows)
    f.close()
def main():

    url = 'https://www.python.org'
    # 获取html文件
    data = get_html(url)

    # 处理数据
    items = deal_with(data)
    # 写入数据
    write_data(items)
    print("写入数据成功~")
    return None

if __name__ == '__main__':
    main()