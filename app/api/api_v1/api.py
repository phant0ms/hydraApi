#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 15:01
# @File    : api.py

from fastapi import APIRouter
from app.api.api_v1.endpoint import hydra
from app.api.api_v1.endpoint import login
api_router = APIRouter()
api_router.include_router(hydra.router, tags=['任务操作'])
api_router.include_router(login.router, tags=['认证'])
