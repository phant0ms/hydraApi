#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/7/30 16:13
# @File    : module.py


from sql_app.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_passwd = Column(String, )
    is_actived = Column(Boolean, default=True)

    items = relationship("Items", back_populates="owner")


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="items")



if __name__ == '__main__':
    user = Users(id=1, email="email@qq.com", hashed_passwd="haswd passwd", is_actived=True)

    print(user.email)