from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
)
from pubSchemas import (
    UserModel,
    PublisherResponseModel_Logged,
    PublisherResponseModel_NotLogged,
)

router = APIRouter(prefix="/pub", tags=["Publishers"])


@router.get("/{publisher_username}")
def get_publisher(publisher_username: str):  ## still need DB connection
    pass
