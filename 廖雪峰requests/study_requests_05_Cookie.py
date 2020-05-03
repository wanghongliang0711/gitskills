# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
from pprint import pprint

import requests

def login():
    data = {'username': '13800138006', 'password': '123456', "verify_code": "1"}
    url = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6719753647589368"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    res = requests.post(url, headers=headers, data=data)
    # cookies = res.cookies.items()   # [('PHPSESSID', 'aoo0b8pa08f59uvnal21a4qoo3'), ('is_distribut', '0')...]
    cookies = res.cookies # <RequestsCookieJar[<Cookie PHPSESSID=nqn8e4eari6kr9qvu62b7cb1j6 for www.testingedu.com.cn/>, <Cookie is...
    print(res.cookies)
    print("888888888888888888888888888888888")
    print(requests.utils.dict_from_cookiejar(cookies))  # {'PHPSESSID': 'uc9mqtha8apjuj8sjujsn24jo6', 'is_distribut': '0', 'is_mobile': '0', 'uname': 'Magic', 'user_id': '8'}
    return requests.utils.dict_from_cookiejar(cookies)  # cookiejar到字典

url = 'http://www.testingedu.com.cn:8000/index.php?m=Home&c=Cart&a=header_cart_list'
headers_1 = {"Cookie":"PHPSESSID=dlp676iipiainfh32a62q7ne86"}

cookies = login()
print("字典到cookiejar")
print(requests.cookies.cookiejar_from_dict(cookies)) #  字典到cookiejar
# login()

# 两种方法都能传cookies
# 一种是放到headers中，一种是放到cookies中
# r_1 = requests.post(url, headers=headers_1)

r_1 = requests.post(url, cookies=cookies)
print(f"--------{url}-------------")
print(r_1.url)
# print(r_1.text)

# 耗时多少秒
print(r_1.elapsed.total_seconds())

print(cookies)


cookies ="_ga=GA1.2.782977993.1559450435; __gads=ID=2a1f89877ea8413e:T=1581423774:S=ALNI_MYcH0zrUgjXZvyJLQ-KkOyNXAQgIQ; Hm_lvt_3eec0b7da6548cf07db3bc477ea905ee=1586662065,1586663831,1588493383; Hm_lpvt_3eec0b7da6548cf07db3bc477ea905ee=1588493383; SERVERID=fb669a01438a4693a180d7ad8d474adb|1588493352|1588493352"
jar = requests.cookies.RequestsCookieJar()
# headers = { ’ Host ’： t 刷w. zh1hu. com', ’User-Agent ’：·川ozilla/S.O (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537. 36 (KHTML, like Gecko) Chrome/53.0. 2785.116 Safari/537. 36'
for cookie in cookies.split(';'):
    key, value = cookie.split ('=', 1)
    jar.set (key, value)
print("jar:")
print(jar)
