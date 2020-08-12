#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/11 14:14
# @File    : login.py

from fastapi import APIRouter

from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from pydantic import BaseModel

from app.schemas.items import Response, Login
from app.core.security import create_access_token

router = APIRouter()

APP_ID = '123'
SECRET_KEY = '234'


@router.post('/login/access-token', response_model=Response)
def login_access_token(login: Login):
    '''

    :param login:
    :return:
    '''
    appid = login.apiKey
    secret_key = login.secretKey
    if appid and secret_key and appid == APP_ID and SECRET_KEY == secret_key:
        token = create_access_token({'appid': APP_ID})
        msg = {
            'success': True,
            'data': {'access_token': token},
            'message': '成功'
        }
        return msg
    else:
        msg = {
            'success': False,
            'data': {},
            'message': '非法请求'
        }
        return msg
