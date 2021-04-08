# !/usr/bin/env python  
# -*- coding:utf-8 -*-
# Author：卢小布
# Date：2021/4/3 14:19
# File：spider_58.py

import requests
from lxml import etree

url = 'https://fs.58.com/ershoufang/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
# 存储的div标签对象
div_list = tree.xpath('//section[@class="list"]/div')
# print(div_list)
with open('./58.txt', 'w', encoding='utf-8') as fp:
    for div in div_list:
        title = div.xpath('./a/div[2]/div/div/h3/text()')[0]
        print(title)
        fp.write(title+'\n')