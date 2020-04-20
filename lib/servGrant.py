#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = "Ming"

from .message import *

class servGrant:
    kserv = ""
    kgrant = ""
    ACK = "success"

    tk = ""
    qk = ""
    ksess1 = ""
    ksess2 = ""
    tserv = ""
    qgrant = ""

    def __init__(self, kserv, kgrant):
        """

        :param kserv:
        :param kgrant:
        """
        self.kserv = kserv
        self.kgrant = kgrant

    def getClient(self, tk, qk):
        msg = message()
        self.tk = tk
        self.qk = qk
        tgrant = msg.decode(tk, self.kgrant)
        self.ksess1 = msg.decode(tgrant, self.kgrant)
        if self.ksess1[-len(self.ACK):len(self.ksess1)] == self.ACK:
            self.ksess1 = self.ksess1[-len(self.ksess1):-len(self.ACK)]
            self.qgrant = msg.decode(qk, self.ksess1)
            self.generateTserv()
            t = msg.encode(self.tserv, self.kserv)
            return [msg.encode(self.ksess2, self.ksess1), msg.encode(t, self.ksess1)]
        else:
            self.errorMsg()

    def generateTserv(self):
        msg = message()
        self.ksess2 = msg.generateKsess()
        t = msg.encode(self.ksess2, self.kserv)
        # print('-' * 50)
        # print(t)
        # print(len(t))

        self.tserv = msg.encode(self.ksess2, self.kserv)+self.ACK
        # print('-' * 50)
        # print("tserv\n"+str(self.tserv))
        # print(t)
        # print(len(t))
        # print(len(self.tserv))
        # print(msg.decode(t, self.kserv))

    def errorMsg(self):
        # print("grant error")
        raise Exception("grant server认证错误")

if __name__ == "__main__":
    msg = message()
    print(msg.generateKsess())