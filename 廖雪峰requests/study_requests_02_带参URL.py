# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
import requests


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = 'https://www.douban.com/'

r = requests.get(url, headers=headers, params={'q':'python','cat':'1001'})  # 豆瓣首页
print("--------https://www.douban.com/-------------")
print(r.url)

print("--------检测编码-------------")
print(r.encoding)

print("--------用content属性获得bytes对象-------------")
print(r.content)
