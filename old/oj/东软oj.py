import re
import requests
import time
import parsel
import xlrd
import xlwt
url = 'http://xiaowushen.xyz/status.php?&top=171376'
t2= time.time()
name = {}
score = {}
name_ac={}
num = 1
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('example')
worksheet.write(0, 0, 'name')
worksheet.write(0, 1, 'type')
worksheet.write(0, 2, 'value')
worksheet.write(0, 3, 'date')
temp_date = '2019-07-01'
for page in range(171376,185871,20):
# for page in range(171376,173000,20):
# for page in range(171376,171397,20):
    print(page)
    try:
        url = f'http://xiaowushen.xyz/status.php?&top={str(page)}'
        response = requests.get(url)
        sle = parsel.Selector(response.text)
        ac = sle.xpath('//*[@id="result-tab"]/tbody').re('title="(.*?)"')
        id = sle.xpath('//*[@id="result-tab"]/tbody').re('user_id=(.*?)#')
        tihao = sle.xpath('//*[@id="result-tab"]/tbody').re('pid=\d">(.*?)</a>')
        timme = sle.xpath('//*[@id="result-tab"]/tbody').re('\<td\>2019(.*?)</td>')
        # print(timme)
        for x,y,z,data_time in zip(id,ac,tihao,timme):
            if y =='Congratulations!':
                if x not in name.keys():
                    req = requests.get(f'http://xiaowushen.xyz/userinfo.php?user={x}')
                    name[x] = re.findall(f'{x}--(.*?)<a', req.text)[0]

                if x+z not in name_ac.keys():
                    # print(x+z)
                    name_ac[x+z]=1
                    if x in score:
                        score[x]+=1
                    else:
                        score[x]=1
                    date = f'2019{data_time[:6]}'
                    print(name[x],score[x])
                    if date != temp_date:
                        for key, value_ in score.items():
                            worksheet.write(num, 0, name[key])
                            worksheet.write(num, 1, key)
                            worksheet.write(num, 2, value_)
                            worksheet.write(num, 3, temp_date)
                            num += 1
                        temp_date = date
        time.sleep(0.3)
    except:
        pass
#
for key, value in score.items():
    worksheet.write(num, 0, name[key])
    worksheet.write(num, 1, key)
    worksheet.write(num, 2, value)
    worksheet.write(num, 3, date)
    num += 1
workbook.save('成绩.xls')

t1 =time.time()
print(t1-t2)



