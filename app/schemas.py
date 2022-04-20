from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

from pydantic.types import conint

class UserCreate(BaseModel):
  email: EmailStr
  password: str

class UserShow(BaseModel):
  id: int
  email: EmailStr
  create_at: datetime
  
  class Config:
    orm_mode = True

class UserLogin(BaseModel):
  email: EmailStr
  password: str

class PostBase(BaseModel):
  title: str
  content: str
  published: bool = True

class PostCreate(PostBase):
  pass

class Post(PostBase):
  id: int
  create_at: datetime
  owner_id: int
  owner: UserShow

  class Config:
    orm_mode = True

class PostOut(BaseModel):
  Post: Post
  votes: int

  class Config:
    orm_mode = True


class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  id: Optional[str] = None


class Vote(BaseModel):
  post_id: int
  dir: conint(le=1)
