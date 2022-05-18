import xlrd
import xlwt
import parsel
import requests
import re
def xie_excel():
    name=[]
    fen=[]
    for xx in range(0,246,25):
        url = f'https://movie.douban.com/top250?start={str(xx)}&filter='
        # print(url)
        response = requests.get(url)
        sle = parsel.Selector(response.text)
        name+=(sle.xpath('//*[@id="content"]/div/div[1]/ol').re(r'<img width="100" alt="(.*?)" src=".*?" class="">',re.S))
        fen+=(sle.xpath('//*[@id="content"]/div/div[1]/ol').re(r'<span class="rating_num" property="v:average">(.*?)</span>',re.S))
            # print(name)
            # print(fen)
            # break
    # print(name)
    # print(len(name))
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(0, 0, '电影名字')
    worksheet.write(0, 1, '评分')
    for x in range(len(name)):
        worksheet.write(x+1,0,name[x])
        worksheet.write(x+1,1,fen[x])
    workbook.save('233.xls')
data = xlrd.open_workbook('233.xls')
table = data.sheet_by_index(0)
for x in table.col_values(1)[1:]:
    print(x)