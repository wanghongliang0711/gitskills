# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
import requests


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = 'https://accounts.douban.com/login'

r = requests.post(url, headers=headers, data={'username': 'abc@example.com', 'password': '123456'})  # 豆瓣首页
print(f"--------{url}-------------")
print(r.url)

'''
requests默认使用application/x-www-form-urlencoded对POST数据编码。
如果要传递JSON数据，可以直接传入json参数：
'''
r = requests.post(url, headers=headers, json={'username': 'abc@example.com', 'password': '123456'})  # 豆瓣首页

'''
上传文件需要更复杂的编码格式，但是requests把它简化成files参数
'''
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)
