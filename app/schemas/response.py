#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/5 14:29
# @File    : response.py

from pydantic import BaseModel
from typing import List, Any


class Response(BaseModel):
    success: bool
    data: List[Any] = []
    message: str

