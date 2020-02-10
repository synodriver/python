import  requests
import  parsel
import os
def download_img(url,name):
    from  urllib.request import urlretrieve
    urlretrieve(url,'./%s.jpg'%name)
url  = 'https://movie.douban.com/top250'
response = requests.get(url)
# print(response.text)
sle = parsel.Selector(response.text)
txt = sle.xpath('//*[@id="content"]/div/div[1]/ol').re("alt\=\"(.*?)\"")
img = sle.xpath('//*[@id="content"]/div/div[1]/ol').re('src\=\"(.*?)\"')
# print(txt)
# print(img)
if not os.path.exists("豆瓣"):
    os.mkdir("豆瓣")
for url,name in zip(img,txt):
    download_img(url,'豆瓣'+'/'+name+'.jpg')