from ...schema import TokenModel, UserModel
from pydantic import Field
from datetime import datetime


### TOKEN


class PublisherTokenDataModel(TokenModel):
    username: str

    class Config:
        from_attribute = True
        populate_by_name = True


### Publisher Response Models


class PublisherResponseModel_Logged(UserModel):
    job: str
    linkedin_url: str
    is_active: str = Field(exclude=True, title="is_active")
    password: str = Field(exclude=True, title="password")


class PublisherResponseModel_NotLogged(UserModel):
    job: str
    linkedin_url: str
    is_active: str = Field(exclude=True, title="is_active")
    password: str = Field(exclude=True, title="password")
    DOB: datetime = Field(exclude=True, title="DOB")
