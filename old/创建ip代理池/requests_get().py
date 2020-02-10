def requests_get(url):
    # url = 'https://www.doutula.com/photo/list/?page=1'
    import requests
    file = open('F:\\可用ip.txt','r')
    txt = file.read().split('\n')
    file.close()
    for ip in txt:
        proxies = {
            "http": "http://%s"%str(ip),
            "https": "http://%s"%str(ip),
        }
        try:
            response = requests.get(url,proxies= proxies,timeout = 5)
            # print(response.text)
            return response
            # break
        except:
            pass
