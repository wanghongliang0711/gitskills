# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:18
# @File    : study_requests_01_基础.py
from pprint import pprint

import requests

# 图片、音频和视频文件
"""
对于某些网站，在测试的时候请求几次， 能正常获取内容。
但是一旦开始大规模爬取，对于大规 模且频繁的请求，网站可能会弹出验证码，
或者跳转到登录认证页面， 
更甚者可能会直接封禁客户端 的 IP，导致一定时间段内无法访问。
"""
proxies = {
    "http":"http://10.10.1.10:555",
    "https":"..."
}
r = requests.get("http://www.taobao.com", proxies=proxies)
# 耗时多少秒
print(r.elapsed.total_seconds())

