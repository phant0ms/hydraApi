#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/4 15:06
# @File    : tasks.py

from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, DateTime, Text


class Tasks(Base):
    __tablename__ = 'pvs_tasks'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    task_id = Column(String, index=True, unique=True, nullable=False, comment="任务 id")
    vul_no = Column(Integer, default=0, comment="发现的漏洞数量")
    creator = Column(String, nullable=False, comment="任务创建者")
    status = Column(Integer, default=1, comment="任务状态, 1:新建, 2: 运行中, 3:完成,4:停止,5 删除")
    create_time = Column(DateTime, comment="任务创建时间")
    end_time = Column(DateTime, comment="任务结束时间")
    targets = Column(Text, comment="任务目标")
