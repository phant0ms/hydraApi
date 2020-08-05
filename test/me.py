#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 14:19
# @File    : me.py



from fastapi import APIRouter

router = APIRouter()


@router.get('/me')
def getme(id):
    return 'this is from me file. you id is '+id

class A():
    def __new__(cls, *args, **kwargs):
        print(cls.__name__)

if __name__ == '__main__':
    A()
