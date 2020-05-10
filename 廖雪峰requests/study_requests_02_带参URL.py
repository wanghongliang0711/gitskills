# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
from pprint import pprint

import requests


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = 'https://www.douban.com/'

r = requests.get(url, headers=headers, params={'q':'python','cat':'1001'})  # 豆瓣首页
print("--------https://www.douban.com/-------------")
print(r.url)                 
print(r.request.url)

print("--------检测编码-------------")
print(r.encoding)

print("--------用content属性获得bytes对象-------------")
print(r.content)


# 天气API
url = "https://tianqiapi.com/api?"
params = {'version':'v61','appid':'46889473','appsecret':'j4IJ8aYU','city':'上海'}
r = requests.get(url, headers=headers, params=params)
print(r.text)
pprint(r.json())
print(r.url)
print(r.status_code)

# IP所在地址API
url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=138.122.122.228&resource_id=6006"
r = requests.get(url)
print(r.text)
print(r.status_code)
pprint(r.json())


# 获取腾讯课堂评论API  需要用到参数 请求头的 Referer参数,不然返回错误的json  {'msg': 'refer错误', 'retcode': 100101, 'type': 1}
url = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=396274&count=10&page=0&filter_rating=0&bkn=488420883&r=0.34757977521467187"
headers = {"referer":"https://ke.qq.com/course/396274"}
r = requests.get(url,headers=headers)
print(r.status_code)
pprint(r.json())

