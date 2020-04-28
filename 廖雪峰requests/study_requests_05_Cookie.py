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
    cookies = res.cookies
    print(requests.utils.dict_from_cookiejar(cookies))  # {'PHPSESSID': 'uc9mqtha8apjuj8sjujsn24jo6', 'is_distribut': '0', 'is_mobile': '0', 'uname': 'Magic', 'user_id': '8'}
    return requests.utils.dict_from_cookiejar(cookies)

url = 'http://www.testingedu.com.cn:8000/index.php?m=Home&c=Cart&a=header_cart_list'
headers_1 = {"Cookie":"PHPSESSID=dlp676iipiainfh32a62q7ne86"}

cookies = login()
# login()

# 两种方法都能传cookies
# 一种是放到headers中，一种是放到cookies中
# r_1 = requests.post(url, headers=headers_1)

r_1 = requests.post(url, cookies=cookies)
print(f"--------{url}-------------")
print(r_1.url)
print(r_1.text)

# 耗时多少秒
print(r_1.elapsed.total_seconds())

