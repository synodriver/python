# -*- coding: utf-8 -*-

"""
    B站粉丝监控，消息发送
    Time : 2020-1-31
    Author : BobH (bilibili:我的小任_真)
    QQ : 1551608379
    仅供学习，请勿用作非法用途
    请勿用作盈利用途
"""

import requests
import ssl
from requests.auth import HTTPBasicAuth
import json
import math
from datetime import datetime
import time
from urllib import parse
import time
import datetime
def get_cook():
    file  = open('cook.txt')
    cook = file.read()
    file.close()
    return cook
def get_csrd_token():
    file  = open('csrd_token.txt')
    csrd_token = file.read()
    file.close()
    return csrd_token
def get_id():
    file  = open('自己的id.txt')
    自己的id = file.read()
    file.close()
    return 自己的id
csrf_token=get_csrd_token()
cook = get_cook()
自己的id = get_id()
msg_template = "小伙伴 {uname} 你好啊[亲亲]，感谢关注我哦~\n\n你是第 {index} 位关注我的人呢，[害羞]对我的视频感兴趣的话，就多多三连分享吧！我会努力做出更多优质视频的！\n\n[斜眼笑]还可以加我们的QQ群:68724983 哦，里面有很多有趣灵魂的人，还有技术人员可以讨论哲学！！！"

# time.sleep(10000)
# print(cook)
def SendWelcomeMsg(fanid,followIndex,fanname):
    # print("欢迎你 " + str(fanname) + " 你是第" + str(followIndex) + "位关注我的!")
    constra_msg = msg_template.replace("{uname}",fanname)
    constra_msg = constra_msg.replace("{index}",str(followIndex))
    return constra_msg
headers = {
    'Accept' : '*/*',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection' : 'keep-alive',
    'Cookie' : "%s"%cook,
    'Host' : 'api.bilibili.com',
    'Referer' : "https://space.bilibili.com/%s/fans/fans"%自己的id,
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
}
msg_headers = {
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection' : 'keep-alive',
    'Cookie' : "%s"%cook,
    'Host' : 'api.vc.bilibili.com',
    'Origin' : 'https://message.bilibili.com',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Referer' : 'https://message.bilibili.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Pragma' : 'no-cache'
}
max_monitor_cnt = 100
fan_list = {}
url = "https://api.bilibili.com/x/relation/followers?vmid=%s&pn={page}&ps=20&order=desc&jsonp=jsonp"%自己的id
msg_url = "https://api.vc.bilibili.com/web_im/v1/web_im/send_msg"
sendmsg_data = "msg%5Bsender_uid%5D={sender_uid}&msg%5Breceiver_id%5D={receiver_id}&msg%5Breceiver_type%5D=1&msg%5Bmsg_type%5D=1&msg%5Bmsg_status%5D=0&msg%5Bcontent%5D=%7B%22content%22%3A%22{content_url_code}%22%7D&msg%5Btimestamp%5D={timestamp}&msg%5Bdev_id%5D=EE0629D2-2B90-4AB0-8D71-0DBA92F62A34&build=0&mobi_app=web&csrf_token=47ed4f492876c08586fdb63906d08563"

# def SendUserMsg(targetUid,msg):
#     # !debug
#     # if targetUid != 501053733:
#     #     return False
#     postdata = sendmsg_data.replace("{sender_uid}",str(自己的id))
#     postdata = postdata.replace("{receiver_id}",str(targetUid))
#     t = time.time()
#     postdata = postdata.replace("{timestamp}",str(int(t)))
#     postdata = postdata.replace("{content_url_code}",str(parse.quote(msg)))
#     thisheader = msg_headers
#     thisheader['Content-Length'] = str(len(postdata))
#     resp = requests.post(url=msg_url,headers=thisheader,data=postdata)
#     print(resp.text)
#     if "html" in resp.text:
#         return False
#     else :
#         return json.loads(resp.text)['code'] == 0

