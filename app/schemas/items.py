#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/5 14:29
# @File    : items.py

from pydantic import BaseModel
from typing import Any, Dict


class Response(BaseModel):
    success: bool
    data: Dict[Any, Any] = None
    message: str


class Targets(BaseModel):
    targets: str


class Login(BaseModel):
    apiKey: str
    secretKey: str
