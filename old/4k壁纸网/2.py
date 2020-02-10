import re
import parsel
import requests
import random
import threading
import time
gg = threading.Lock()
URL = []
num = 0
def dailichi():
    daili = [
         'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    ]
    dai = random.choice(daili)
    # print(dai)
    head  ={
        'Referer': 'http://www.lyckapp.com/ajax_file_list.php?pg=0&type=0&so_tag=&so_name=',
        'User-Agent':'%s'% dai
    }
    return head
def main():
    global URL
    url = 'http://www.lyckapp.com/ajax_file_list.php?pg=0&type=0&so_tag=&so_name='
    response = requests.get(url,headers = dailichi(),timeout = 5)
    sle  = parsel.Selector(response.text)
    xx = sle.xpath('/html/body').re('src\=\"(.*?)\"')
    num = int(1)
    for urll in xx:
        # print(urll)
        URL.append(urll)
def xiazai():
    global URL
    global num
    while True:
        gg.acquire()
        if len(URL)==0:
            gg.release()
            break
        else :
            url  = URL.pop()
            gg.release()

            try:
                name = url[-19:-4]
                req = requests.get(url,headers = dailichi(),timeout = 5)
                with open(name+'.jpg','wb') as f:
                    f.write(req.content)
                    num= num+1
                    print("正在下载第%s张"%str(num))

            except:
                try:
                    name = url[-19:-4]
                    req = requests.get(url,headers = dailichi(),timeout = 5)
                    with open(name+'.jpg','wb') as f:
                        f.write(req.content)
                        num= num+1
                        print("正在下载第%s张"%str(num))
                except:
                    num+=1
                    print("第%s张下载失败" % str(num))
                    print(url)
                    pass


if __name__ == '__main__':
    n = int(input("输入你要下载的轮数："))
    for x in range(n):
        try:
            main()
            time.sleep(1.5)
            print("正在获取第%s轮的图片地址"%str(x+1))
        except:
            pass
    print("原本"+str(len(URL))+"张图片")
    URl = list(set(URL))
    print("去重后"+str(len(URL))+"张图片")

    for y in range(10):
         threading.Thread(target=xiazai).start()
    while len(threading.enumerate())>1:
         pass
    print("下载完毕")


