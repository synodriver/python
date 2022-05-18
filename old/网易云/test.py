import  requests
import  parsel
import  re
import threading
from  urllib.request import urlretrieve
u = []
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
    return {'User-Agent': f'{dai}'}
def tihuan(ss):
    return  ss.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','').replace('.','')
gg = threading.Lock()
def down():
    global u
    while True:
        gg.acquire()
        if len(u)==0:
            gg.release()
            break
        else :
            url = u.pop()
            print(url)
            gg.release()
        # url = 'https://music.163.com/#/song?id=28891492'
        id = re.findall(r'https://music.163.com/#/song\?id=(.*)',url,re.S)[0]
        url = f'http://www.flvcd.com/parse.php?format=&kw=http%3A%2F%2Fmusic.163.com%2F%23%2Fsong%3Fid%3D{id}'

        # print(url)
        req = requests.get(url,headers = dailichi())
        # print(req.text)
        urll= re.findall('<TD align="left" width="45%"><a href="(.*?)">',req.text,re.S)[0]
        name = re.findall('<TD align="left" width="45%">(.*?)</TD>',req.text,re.S)[3]+' - '
        name += re.findall('<TD align="left" width="45%"><a href=".*?">(.*?)</a>',req.text,re.S)[0]
        name = tihuan(name)
        # print(urll,name)
##        response = requests.get(urll)
##        with open('%s.mp3'%name,'wb')as f:
##            f.write(response.content)
        urlretrieve(url, f'./{name}.mp3')

def main():
    global u
    url = 'https://music.163.com/#/playlist?id=2717223253'
    url= url.replace('/#','')
    head = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'cookie': 'starttime=; _iuqxldmzr_=32; _ntes_nnid=c6af2f5979cb33639357220962ec6413,1554769525568; _ntes_nuid=c6af2f5979cb33639357220962ec6413; WM_TID=epKRld70CrhEERBQRQMs1uquP%2FUO7frT; watch_times=0; level=7; user_level=7; NTES_SESS=NlpegKJSxw3J6FKxMWEKhOJkEomROX6G6bqbfVm7g_DxIBoZIK0.mF8JZzlQkDstghy9eySl6UTdEaBrpOGA5yg9q0WKVtUFmE3fpQYdTsMyBuSO6UpU9Jmlt1zUNq.qX2UQQDA_68Wx.WdT3xkxqzfCHZ4ZJcKZw.f6BF2iOKo6O6jMOv0qgZFRQj4JWd9D1bl08JWbwEgXF; S_INFO=1558697536|0|3&80##|l1761512493; P_INFO=l1761512493@163.com|1558697536|0|mail163|00&99|sic&1558697495&nmtp#sic&510100#10#0#0|&0|nmtp|l1761512493@163.com; nts_mail_user=l1761512493@163.com:-1:1; df=mail163_letter; MUSIC_EMAIL_U=f85ebfd7ca20950c4a519b242bc0a54d4af3aefa0477470ad066339d69c3e03e0ae72a8cdcaa9bb5ad4ce630b39e45229074ea3220a9c0f341049cea1c6bb9b6; playliststatus=visible; NTES_CMT_USER_INFO=270654612%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0g8tOk%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CbDE3NjE1MTI0OTNAMTYzLmNvbQ%3D%3D; __oc_uuid=711a3c10-9efd-11e9-90ca-3d968c47ff58; FromPlatform=uwp; usertrack=ezq0J102qiYl7RwQAzCTAg==; ne_analysis_trace_id=1565849904336; s_n_f_l_n3=638f954e535bb5df1565849904342; vinfo_n_f_l_n3=638f954e535bb5df.1.0.1565849904341.0.1565849904802; ntes_kaola_ad=1; WM_NI=O97g2UX0A%2B4ms32Zr5%2Bn0u%2BogAusmOyyaIhEBuYqE9EtQiD53VFc%2BiQi3AS4dKnelL6QxuXnXGVd64w38IOovKUj%2B7Er1O1yqKtiw6A%2FYhwFqAqQC9YgsWgcmg3fjC%2BEN3o%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6f165868abc8cc47397e78aa2d44b928b9ebbf780f295fe95fb5afca68585d22af0fea7c3b92a8de7f988b15f9cf08fccb767b1edfebbf13fe9b20096aa65a59fbb94f045bba7afaaeb4f82ab9792c83387ac9f8ac73ff18a8a84aa6393b7fda2d240a895a286ef48f68fb896db669c999a85b540b5edf8aace65b6959b8baa3d87aeffb0b473b395bc8af63e83f19789f64eb39fbfb2c2339bb9bdb8e669afb9fd87e949e99b82d4ee37e2a3; playerid=54487469; JSESSIONID-WYYY=DkpDR0cNm8DVG%2F9xdcTfGAiioYyUv%2FHw2p7Nj%2F9an7GgjN1j6EHZmJEknTW1PiN70vqaABENEeOzc5GToJzPrhyDho9mJcgQOyYqeVTsv2%5CFg%5C1xeMhmh8SvDRqdFypfx%5CMhi2413zRw%2B00fvG6lGs4QPbzTlAIcbaMi7%2BCF6Arb1uWw%3A1569288022268',
        'referer': 'https://music.163.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }
    response = requests.get(url,headers = head)
    song_id = re.findall('<li><a href="/song\?id=(.*?)">',response.text,re.S)
    for url in song_id:
        url = f'https://music.163.com/#/song?id={url}'
        # print(url)
        u.append(url)
        # down(url)
if __name__ == '__main__':
    main()
    print(u)
    print("ok")
    for _ in range(32):
        threading.Thread(target=down).start()
