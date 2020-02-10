import requests
import re
import time
import os
class cos():
    def __init__(self,url):
        self.url = url
    def download_img(self,url, name):
        from urllib.request import urlretrieve
        urlretrieve(url, '%s.jpg' % name)
    def dayin(self):
        print(self.txt)
    def jiexi(self):
        self.response  = requests.get(self.url)
        self.txt = str(re.findall(r'window.__ssr_data = JSON.parse(.*?)window._UID', self.response.text, re.S))
        self.txt = self.txt.replace('\\\\\\\\', '/')
        self.txt = self.txt.replace('u002F', '')
        self.txt = str(re.findall(r'https://p(.*?)image', self.txt, re.S))
        self.txt = eval(self.txt)
    def down(self):
        title = time.time()
        title= str(title)
        if not os.path.exists(title):
            os.mkdir(title)
        num = 1
        for x in range(0, len(self.txt), 3)[:-2]:
            # print("https://p%simage"%txt[x])
            self.download_img(url="https://p%simage" % self.txt[x], name=(title + '/' + str(num)))
            num += 1
if __name__ == '__main__':
    # url = 'https://bcy.net/item/detail/6725353762984050952?_source_page=cos'
    url = input()
    url =url.split(' ')
    for x in url:
       a= cos(url)
       a.jiexi()
       # a.dayin()
       a.down()
