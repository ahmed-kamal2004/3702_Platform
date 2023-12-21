import schema
from schema import TokenModel, UserModel, PublisherModel
from pydantic import Field
from datetime import datetime
from fastapi import UploadFile


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
    is_active: bool = Field(exclude=True, title="is_active")
    password: str = Field(exclude=True, title="password")
    DOB: datetime = Field(exclude=True, title="DOB")
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
