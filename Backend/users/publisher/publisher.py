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
    Request,
)
from typing import Annotated
from .pubSchemas import UserModel, PublisherResponseModel, ChannelCreatedModel
from pathlib import Path
from datetime import date, datetime
import imghdr
import aiofiles
from .constants import TokenInteraction

router = APIRouter(prefix="/pub", tags=["Publishers"])


@router.post(
    "/pub-sign-up/",
    status_code=status.HTTP_201_CREATED,
)
async def sign_up(
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
            release_conn(db_conn)
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


#######################################################################
#        Publisher Interaction With channel
#######################################################################


@router.post("/create-channel", status_code=status.HTTP_201_CREATED)
def create_channel(
    username: str = Form(...),
    channel_id: int = Form(...),
    type: str = Form(...),
    description: str = Form(...),
    title: str = Form(...),
    code: str = Form(...),
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user: str = Depends(
        TokenInteraction.get_current_user,
    ),
):
    if user != username:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Login First"
        )
    with db_conn.cursor(dictionary=True) as cursor:
        query = "SELECT * from publisher Where username =%s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if not result:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Login First"
            )
        else:
            try:
                type = 0 if type.lower().strip() == "public" else 1
                query = "INSERT INTO channel (id, type, is_active, description,creationdate, rating, title, code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                print(query)
                ## code must be automatically generated
                cursor.execute(
                    query,
                    (
                        channel_id,
                        type,
                        True,
                        description,
                        date.today(),
                        5,
                        title,
                        PasswordInteraction.hash_password(code),
                    ),
                )
                print(cursor)
                query = "INSERT INTO publisher_manage_channel (publisher_username,channel_id,state) VALUES(%s,%s,%s)"
                cursor.execute(query, (username, channel_id, False))
                db_conn.commit()
                release_conn(db_conn)
                model = ChannelCreatedModel(
                    username=username,
                    type=type,
                    channel_id=channel_id,
                    is_active=True,
                    description=description,
                    rating=5,
                    title=title,
                )
                return model
            except Exception as e:
                return HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Code Error",
                )


@router.post("/join-channel")
def join_channel(
    username: str = Form(...),
    channel_id: int = Form(...),
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user: str = Depends(
        TokenInteraction.get_current_user,
    ),
):
    ## first we check for authentication

    if user != username:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Login First"
        )

    ## second we check for a channel exists
    with db_conn.cursor() as cursor:
        query = "SELECT * FROM Channel Where id = %s"
        cursor.execute(query, (channel_id,))
        result = cursor.fetchone()

        if not result:
            ## means that the channel not exists
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Channel not found"
            )

        ## check if it is already operates the channel
        query = "SELECT * FROM publisher_manage_channel WHERE channel_id = %s AND publisher_username = %s"
        cursor.execute(query, (channel_id, user))
        result = cursor.fetchone()
        if result:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_204_NO_CONTENT,
                detail="Already operates the channel",
            )
            return

        query = "INSERT INTO publisher_manage_channel(publisher_username,channel_id) VALUES(%s,%s,%s)"
        cursor.execute(query, (username, channel_id, 0))
        db_conn.commit()
        release_conn(db_conn)
        return HTTPException(
            status_code=status.HTTP_202_ACCEPTED,
            detail=f"Publisher : {username} Joined Channel : {channel_id}",
        )
        return
