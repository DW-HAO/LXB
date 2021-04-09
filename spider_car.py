# !/usr/bin/env python  
# -*- coding:utf-8 -*-
# Author：卢小布
# Date：2021/4/7 10:57
# File：spider_car.py

import requests
from lxml import etree
import os

url = 'https://pic.netbian.com/4kqiche/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
page_text = requests.get(url=url, headers=headers).text


tree = etree.HTML(page_text)
tree_list = tree.xpath('//div[@class="slist"]//li')

if not os.path.exists('./carpic'):
    os.mkdir('./carpic')
for li in tree_list:
    pic_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    pic_name = li.xpath('./a/img/@alt')[0] + '.jpg'
    pic_cname = pic_name.encode('iso-8859-1').decode('gbk')
    # print(pic_name, pic_src)

    pic_data = requests.get(url=pic_src, headers=headers).content
    pic_path = 'carpic/' + pic_cname
    with open(pic_path, 'wb') as fp:
        fp.write(pic_data)
        print(pic_cname, "下载成功!")

