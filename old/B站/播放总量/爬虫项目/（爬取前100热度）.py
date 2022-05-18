import requests
def get_av(url):
    headers = {
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "1ca4a9aa-98de-4942-b417-942b8c2a3e00,7d94cc7d-2acb-4fff-9886-986fa1aae7d4",
        'Accept-Encoding': "gzip, deflate",
        'Referer': "https://www.bilibili.com/ranking/all/0/0/3",
        'Cookie': "main_confirmation=ISMe0ZcZC2g5nL3QnGXOHZWrKAMIzC7qcsDt5i3RS4k=",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers)
    import parsel
    sel = parsel.Selector(response.text)
    urls = sel.xpath('//div[@class="rank-list-wrap"]//a/@href').re("av(.*)")
    with open("av.txt",'a+')as f:
        for x in urls:
            f.write(f'{x},')


# url_list = ["https://www.bilibili.com/ranking/all/0/0/3","https://www.bilibili.com/ranking/all/1/0/3","https://www.bilibili.com/ranking/all/168/0/3","https://www.bilibili.com/ranking/all/3/0/3","https://www.bilibili.com/ranking/all/129/0/3","https://www.bilibili.com/ranking/all/4/0/3",'https://www.bilibili.com/ranking/all/36/0/3','https://www.bilibili.com/ranking/all/188/0/3','https://www.bilibili.com/ranking/all/160/0/3','https://www.bilibili.com/ranking/all/119/0/3','https://www.bilibili.com/ranking/all/155/0/3','https://www.bilibili.com/ranking/all/5/0/3','https://www.bilibili.com/ranking/all/181/0/3',"https://www.bilibili.com/ranking/cinema/0/0/3","https://www.bilibili.com/ranking/cinema/1/0/3","https://www.bilibili.com/ranking/cinema/168/0/3","https://www.bilibili.com/ranking/cinema/3/0/3","https://www.bilibili.com/ranking/cinema/129/0/3","https://www.bilibili.com/ranking/cinema/4/0/3",'https://www.bilibili.com/ranking/cinema/36/0/3','https://www.bilibili.com/ranking/cinema/188/0/3','https://www.bilibili.com/ranking/cinema/160/0/3','https://www.bilibili.com/ranking/cinema/119/0/3','https://www.bilibili.com/ranking/cinema/155/0/3','https://www.bilibili.com/ranking/cinema/5/0/3','https://www.bilibili.com/ranking/cinema/181/0/3',"https://www.bilibili.com/ranking/origin/0/0/3","https://www.bilibili.com/ranking/origin/1/0/3","https://www.bilibili.com/ranking/origin/168/0/3","https://www.bilibili.com/ranking/origin/3/0/3","https://www.bilibili.com/ranking/origin/129/0/3","https://www.bilibili.com/ranking/origin/4/0/3",'https://www.bilibili.com/ranking/origin/36/0/3','https://www.bilibili.com/ranking/origin/188/0/3','https://www.bilibili.com/ranking/origin/160/0/3','https://www.bilibili.com/ranking/origin/119/0/3','https://www.bilibili.com/ranking/origin/155/0/3','https://www.bilibili.com/ranking/origin/5/0/3','https://www.bilibili.com/ranking/origin/181/0/3',"https://www.bilibili.com/ranking/bangumi/0/0/3","https://www.bilibili.com/ranking/bangumi/1/0/3","https://www.bilibili.com/ranking/bangumi/168/0/3","https://www.bilibili.com/ranking/bangumi/3/0/3","https://www.bilibili.com/ranking/bangumi/129/0/3","https://www.bilibili.com/ranking/bangumi/4/0/3",'https://www.bilibili.com/ranking/bangumi/36/0/3','https://www.bilibili.com/ranking/bangumi/188/0/3','https://www.bilibili.com/ranking/bangumi/160/0/3','https://www.bilibili.com/ranking/bangumi/119/0/3','https://www.bilibili.com/ranking/bangumi/155/0/3','https://www.bilibili.com/ranking/bangumi/5/0/3','https://www.bilibili.com/ranking/bangumi/181/0/3',"https://www.bilibili.com/ranking/rookie/0/0/3","https://www.bilibili.com/ranking/rookie/1/0/3","https://www.bilibili.com/ranking/rookie/168/0/3","https://www.bilibili.com/ranking/rookie/3/0/3","https://www.bilibili.com/ranking/rookie/129/0/3","https://www.bilibili.com/ranking/rookie/4/0/3",'https://www.bilibili.com/ranking/rookie/36/0/3','https://www.bilibili.com/ranking/rookie/188/0/3','https://www.bilibili.com/ranking/rookie/160/0/3','https://www.bilibili.com/ranking/rookie/119/0/3','https://www.bilibili.com/ranking/rookie/155/0/3','https://www.bilibili.com/ranking/rookie/5/0/3','https://www.bilibili.com/ranking/rookie/181/0/3']
url_list=['https://www.bilibili.com/ranking/all/4/0/3','https://www.bilibili.com/ranking/origin/4/0/3','https://www.bilibili.com/ranking/rookie/4/0/3']
import time
for url in url_list:
    get_av(url)
    time.sleep(1)