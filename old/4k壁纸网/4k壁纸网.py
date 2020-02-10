import  requests
import  re
import  parsel
import time
xxx = input("输入你的类型的网址：")
z = int(input("页面左区间："))
y = int(input("页面右区间："))
def download_img(url,name):
    from  urllib.request import urlretrieve
    urlretrieve(url,'%s.jpg'%name)
for num in range(z,y+1):
    if num == 1:
        url = xxx
    else :
        url = xxx+'index_%s.html'%str(num)

    response = requests.get(url)
    response.encoding = response.apparent_encoding
    sle = parsel.Selector(response.text)
    img = sle.xpath('//*[@id="main"]/div[3]/ul').re('href="(.*?)"')
    img = ['http://pic.netbian.com/' + i for i in img]
    # print(img)
    for img_url in img:
        req = requests.get(img_url)
        req.encoding = req.apparent_encoding
        slee= parsel.Selector(req.text)
        urll = slee.xpath('//*[@id="img"]/img').re('src="(.*?)"')[0]
        name = slee.xpath('//*[@id="img"]/img').re('alt="(.*?)"')[0]
        urll = 'http://pic.netbian.com/'+urll
        print(urll)
        print(name)
        try :
            download_img(urll,name)
        except:
            pass