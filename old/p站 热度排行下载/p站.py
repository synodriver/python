import  requests
import  re
import datetime
import time
import os
import threading
import random
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
    return str(dai)
def down_get_and_down(url,name,yy):
    try:
        id = url[-12:-4]
        urll = url+'png'
        # print(id)
        head = {
            'referer': "http://www.pixiv.net/member_illust.php?mode=manga_big&illust_id="+str(id)+"&page=0",
            'User-Agent': '%s' % dailichi()
        }
        r= requests.get(urll,headers = head,timeout = 5,)
        if (r.status_code==404):
            urll = urll[:-3]+'jpg'
            r = requests.get(urll, headers=head,timeout = 5)
        # print(urll)
        with open(yy+'/'+'%s.jpg' % name, mode='wb') as f:
            f.write(r.content)
    except:
        pass
def main():
    timee = str(datetime.datetime.now())[:10]
    op = input("下载日榜按1 "+'\n'+'下载月榜按 2 '+'\n'+'下载周榜按 3' +'\n'+'下载最受男性喜欢的按 4 '+'\n'+'下载最受女性喜欢的按 5 '+'\n'+'下载新人榜按 6 '+'\n'+'下载原创榜按7 ：  ')
    op = int(op)
    # op = int(4)
    if op==1:
        url = 'https://www.pixiv.net/ranking.php?mode=daily'
        yy ='日榜'
    elif op==2:
        url = 'https://www.pixiv.net/ranking.php?mode=monthly'
        yy ='月榜'
    elif op==3 :
        url = 'https://www.pixiv.net/ranking.php?mode=weekly'
        yy ='周榜'
    elif op==4:
        url = 'https://www.pixiv.net/ranking.php?mode=male'
        yy ='男生榜'
    elif op==5:
        url = 'https://www.pixiv.net/ranking.php?mode=female'
        yy ='女生榜'
    elif op ==6:
        url = 'https://www.pixiv.net/ranking.php?mode=rookie&content=illust'
        yy = '新人榜'
    elif op ==7:
        url = 'https://www.pixiv.net/ranking.php?mode=original'
        yy = '原创榜'
    start = input("下载不稳定，请手动输入开始的位置[1,50]:")
    # start = int(1)
    yy = timee+yy
    if not os.path.exists(yy):
        os.mkdir(yy)
    response = requests.get(url)
    if not os.path.exists(yy+'/'+yy+'.txt'):
        with open(yy+'/'+yy+'.txt','w+',encoding='utf-8')as f:
            f.write(response.text)

    f= open(yy+'/'+yy+'.txt','r',encoding='utf-8')
    txt = f.read()
    f.close()
    # print(txt)
    img = re.findall(r'pixiv.context.mode(.*)</a></li></ul></nav></div>',txt,re.S)
    img = re.findall(r'thumbnail-filter lazy-image"data-src="(.*?)"data-type="illust"',str(img), re.S)
    # print(len(img))
    # print(img)
    num = int(start)
    # maxx = threading.Lock
    for x in img[num-1:]:
        x= str(x)
        x = x[:-16] + x[-5:]
        x = x.replace('c/240x480/img-master', 'img-original')
        # print(x)
        try :
            # down_get_and_down(x[:-3],num,yy)
            # maxx.acquire()
            threading.Thread(target=down_get_and_down,args=(x[:-3],num,yy)).start()
            # maxx.release()
            time.sleep(1)
            print("下载第%s张图片成功！！" % num)
        except:
            print("下载第%s张图片失败！！" % num)
        # time.sleep(1)
        num +=1
if __name__ == '__main__':
    main()
