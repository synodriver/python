import requests
import re
import parsel
url = 'http://quote.eastmoney.com/stock_list.html'
response = requests.get(url)
response.encoding= "GBK"
name = re.findall('\<li\>\<a target\=\"_blank\" href\=\"http\:\/\/quote\.eastmoney\.com\/(.*?)\.html\"\>(.*?)\<\/a\>\<\/li\>',response.text)
# print(response.text)
file = open('list.txt',encoding="GBK",mode='a+')
for x in name:
    file.write(x[1]+'\t')
    file.write(x[0]+'\n')
file.close()