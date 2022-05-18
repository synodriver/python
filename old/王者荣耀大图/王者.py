import re
import requests
import parsel
import time
import random
import threading
import requests
import parsel
import re
import random
import time
import threading
import os
def requests_get(url):
    # url = 'https://www.doutula.com/photo/list/?page=1'
    import requests
    with open('F:\\可用ip.txt','r') as file:
        txt = file.read().split('\n')
    for ip in txt:
        proxies = {"http": f"http://{str(ip)}", "https": f"http://{str(ip)}"}
        try:
            # print(response.text)
            return requests.get(url,proxies= proxies,timeout = 5)
                    # break
        except:
            pass

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


img = []
url_page=[]
gg = threading.Lock()

def get_page():
    global url_page
    for num in range(19):
        url = (
            f'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={str(num)}'
            + '&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17105686725581784895_1567387993957&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=156738817'
        )

        url_page.append(url)
    # print(url_page)

def get_url():
    global url_page,img
    while True:
        gg.acquire()
        if len(url_page)==0:
            gg.release()
            break
        else :
            # url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page='+str(num)+'&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17105686725581784895_1567387993957&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=156738817'
            url = url_page.pop()
            gg.release()
            response = requests.get(url,headers = dailichi())
            # response = requests_get(url)
            # response.encoding= response.apparent_encoding
            # print(response.text)
            imgg = response.text
            imgg = imgg.replace('%3A', ':')
            imgg = imgg.replace('%2F', '/')
            imgg = imgg.replace('%2E', '.')
            imgg = imgg.replace('%5F', '_')
            imgg = imgg.replace('/200', '/0')
            imgg = imgg.replace('sProdImgNo_1', 'sProdImgNo_2')
            img+=(re.findall('"sThumbURL":"(.*?)"',imgg,re.S))

def down_img():
    global img
    while True:
        gg.acquire()
        if len(img)==0:
            gg.release()
            break
        else:
            url = img.pop()
            gg.release()
            num = url[36:46]
            # req = requests_get(url)
            # print(url)
            numm = 0
            while requests.get(url, headers=dailichi()).status_code != 200:
                if url[44] == '0':
                    url = f'{url[:44]}0{str(int(url[44:46]) + 1)}{url[46:]}'
                else:
                    url = url[:44] + str(int(url[44:46]) + 1) + url[46:]
                # print(url)
                if numm > 50:
                    break
                numm += 1

            with open(f'{str(num)}.jpg', 'wb') as f:
                f.write(requests.get(url, headers=dailichi()).content)



if __name__ == '__main__':
    get_page()
    for _ in range(32):
        threading.Thread(target=get_url).start()

    time.sleep(1)

    for _ in range(32):
        threading.Thread(target=down_img).start()
