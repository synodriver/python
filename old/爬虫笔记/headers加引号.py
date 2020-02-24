import re
headers_str = """
accept-language: zh-CN,zh;q=0.9
content-length: 530
content-type: application/x-www-form-urlencoded
cookie: _ntes_nnid=ce56c68af18a79e30cd3f6b1c7bfd780,1580904097931; _ntes_nuid=ce56c68af18a79e30cd3f6b1c7bfd780; _iuqxldmzr_=32; watch_times=0; WM_TID=pJbBecQDipBBVUVBARJuRDILapn7Hly1; WM_NI=HsFsZMib6j3iW%2BCnKheF2v2%2BKHMZb6fHgLb2Oll%2FicMhb%2BB9PuycvwScbP42wYOpCXRYU%2FWw7TkMKaSSeY0bSy%2BJAN6%2F874MwKY0nGRMIQcrh1MJZwV719ZHsOQ4Uqi8R3Q%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee90bc5bbb97ffb3d2549aac8eb7c84e968e8aaaf55a9cb4adaee74db5e9fb96cf2af0fea7c3b92a8cad8a94d947abbefa8bb26395f58d8fca64a79afe97b121899883bbe13ea698a9ade13a8db4a4d0ec698fb8aeccc13394abb784f57d91bdaeb1b73ab5878191c25492879bd0d67df58ca5aeca6b918dabbab36a91a7e5abc446f6f1f8d8b747b59597d1ed4d929387b2e27aacef83abd97d96e9ffdad944b1919fd5d87babe89ed4d437e2a3; __remember_me=true; ntes_kaola_ad=1; playerid=19873434; JSESSIONID-WYYY=DmBBcX7zFquVXGM4dxgR%2FRcnZ5%5CUoP0q2ZbU1PPVOchgigou6fJwf541NSx8i7dc2viI8BezIBtzMGXKRAOIi0UWsq%2FCJpOlNP6%2Bc7B24C3FjTkzeQGam6s4qORdlBxbxmhPeCGhi0ybw9HmBekCckjhb7kTPiODbvjrh4THrVWxUPaC%3A1582201942519; MUSIC_U=dcc2958153d75d0e5dc88acde4c7e13a281f30159cdbbf83c490fffca08c7d525df4d309fdf3c5bd569b62383635dbfb05cb903b247e7fc7b47fb10558317a42eaddadb4a09cb5fbde39c620ce8469a8; __csrf=03246e1ef1521c2460bf5ad4d040b9e1
origin: https://music.163.com
referer: https://music.163.com/my/
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
"""
pattern = '^(.*?): (.*)$'
print('headers = {',end='')
for line  in headers_str.splitlines():
    print("\t",end='')
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))
print("}")