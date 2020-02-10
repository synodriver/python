# def qq_youjian(fajianren,shoujianren,zhuti,txt):
#     import smtplib
#     from email.mime.text import MIMEText
#     msg_from=fajianren                                 #发送方邮箱
#     # passwd='eyfdfamsmdsldchg'                                   #填入发送方邮箱的授权码
#     passwd='fcznjllwfnqcdbca'                         #填入发送方邮箱的授权码
#     msg_to=shoujianren                                       #收件人邮箱
#
#     subject=zhuti                                   #主题
#     content=txt #正文
#     msg = MIMEText(content)
#     msg['Subject'] = subject
#     msg['From'] = msg_from
#     msg['To'] = msg_to
#     try:
#         s = smtplib.SMTP_SSL("smtp.qq.com",465) #邮件服务器及端口号
#         s.login(msg_from, passwd)                               #登录SMTP服务器
#         s.sendmail(msg_from, msg_to, msg.as_string())#发邮件 as_string()把MIMEText对象变成str
#         print ("发送成功")
#     except s.SMTPException:
#         print ("发送失败")
#     finally:
#         s.quit()
# import requests
# import re
# meiri = requests.get('https://api.ooopn.com/ciba/api.php').json()["ciba"]
# tianqi= requests.get('http://wthrcdn.etouch.cn/weather_mini?city=都江堰').json()
# today = tianqi['data']['forecast'][0]
# tishi = tianqi['data']['ganmao']
# shijian = today['date']
# zuigao = today['high']
# zuidi = today['low']
# fengli = re.findall('\<\!\[CDATA\[\<(.*?)\]\]\>',today['fengli'])[0]
# fengxiang = today['fengxiang']
# leixing = today['type']
# txt  = meiri + '\n  '+shijian+'\n  '+zuigao+'\n  '+zuidi+'\n  '+'风力:'+fengli+'\n  '+fengxiang+'\n  '+leixing+'\n  '
# #      ******       ******
# #    **********   **********
# #  ************* *************
# # *****************************
# # *****************************
# # *****************************
# #  ***************************
# #    ***********************
# #      *******************
# #        ***************
# #          ***********
# #            *******
# #              ***
# #               *
# txt+="""
#
#  　　　我　　　　* *　　　　 * *
# 　　　　　　　*　　 *　　 *　　　*
# 　　　　　　 *　　　　* *　　　　 *
# 　　　　　　 *　　　　 *　　　　　*
# 　　　　　　　*　 I　LOVE　YOU　 *
# 　　　　　　　　*　　　　　　　*
# 　　　　　　　　　*　　爱　　*
# 　　　　　　　　　　 *　　*
# 　　　　　　　　　　　　*　　　　　 你！！！
#      ******       ******
#    ********   ********
#  ********** **********
# **********************
# **********************
# *********************
#   *******************
#    *****************
#      ***************
#        *************
#          **********
#            ********
#               *****
#                 ***
#                   *
# """
# txt+=("给老子听好了"+tishi)
# # print(txt)
# qq_youjian('1761512493@qq.com','1761512493@qq.com',"今天的天气预报，认真听",txt)
# #qq_youjian('1761512493@qq.com','1627925921@qq.com',"今天的天气预报，认真听",txt)




import requests
import re
import random
def dailichi():
    import random
    daili = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; WOW64; Trident/4.0; SLCC1)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    ]
    dai = random.choice(daili)
    # print(dai)
    head  ={
        'User-Agent':'%s'% dai
    }
    return head
def get_txt():
    num = random.randint(2,16)
    url = 'http://xiaohua.zol.com.cn/neihan/%s.html'%str(num)
    # print(url)
    response = requests.get(url,headers = dailichi())
    # print(response.text)
    txt = re.findall('\<span class\=\"article\-title\"\>\<a target\=\"_blank\" href\=\"(.*?)"\>.*?\<\/a\>\<\/span\>',response.text,re.S)
    return txt
def down(url):
    url = 'http://xiaohua.zol.com.cn'+str(url)
    req = requests.get(url,headers = dailichi())
    title = re.findall('<h1 class="article-title">(.*?)</h1>',req.text)[0]
    txtt = re.findall('\<div class\=\"article\-text\"\>(.*?)\<\/div\>',req.text,re.S)[0]
    txtt = txtt.replace(" ","").replace("\&nbsp\;","").replace("</p>","").replace("<p>","")
    return title,txtt
txt = get_txt()
# print(txt)
xx = random.choice(txt)
title,txtt= down(xx)


def qq_youjian(fajianren,shoujianren,zhuti,txt):
    import smtplib
    from email.mime.text import MIMEText
    msg_from=fajianren                            #发送方邮箱
    # passwd='eyfdfamsmdsldchg'                                   #填入发送方邮箱的授权码
    passwd='fcznjllwfnqcdbca'                         #填入发送方邮箱的授权码
    msg_to=shoujianren                                       #收件人邮箱

    subject=zhuti                                   #主题
    content=txt #正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465) #邮件服务器及端口号
        s.login(msg_from, passwd)                               #登录SMTP服务器
        s.sendmail(msg_from, msg_to, msg.as_string())#发邮件 as_string()把MIMEText对象变成str
        print ("发送成功")
    except s.SMTPException:
        print ("发送失败")
    finally:
        s.quit()

qq_youjian('1761512493@qq.com','1761512493@qq.com',title,txtt)