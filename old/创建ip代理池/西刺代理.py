#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   西刺代理.py
@Time    :   2019/12/18 17:26:14
@Author  :   刘华强
@Contact :   1761512493@qq.com
'''
import requests,parsel,re,time 
from concurrent.futures import ThreadPoolExecutor
import os 
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
    # print(dai)
    head  ={
        'User-Agent':'%s'% dai
    }
    return head
def get_ip(x,y):
    ip = []
    for idd in range(x,y+1):
        url = f'https://www.xicidaili.com/nn/{idd}'
        response = requests.get(url=url,headers=dailichi())
        txt = response.content.decode('utf-8')
        sle = parsel.Selector(response.text)
        ips = sle.xpath('//table[@id="ip_list"]//tr/td[2]/text()').getall()
        duankous = sle.xpath('//table[@id="ip_list"]//tr/td[3]/text()').getall()
        [ip.append([x,y]) for x,y in zip(ips,duankous)]
    return ip

def yanzheng(ip):
    # print(ip)
    proxies= {
        'http':f'{ip[0]}:{ip[1]}',
        'https':f'{ip[0]}:{ip[1]}',
    }
    try :
        url = 'http://httpbin.org/get'
        response = requests.get(url=url,headers=dailichi(),proxies = proxies,timeout=5)
        if response.status_code==200:
            txt = response.json()['origin'].split(',')[0]
            # print(txt)
            print(ip)
            with open('可用ip.txt','a+',encoding='utf-8')as f:    
                f.write(ip[0]+','+ip[1]+'\n')            
    except:  
        #print(ip[0]+':'+ip[1]+'不可用')
        pass
def duoxiancheng(Hanshu,List,Time):
   import time
   from concurrent.futures import ThreadPoolExecutor
   pool= ThreadPoolExecutor(max_workers=32)
   for i in List:
       pool.submit(Hanshu,i)
       time.sleep(Time)
   pool.shutdown()
def xicidaili():
    if os.path.exists('可用ip.txt'):
        os.remove('可用ip.txt')
    x = get_ip(1,1)
    duoxiancheng(yanzheng,x,0)
    file= open('可用ip.txt','r',encoding='utf-8')
    ips = file.read()
    file.close()
    ips = ips.split('\n')[:-1]
    ip = []
    for x in ips:
        x = x.split(',')
        ip.append([x[0],x[1]])
    # print(ip)
    return ip
ips = xicidaili()
print(ips)
