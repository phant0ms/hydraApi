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
from app.modules.invoker import Invoker
from app.db.session import SessionLocal
from sqlalchemy.orm import Session, Query
from app.core.log import logger

router = APIRouter()


# APP_ID = '123'
# SECRET_KEY = '234'


@router.post('/login/access-token', response_model=Response)
def login_access_token(login: Login):
    '''

    :param login:
    :return:
    '''
    appid = login.appId
    secret_key = login.secretKey
    try:
        db: Session = SessionLocal()
        invoker: Invoker = db.query(Invoker).filter(Invoker.app_id == appid).filter(Invoker.secret_key == secret_key)\
            .filter(Invoker.active==1).first()
        if invoker:
            # token = create_access_token({'appid': appid, 'nick_name': invoker.nick_name})
            token = create_access_token(appid)
            msg = {
                'success': True,
                'data': {'access_token': token},
                'message': '成功'
            }
            return msg

    except Exception as e:
        logger.exception(e)
    msg = {
        'success': False,
        'data': {},
        'message': '非法请求'
    }
    return msg
