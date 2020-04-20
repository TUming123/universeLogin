#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = "Ming"

from .message import *

class servAuth:
    uname = ""
    kgrant = ""
    ksess1 = ""
    tgrant = ""
    ACK = "success"
    auth = False

    dpw = ""

    def __init__(self, kgrant):
        """

        :param kgrant:
        """
        self.kgrant = kgrant

    def getDpw(self):
        return

    def generateTgant(self):
        self.tgrant = message().encode(self.ksess1 + self.ACK, self.kgrant)

    def send2Client(self):
        self.verifyUname()
        if self.auth:
            msg = message()
            self.ksess1 = msg.generateKsess()
            self.generateTgant()
            return [msg.encode(self.ksess1, self.dpw),
                    msg.encode(msg.encode(self.tgrant, self.kgrant), self.dpw),
                    msg.encode(self.ACK, self.dpw)]
        self.errorMsg()

    def verifyUname(self):
        self.auth = True

    def errorMsg(self):
        print("auth error")


if __name__ == "__main__":
    a = "123456"
    b = '234'
    print(message().encode(a, a))
    print(a[-len(b):len(a)])