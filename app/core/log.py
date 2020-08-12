#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 22:07
# @File   : log

"""

"""

import os
import sys
import logging.config


# BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
BASE_DIR = './'
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)


# from cloghandler import ConcurrentRotatingFileHandler 进程安全

# 给过滤器使用的判断
class RequireDebugTrue(logging.Filter):
    # 实现filter方法
    def filter(self, record):
        return True


LOGGING = {
    # 基本设置
    'version': 1,  # 日志级别
    'disable_existing_loggers': True,  # 是否禁用现有的记录器

    # 日志格式集合
    'formatters': {
        # 标准输出格式
        'standard': {
            # [具体时间][线程名:线程ID][日志名字:日志级别名称(日志级别ID)] [输出的模块:输出的函数]:日志内容
            # 'format': '[%(asctime)s][%(threadName)s:%(thread)d][%(name)s:%(levelname)s(%(lineno)d)][%(module)s:%(funcName)s]:%(message)s'
            'format': '%(asctime)s|%(levelname)s|%(filename)s|%(threadName)s|%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },

        # 仅保存日志
        'simple': {
            # [具体时间][线程名:线程ID][日志名字:日志级别名称(日志级别ID)] [输出的模块:输出的函数]:日志内容
            # 'format': '[%(asctime)s][%(threadName)s:%(thread)d][%(name)s:%(levelname)s(%(lineno)d)][%(module)s:%(funcName)s]:%(message)s'
            'format': '%(message)s',
            #'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },

    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': RequireDebugTrue,
        }
    },

    # 处理器集合
    'handlers': {
        # 输出到控制台
        'console': {
            'level': 'DEBUG',  # 输出信息的最低级别
            'class': 'logging.StreamHandler',
            'formatter': 'standard',  # 使用standard格式
            'filters': ['require_debug_true', ],  # 仅当 DEBUG = True 该处理器才生效
        },
        # 输出到文件
        'file': {
            'level': 'DEBUG',
            # 'class': 'cloghandler.ConcurrentRotatingFileHandler', #fixme 多进程安全
            #'class': 'logging.handlers.RotatingFileHandler',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(BASE_DIR, 'core.log'),  # 输出位置
            #'maxBytes': 1024 * 1024 * 50,  # 文件大小 50M
            'when':'MIDNIGHT',
            'backupCount': 10,  # 备份份数
            'encoding': 'utf8',  # 文件编码
            'delay': True,
        }
    },

    # 日志管理器集合
    'loggers': {
        # 管理器
        'default': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,  # 是否传递给父记录器
        }
    }
}

logging.config.dictConfig(LOGGING)
# logging.disable(logging.DEBUG) #禁用debug level 日志
logger = logging.getLogger('default')

