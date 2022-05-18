import requests
import re

def get_score(url):
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
    # sel = parsel.Selector(response.text)
    # print(response.text)
    score = re.findall('\{\"poiId\"\:(.*?)\,\"frontImg\"\:\".*?\"\,\"title\"\:\"(.*?)\"\,\"avgScore\"\:(.*?)\,\"allCommentNum\"\:.*?\,\"address\"\:\".*?\"\,\"avgPrice\"\:.*?\,\"dealList\"\:.*?\,\"hasAds\"\:.*?\,\"adsClickUrl\"\:\".*?\"\,\"adsShowUrl\"\:\".*?\"\}',response.text)
    # print(score)
    for i in score:
        # print(i[0],i[1])
        with open('a.txt','a+')as f:
            f.write(f'店铺id：{i[0]}' + '\n' + i[1] + ',评分：' + i[2] + '\n')
        ip_chi.append([i[0],i[1]])
def get_id():
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=32)
    # 2 循环指派任务
    [pool.submit(get_score, i)for i in url_list]
    # 3 关闭
    pool.shutdown()
def get_pinglun(id):
    url = "https://www.meituan.com/meishi/api/poi/getMerchantComment"
    headers = {
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "9fba7454-5904-4cc1-9b8a-8b8849804344,e7ff34b2-9ae9-46c3-b16b-98217bb344aa",
        'Host': "www.meituan.com",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "iuuid=54F5A1EBEA13B7091828DAE9B3F8CBEB08AB7D574902091156A3F0029325C5FE; cityname=%E6%88%90%E9%83%BD; client-id=e1b034ec-279b-4432-b2c8-bfb9df8af98a; uuid=4522b7c440084b7f9141.1576472601.1.0.0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
    for num in range(0,100,10):
        querystring = {
            "uuid": "4522b7c440084b7f9141.1576472601.1.0.0",
            "platform": "1",
            "partner": "126",
            "originUrl": "https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F5218010%2F",
            "riskLevel": "1",
            "optimusCode": "10",
            "id": f"{str(id[0])}",
            "userId": "1062342147",
            "offset": f"{str(num)}",
            "pageSize": "10",
            "sortType": "1",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response.text)
        txt  = response.json()
        txt = txt['data']['comments']
        for x in txt:
            # print(x['comment'])
            with open(f'{str(id[1])}.txt', 'a+', encoding='utf-8') as f:
                f.write(x['comment']+'\n')
if __name__ == '__main__':
    url_list = [
        f"https://cd.meituan.com/meishi/sales/pn{str(i)}/"
        for i in range(1, 65)
    ]

    ip_chi = []
    get_id()
    print("获取ip完成")
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=32)
    # 2 循环指派任务
    [pool.submit(get_pinglun, i) for i in ip_chi]
    # 3 关闭
    pool.shutdown()
