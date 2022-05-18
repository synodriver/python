def requests_get(url):
    # url = 'https://www.doutula.com/photo/list/?page=1'
    import requests
    with open('F:\\可用ip.txt','r') as file:
        txt = file.read().split('\n')
    for ip in txt:
        proxies = {"http": f"http://{str(ip)}", "https": f"http://{str(ip)}"}
        try:
            # print(response.text)
            return requests.get(url,proxies= proxies,timeout = 5)
                    # break
        except:
            pass
