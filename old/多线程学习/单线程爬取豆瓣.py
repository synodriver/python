#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   单线程爬取豆瓣.py
@Time    :   2019/12/16 17:13:53
@Author  :   刘华强
@Contact :   1761512493@qq.com
'''

import os
if not os.path.exists('豆瓣'):
    os.mkdir('豆瓣')
import requests
def dailichi():
    import random
    daili = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; WOW64; Trident/4.0; SLCC1)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    ]
    dai = random.choice(daili)
    return {'User-Agent': f'{dai}'}
def down_img(url,name):
    with open(file = '豆瓣'+'/'+name+'.jpg',mode='wb')as f:
        f.write(requests.get(url=url,headers=dailichi()).content)
def down_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    }
    response = requests.get(url= url,headers=headers)
    html = response.text
    import re 
    txt = re.findall('<img width="100" alt="(.*?)" src="(.*?)" class="">',html)
    [down_img(i[1],i[0]) for i in txt]

for num in range(0,251,25):  
    url = f'https://movie.douban.com/top250?start={str(num)}&filter='
    down_page(url)