#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/5 10:18
# @File    : task_opts.py

import json
from app.db.session import SessionLocal
from app.modules.tasks import Tasks
from app.schemas.items import Response
# from app.core.log import logger

from app.utils.common import task_id_generator
from app.utils.common import current_datetime

# from fastapi import HTTPException
from sqlalchemy.orm import Session, Query
from fastapi.encoders import jsonable_encoder
from app.utils.redishelper import RedisHelper

db: Session = SessionLocal()


def new_tasks():
    task_id = task_id_generator()
    create_time = current_datetime()
    creator = 'admin'
    task = Tasks(
        # id=1,
        task_id=task_id,
        create_time=create_time,
        status=1,
        creator=creator
    )
    try:
        db.add(task)
        msg = {'success': True, 'data': [{'task_id': task_id, 'create_time': create_time, 'creator': creator}],
               'message': '成功'}

        db.commit()
        # logger.info('task_id:{}|creator:{}'.format(task_id, creator))
    except Exception as e:
        db.rollback()
        msg = {'success': False, 'data': [], 'message': '系统错误'}
        # logger.exception(e)
    return msg


def start_tasks(task_id: str, target):
    if not task_id:
        msg = {'success': False, 'data': [], 'message': 'task_id不能为空'}
        return msg
    targets = jsonable_encoder(target)
    if not targets['targets']:
        msg = {'success': False, 'data': [], 'message': '扫描目标不能为空'}
        return msg
    rst: Query = db.query(Tasks).filter(Tasks.task_id == task_id).filter(Tasks.status==1).first()
    if not rst:
        msg = {'success': False, 'data': [], 'message': '任务id:{}不存在,请先创建'.format(task_id)}
        return msg
    try:
        total = fetch_tasks(targets)

        db.query(Tasks).filter(Tasks.task_id==task_id).filter(Tasks.status==1).\
            update({'targets': targets['targets'], 'status': 2})
        db.commit()

        msg = {'success': True, 'data': [{'targets': targets['targets'], 'total':total}], 'message': '任务启动成功'}
        return msg
    except Exception as e:
        db.rollback()
        logger.exception(e)
        msg = {'success': False, 'data': [], 'message': '系统错误'}
        return msg


def fetch_tasks(targets):
    '''
    从 redis 和 es中获取扫描报文
    :param targets:
    :return:
    '''
    total = 0
    targets_list = targets.split(',')
    for host in targets_list:
        cursor =0
        key = 'request_'+host
        request_count = RedisHelper().hLen(key)
        logger.info('host:{}|total request:{}|'.format(host, request_count))
        while True:
            rst = RedisHelper().hScan(key, cursor)
            cursor = rst[0]
            data_set = rst[1]
            for request in data_set.values():
                new_request, refresh = update_session(request)
                save_to_immediate_queue(new_request)
                ''''
                '''

    #---- load request from es---

    return total
