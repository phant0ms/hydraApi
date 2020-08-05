#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 14:47
# @File    : hydra.py


from app.schemas.response import Response

from fastapi import APIRouter
# from app.modules.tasks import Tasks
from app.services.task_opts import new_tasks

router = APIRouter()


@router.get('/task/new', response_model=Response)
def new():
    '''
    创建一个新的任务

    return: 返回任务 id
    '''
    return new_tasks()


@router.get('/task/{task_id}/delete')
def delete(task_id:str):
    '''
    删除指定的任务
    :param task_id:
    :return:
    '''
    return True


@router.get('/task/{task_id}/stop')
def stop(task_id:str):
    '''
    停止指定的任务
    :param task_id:
    :return:
    '''
    return task_id


@router.post('/task/{task_id}/start')
def start(task_id:str):
    print(status)
    return 'task start'


@router.get('/task/{task_id}/status')
def status(task_id:str):
    return 'task status'