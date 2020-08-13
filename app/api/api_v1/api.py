#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 15:01
# @File    : api.py

from fastapi import APIRouter
from app.api.api_v1.endpoint import hydra
from app.api.api_v1.endpoint import login
from app.api.api_v1.endpoint import docs
api_router = APIRouter()
api_router.include_router(hydra.router, tags=['任务操作'])
api_router.include_router(login.router, tags=['认证'])
api_router.include_router(docs.router, tags=['Swagger'])
