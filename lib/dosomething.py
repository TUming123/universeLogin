#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.http import HttpResponse

__author__ = "Ming"
"""
@author:Mingming
@e-mail:mingming888888888@163.com
@file:message-PyCharm-dosomething.py
@time:2020/4/24 0024 21:10
Any bug, any question, mail me.
"""

class dosomething:
    @staticmethod
    def doSomething():
        return HttpResponse("Something goes wrong")
    @staticmethod
    def doNothing():
        pass