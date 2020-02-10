import re 
import requests
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
    # print(dai)
    head  ={
        'User-Agent':'%s'% dai
    }
    return head

def get_cid(av):
    url = f'https://www.bilibili.com/video/av{av}'
    response = requests.get(url=url,headers=dailichi())
    txt = response.content.decode('utf-8')
    cid = re.findall('cid=(.*?)&aid=.*?&',txt)[0]
    return cid 
def get_danmu(av):
    cid = get_cid(av)
    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}'
    response = requests.get(url=url,headers=dailichi())
    txt = response.content.decode('utf-8')
    # print(txt)
    txt = re.findall('<d p=".*?">(.*?)</d>',txt,re.S)
    # return txt
    with open('弹幕.txt','a+',encoding='utf-8')as f:
        for x in txt :
            f.write(x+'\n')

def get_all_av(mid):
    AID = []
    for num in range(0,100):
        url = f'https://space.bilibili.com/ajax/member/getSubmitVideos?mid={mid}&pagesize=100&tid=0&page={num}&keyword=&order=pubdate'
        # print(url)
        response = requests.get(url=url,headers=dailichi())
        txt = response.content.decode('utf-8')
        aid = re.findall('"aid":(\d*),',txt,)
        if len(aid)==0:
            break
        for x in aid:
            AID.append(x)
        AID = list(set(AID))
        if (len(AID)>=200):
            break
    AID = list(set(AID))
    return AID 

def ciyun(path):
   from wordcloud import WordCloud
   import matplotlib.pyplot as plt  #绘制图像的模块
   import  jieba                    #jieba分词
   path_txt=path
   f = open(path_txt,'r',encoding='UTF-8').read()
   cut_text = ' '.join(jieba.cut(f))
   wordcloud = WordCloud(
      font_path='C:/Windows/Fonts/simfang.ttf',
      background_color='white',width=1000,height=880).generate(cut_text)
   plt.imshow(wordcloud, interpolation='bilinear')
   plt.axis('off')
   plt.show()

def duoxiancheng(Hanshu,List,Time):
   import time
   from concurrent.futures import ThreadPoolExecutor
   pool= ThreadPoolExecutor(max_workers=10)
   for i in List:
       pool.submit(Hanshu,i)
       time.sleep(Time)
   pool.shutdown()
def cipin(path):
    txt = open(path,'r',encoding='utf-8').read().split('\n')
    words = txt
    count={}
    for word in words:
        if len(word) ==1:
            continue
        else:
            count[word]=count.get(word,0)+1
    result = sorted(count.items(),key=lambda x:x[1],reverse=True)
    for i in range(30):
        word,count=result[i]
        print(str(i+1)+'->'+word,':',count)

import random
import time 
import os 
if __name__ == "__main__":
    if  os.path.exists('弹幕.txt'):
        os.remove('弹幕.txt')
    mid = '9824766'
    # mid = input("请输如up主的个人空间号码:")
    all_av = get_all_av(mid)
    duoxiancheng(get_danmu,all_av,random.randint(1,5))
    # print(len(all_av))
    time.sleep(10)
    path = '弹幕.txt'
    cipin(path)