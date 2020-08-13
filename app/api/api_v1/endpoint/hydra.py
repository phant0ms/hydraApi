#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 14:47
# @File    : hydra.py


from app.schemas.items import Response
from app.core.config import settings
from fastapi import APIRouter, Security, HTTPException
# from app.modules.tasks import Tasks
from app.services.task_opts import new_tasks
from app.services.task_opts import start_tasks
from app.schemas.items import Targets

from fastapi import Depends, Header
from typing import Optional

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse
from app.core.security import authenticate
from app.modules.invoker import Invoker


router = APIRouter()


@router.get('/task/new', response_model=Response, )
def new(invoker:Invoker = Depends(authenticate)):
    '''
    创建一个新的任务

    如果成功则返回任务id
    '''
    # if not auth:
    #     return invalid_token()
    return new_tasks(invoker)


@router.post('/task/{task_id}/start', response_model=Response, )
def start(task_id: str, target: Targets):
    '''

    :param task_id: 任务 id.
    :param target: 扫描的域名或者 ip. 多个目标使用`,`分隔
    :return:
    '''
    return start_tasks(task_id, target)
    # return 'task start'


@router.get('/task/{task_id}/stop')
def stop(task_id: str):
    '''
    停止指定的任务
    :param task_id:
    :return:
    '''
    return task_id


@router.get('/task/{task_id}/status')
def status(task_id: str, ):
    return 'task status'


@router.get('/task/{task_id}/delete')
def delete(task_id: str):
    '''
    删除指定的任务
    :param task_id:
    :return:
    '''
    return True
