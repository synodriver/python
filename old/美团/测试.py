import requests
url = 'https://cd.meituan.com/meishi/sales/pn1/'
querystring = {"Accept":"%20image/webp,image/apng,image/%2A,%2A/%2A;q=0.8","Accept-Encoding":"%20gzip,%20deflate,%20br","Accept-Language":"%20zh-CN,zh;q=0.9","Cache-Control":"%20no-cache","Connection":"%20keep-alive","Host":"%20p1.meituan.net","Pragma":"%20no-cache","Referer":"%20https://cd.meituan.com/meishi/sales/","Sec-Fetch-Mode":"%20no-cors","Sec-Fetch-Site":"%20cross-site","User-Agent":"%20Mozilla/5.0%20%28Windows%20NT%2010.0;%20Win64;%20x64%29%20AppleWebKit/537.36%20%28KHTML,%20like%20Gecko%29%20Chrome/79.0.3945.79%20Safari/537.36"}

headers = {
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "5aa68590-55aa-4448-872e-8f996bf60a6c,3ff64de7-92b9-4cd7-a00b-3c5bd2f9ab9f",
    'Host': "cd.meituan.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "IJSESSIONID=9bprceoumo2la6fipwfbqhi; iuuid=54F5A1EBEA13B7091828DAE9B3F8CBEB08AB7D574902091156A3F0029325C5FE; ci2=; ci=59; cityname=%E6%88%90%E9%83%BD; meishi_ci=59; cityid=59; uuid=a3ea4710-cae8-48e6-a3b5-91cccb83b9a0; client-id=c51776b7-b2d4-4fcc-9c0f-f0c0f6e4466a",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

