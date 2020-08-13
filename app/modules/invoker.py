#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/13 10:51
# @File    : invoker.py

from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean


class Invoker(Base):
    '''
    调用方信息
    '''
    __tablename__ = 'pvs_invoker'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    app_id = Column(String, nullable=False, )
    secret_key = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, comment='账号是否启用,1: 启用;0:禁用')
    nick_name = Column(String, nullable=False)