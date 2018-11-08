
import requests
import os


def wfile(s):
    with open('1.png', 'wb') as f: 
        f.write(s)

res = requests.get(r'https://wz.stc.gov.cn/szwsjj_web/ImgServlet.action?rnd=0.14253165441443905')

wfile(res.content)

va = input("输入验证码>")

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'wz.stc.gov.cn',
    'Origin': 'https://wz.stc.gov.cn',
    'Referer': 'https://wz.stc.gov.cn/szwsjj_web/jsp/xxcx/jdcsydqcqqkcx.jsp',
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'cookie': 'JSESSIONID=8FA3454EF0B3F0028352C2EF9C6381E0'
}

data = {
    'YANZHEN': va,
    'cph': '粤B6C5V8',
    'jdclx': '02'
}

res = requests.post('https://wz.stc.gov.cn/szwsjj_web/JdcSydqcqqkcxServlet', headers = headers, data = data)

print(res.text)