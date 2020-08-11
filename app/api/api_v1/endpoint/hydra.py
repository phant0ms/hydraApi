#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 14:47
# @File    : hydra.py


from app.schemas.items import Response

from fastapi import APIRouter
from typing import List
# from app.modules.tasks import Tasks
from app.services.task_opts import new_tasks
from app.services.task_opts import start_tasks
from app.schemas.items import ItemsCreate

from fastapi import Depends

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


@router.get('/task/new', response_model=Response)
def new():
    '''
    创建一个新的任务

    return: 返回任务 id
    '''
    return new_tasks()


@router.post('/task/{task_id}/start', response_model=Response)
def start(task_id:str, target: ItemsCreate):
    '''

    :param task_id: 任务 id.
    :param target: 扫描的域名或者 ip. 多个目标使用`,`分隔
    :return:
    '''
    return start_tasks(task_id, target)
    # return 'task start'


@router.get('/task/{task_id}/stop')
def stop(task_id:str):
    '''
    停止指定的任务
    :param task_id:
    :return:
    '''
    return task_id

@router.get('/task/{task_id}/status')
def status(task_id:str, ):
    return 'task status'


@router.get('/task/{task_id}/delete')
def delete(task_id:str):
    '''
    删除指定的任务
    :param task_id:
    :return:
    '''
    return True


@router.post('/login/access-token')
def login_access_token(from_data: OAuth2PasswordRequestForm = Depends()):
    print(from_data.username, from_data.password)
    print(from_data)


