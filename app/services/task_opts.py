#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/5 10:18
# @File    : task_opts.py

import json
from app.db.session import SessionLocal
from app.modules.tasks import Tasks
from app.schemas.response import Response
# from app.core.log import logger

from app.utils.common import task_id_generator
from app.utils.common import current_datetime

db = SessionLocal()


def new_tasks():
    task_id = task_id_generator()
    create_time = current_datetime()
    creator = 'admin'
    task = Tasks(
        #id=1,
        task_id= task_id,
        create_time = create_time,
        status= 1,
        creator=creator
    )
    try:
        db.add(task)
        msg = {'success': True, 'data':[{'task_id':task_id, 'create_time':create_time, 'creator':creator}], 'message':'成功'}

        db.commit()
        # logger.info('task_id:{}|creator:{}'.format(task_id, creator))
    except Exception as e:
        msg = {'success':False, 'data':[], 'message':'系统错误'}
        # logger.exception(e)
    return msg
