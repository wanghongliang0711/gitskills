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

'''
requests默认使用application/x-www-form-urlencoded对POST数据编码。
如果要传递JSON数据，可以直接传入json参数：
'''
# r = requests.post(url, headers=headers, json={'username': 'abc@example.com', 'password': '123456'})  # 豆瓣首页
print("-------------")
'''
上传文件需要更复杂的编码格式，但是requests把它简化成files参数
'''
url = "http://www.testingedu.com.cn:8000/index.php/home/Uploadify/imageUp/savepath/head_pic/pictitle/banner/dir/images.html"
upload_files = {'file': open(r'test2.jpg', 'rb')}
headers = {"Content-Type":"multipart/form-data"}
r = requests.post(url, files=upload_files)
# r = requests.post(url, headers=headers, files=upload_files)  # 写了headers 反而报错？？
print(r.text)
pprint(r.json())
