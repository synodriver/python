import  requests
import re
import os
import parsel
import time
import threading
def download_img(url,name):
    from  urllib.request import urlretrieve
    urlretrieve(url,'./%s.jpg'%name)
# url = 'http://acg17.com/49646.html'
def main(url):
    response = requests.get(url)
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
        download_img(url_img,'./'+name+'/'+'%s'%num)
        # print('下载第%s张图片成功'%num)
        num+=1
if __name__ == '__main__':
    while True:
        # t1 =time.time()
        url = input ("请输入网址：")
        # url = 'http://acg17.com/49993.html'
        # main(url)
        t= threading.Thread(target=main,args=(url,))
        t.start()
        # t2 = time.time()
        # print(t2-t1)
