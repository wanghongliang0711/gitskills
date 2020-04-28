# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 17:19
# @File    : demo01.py
import json

data = {"username": "13800138006", "password": "123456", 2: "1"}
print(type(data))

json_data = json.dumps(data)
print(type(json_data))
