#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/5 10:22
# @File    : common.py

import time
from uuid import uuid4


def task_id_generator():
    '''

    :return:
    '''
    rnd_id = str(uuid4()).replace('-','')[:16]
    return rnd_id


def current_datetime():
    '''

    :return:
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
