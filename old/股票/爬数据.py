
import requests
import parsel
import re
import threading
gg = threading.Lock()
URL = []
file = open('list.txt','r')
urll = file.readlines()
# print(urll)
file.close()
def url_list():
    global URL
    for x in urll:
        x= x.split('\t')
        url = "http://gu.qq.com/%s/gp"%x[1][:-1]
        URL.append(url+' '+x[0])
# print(URL)
def down(url,name):
    try:
        response = requests.get(url)
        # print(response.text)
        sel = parsel.Selector(response.text)
        txtt = sel.xpath('//*[@id="hqpanel"]/div[2]').getall()[0]
        zuoshou = re.findall('昨\ 收\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\"\..*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[0]
        zuigao = re.findall('最\ 高\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\"\..*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[0]
        chengjiaoliang = \
        re.findall('成交量\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\"\..*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[0]
        jinkai = re.findall('今\ 开\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\".*?"\>(.*?)\<\/span\>\<\/li\>', txtt)[0]
        chengjiaoge = \
        re.findall('成交额\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\"\..*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[0]
        zuidi = re.findall('最\ 低\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\".*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[0]
        zongshizhi = re.findall('总市值\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\"\..*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[
            0]
        liutongshizhi = \
        re.findall('流通市值\:\<\/span\>\<span id\=\".*?\" class\=\".*?\" data\-reactid\=\".*?"\>(.*?)\<\/span\>\<\/li\>', txtt)[0]
        huanshoulv = re.findall('换手率\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\"\..*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[
            0]
        shijinglv = re.findall('市净率\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\"\..*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[
            0]
        zhenfu = re.findall('振\ 幅\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\".*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[0]
        shiyinglv = re.findall('市盈率\:\<\/span\>\<span class\=\".*?\" data\-reactid\=\"\..*?\"\>(.*?)\<\/span\>\<\/li\>', txtt)[
            0]
        # print(txtt)
        with open('ans.txt', 'a+', encoding="GBK")as f:
            f.write(name + '\t')
            f.write(zuoshou + '\t')
            f.write(jinkai + '\t')
            f.write(zuigao + '\t')
            f.write(zuidi + '\t')
            f.write(chengjiaoliang + '\t')
            f.write(chengjiaoge + '\t')
            f.write(zongshizhi + '\t')
            f.write(liutongshizhi + '\t')
            f.write(huanshoulv + '\t')
            f.write(shijinglv + '\t')
            f.write(zhenfu + '\t')
            f.write(shiyinglv + '\n')
    except:
        print("失败")
def MAIN():
    global URL
    # print(URL)
    while True:
        gg.acquire()
        if len(URL)==0:
            gg.release()
            break
        gg.release()
        url = URL.pop()
        url = url.split(" ")
        print(url[1])
        down(url[0],url[1])
if __name__ == '__main__':
    url_list()
    for x in range(10):
        threading.Thread(target=MAIN).start()
    while len(threading.enumerate())>1:
        pass
