from uuid import uuid4
import schema
from schema import TokenModel, UserModel, BaseModel
from pydantic import Field, EmailStr
from datetime import datetime
from fastapi import UploadFile, Form


### TOKEN


class PublisherTokenDataModel(TokenModel):
    username: str

    class Config:
        from_attribute = True
        populate_by_name = True


### Publisher Response Models


class PublisherResponseModel(BaseModel):
    photo: str
    job: str
    linked_url: str
    username: str
    email: EmailStr
    nickname: str
    phonenumber: str

    class Config:
        from_attribute = True
        populate_by_name = True


class ChannelCreatedModel(BaseModel):
    username: str
    channel_id: int
    type: int
    description: str
    title: str
    is_active: bool
    rating: int

    class Config:
        from_attribute = True
        populate_by_name = True
