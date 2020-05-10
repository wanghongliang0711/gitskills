# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
import requests


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = 'https://www.douban.com/'

r = requests.get(url, headers=headers)  # 豆瓣首页
print("--------https://www.douban.com/-------------")
print(r.url)

print("--------200-------------")
print(r.status_code)

print("--------网页内容-------------")
print(r.text)



r.encoding = "utf-8"  # 输出中文
r.raise_for_status()   # 不是200 抛出异常 try except
r.encoding = r.apparent_encoding  # 可以使用apparent_encoding查看真实编码 自动获取编码，不用每次都输  r.encoding = "utf-8"  了 ？？？




