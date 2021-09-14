#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import sha256

class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __int__(self,data,number=0):
        self.data = data
        self.number = number

class Blockchain():
    pass







def main():
    block = Block("hello world",1)

if __name__=='__name__':
    main()


