#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : phant0ms
# @Time    : 2020/8/11 10:08
# @File    : security.py


from datetime import datetime, timedelta
from typing import Any, Union,Optional
from app.schemas.token import TokenPayload

from jose import jwt
from passlib.context import CryptContext
from pydantic import ValidationError
from fastapi import HTTPException, status, Header

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


@DeprecationWarning
def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[ALGORITHM]
        )
        print(payload)
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        return False

    return True

    # user = crud.user.get(db, id=token_data.sub)
    # if not user:
    #     raise HTTPException(status_code=404, detail="User not found")
    # return user


def authenticate(access_token: Optional[str] = Header(None)):
    print(access_token)
    if not access_token or access_token=='':
        return False
    try:
        payload = jwt.decode(
            access_token, settings.SECRET_KEY, algorithms=[ALGORITHM]
        )
        print(payload)
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        return False

    return True






if __name__ == '__main__':
    d = create_access_token({'auth': 'admin'})
    print(d)
    b = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTcxMjkyODMsInN1YiI6InsnYXV0aCc6ICdhZG1pbid9In0.sSawiR_vOf1iNL-wmahLTNVRuRjEA_Y-n0dwpv4Dmg4'
    ad = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTc4MTk3ODMsInN1YiI6InsnYXV0aCc6ICdhZG1pbid9In0.fcUMTTatJPkL-I4aNiRtsBAjHhZShZM8WzVhwkluV2U'
    a = verify_token(b)
    print(a)
