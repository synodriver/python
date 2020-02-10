import re
import  requests
import os
def jie(s):
    from urllib import parse
    return  parse.unquote(s)
def download_img(url,name):
    from  urllib.request import urlretrieve
    urlretrieve(url,'%s'%name)
    print(name[:-4]+'下载成功')
def main():
    # url = 'https://github.com/anlen123/phtoto/tree/master/%E7%8C%AB%E7%B2%AE'
    url = input("输入网站：")
    wjj = re.findall(r'https://github.com/anlen123/phtoto/tree/master/(.*)',url)[0]
    jiewjj = jie(wjj)
    if not os.path.exists(jiewjj):
        os.mkdir(jiewjj)
    response = requests.get(url)
    img = re.findall('href="/anlen123/phtoto/blob/master/(.*?)"',response.text)
    for x in img:
        name = jie(re.findall(wjj+'/(.*)',x)[0])
        path = jiewjj+'/'+name
        # print(path)
        download_img('https://raw.githubusercontent.com/anlen123/phtoto/master/'+x,path)
if __name__ == '__main__':
    main()