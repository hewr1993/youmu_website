#!/usr/bin/python
# -*- coding:utf-8 -*-
# Created Time: Thu 30 Oct 2014 12:15:11 PM CST
# Author: Wayne Ho
# Purpose: test api for tunet
# Mail: hewr2010@gmail.com

import requests

if __name__ == "__main__":
    url = "http://student.tsinghua.edu.cn/practiceLogin.do"
    r = requests.post(url, {"userName":"hwr12", "password":"blah"})
    if r.text.encode("utf8") == "":
        print "failed"
    else:
        print "success"
