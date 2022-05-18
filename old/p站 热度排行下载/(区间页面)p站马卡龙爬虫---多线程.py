import re
import requests
import time
import random
import os
import threading
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
    return str(dai)
url_img = []
gg = threading.Lock()
page_url=[]
yemian= []
def down():
    global url_img
    while True:
        gg.acquire()
        if len(url_img)==0:
            gg.release()
            break
        else:
            url = url_img.pop()
            gg.release()
            url = url[:-3]
            try:
                id = url[-12:-4]
                urll = f'{url}png'
                # print(id)
                head = {
                    'referer': f"http://www.pixiv.net/member_illust.php?mode=manga_big&illust_id={str(id)}&page=0",
                    'User-Agent': f'{dailichi()}',
                }

                r= requests.get(urll,headers = head,timeout = 5,)
                if (r.status_code==404):
                    urll = f'{urll[:-3]}jpg'
                    r = requests.get(urll, headers=head,timeout = 5)
                # print(urll)
                with open(f'{urll[-15:-7]}.jpg', mode='wb') as f:
                    f.write(r.content)
            except:
                pass
    # print(urll)

def main():
    global url_img,page_url
    while True:
        gg.acquire()
        if len(page_url)==0:
            gg.release()
            break
        else :
            urll = page_url.pop()
            gg.release()
            response= requests.get(urll)
            # print(response.text)
            imgg = re.findall('container fit-inner"><img src="(.*?)"',response.text,re.S)
            for img in imgg:
                img = img.replace ('c/768x1200_80/img-master','img-original')
                img = img.replace ('_master1200','')
                url_img.append(img)
                # print(img)
                # down(img)


def shengchanzhe():
    # url= 'https://www.pixivision.net/zh/c/illustration/?p=1'
    global yemian
    while True:
        gg.acquire()
        if len(yemian)==0:
            gg.release()
            break
        else:
            url = yemian.pop()
            gg.release()
            response = requests.get(url)
            # print(response.text)
            page_web = list(set(re.findall('href="/en/a/(.*?)"',response.text,re.S)))
            # print(page_web)
            for x in page_web:
                page_url.append(f'https://www.pixivision.net/zh/a/{x}')

def get_yemian(z,y):
    global yemian
    for x in range(z,y+1):
        yemian.append(f'https://www.pixivision.net/zh/c/illustration/?p={str(x)}')
if __name__ == '__main__':
    z = int(input("请输入你的起始页面[a,b]："))
    y = int(input("请输入你的起始页面[b,b+]："))
    n = int(input("请输入你要下载的线程数(ps:线程太大倒是反爬系统监测推荐5到10)："))
    get_yemian(z,y)
    time.sleep(1)
    for _ in range(n):
        threading.Thread(target=shengchanzhe).start()
    time.sleep(2)

    # print(page_url)

    for _ in range(n):
        threading.Thread(target=main).start()

    time.sleep(2)
    # print(url_img)

    for _ in range(n):
        threading.Thread(target=down).start()



