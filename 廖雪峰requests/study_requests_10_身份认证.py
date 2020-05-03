# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth

# 图片、音频和视频文件


r = requests.get("https://www.taobao1.com",auth=HTTPBasicAuth("username","password"))

# 上面的代码可以直接简写如下：
r = requests.get("https://www.taobao1.com",auth=("username","password"))





# 耗时多少秒
print(r.elapsed.total_seconds())

