import requests
import time
import hashlib
import random
def make_md5(string):
    string = string.encode('utf-8')
    return hashlib.md5(string).hexdigest()

def translation():
    code = t1.get(0.0,'end')
    r = int(time.time()*1000)
    # print(r)
    t = make_md5('5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
    # print(t)
    i  = str(r)+ str(random.randint(0,10))
    # print(i)
    data = {
        'i': code,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': i,
        'sign': make_md5(f"fanyideskweb{code}{i}n%A-rKaT5fb[Gy?;N5@Tj"),
        'ts': r,
        'bv': t,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }

    head = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '260',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1401571795@10.169.0.84; JSESSIONID=aaa8qe3C1gHzybPOTR8Yw; OUTFOX_SEARCH_USER_ID_NCOO=1374430056.1262918; watch_times=0; level=7; user_level=7; ___rl__test__cookies=1567511330312',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://fanyi.youdao.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }
    response = requests.post(url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule',data = data,headers = head).json()
    t1.delete(0.0,'end')

    text = response["translateResult"][0][0]['tgt']
    # print(text)
    t1.insert(0.0,str(text))


import tkinter as tk
window = tk.Tk()
window.geometry('500x350')
window.title('翻译小软件')
b1 = tk.Button(window,text = '一键翻译',command = translation)
b1.pack()
t1 = tk.Text(window,font = ('','15',''))
t1.pack()


tk.mainloop()
