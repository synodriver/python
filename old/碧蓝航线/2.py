import  re
import  root
# import parsel
import requests
import os
if not os.path.exists("碧蓝航线微博图"):
    os.mkdir("碧蓝航线微博图")
for num in range(1,235+1):
    try:
        url = f'https://m.weibo.cn/api/container/getIndex?uid=5770760941&luicode=10000011&lfid=100103type%3D1%26q%3D%E7%A2%A7%E8%93%9D%E8%88%AA%E7%BA%BF&type=uid&value=5770760941&containerid=1076035770760941&page={str(num)}'

        # print(url)
        req = requests.get(url)
        txt = req.text.replace('\\','')
        # print(txt)
        img = re.findall('"size":"large",\"url\"\:\"(.*?large.*?)\"',txt,re.S)
        for xxx, x in enumerate(img, start=1):
            print(f"正在下载第{num}的图片{str(xxx)}")
            root.download_img(x,'碧蓝航线微博图'+'/'+str(num)+"_"+str(xxx))
    except:
        pass