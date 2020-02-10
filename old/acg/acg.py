import  requests
import re
import os
import parsel
import time
import random
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
    # print(dai)
    head  ={
        'User-Agent':'%s'% dai
    }
    return head
def download_img(url,name):
    from  urllib.request import urlretrieve
    urlretrieve(url,'./%s.jpg'%name)
def html_down(url):
    response = requests.get(url,headers = dailichi())
    sle = parsel.Selector(response.text)
    name = str(sle.xpath('//*[@id="the-post"]/div/h1/span').re('"name">(.*?)</span>')[0])
    name = name.replace('*','')
    name = name.replace('\\','')
    name = name.replace('/','')
    name = name.replace('?','')
    name = name.replace('\"','')
    name = name.replace(':','')
    name = name.replace('>','')
    name = name.replace('<','')
    if not os.path.exists(name):
        os.mkdir(name)
    img =sle.xpath('//*[@id="the-post"]/div/div[2]').re('src="(.*?)"')
    # print(id)
    num = 1
    for url_img in img[:-2]:
        # print(url_img)
        try:
            download_img(url_img,'./'+name+'/'+'%s'%num)
            print('下载第%s张图片成功' % num)
        except:
            print("这一张图下载失败！！")
        num+=1
def main(url):
    response = requests.get(url)
    sle = parsel.Selector(response.text)
    urll = list(set(sle.xpath('//*[@id="main-content"]/div[1]/div[3]').re('<a href="(.*?).html">')))
    for xx in urll:
        # print(x+'.html')
        xx = xx +'.html'
        # print(xx)
        html_down(xx)
        # print("休息五秒钟（为了防止他认为你是爬虫）")
        # for zz in range(5):
        #     time.sleep(1)
        #     print("还剩%s秒"%str(5-zz))
if __name__ == '__main__':
    # url = 'http://acg17.com/category/meitu/pixiv-painter/'
    print("在这个网站下http://acg17.com/category/meitu/pixiv-painter/")
    z = input ("请输入网址你要爬取的起始页数[1,152]:")
    y = input ("请输入网址你要爬取的末尾页数[1,152]:")
    z=  int(z)
    y = int(y)
    t1 = time.time()
    for num in range(z,y+1):
        if num == 1:
            url ='http://acg17.com/category/meitu/pixiv-painter/'
        else :
            url ='http://acg17.com/category/meitu/pixiv-painter/page/%s/'%num
        # main(url)
        threading.Thread(target=main,args=(url,)).start()
    t2 = time.time()
    print(t2-t1)
    # t2 = time.time()
    # print(t2-t1)