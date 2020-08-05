#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 15:01
# @File    : api.py

from fastapi import APIRouter
from app.api.api_v1.endpoint import hydra

api_router = APIRouter()
api_router.include_router(hydra.router,)

