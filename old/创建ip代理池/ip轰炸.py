import requests
import parsel
import re
import random
import time
import threading
import os
ip=[]
gg = threading.Lock()
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
    return {'User-Agent': f'{dai}'}
def get_ip():
    global ip
    response = requests.get('http://www.gatherproxy.com/zh/proxylist/country/?c=China',headers = dailichi())
    # print(response.text)
    sle = parsel.Selector(response.text)
    ipp = sle.xpath('//*[@id="tblproxy"]').re('"PROXY_IP":"(.*?)"',re.S)
    # print(sle.xpath('//*[@id="tblproxy"]').getall())
    duankou_16 = sle.xpath('//*[@id="tblproxy"]').re('"PROXY_PORT":"(.*?)"',re.S)
    # print(ipp)
    # print(len(ipp))
    duankou = [str(int(x,16)) for x in duankou_16]
    # print(duankou)
    # print(len(duankou))
    for x in zip(ipp,duankou):
        ip.append(f"{x[0]}:{x[1]}")

def yanzheng():
    global  ip
    while True:
        gg.acquire()
        if len(ip)==0:
            gg.release()
            break
        ip_chi = ip.pop()
        gg.release()
        proxies = {"http": f"http://{ip_chi}", "https": f"http://{ip_chi}"}
        try:
            req = requests.get('https://mcheika.com/', proxies=proxies, timeout=3)
            with open('可用ip.txt','a') as file:
                file.write(ip_chi+'\n')
                    # print('yes')
        except:
            # print('no')
            pass
def requests_get(url):
    # url = 'https://www.doutula.com/photo/list/?page=1'
    import requests
    with open('可用ip.txt','r') as file:
        txt = file.read().split('\n')
    while True:
        proxies = {"http": f"http://{str(txt[0])}", "https": f"http://{str(txt[0])}"}
        try:
            response = requests.get(url,proxies= proxies,timeout = 5)
            return
        except:
            pass
def get_ipchi():
    if os.path.exists('可用ip.txt'):
        os.remove('可用ip.txt')
    get_ip()
    for _ in range(20):
        threading.Thread(target=yanzheng).start()
    while   len(threading.enumerate())>1:
        pass
get_ipchi()
def xxx():
    req = requests_get('https://mcheika.com/')
    # print(req.text)
    print("233")
while True:
    for _ in range(10):
        threading.Thread(target=xxx).start()