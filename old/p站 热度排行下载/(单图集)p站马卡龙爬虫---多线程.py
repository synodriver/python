import re
import requests
import time
import random
import os
import threading
name = ''
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

def down(url):
    global name
    # print(name)
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
        with open(f'{name}/' + f'{urll[-15:-7]}.jpg', mode='wb') as f:
            f.write(r.content)
    except:
        pass
    # print(urll)

def main(url):
    global name
    head={
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://www.pixivision.net/zh/c/illustration',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }
    response= requests.get(url,headers = head)
    # print(response.text)
    imgg = re.findall('container fit-inner"><img src="(.*?)"',response.text,re.S)
    name = re.findall('<h1 class="am__title">(.*?)</h1>',response.text,re.S)[0]
    name= name.replace('/','')
    name= name.replace('\\','')
    name= name.replace('*','')
    name= name.replace('>','')
    name= name.replace('<','')
    name= name.replace('\"','')
    name= name.replace('|','')
    name= name.replace('?','')
    if not os.path.exists(name):
        os.mkdir(name)
    for img in imgg:
        img = img.replace ('c/768x1200_80/img-master','img-original')
        img = img.replace ('_master1200','')
        # print(img)
        # down(img)
        threading.Thread(target=down,args={img,}).start()
if __name__ == '__main__':
    # url = 'https://www.pixivision.net/zh/a/4611'
    url = input("输入网站(https://www.pixivision.net/zh/c/illustration)你想要下载的图集的地址:")
    main(url)
