#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = "Ming"

# from Crypto.Cipher import AES
import datetime

from django.core.signing import Signer

salt = "mingming"


class message:
    """

    """

    # aesLen = 32

    def encode(self, s, key):
        return Signer(key).sign(s)

    def decode(self, s, key):
        try:
            return Signer(key).unsign(s)
        except Exception as e:
            raise e

    # def make32(self, s, cut =False):
    #     while len(s) % 32 != 0:
    #         s += '\x20'
    #     if cut:
    #         return s[0:self.aesLen]
    #     return s
    #
    # def encode(self, s, key):
    #     s1 = self.make32(s)
    #     key1 = self.make32(key, True)
    #     aes = AES.new(str.encode(key1), AES.MODE_ECB)
    #     t1 = aes.encrypt(str.encode(s1))
    #     t1 = base64.encodebytes(t1)
    #     t1 = str(t1, encoding="utf-8")
    #     return t1
    #     # return str(base64.encodebytes(aes.encrypt(str.encode(s1))), encoding="utf-8")
    #
    # def decode(self, s, key):
    #     s1 = self.make32(s)
    #     key1 = self.make32(key, True)
    #     key1 = str.encode(key1)
    #     aes = AES.new(key1, AES.MODE_ECB)
    #     t1 = base64.decodebytes(s1.encode(encoding="utf-8"))
    #     t1 = aes.decrypt(t1)
    #     t1 = str(t1, encoding="utf-8").replace('\x20', '')
    #     return t1
    #     # return str(aes.decrypt(base64.decodebytes(s.encode(encoding="utf-8"))), encoding="utf-8").replace('\0', '')

    def generateKsess(self):
        source = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')
        t1 = self.encode(source, source)
        # t2 = self.decode(t1,source)
        # return [t1, t2]
        return t1


if __name__ == "__main__":
    msg = message()
    print(msg.generateKsess())
    # a = "hellp"
    # b = msg.encode(a, a)
    # while a == msg.decode(b, a):
    #     print(a, end=" ")
    #     print(b)
    #     print('+'*50)
    #     a = b[0:5]
    #     b = msg.encode(a, a)
