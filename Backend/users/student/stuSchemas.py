import schema
from schema import TokenModel, UserModel, StudentModel
from pydantic import Field
from datetime import datetime
from fastapi import UploadFile


### TOKEN


class StudentTokenDataModel(TokenModel):
    username: str

    class Config:
        from_attribute = True
        populate_by_name = True


### Publisher Response Models


class StudentResponseModel(StudentModel):
    class Config:
        from_attribute = True
        populate_by_name = True
