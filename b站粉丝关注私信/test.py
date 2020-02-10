import requests
import time
import re 
import math
import os 
cook = "xxx"
自己的id='xxx'
信息 = '小伙伴你好啊，感谢你关注我[斜眼笑]，对我的视频感兴趣的话[难过]，记得三连和分享哦，我会努力做出更优质的视频的[坏笑]，还可以加我的粉丝群讨论哦[斜眼笑]，77743648[doge][doge]'

def 私信(对方的id):
    headers = {
        'Cookie': "%s"%cook,
        'Host': 'api.vc.bilibili.com',
        'Origin': 'https://message.bilibili.com',
        'Referer': 'https://message.bilibili.com/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    url = 'https://api.vc.bilibili.com/web_im/v1/web_im/send_msg'
    data = {
            'msg[sender_uid]': f'{自己的id}',
            'msg[receiver_id]': f"{对方的id}",
            'msg[receiver_type]': '1',
            'msg[msg_type]': '1',
            'msg[msg_status]': '0',
            'msg[content]': '{"content":"%s\n"}'%(信息),
            'msg[dev_id]': '9F0DA942-7E8C-4B78-8A5B-E8C82F09AF8D',
            'mobi_app': 'web',
            'csrf_token': '5cba8f4343b9f978a2288fce99cb7a6f',
    }
    requests.post(url=url,headers=headers,data = data)

def 获取新粉丝的id():
    headers = {
            'Cookie': "%s"%cook,
            'Host': 'api.bilibili.com',
            'Referer': 'https://space.bilibili.com/32482364/fans/fans',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    url = f'https://api.bilibili.com/x/relation/stat?vmid={自己的id}'
    pep = requests.get(url=url,headers=headers).json()['data']['follower']
    总页数 = math.ceil(pep/20)
    粉丝id =[]
    for 页数 in range(1,总页数+1,1):
        url = f'https://api.bilibili.com/x/relation/followers?vmid={自己的id}&pn={页数}&ps=20&order=desc&jsonp=jsonp&callback=__jp{页数}'
        headers = {
                'Cookie': "%s"%cook,
                'Host': 'api.bilibili.com',
                'Referer': 'https://space.bilibili.com/32482364/fans/fans',
                'Sec-Fetch-Mode': 'no-cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }
        response = requests.get(url=url,headers=headers)
        txt = response.text
        粉丝id+=re.findall('"mid":(.*?),',txt)

    if not os.path.exists('之前的粉丝id.txt'):
        with open('之前的粉丝id.txt','w+')as f:
            f.write(str(粉丝id))
        exit()
    file = open('之前的粉丝id.txt')
    之前的粉丝id = file.read()
    list(之前的粉丝id)
    file.close()
    # print(之前的粉丝id)
    d = [y for y in 粉丝id if y not in 之前的粉丝id]
    with open('之前的粉丝id.txt','w+')as f:
        f.write(str(粉丝id))
    return d

try:
    list1 = 获取新粉丝的id()
    print(list1)
    for x in list1:
        私信(x)
except:
    print("出错了，再运行一遍！")
    pass