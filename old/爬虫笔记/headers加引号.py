import re
headers_str = """
Host: api.bilibili.com
Referer: https://space.bilibili.com/32482364/fans/fans
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
"""
pattern = '^(.*?): (.*)$'
print('headers = {',end='')
for line  in headers_str.splitlines():
    print("\t",end='')
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))
print("}")