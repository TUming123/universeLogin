#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = "Ming"
"""
@author:Mingming
@e-mail:mingming888888888@163.com
@file:message-PyCharm-xadimn.py
@time:2020/4/17 0017 16:54
Any bug, any question, mail me.
"""

import xadmin

from apps.tips.models import TipMessage, TipUser


class TipUserAdmin(object):
    pass


class TipMessageAdmin(object):
    pass


xadmin.site.register(TipUser, TipUserAdmin)
xadmin.site.register(TipMessage, TipMessageAdmin)