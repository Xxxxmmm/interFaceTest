#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 14:04
# @Author  : 野猪佩奇
# @File    : runmethond.py
# @Software: PyCharm
# @contact: 2790279232@qq.com
import json
import requests
requests.packages.urllib3.disable_warnings()

class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data,header)
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    url = 'https://shidaizhu.com/auth/user/getUserToken'
    headers = {"content-type": "application/json;charset=UTF-8"}
    data = {
    "code": "033lCGB20NC52H1enbC20yfoB20lCGBM",
    "deviceModel": "string",
    "terminal": "0",
    "version": "string"
  }
    run = RunMethod()
    run_test = run.run_main(method="Post", url=url, data=json.dumps(data),header=headers)
    print((run_test))
