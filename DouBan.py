# !/usr/bin/env python  
# -*- coding:utf-8 -*-
# Author：卢小布
# Date：2021/3/24 16:45
# File：DouBan.py


import requests
import json
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list?'

    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0', # 从库中的第几部电影去取
        'limit': '20' # 一次请求取出的个数
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)

    list_data = response.json() # 接收响应数据

    with open('test/DouBan.json', 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp=fp, ensure_ascii=False)     # 将响应数据存储到指定目录 为.json文件

    print('over!!')