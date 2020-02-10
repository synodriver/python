import execjs
import json
def translation():
    text = t1.get(0.0,'end')
    # text = '我'
    ctx = execjs.compile(""" 
       function TL(a) { 
       var k = ""; 
       var b = 406644; 
       var b1 = 3293161072;       
       var jd = "."; 
       var $b = "+-a^+6"; 
       var Zb = "+-3^+b+-f";    
       for (var e = [], f = 0, g = 0; g < a.length; g++) { 
           var m = a.charCodeAt(g); 
           128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
           e[f++] = m >> 18 | 240, 
           e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
           e[f++] = m >> 6 & 63 | 128), 
           e[f++] = m & 63 | 128) 
       } 
       a = b; 
       for (f = 0; f < e.length; f++) a += e[f], 
       a = RL(a, $b); 
       a = RL(a, Zb); 
       a ^= b1 || 0; 
       0 > a && (a = (a & 2147483647) + 2147483648); 
       a %= 1E6; 
       return a.toString() + jd + (a ^ b) 
     };      
     function RL(a, b) { 
       var t = "a"; 
       var Yb = "+"; 
       for (var c = 0; c < b.length - 2; c += 3) { 
           var d = b.charAt(c + 2), 
           d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
           d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
           a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
       } 
       return a 
     } 
    """)

    def getTk(text):
        return ctx.call("TL", text)
    import requests
    head = {
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'watch_times=0; _ga=GA1.3.753807373.1556544225; watch_times=0; level=7; user_level=7; NID=186=Xz0OZAMYy-lanx4-WAqB_EjzICESRlL6HxqKjZ6YEz-PzVG5RPAOkaSVaQ44pQmfYDpJVjA82mf1xggpo4rJoD5EqstL4rE8Qc5MB4k4VCZvur53OwpWWB_pE_hsbeREATkkuHH16tuOY4CcEzfEuUKSKsqcicJwD3ZKy4GFqYQ; _gid=GA1.3.1519618706.1570185394; 1P_JAR=2019-10-4-10',
        'referer': 'https://translate.google.cn/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }
    # url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&source=bh&ssel=0&tsel=0&kc=1&tk='+str(getTk(text))+'&q='+str(text)
    url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&source=bh&ssel=0&tsel=0&kc=1&tk='+str(getTk(text))+'&q='+str(text)
    response = requests.get(url,headers = head)
    # print(response.text)
    # print(response.json())
    txt = response.json()
    # print(txt[1][0][0],end='->')
    # for x in txt[1][0][1]: print(x,end=',')
    # print()
    # print(txt[1][1][0], end='->')
    # for x in txt[1][1][1]: print(x, end=',')
    ss = txt[1][0][0]+'-> '
    for x in txt[1][0][1]: ss+=(x+',')
    ss+='\n'+txt[1][1][0]+'-> '
    for x in txt[1][1][1]: ss+=x+','
    # print(ss)
    t1.delete(0.0, 'end')
    t1.insert(0.0, str(txt[0:1][0][0][0]))
import tkinter as tk
window = tk.Tk()
window.geometry('500x350')
window.title('谷歌翻译小软件')
b1 = tk.Button(window,text = '英翻汉',command = translation)
b1.pack()
t1 = tk.Text(window,font = ('','15',''))
t1.pack()
tk.mainloop()