path = r'F:\python\代码\B站在线人数\情感分析\pinlun_full.txt'
with open(path,encoding='utf-8') as f:
    x = f.read()
x = x.replace('--------------------','')
x= x.split('\n')
for xx in x:
    if xx!="":
        print(xx)
# print(x)