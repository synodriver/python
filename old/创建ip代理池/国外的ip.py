import requests
import parsel
import re
import random
import time
import threading
import os
class ip_daili_chi():
    ip = []
    gg = threading.Lock()

    def __init__(self):
        self.get_ipchi()
        self.get_ip()
        time.sleep(1)
        self.main()

    def get_ipchi(self):
        if os.path.exists('可用ip.txt'):
            os.remove('可用ip.txt')

    def get_ip(self):
        response = requests.get('http://www.gatherproxy.com/zh/proxylist/country/?c=China', headers=self.dailichi())
        sle = parsel.Selector(response.text)
        ipp = sle.xpath('//*[@id="tblproxy"]').re('"PROXY_IP":"(.*?)"', re.S)
        duankou_16 = sle.xpath('//*[@id="tblproxy"]').re('"PROXY_PORT":"(.*?)"', re.S)
        duankou = []
        for x in duankou_16:
            duankou.append(str(int(x, 16)))
        for x in zip(ipp, duankou):
            self.ip.append(x[0] + ":" + x[1])

    def dailichi(self):
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
        head = {
            'User-Agent': '%s' % dai
        }
        return head

    def yanzheng(self):
        while True:
            self.gg.acquire()
            if len(self.ip) == 0:
                self.gg.release()
                break
            ip_chi = self.ip.pop()
            # print(ip_chi)
            self.gg.release()
            proxies = {
                "http": "http://" + ip_chi,
                "https": "http://" + ip_chi,
            }
            try:
                req = requests.get('https://mcheika.com/', proxies=proxies, timeout=3)
                # print(ip_chi)
                file = open('可用ip.txt', 'a')
                file.write(ip_chi + '\n')
                file.close()
                # print('yes')
            except:
                # print('no')
                pass

    def main(self):
        for x in range(20):
            threading.Thread(target=self.yanzheng).start()
        while len(threading.enumerate()) > 1:
            pass

    def requests_get(self,url):
        # url = 'https://www.doutula.com/photo/list/?page=1'
        import requests
        file = open('可用ip.txt','r')
        txt = file.read().split('\n')
        file.close()
        for ip in txt:
            proxies = {
                "http": "http://%s"%str(ip),
                "https": "http://%s"%str(ip),
            }
            try:
                response = requests.get(url,proxies= proxies,timeout = 5)
                # print(response.text)
                return response
            except:
                pass
        print("没有可用ip")

a = ip_daili_chi()
response = a.requests_get('https://www.baidu.com')
print(response.text)
















