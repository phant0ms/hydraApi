#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/7/30 16:59
# @File    : sql_orm.py


import sqlalchemy
print(sqlalchemy.__version__)
from app.utils.common import task_id_generator
from app.utils.common import current_datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:t00r@127.0.0.1:3306/pvs', echo=True)
Base = declarative_base()

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

class Tasks(Base):
    __tablename__ = 'pvs_tasks'
    id = Column(Integer, primary_key=True,)
    task_id = Column(String, index=True, unique=True, comment="任务 id")
    vul_no = Column(Integer, default=0, comment="发现的漏洞数量")
    creator = Column(String,comment="任务创建者" )
    status = Column(Integer, comment="任务状态, 1:新建, 2: 运行中, 3:完成,4:停止,5 删除")
    create_time = Column(DateTime, comment="任务创建时间")
    end_time = Column(DateTime, comment="任务结束时间")

session = sessionmaker(bind=engine)
db= session()

print(Tasks.__tablename__)
task = Tasks(
        id=1,
        task_id= "ddd",
        create_time = current_datetime(),
        creator='admin'
    )

db.add(task)
db.commit()