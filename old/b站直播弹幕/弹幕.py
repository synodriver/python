import requests
url = 'https://api.live.bilibili.com/msg/send'
data = {
    'color': '16777215',
    'fontsize': '25',
    'mode': '1',
    'msg': '1',
    'rnd': '1573203932',
    'roomid': '21663729',
    'bubble': '0',
    'csrf_token': '62efef67a0d7454f9dab44df6929f1c3',
    'csrf': '62efef67a0d7454f9dab44df6929f1c3',
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '160',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'LIVE_BUVID=AUTO9915732038844875; _uuid=94FA2AA2-2EFE-97D3-18CC-0555DDA85D5687871infoc; buvid3=030DB00B-5C3F-42B7-9B8A-714F167D8541190961infoc; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1573203888; sid=922hqc34; DedeUserID=32482364; DedeUserID__ckMd5=ce93b510ef5be598; SESSDATA=e92a73c9%2C1575795931%2C0d0858b1; bili_jct=62efef67a0d7454f9dab44df6929f1c3; _dfcaptcha=6e934e8a1b29ac8fe40a7f35281d6324; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1573203937',
    'Host': 'api.live.bilibili.com',
    'Origin': 'https://live.bilibili.com',
    'Referer': 'https://live.bilibili.com/428',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}
import time
while True:
    requests.post(url,data=data,headers= headers)