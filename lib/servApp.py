#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = "Ming"

from .message import *

class servApp:
    ACK = "success"
    kserv = ""
    qserv = ""

    def __init__(self, kserv):
        """

        :param uname:
        :param dpw:
        """
        self.kserv = kserv

    def getClient(self, clientRes):
        msg = message()
        tserv = msg.decode(clientRes[1], self.kserv)
        if tserv[-len(self.ACK):len(tserv)] == self.ACK:
            tserv = tserv[0:-len(self.ACK)]
            # print('-'*50)
            # print("tserv\n"+str(tserv))
            # print(len(tserv))
            ksess2 = msg.decode(tserv, self.kserv)
            self.qserv = msg.decode(clientRes[0], ksess2)
            # self.appClient()
            # print('-' * 50)
            # print(qserv)
            # print(ksess2)
        else:
            self.errorMsg()

    def appClient(self):
        """
        start serve to client
        :return:
        """
        # print("App start")

    def errorMsg(self):
        # print("SERV error")
        raise Exception("APP serv 认证失败")

if __name__ == "__main__":
    msg = message()
    print(msg.generateKsess())

