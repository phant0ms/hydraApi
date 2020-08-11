#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-08-23 15:47
# @File    : misc.py

import redis
from app.core.log import logger
from app.core.config import settings


class RedisHelper(object):
    __pool = None

    def __init__(self, db=1):
        RedisHelper.__get_connect(db)

    @staticmethod
    def __get_connect(db):
        # 创建连接池，提高性能
        # redis使用连接池是不需要关闭的

        if RedisHelper.__pool is None:
            pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB,
                                        password=settings.REDIS_AUTH)
            RedisHelper.__pool = redis.Redis(connection_pool=pool)

        return RedisHelper.__pool

    @staticmethod
    def sAddMember(setName, value):
        if setName is None or setName == '':
            errMsg = 'error, set key can\'t be empty.'
            logger.error(errMsg)
            return False
        try:
            RedisHelper().__pool.sadd(setName, value)
            return True
        except Exception as e:
            errMsg = 'a error was occurred in sAddMember when insert key:{} value:{}.'.format(setName, value)
            logger.exception(errMsg)

    @staticmethod
    def sPop(setName):
        try:
            return RedisHelper().__pool.spop(setName)
        except Exception as e:
            errMsg = 'a error was occurred in sAddMember when insert key:{}.'.format(setName)
            logger.exception(errMsg)

    @staticmethod
    def sIsMember(setName, value):
        if setName is None or setName == '':
            errMsg = 'error, set key can\'t be empty.'
            logger.error(errMsg)
            return False
        try:
            return RedisHelper().__pool.sismember(setName, value)
        except Exception as e:
            errMsg = 'a error was occurred in sIsMember when check key:{} value:{}.'.format(setName, value)
            logger.exception(errMsg)
            return False

    @staticmethod
    def sRemMember(setName, value):
        if setName is None or setName == '':
            errMsg = 'error, set key can\'t be empty.'
            logger.error(errMsg)
            return False
        try:
            RedisHelper().__pool.srem(setName, value)
        except Exception as e:
            errMsg = 'a error was occurred in sRemMember when remove key:{} value:{}.'.format(setName, value)
            logger.exception(errMsg)
            return False

    @staticmethod
    def set_expire(key, time):
        try:
            RedisHelper().__pool.expire(key, time)
        except Exception as e:
            errMsg = 'a error was occurred when set expire time on key:{}, time {}'.format(key, time)
            logger.exception(errMsg)
            return False

    @staticmethod
    def get_ttl(key, ):
        return RedisHelper().__pool.ttl(key)

    @staticmethod
    def sMembers(setName):
        if setName is None or setName == '':
            errMsg = 'error, set key can\'t be empty.'
            logger.error(errMsg)
            return False
        try:
            return RedisHelper().__pool.smembers(setName)
        except Exception as e:
            errMsg = 'a error was occurred in sMembers when load ({}) members.'.format(setName, )
            logger.exception(errMsg)
            return None

    @staticmethod
    def multi_push(setName, vals):
        pipe = RedisHelper().__pool.pipeline()
        for var in vals:
            pipe.sadd(setName, var)
        pipe.execute()

    @staticmethod
    def delete_key(setName):
        return RedisHelper().__pool.delete(setName)

    @staticmethod
    def zAdd(key, score, value):
        return RedisHelper().__pool.zadd(key, {value: score})

    @staticmethod
    def zPopMin(key):
        '''
        返回一个分数最小。
        数据结构：[(data, source)]
        :param key:
        :return:
        '''
        return RedisHelper().__pool.zpopmin(key)

    @staticmethod
    def lPush(key, value):
        return RedisHelper().__pool.lpush(key, value)

    @staticmethod
    def get_key_like(pattern="*"):
        return RedisHelper().__pool.keys(pattern)

    @staticmethod
    def lPop(key):
        return RedisHelper().__pool.lpop(key)

    @staticmethod
    def hGet(key, field):
        return RedisHelper().__pool.hget(key, field)

    @staticmethod
    def hSet(key, field, valud):
        return RedisHelper().__pool.hset(key, field, valud)

    @staticmethod
    def hScan(key, cursor, match=None, count=10):
        return RedisHelper().__pool.hscan(key, cursor, match, count)


if __name__ == '__main__':

    # print(conf)
    # for i in range(1000):
    #     k = 'key'+str(i)
    #     v = 'value'+ str(i)
    #     a = RedisHelper().hSet('host', k, v)

    i = 0
    cursor = 0
    while True:
        rst = RedisHelper().hScan('host', cursor,)
        cursor = rst[0]
        data = rst[1]
        for req in data.values():
            i +=1
            print(req)
        if cursor ==0:
            break
    print(i)


