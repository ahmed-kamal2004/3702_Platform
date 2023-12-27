import schema
from schema import TokenModel, UserModel, StudentModel
from pydantic import Field
from datetime import datetime
from fastapi import UploadFile




### Publisher Response Models


class StudentResponseModel(StudentModel):
    class Config:
        from_attribute = True
        populate_by_name = True