def GetFollowerJsonData(page):
    reqUrl = url.replace("{page}",str(page))
    resp = requests.get(url=reqUrl,headers=headers)
    responText = str(resp.text)
    return json.loads(responText)

def GetTotalFlollowerCnt():
    jd = GetFollowerJsonData(1)
    return jd['data']['total'];

def 私信(对方的id,信息):
    
    headerss = {
        'Cookie': "%s"%cook,
        'Host': 'api.vc.bilibili.com',
        'Origin': 'https://message.bilibili.com',
        'Referer': 'https://message.bilibili.com/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    url = 'https://api.vc.bilibili.com/web_im/v1/web_im/send_msg'
    dataa = {
            'msg[sender_uid]': f'{自己的id}',
            'msg[receiver_id]': f"{对方的id}",
            'msg[receiver_type]': '1',
            'msg[msg_type]': '1',
            'msg[msg_status]': '0',
            'msg[content]': '{"content":"%s\n"}'%(信息),
            'mobi_app': 'web',
            'csrf_token': "%s"%(csrf_token),
    }
    requests.post(url=url,headers=headerss,data = dataa)
def CheckFans():
    global fan_list
    now_list = {}
    targetGet = min(max_monitor_cnt,GetTotalFlollowerCnt())
    totPage = math.ceil(targetGet / 20.0)
    totget = 0
    nowindex = 0
    nowtot = 0
    for i in range(1,totPage+1):
        tmp = GetFollowerJsonData(i)
        nowtot = tmp['data']['total']
        if len(tmp['data']['list']) != 0 :
            totget += len(tmp['data']['list'])
            for tmpfan in tmp['data']['list']:
                nowindex = nowindex + 1
                now_list[tmpfan['mid']] = tmpfan
                now_list[tmpfan['mid']]['index'] = nowindex
        else :
            break;
    for tmpfan in now_list:
        if tmpfan not in fan_list:
            print("[CheckFans] 检测到新增一名粉丝，uid = " + str(now_list[tmpfan]['mid']) + " ,uname = " + str(now_list[tmpfan]['uname']))
            print(tmpfan)
            try:
                # 信息 = 'msg_template = \'小伙伴 '+str(now_list[tmpfan]['uname'])+' 你好啊[亲亲]，感谢关注我哦~\n\n你是第 '+str(nowtot-now_list[tmpfan]['index']+1)+' 位关注我的人呢，[害羞]对我的视频感兴趣的话，就多多三连分享吧！我会努力做出更多优质视频的！\n\n[斜眼笑]还可以加我QQ小号:1761512493 哦，一般大号不添加陌生人哒'
                私信(str(tmpfan),SendWelcomeMsg(now_list[tmpfan]['mid'],nowtot-now_list[tmpfan]['index']+1,str(now_list[tmpfan]['uname'])))
            except:
                print("失败!!!!")
        else:
            break
    fan_list = now_list
    print(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]") + "[CheckFans] 完成一次检测!")
        # print(now_list[tmpfan])

def InitFanList():
    global fan_list
    fan_list = {}
    targetGet = min(max_monitor_cnt,GetTotalFlollowerCnt())
    totPage = math.ceil(targetGet / 20.0)
    totget = 0
    for i in range(1,totPage+1):
        print("[InitFanList] 获取第 " + str(i) + " 页粉丝...")
        tmp = GetFollowerJsonData(i)
        if len(tmp['data']['list']) != 0 :
            totget += len(tmp['data']['list'])
            for tmpfan in tmp['data']['list']:
                fan_list[tmpfan['mid']] = tmpfan
        else :
            break;
    if totget < targetGet:
        print("[Warn][InitFanList] 没有获取到目标数量的粉丝，检查网络或者权限!")
        print("[Warn][InitFanList] 目标个数: " + str(targetGet) + " 实际个数: " + str(totget))
    else:
        print("[InitFanList] 获取初始粉丝完毕！")

InitFanList()
def MainLoop(delay):
    while True:
        CheckFans()
        time.sleep(delay)
MainLoop(3)