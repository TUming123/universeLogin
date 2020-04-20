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

from apps.messageForm.models import MessageUser,Message

class MessageUserAdmin(object):
    pass

class MessageAdmin(object):
    pass

class GlobalSettings(object):
    site_title = "Ming后台管理系统"
    site_footer = "Ming"
    # menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True
    menu_style = "accordion"


xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(MessageUser, MessageUserAdmin)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
