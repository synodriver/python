import requests
import parsel
import re  

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
def dd(url):
    response = requests.get(url=url,headers=dailichi())
    txt = response.text
    urls = re.findall('<a href="(.*?)" target=".*?" rel=".*?"> <img src="',txt)
    for url in urls:
        with open(f'F:\\nicemoe\\{url[-15:]}.png','wb')as f:
            f.write(requests.get(url=url,headers=dailichi()).content)

def duoxiancheng(Hanshu,List,Time):
   import time
   from concurrent.futures import ThreadPoolExecutor
   pool= ThreadPoolExecutor(max_workers=10)
   for i in List:
       pool.submit(Hanshu,i)
       time.sleep(Time)
   pool.shutdown()

urlss = []
for num in range(1,3):
    url = f'https://nicemoe02.com/picture/atlas/page/{num}/?by=pop'
    response = requests.get(url=url,headers=dailichi())
    txt = response.text
    sel = parsel.Selector(txt)
    urls  = sel.xpath('//div[@class="poi-row inn-archive__container"]//article/div/a/@href').getall()
    urlss.extend(iter(urls))
print(urlss)
print(len(urlss))
duoxiancheng(dd,urlss,1)
