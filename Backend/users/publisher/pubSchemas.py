from uuid import uuid4
import schema
from schema import TokenModel, UserModel, PublisherModel, BaseModel
from pydantic import Field
from datetime import datetime
from fastapi import UploadFile, Form


### TOKEN


class PublisherTokenDataModel(TokenModel):
    username: str

    class Config:
        from_attribute = True
        populate_by_name = True


### Publisher Response Models


class PublisherResponseModel(PublisherModel):
    job: str
    linkedin_url: str
    photo: str

    class Config:
        from_attribute = True
        populate_by_name = True


class PublisherSignUpModel(PublisherModel):
    photo: UploadFile
    is_active: bool = Field(exclude=True, title="is_active")

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
