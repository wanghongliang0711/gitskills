# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
from pprint import pprint

import requests

# 图片、音频和视频文件

r = requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)

# 保存图片
with open('favicon.ico', 'wb') as f:
    f.write(r.content)

print(r.status_code)
if r.status_code == 200:
    print("status : 200")


# 耗时多少秒
print(r.elapsed.total_seconds())

