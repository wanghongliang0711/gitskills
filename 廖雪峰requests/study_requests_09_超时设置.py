# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
from pprint import pprint

import requests

# 图片、音频和视频文件
"""
在本机网络状况不好或者服务器网络响应太慢甚至无响应时，
我们可能会等待特别久的时间才可 能收到响应，甚至到最后收不到响应而报错。 
为了防止服务器不能及时响应，应该设置一个超时时间， 
即超过了这个时间还没有得到响应，那就报错。 这需要用到 timeout 参数。 
这个时间的计算是发归请 求到服务器返回响应的时间。 

如果想永久等待，可以直接将 timeout 设置为 None，
或者不设置直接留空，因为默认是 None。 
"""

r = requests.get("https://www.taobao1.com", timeout=10)


"""
请求分为两个阶段，即连接（ connect ）和读取（ read ）。
上面设置的 timeout 将用作连接和读取这二者的 timeout 总和。

"""


# 耗时多少秒
print(r.elapsed.total_seconds())

