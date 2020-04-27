# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 13:24
# @File    : 视频_01.py

# 新增用户接口
import requests
# URL
addUser_url = 'http://47:96:181.17:9090/rest/ac01CrmController'
userData = {
    "aac003":"张三",
    "aac004":"1",
    "aac011":"21",
    "aac030":"1234567891234",
    "aac01u":"8800225",
    "crm003":"1",
    "crm004":"1",
    "crm00a":"2018-11-11",
    "crm00b":"aaaaaa",
    "crm00c":"2019-02-28",
    "crm00d":"bbbbbb"
}
headers = {"Content-Type":"application/json", "X-AUTH-TOKEN":""}
rep = requests.post(addUser_url, data=userData, headers=headers)
print(rep.text)

