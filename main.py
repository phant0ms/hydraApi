#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 14:44
# @File    : main.py

import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.api.api_v1.api import api_router
# print(settings.PROJECT_NAME)

webapp = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json", debug = True)
# webapp = FastAPI()

webapp.include_router(api_router, prefix= settings.API_V1_STR)

if __name__ == '__main__':
    uvicorn.run(webapp, host="127.0.0.1", port=8000, log_level='debug')