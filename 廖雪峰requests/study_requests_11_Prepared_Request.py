# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth
from requests import Request, Session

"""
可以看到，我们达到了同样的 POST请求效果。
有了 Request 这个对象，就可以将请求当作独立的对象来看待，
这样在进行队列调度时会非常方 便。 我们会用它来构造一个 Request 队列。

"""

url = "http://httpbin.org/post"
data = {
    'name':'wang'
}
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}

s = Session()
req = Request('POST', url, data=data, headers=headers)

prepped = s.prepare_request(req)

r = s.send(prepped)
print(r.text)


# 耗时多少秒
print(r.elapsed.total_seconds())

