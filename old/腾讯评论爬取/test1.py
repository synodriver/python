# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  刘华强
@Version        :  
------------------------------------
@File           :  test1.py
@Description    :  
@CreateTime     :  2019/12/12 11:33
------------------------------------
@ModifyTime     :  
"""
import requests
import re
import time
# import  sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
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
def get_id(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    video_id = re.findall('\"comment_id\"\:\"(.*?)\"',req.text)[0]
    title  = re.findall('\<title\>(.*?)\<\/title\>',req.text)[0]
    return video_id,title
def main(video_id,xx_id,title):
    while True:
        try:
            url  = "https://video.coral.qq.com/varticle/"+video_id+"/comment/v2?callback=_varticle4489357899commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+xx_id+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&"
            # print(url)
            response = requests.get(url,headers = dailichi())
            # print(response.text)
            txt_data = re.findall('\"content\"\:\"(.*?)"\,\"up\"\:',response.text)
            # print(txt_data)
            for y in txt_data:
                with open(file='%s.txt'%str(title),encoding='utf-8',mode='a+')as f:
                    f.write(y+'\n')
            xx_id = re.findall('"last":"(.*?)"',response.text)[0]
        except:
            break
        time.sleep(0.5)

def mainn(url):
    # url = 'https://v.qq.com/x/cover/m441e3rjq9kwpsc/m00253deqqo.html'
    video_id ,title= get_id(url)
    main(video_id,'0',title)
def get_url_list(url):
    headers = {
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "6028852a-9501-4d6c-b0fa-7b19792d6352,386cbd7f-5af6-485a-9866-36a2283faada",
        'Host': "v.qq.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers)
    response.encoding = 'GBK'
    urll = re.findall("\<a href\=\"(.*?)\" _stat\=\"videolist\:click\" r\-on\=\"\{click\: changeToVideo\.bind\(null\,\'.*?\'\)\}\"\>",response.text)
    url_list = ['https://v.qq.com'+str(i) for i in urll]
    url_list = list(set(url_list))
from concurrent.futures import ThreadPoolExecutor
if __name__ == '__main__':
    # url = input("腾讯视频地址：")
    url = "https://v.qq.com/x/cover/m441e3rjq9kwpsc.html"
    url_list = get_url_list(url)
    pool= ThreadPoolExecutor(max_workers=5)
    import time
    num =1
    for i in url_list:
        pool.submit(mainn,i)
        time.sleep(5)
        print(num)
        num+=1
    pool.shutdown()