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

def p_down(url):
    # print(name)
    url = url[:-3]
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
        with open('%s.jpg'%urll[-15:-7], mode='wb') as f:
            f.write(r.content)
    except:
        pass
        print('下载失败')
    # print(urll)

url = 'https://api.pixivic.com/illustrations?keyword=%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F&page=7'
response = requests.get(url=url,headers=dailichi())
txt = response.text
print(txt)



