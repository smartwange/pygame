# -*- coding:utf-8 -*-
class Login:
    def __init__(self,name,email):
        self.__names = name
        self.__email = email

    def getEmail(self, name):
        if name == self.__names:
            return self.__email
        else:
            return 'nn'

# a=Login('张三','111@qq.com')
#  a._Login__email
