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
from .constants import TokenInteraction

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



# @router.get("/get_profile_photo")
# async def get_photo(filename: str = Form(...)):
    # try:
    #     file_path = Path("uploads/photos/profile_picture") / filename

    #     # Use imghdr to determine the image type
    #     image_type = imghdr.what(file_path)
    #     if not image_type:
    #         return Response(status_code=415, content="Unsupported Media Type")

    #     with open(file_path, "rb") as f:
    #         photo_data = f.read()

    #     return Response(content=photo_data, media_type=f"image/{image_type}")
    # except FileNotFoundError:
    #     return Response(status_code=404, content="Photo not found")
    # except Exception as e:
    #     return Response(status_code=500, content=f"Error retrieving photo: {e}")


@router.get("/student/{username}", response_model=StudentResponseModel)
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




@router.put("/change-password",status_code=status.HTTP_202_ACCEPTED)
async def change_passowrd(request:Request,username :str = Depends(TokenInteraction.get_current_user),db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn)):
    request_body = await request.json()
    password = request_body["password"]



        ## if changed return Success with 202
        ## else return Failure with 422
    with db_conn.cursor() as cursor:
        try:
            query = "UDPATE user SET password = %s WHERE username = %s"
            cursor.execute(query,(PasswordInteraction.hash_password(password),username))
            db_conn.commit()
            release_conn(db_conn)
            return {"message":"Success"}
        except Exception as e:
            try:
                release_conn(db_conn)
            except:
                pass
            return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail = e)
        



############################################## Channel Management
        
@router.post("/join-channel",status_code=status.HTTP_200_OK)
async def join_channel(
    request:Request,
    user:str = Depends(TokenInteraction.get_current_user),
    db_conn:DatabaseConnection.PooledMySQLConnection = Depends(get_conn)
):
    request_body = await request.json()

    channel_id = request_body["channel_id"]
    code = request_body["code"]


    try:

    ## Return Error if code is not found  Error -> 401 UNAuthorized
        with db_conn.cursor(dictionary = True) as cursor:

            query = "SELECT code FROM channel WHERE id = %s"
            cursor.execute(query,(channel_id,))
            result = cursor.fetchone()
            if PasswordInteraction.verify_password(password=code,hashed_password=result['code']):
                query = "INSERT INTO join_channel (studentUsername,channel_id,requestStatus) VALUES (%s,%s,%s)"

                cursor.execute(query,(user,channel_id,True))

                db_conn.commit()
                release_conn(db_conn)
                return {"Message":"Success"}
            else:
                try:
                    release_conn(db_conn)
                except:
                    pass
                return HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,detail = "Wrong Code"
                )
    except Exception as e:
        release_conn(db_conn)
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,detail = e
        )



@router.post("/disjoin-channel",status_code=status.HTTP_200_OK)
async def disjoin_channel(
    request:Request,
    user:str = Depends(TokenInteraction.get_current_user),
    db_conn:DatabaseConnection.PooledMySQLConnection = Depends(get_conn)
):
    request_body = await request.json()

    channel_id = request_body["channel_id"]


    try:

    ## Return Error if code is not found  Error -> 401 UNAuthorized
        with db_conn.cursor(dictionary = True) as cursor:
                query = "DELETE FROM join_channel WHERE studentUsername = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                db_conn.commit()
                release_conn(db_conn)
                return {"Message":"Success"}
    except Exception as e:
        release_conn(db_conn)
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,detail = e
        )





@router.post("/solve-quiz")
async def solve_quiz(request:Request,username :str = Depends(TokenInteraction.get_current_user),db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn)):
    request_body = await request.json()

    channel_id = request_body["channel_id"]
    quiz_id = request_body["content_id"]
    grade = request_body["grade"]


    ## return unauthorized response if solved twice 
    ## return unauthorized response if the student is not in the channel
    with db_conn.cursor(dictionary = True) as cursor:

        ## first check if the user is joined channel
        query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"

        cursor.execute(query,(username,channel_id))

        result = cursor.fetchall()

        if result:

            ## check if solved ?

            query = "SELECT * FROM solve_quiz WHERE studentUsername = %s AND content_id =%s"
            cursor.execute(query,(username,quiz_id))
            result = cursor.fetchall()
            if result:
                release_conn(db_conn)
                return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "Already solved")
            
            query = "INSERT INTO solve_quiz (studentUsername,content_id,grade) VALUES (%s,%s,%s)"
            cursor.execute(query,(username,quiz_id,grade))
            db_conn.commit()
            release_conn(db_conn)
            return {"message":"Success"}
        else:
            release_conn(db_conn)
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "Join Channel First")

        




@router.post("/solve-problem-set")
async def solve_problemset(request:Request,username :str = Depends(TokenInteraction.get_current_user),db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn)):
    request_body = await request.json()

    channel_id = request_body["channel_id"]
    problemSet_id = request_body["content_id"]
    grade = request_body["grade"]


    ## return unauthorized response if solved twice 
    ## return unauthorized response if the student is not in the channel
    with db_conn.cursor(dictionary = True) as cursor:

        ## first check if the user is joined channel
        query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
        cursor.execute(query,(username,channel_id))
        result = cursor.fetchall()

        if result:
            ## check if solved ?
            query = "SELECT * FROM solve_problem_set WHERE studentUsername = %s AND content_id =%s"
            cursor.execute(query,(username,problemSet_id))
            result = cursor.fetchall()
            if result:
                ## if solved we remove the last one and solve it again
                query = "DELETE FROM solve_problem_set WHERE studentUsername = %s AND content_id = %s"
                cursor.execute(query,(username,problemSet_id))
                db_conn.commit()
                release_conn(db_conn)
            
            query = "INSERT INTO solve_problem_set (studentUsername,content_id,grade) VALUES (%s,%s,%s)"
            cursor.execute(query,(username,problemSet_id,grade))
            db_conn.commit()
            release_conn(db_conn)
            return {"message":"Success"}
        else:
            release_conn(db_conn)
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "Join Channel First")

        




@router.post("/solve-homework")
async def solve_homework(request:Request,username :str = Depends(TokenInteraction.get_current_user),db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn)):
    request_body = await request.json()

    channel_id = request_body["channel_id"]
    HW_id = request_body["content_id"]


    ## return unauthorized response if solved twice 
    ## return unauthorized response if the student is not in the channel
    with db_conn.cursor(dictionary = True) as cursor:

        ## first check if the user is joined channel
        query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
        cursor.execute(query,(username,channel_id))
        result = cursor.fetchall()

        if result:
            ## check if solved ?
            query = "SELECT * FROM solve_problem_set WHERE studentUsername = %s AND channel_id =%s"
            cursor.execute(query,(username,channel_id))
            result = cursor.fetchall()
            if result:
                db_conn.commit()
                release_conn(db_conn)
                return {"message":"Success"}
            
            query = "INSERT INTO solve_hw (studentUsername,HW_id) VALUES (%s,%s,%s)"
            cursor.execute(query,(username,HW_id))

            db_conn.commit()
            release_conn(db_conn)
            return {"message":"Success"}

        else:
            release_conn(db_conn)
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "Join Channel First")

        