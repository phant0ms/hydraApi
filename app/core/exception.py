#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/12 09:33
# @File    : exception.py


from fastapi import Request

from fastapi.responses import JSONResponse
from app.core.config import webapp


class Invalid_Token_Exception(Exception):
    def __init__(self, msg: str = ''):
        self.msg = msg


@webapp.exception_handler(Invalid_Token_Exception)
def invalid_token_exception_handler(request: Request, exc: Invalid_Token_Exception):
    if not exc.msg:
        exc.msg = '无效的Access_Token'
    return JSONResponse(
        status_code=200,
        content={
            'success': True,
            'data': {},
            'message': exc.msg
        }
    )
