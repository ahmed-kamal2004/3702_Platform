import DatabaseConnection
from DatabaseConnection import get_conn, release_conn
from auth.auth import PasswordInteraction
import query
from query import NonQuery, Query
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
    UploadFile,
    File,
    Form,
    Response,
)
from typing import Annotated
from .pubSchemas import UserModel, PublisherResponseModel, PublisherSignUpModel
from pathlib import Path
from datetime import date, datetime
import imghdr
import aiofiles

router = APIRouter(prefix="/pub", tags=["Publishers"])


@router.post(
    "/pub-sign-up/",
    status_code=status.HTTP_201_CREATED,
)
async def create_publisher(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    linked_url: str = Form(...),
    job: str = Form(...),
    DOB: date = Form(...),
    nickname: str = Form(...),
    phonenumber: str = Form(...),
    photo: UploadFile = Form(...),
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
):
    print(username, email, password, DOB, nickname, phonenumber)
    with db_conn.cursor() as cursor:
        ## First Check for username
        query = f"SELECT * FROM user WHERE username=%s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if result:
            return HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username in Use",
            )

        ## second we check for email
        query = f"SELECT * FROM user WHERE email=%s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if result:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email in Use"
            )

        file_path = Path("uploads/photos/profile_picture")  # Adjust base path as needed
        file_path.mkdir(parents=True, exist_ok=True)  # Create directories if needed

        # Generate unique filename with extension
        filename = f"{username}.{photo.filename.split('.')[-1]}"
        print(filename)
        file_path = file_path / filename

        # Read file content and save to disk
        async with aiofiles.open(file_path, "wb") as f:
            while content := await photo.read(1024):  # async read chunk
                await f.write(content)

        try:
            query = "INSERT INTO user (username,email,password,is_active,photo,DOB,nickname,phonenumber)VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(
                query,
                (
                    username,
                    email,
                    PasswordInteraction.hash_password(password),
                    True,
                    str(filename),
                    DOB,
                    nickname,
                    phonenumber,
                ),
            )
            query = "INSERT INTO publisher (username,linked_url,job) VALUES (%s,%s,%s)"

            cursor.execute(query, (username, linked_url, job))

            db_conn.commit()
        except Exception as e:
            release_conn(db_conn)
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e)
        else:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_201_CREATED,
                detail=f"Succes username of {username} is created",
            )


@router.get("/get_profile_photo")
async def get_photo(filename: str = Form(...)):
    try:
        file_path = Path("uploads/photos/profile_picture") / filename

        # Use imghdr to determine the image type
        image_type = imghdr.what(file_path)
        if not image_type:
            return Response(status_code=415, content="Unsupported Media Type")

        with open(file_path, "rb") as f:
            photo_data = f.read()

        return Response(content=photo_data, media_type=f"image/{image_type}")
    except FileNotFoundError:
        return Response(status_code=404, content="Photo not found")
    except Exception as e:
        return Response(status_code=500, content=f"Error retrieving photo: {e}")


@router.get("/publisher/{username}", response_model=PublisherResponseModel)
def get_publisher(
    username: str, db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn)
):
    with db_conn.cursor(dictionary=True) as cursor:
        query = "SELECT user.username,email,photo,DOB,nickname,phonenumber,linked_url,job From user,publisher WHERE publisher.username = user.username AND publisher.username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        release_conn(db_conn)
        print(result)
        print(result["username"])
        if result:
            output = PublisherResponseModel(
                username=result["username"],
                email=result["email"],
                nickname=result["nickname"],
                phonenumber=result["phonenumber"],
                job=result["job"],
                linkedin_url=result["linked_url"],
                photo=result["photo"],
            )
            return output
        else:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Username Not Found"
            )
