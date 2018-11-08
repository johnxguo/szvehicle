
import requests
import os
import random

def wfile(s):
    with open('1.png', 'wb') as f: 
        f.write(s)
url = r'https://wz.stc.gov.cn:443/szwsjj_web/ImgServlet.action?rnd=%19.17f'%(random.random())

# 这里cookie改成用session请求带回来
res = requests.get(url, headers={'cookie':'JSESSIONID=67948162E0BEF8CC4CF1E51644A417CA'})
print(url)

wfile(res.content)

va = input("输入验证码>")

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'wz.stc.gov.cn',
    'Connection': 'keep-alive',
    'Origin': 'https://wz.stc.gov.cn',
    'Referer': 'https://wz.stc.gov.cn/szwsjj_web/jsp/xxcx/jdcsydqcqqkcx.jsp',
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'cookie': 'JSESSIONID=67948162E0BEF8CC4CF1E51644A417CA',
    'Content-Length': '41'
}

data = { 
    'YANZHEN': va,
    'cph': r'%E7%B2%A4B6C5V8',
    'jdclx': '02'
}

print(data)

res = requests.post('https://wz.stc.gov.cn/szwsjj_web/JdcSydqcqqkcxServlet', headers = headers, data = data)

print(res.text)