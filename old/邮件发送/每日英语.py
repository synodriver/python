# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  刘华强
@Version        :  
------------------------------------
@File           :  每日英语.py.py
@Description    :  
@CreateTime     :  2019/11/27 17:02
------------------------------------
@ModifyTime     :  
"""
import  parsel
import requests
import re
def get_danci(url):
    response = requests.get(url)
    response.encoding = 'UTF-8'
    # print(response.text)
    txtt = """
    """
    txt = re.findall('\<div class\=\"qh_..\" id\=\"..\d\"\>(.*?)<\/div\>',response.text)
    num  = 0
    zimu = []
    for i in range(ord("A"),ord("Z")+1):
        zimu.append(chr(i))
    for i in range(ord("a"),ord("z")+1):
        zimu.append(chr(i))
    for x in txt:
        x= x.replace("&#39;",'\'').replace("&quot;",'').replace("<p>","").replace("</p>","")
        if "img src=" not in x and "<img alt=" not in x and "<p style=" not in x:
            pass
            # print(x)\
            if x[0] in zimu:
                txtt+='英文：'
            else:
                txtt+='中文:'
            txtt+=x
            txtt+='\n\n'
    txtt+='\n\n\n'
    danci = re.findall('\<span\>\<a href\=\".*?" target\=\"_blank\"\>(.*?)\<\/a\>\<\/span\>',response.text)
    yisi = re.findall('\<p style\=\"line\-height\:20px\;\"\>(.*?)\<\/p\>',response.text)
    for x,y in zip(danci,yisi):
        y = y.replace("<br />"," ")
        txtt+=x
        txtt+=y
        txtt+="\n"
    txtt+='\n'
    return txtt
import random
def get_url():
    url = 'http://www.kekenet.com/read/ss/List_'+str(random.randint(1,1086))+'.shtml'
    # url = 'http://www.kekenet.com/read/ss/List_1086.shtml'
    req = requests.get(url)
    req.encoding= 'UTF-8'
    urll = re.findall('\<a href\=\"\/read\/(.*?)\.shtml\" target\=\"',req.text)
    return 'http://www.kekenet.com/read/'+str(random.choice(urll))+'.shtml'
url = get_url()
txtttt = get_danci(url)



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

qq_youjian('1761512493@qq.com','1761512493@qq.com',"每日英语",txtttt)
qq_youjian('1761512493@qq.com','1627925921@qq.com',"每日英语",txtttt)