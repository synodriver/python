# # !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  刘华强
@Version        :
------------------------------------
@File           :  app.py
@Description    :
@CreateTime     :  2019/12/16 14:14
------------------------------------
@ModifyTime     :
"""


import requests
import os
url = "http://meishi.meituan.com/i/api/channel/deal/list"
path = 'F:\python\代码\美团\Cookie.txt'
with open(path,'r') as file:
    cook =str(file.read())
headers = {
    'Accept': 'application/json',
    'Cookie': cook,
    'Host': 'meishi.meituan.com',
    'Origin': 'http://meishi.meituan.com',
    'Referer': 'http://meishi.meituan.com/i/?ci=59&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
}


data = {
	'uuid': "d01b76ac-372e-4740-876e-e42c86d46300",
	'version': '"8.2.0"',
	'platform': '3',
	'app': '""',
	'partner': '126',
	'riskLevel': '1',
	'optimusCode': '10',
	'originUrl': 'http://meishi.meituan.com/i/?ci=59&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1',
	'offset': '0',
	'limit': '15',
	'cateId': '1',
	'lineId': '0',
	'stationId': '0',
	'areaId': '0',
	'sort': 'default',
	'deal_attr_23': '',
	'deal_attr_24': '',
	'deal_attr_25': '',
	'poi_attr_20043': '',
	'poi_attr_20033': '',
}
response = requests.request("POST", url, headers=headers,data=data)
print(response.text)
txt = response.json()
txt = txt['data']['poiList']['poiInfos'][2]
print(txt)