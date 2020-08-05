#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 15:12
# @File    : session.py

from app.core.config import settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping= True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

