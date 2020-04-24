#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import logging


class myLog:

    def __init__(self):
        self.formLog = logging.getLogger('formLogin')
        self.tipsLog = logging.getLogger('formLogin')
        self.universeLog = logging.getLogger('formLogin')
        self.infoLog = logging.getLogger('info')
        self.warningLog = logging.getLogger('warning')
        self.errorLog = logging.getLogger('error')
        self.criticalLog = logging.getLogger('critical')

    def form(self, user, ip, pfix):
        self.formLog.info("formuser:%s ip:%s" % (user, ip) + pfix)

    def tips(self, user, ip, pfix):
        self.tipsLog.info("tpsuser:%s ip:%s" % (user, ip) + pfix)

    def universe(self, user, ip, pfix):
        self.universeLog.info("universeuser:%s ip:%s" % (user, ip) + pfix)

    def info(self, msg):
        self.infoLog.info("msg:%s" % msg)

    def warning(self, msg):
        self.warningLog.warning("msg:%s" % msg)

    def error(self, msg):
        self.errorLog.error("msg:%s" % msg)

    def critical(self, msg):
        self.criticalLog.critical("msg:%s" % msg)

    def getIp(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        return ip
    
    def try2sign(self, id, ip, prefix=""):
        self.infoLog.info(prefix+"try toregister:%s ip:%s" % (id, ip))
    
    def fail2sign(self, id, ip, prefix=""):
        self.infoLog.info(prefix+"register fail:%s ip:%s" % (id, ip))
        
    def succeed2sign(self, id, ip, prefix=""):
        self.infoLog.info(prefix+"register succeed:%s ip:%s" % (id, ip))

    def try2login(self, id, ip, prefix=""):
        self.infoLog.info(prefix + "try to login:%s ip:%s" % (id, ip))

    def fail2login(self, id, ip, prefix=""):
        self.infoLog.info(prefix + "login fail:%s ip:%s" % (id, ip))

    def succeed2login(self, id, ip, prefix=""):
        self.infoLog.info(prefix + "login succeed:%s ip:%s" % (id, ip))
    
    def succeed2tip(self, id, ip, prefix=""):
        self.tipsLog.info(prefix + "tips succeed:%s ip:%s" % (id, ip))
    
    def fail2tip(self, id, ip, prefix=""):
        self.tipsLog.info(prefix + "tips fail:%s ip:%s" % (id, ip))
        
    def succeed2form(self, id, ip, prefix=""):
        self.formLog.info(prefix + "form succeed:%s ip:%s" % (id, ip))
        
    def fail2form(self, id, ip, prefix=""):
        self.formLog.info(prefix + "form fail:%s ip:%s" % (id, ip))
        
    def blog(self, id, ip, prefix=""):
        self.infoLog.info(prefix + "skin blog:%s ip:%s" % (id, ip))
        
    def runtime(self, e, id, ip):
        self.error("Runtime error:%s ip:%s" % (id, ip) + str(e))
        
    def system(self, e, id, ip):
        self.critical("Runtime error:%s ip:%s" % (id, ip) + str(e))