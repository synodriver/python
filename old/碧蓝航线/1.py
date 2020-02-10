import root
import re
import requests
import parsel
def down(url,name):
    req = requests.get(url)
    req.encoding = "GBK"
    urll = re.findall('src\=\"(.*?)\" />',req.text)[0]
    # print(urll)
    with open(name+'.jpg','wb') as f :
        f.write(requests.get(urll).content)
def get():
    response = requests.get("http://news.4399.com/blhx/tujian/")
    response.encoding = 'GBK'
    # print(response.text)
    urll = re.findall('<li><a href="(.*?)"><img src=".*?" alt=".*?"/>(.*?)</a></li>',response.text)
    urll += re.findall('\<li style\=\"display\:none\"\>\<a href\=\"(.*?)\"\>\<img lz_src\=\".*?\" alt\=\".*?\"\/\>(.*?)\<\/a\>\<\/li\>',response.text)
    urll = list(set(urll))
    return  urll
def tihuan(ss):
    return  ss.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','').replace('.','').replace(' ','')

if __name__ == '__main__':
    urll = get()
    num = 1
    for x in urll:
        try:
            down(x[0],x[1])
            num+=1
            print(num)
        except:
            print(x[0])
            # break
