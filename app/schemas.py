
from datetime import datetime
import email
from typing import Optional,List
from pydantic import BaseModel,EmailStr
from pydantic.types import conint
class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True
    #rating:Optional[int]=None
class PostCreate(PostBase):
    pass


class Userout(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode=True


class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)

#response
class Post(PostBase):
    
    created_at:datetime
    id : int 
    owner_id:int
    owner: Userout
  
    class Config:
        orm_mode = True

class Postout(BaseModel):
    Post:Post
    vote:int
  
    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token (BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Optional[str]=None

