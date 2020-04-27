# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
from pprint import pprint

import requests


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = 'https://accounts.douban.com/login'

r = requests.post(url, headers=headers, data={'username': 'abc@example.com', 'password': '123456'})  # 豆瓣首页
print(f"--------{url}-------------")
print(r.url)

print("--------检测编码-------------")
print(r.encoding)

print("--------text-------------")
print(r.text)

'''
requests默认使用application/x-www-form-urlencoded对POST数据编码。
如果要传递JSON数据，可以直接传入json参数：
在postman中要在headers中加 application/x-www-form-urlencoded的配置
'''
data = {'username': '13800138006', 'password': '123456', "verify_code":"1"}
url = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6719753647589368"
headers = {"Content-Type":"application/x-www-form-urlencoded"}

# 下面两种方式都能成功
# r = requests.post(url, json=data)  # 豆瓣首页
r = requests.post(url, headers=headers, data=data)
print(r.status_code)
pprint(r.json())


