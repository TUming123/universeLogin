#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = "Ming"

"""
need to install pycryptodome
"""

import hashlib
import base64

from .message import *

class client:
    uname = ""
    dpw = ""

    ksess1 = ""
    ksess2 = ""
    ACK = "success"
    tk = ""
    qgrant = ""
    qk = ""
    qserv = '"'

    def __init__(self, uname, dpw) :
        """

        :param uname:
        :param dpw:
        """
        self.uname = uname
        self.dpw = dpw

    def send2Auth(self):
        return self.uname

    def getAuth(self, authRes):
        msg = message()
        if self.ACK == msg.decode(authRes[2], self.dpw):
            self.ksess1 = msg.decode(authRes[0], self.dpw)
            self.tk = msg.decode(authRes[1], self.dpw)
            self.loginAck()
        else:
            self.errorMessage()

    def generateQgrant(self):
        self.qgrant = "mmm"

    def send2Grant(self):
        """
        creat Qgrant
        :return:
        """
        msg = message()
        # self.generateQgrant()
        self.qk = msg.encode(self.qgrant, self.ksess1)
        return [self.tk, self.qk]
    #     send to serv_grant tk, qk

    def getGrant(self, grantRes):
        msg = message()
        self.ksess2 = msg.decode(grantRes[0], self.ksess1)
        tk = msg.decode(grantRes[1], self.ksess1)
        self.generateQserv()
        qk = msg.encode(self.qserv, self.ksess2)
        return [qk, tk]
    #     send to servApp   new qk,tk

    def loginAck(self):
        """
        succeed logining
        :return:
        """
        # print("login success")

    def generateQserv(self):
        """
        get application
        :return:
        """
        # self.qserv = "kkk"

    # append ACK on tail



    def errorMessage(self):
        """
        if any of authentication fail
        :return:
        """
        # print("clienterror")

if __name__ == "__main__":
    client = message()
    a = "hello-+"
    key = "hi"
    b = client.encode(a, key)
    c = client.decode(b, key)
