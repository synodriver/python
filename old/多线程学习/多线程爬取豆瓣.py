import threading
import requests
import parsel
import os
import time
import re
import random
def dailichi():
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
name = []
img=[]
page_url = []
lock = threading.Lock()
if not os.path.exists('豆瓣'):
    os.mkdir('豆瓣')
def download_img(url,name):
    from  urllib.request import urlretrieve
    urlretrieve(url,'豆瓣'+'/'+'%s.jpg'%name)
def shengchanzhe():
    global img
    global name
    while True:
        lock.acquire()
        if len(page_url)==0:
            lock.release()
            break
        url = page_url.pop()
        lock.release()
        response = requests.get(url,headers = dailichi())
        sle = parsel.Selector(response.text)
        name_title=(sle.xpath('//*[@id="content"]/div/div[1]/ol').re(r'<img width="100" alt="(.*?)" src=".*?" class="">',re.S))
        for x in name_title:
            name.append(x)
        img_url=sle.xpath('//*[@id="content"]/div/div[1]/ol').re(r'<img width="100" alt=".*?" src="(.*?)" class="">')
        for x in img_url:
            img.append(x)
def xiaofeizhe():
    while True:
        lock.acquire()
        if len(img)==0 and len(name)==0:
            lock.release()
            break
        url = img.pop()
        title = name.pop()
        lock.release()
        req = requests.get(url)
        with open('豆瓣'+'/'+'%s.jpg'%title,'wb')as f:
            f.write(req.content)
def page_url_get():
    global page_url
    for xx in range(0,246,25):
        url = 'https://movie.douban.com/top250?start=%s&filter='%str(xx)
        page_url.append(url)
if __name__ == '__main__':
    t2 = time.time()
    page_url_get()
    for num in range(64):
        t = threading.Thread(target=shengchanzhe)
        t.start()
    time.sleep(1)
    for num in range(64):
        t= threading.Thread(target=xiaofeizhe)
        t.start()
    time.sleep(1)
    while len(threading.enumerate())>1:
        pass
    t1 = time.time()
    print(t1-t2)