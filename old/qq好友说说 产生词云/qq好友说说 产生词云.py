import re
import parsel
import requests
import threading
import time
import random
from selenium import webdriver
import os
##qq_num = '469910326'
qq_num = input('请输入你要看的人的qq号码')
def login():
    url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=1'
    driver = webdriver.Chrome()
    # driver = webdriver.PhantomJS()
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="img_out_1761512493"]').click()
    time.sleep(1)
    return driver

def getGTK(cookie):
    hashes = 5381
    for letter in cookie['p_skey']:
        hashes += (hashes << 5) + ord(letter)
    return hashes & 0x7fffffff

def get_g_qzonetoken():
    with open('1.txt','r',encoding='utf-8')as f:
        g_qzonetoken = re.findall('window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)',f.read(),re.S)[0]
        # print(g_qzonetoken)
        return  g_qzonetoken


def get_cookies(driver):
    cookie = {}
    for elem in driver.get_cookies():  # 取cookies
        cookie[elem['name']] = elem['value']
    return cookie
driver = login()
time.sleep(1)
html = driver.page_source
with open('1.txt','w',encoding='utf-8')as f:
    f.write(html)
g_qzonetoken = get_g_qzonetoken()
cookie =get_cookies(driver)
tk = getGTK(cookie)
driver.get_cookies()
# url = 'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_hat_get.cgi?hat_seed=1&uin=1761512493fupdate=1&g_tk='+str(tk)+'&qzonetoken='+str(g_qzonetoken)+'&g_tk='+str(tk)
# print(url)
# driver.get(url)
# time.sleep(2)
for begin in range(0,100000,40):
    url = 'https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=' + str(
    qq_num) + '&ftype=0&sort=0&pos=' + str(begin) + '&num=40&replynum=200&g_tk=' + str(
    tk) + '&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1&qzonetoken=' + str(
    g_qzonetoken) + '&g_tk=' + str(tk)
    driver.get(url)
    # html = driver.page_source
    msg_list_json= driver.page_source
    # print(msg_list_json)
    time.sleep(3)

    abtract_pattern = re.compile(',"message":"(.*?)","name":', re.S)
    message = re.findall(abtract_pattern, str(msg_list_json))
    if message != []:
        if str(message[0]) == '对不起,主人设置了保密,您没有权限查看':  # 对不起,主人设置了保密,您没有权限查看
            print("不准看")
            pass
        else :
            msg_list_json = msg_list_json.split("msglist")[1]  # 拆分json，缩小范围，也能加快解析速度
            msg_list_json = msg_list_json.split("smoothpolicy")[0]
            msg_list_json = msg_list_json.split("commentlist")[1:]
            # 说说动态分4种：1、文字说说（或带有配图的文字说说）
            #              2、只有图片的说说
            #              3、转发，并配有文字
            #              4、转发，不配文字
            for text in msg_list_json:
                # 1、先检查说说，用户是否发送了文字，如果没有文字，正则表达式匹配无效
                abtract_pattern = re.compile('\}\],"content":"(.*?)","createTime":"(.*?)","created_time":(.*?),"', re.S)
                msg_time = re.findall(abtract_pattern, str(text))
                if msg_time != []:
                    # 2、如果作者说说有文字，那么检查是否有转发内容
                    msg = str(msg_time[0][0])
                    sendTime = str(msg_time[0][1])
                    abtract_pattern = re.compile('\}\],"content":"(.*?)"},"rt_createTime":"(.*?)","', re.S)
                    text = text.split("created_time")[1]
                    msg_time2 = re.findall(abtract_pattern, str(text))
                    # 合并发送内容 格式：评论+转发内容
                    if msg_time2 != []:
                        msg = msg + "  转发内容:" + str(msg_time2[0][0])
                else:
                    # 3、说说内容为空，检查是否为 =>只有图片的说说 or 转发，不配文字
                    # 获取正文发送时间 （发送时间分为：正文发送时间 or 转发时间）
                    abtract_pattern = re.compile('"conlist":null,"content":"","createTime":"(.*?)",', re.S)
                    msgNull_time = re.findall(abtract_pattern, str(text))
                    if msgNull_time != []:
                        # 如果有正文发送时间，那么就是这条说说仅含有图片  =>只有图片的说说
                        msg = "图片"
                        sendTime = str(msgNull_time[0])
                    else:
                        # 如果没有正文发送时间，那么就是说这条说为 =>转发，不配文字
                        abtract_pattern = re.compile('\}\],"content":"(.*?)"},"rt_createTime":"(.*?)","', re.S)
                        msg_time = re.findall(abtract_pattern, str(text))
                        msg = "  转发内容:" + str(msg_time[0][0])
                        sendTime = str(msg_time[0][1])

                msg= msg.replace('\\n','')
                msg= msg.replace('[\/em]','')
                msg= msg.replace('[em]','')
                msg= msg.replace('e404','')
                msg= msg.replace('\\u0027','')
                msg= msg.replace('','')
                msg= msg.replace('1','')
                msg= msg.replace('2','')
                msg= msg.replace('3','')
                msg= msg.replace('4','')
                msg= msg.replace('5','')
                msg= msg.replace('6','')
                msg= msg.replace('7','')
                msg= msg.replace('8','')
                msg= msg.replace('9','')
                msg= msg.replace('0','')
                msg= msg.replace('e','')
                print(sendTime + " : " + msg)
                with open(qq_num+'.txt','a',encoding='utf-8')as f:
                    f.write(msg)
                    f.write('\n')

    else:
        print("没有说说")
        break

driver.quit()


def ciyun(path):
   from wordcloud import WordCloud
   import matplotlib.pyplot as plt  #绘制图像的模块
   import  jieba                    #jieba分词

   path_txt=path
   f = open(path_txt,'r',encoding='UTF-8').read()
   cut_text = " ".join(jieba.cut(f))
   wordcloud = WordCloud(
      font_path="C:/Windows/Fonts/simfang.ttf",
      background_color="white",width=1000,height=880).generate(cut_text)
   plt.imshow(wordcloud, interpolation="bilinear")
   plt.axis("off")
   plt.show()
ciyun(qq_num+'.txt')










def ciyun(path):
   from wordcloud import WordCloud
   import matplotlib.pyplot as plt  #绘制图像的模块
   import  jieba                    #jieba分词

   path_txt=path
   f = open(path_txt,'r',encoding='UTF-8').read()
   cut_text = " ".join(jieba.cut(f))
   wordcloud = WordCloud(
      font_path="C:/Windows/Fonts/simfang.ttf",
      background_color="white",width=1000,height=880).generate(cut_text)
   plt.imshow(wordcloud, interpolation="bilinear")
   plt.axis("off")
   plt.show()
































