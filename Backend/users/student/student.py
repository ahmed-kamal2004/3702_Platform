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
    Request
)
from typing import Annotated
from .stuSchemas import UserModel, StudentResponseModel
from pathlib import Path
from datetime import date, datetime
import imghdr
import aiofiles

router = APIRouter(prefix="/stu", tags=["Students"])


@router.post(
    "/stu-sign-up/",
    status_code=status.HTTP_201_CREATED,
)
async def sign_up(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
):
    request_body = await request.json()

    username = request_body["username"]
    email = request_body["email"]
    password = request_body["password"]
    DOB = request_body["DOB"]
    nickname = request_body["nickname"]
    phonenumber = request_body["phonenumber"]
    photo = request_body["photo"]

    print(username, email, password, DOB, nickname, phonenumber)
    with db_conn.cursor() as cursor:
        ## nedd validation for data

        ## First Check for username
        query = "SELECT * FROM user WHERE username=%s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if result:
            return HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username in Use",
            )

        ## second we check for email
        query = "SELECT * FROM user WHERE email=%s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if result:
            return HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email in Use"
            )
        DOB = datetime.strptime(DOB, "%Y-%m-%d")
        try:
            query = "INSERT INTO user (username,email,password,is_active,photo,DOB,nickname,phonenumber)VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(
                query,
                (
                    username,
                    email,
                    PasswordInteraction.hash_password(password),
                    True,
                    photo,
                    DOB,
                    nickname,
                    phonenumber,
                ),
            )
            query = "INSERT INTO student (username) VALUES (%s)"

            cursor.execute(query, (username,))

            db_conn.commit()
            release_conn(db_conn)
        except Exception as e:
            release_conn(db_conn)
            print(e)
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e)
        else:
            release_conn(db_conn)
            return {"detail": f"Succes username of {username} is created"}



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


@router.get("/studnet/{username}", response_model=StudentResponseModel)
def get_student(
    username: str, db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn)
):
    with db_conn.cursor(dictionary=True) as cursor:
        query = "SELECT user.username,email,photo,DOB,nickname,phonenumber From user,student WHERE student.username = user.username AND student.username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        release_conn(db_conn)
        print(result)
        print(result["username"])
        if result:
            output = StudentResponseModel(
                username=result["username"],
                email=result["email"],
                nickname=result["nickname"],
                phonenumber=result["phonenumber"],
                photo=result["photo"],
            )
            return output
        else:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student Username Not Found",
            )
