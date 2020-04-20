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

from apps.universe.models import UniverseUser

class UniverseUserAdmin(object):
    pass



xadmin.site.register(UniverseUser, UniverseUserAdmin)