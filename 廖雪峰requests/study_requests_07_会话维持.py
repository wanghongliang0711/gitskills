# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
from pprint import pprint

import requests

# 图片、音频和视频文件
"""
这里我们请求了一个测试网址 
http://httpbin.org/cookies/set/number/123456789
请求这个网址时， 可以设置一个 cookie，名称叫作 number，
内容是 123456789，
随后又请求了 http://httpbin.org/cookies
此网址可以获取当前的 Cookies。
"""
requests.get("http://httpbin.org/cookies/set/number/123456789")
r = requests.get('http://httpbin.org/cookies')
print(r.text)
"""
{
  "cookies": {}
}
"""

# 这并不行。 我们再用 Sessios  试试看：
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456789")
r = s.get('http://httpbin.org/cookies')
print(r.text)

res = requests.get("https://www.12306.cn")
print(res.status_code)




# 耗时多少秒
print(r.elapsed.total_seconds())

