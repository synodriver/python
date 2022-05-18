import requests
import re 
import json
import time
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
def get_time():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    shijian = re.findall("\d*-\d*-\d*\ (.*)",otherStyleTime)[0]
    return shijian[:-3]
def get_data(): 
    url = "https://api.bilibili.com/x/web-interface/online"
    response = requests.get(url,headers=dailichi())
    date = response.json()['data']
    # print(date)
    # date = {'region_count': {'1': 601, '11': 1, '119': 33, '129': 218, '13': 37, '138': 720, '155': 341, '160': 7230, '165': 48, '167': 31, '17': 1407, '177': 32, '181': 1438, '188': 237, '23': 0, '3': 1458, '36': 1234, '4': 6243, '5': 1589, '75': 543, '76': 455}, 'all_count': 20771, 'web_online': 2710876, 'play_online': 3762202}
    web_online = date['web_online']
    play_online = date['play_online']
    return web_online+play_online
def main():
    time = get_time()
    zong_online = get_data()
    with open(file = "B站在线人数统计.txt",mode = 'a+',encoding='utf-8')as f:
        f.write(f'{str(time)},{str(zong_online)}' + '\n')
print(get_time())
if __name__ == "__main__":
    while True:
        main()