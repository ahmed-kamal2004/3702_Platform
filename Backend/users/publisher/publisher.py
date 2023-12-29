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
from typing import Annotated, List
from .pubSchemas import  PublisherResponseModel, ChannelCreatedModel
from pathlib import Path
from datetime import date, datetime
import imghdr
from .constants import TokenInteraction
from pydantic import TypeAdapter

router = APIRouter(prefix="/pub", tags=["Publishers"])


## NOTES


## NEED to check if the channel already exists in make channel list
###################################################################
@router.post("/pub-sign-up/", status_code=status.HTTP_201_CREATED)
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
    linked_url = request_body["linked_url"]
    job = request_body["job"]
    photo = request_body["photo"]

    with db_conn.cursor() as cursor:
        ## nedd validation for data

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
            query = "INSERT INTO publisher (username,linked_url,job) VALUES (%s,%s,%s)"

            cursor.execute(query, (username, linked_url, job))

            db_conn.commit()
            release_conn(db_conn)
        except Exception as e:
            release_conn(db_conn)
            print(e)
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e)
        else:
            release_conn(db_conn)
            return {"detail": f"Succes username of {username} is created"}


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
        


## Get All Active Publishers Code
@router.get(
    "/publishers",
    status_code=status.HTTP_200_OK,
    response_model=List[PublisherResponseModel],
)
def get_publishers(db_conn: DatabaseConnection.MySQLConnectionPool = Depends(get_conn)):
    with db_conn.cursor(dictionary=True) as cursor:
        query = "SELECT user.username,email,photo,DOB,nickname,phonenumber,linked_url,job From user,publisher where user.is_active = 1;"
        cursor.execute(query)
        result = cursor.fetchall()
        ta = TypeAdapter(List[PublisherResponseModel])
        release_conn(db_conn)
        return ta.validate_python(result)


## Get Specific Publisher Code
@router.get("/publisher/{username}", response_model=PublisherResponseModel)
def get_publisher(
    username: str, db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn)
):
    with db_conn.cursor(dictionary=True) as cursor:
        query = "SELECT user.username,email,photo,DOB,nickname,phonenumber,linked_url,job From user,publisher WHERE publisher.username = user.username AND publisher.username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        release_conn(db_conn)
        if result:
            output = PublisherResponseModel(
                username=result["username"],
                email=result["email"],
                nickname=result["nickname"],
                phonenumber=result["phonenumber"],
                job=result["job"],
                linked_url=result["linked_url"],
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
async def create_channel(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user: str = Depends(
        TokenInteraction.get_current_user,
    ),
):
    request_body = await request.json()

    username = request_body["username"]
    channel_id = request_body["channel_id"]
    type = request_body["type"]
    description = request_body["description"]
    title = request_body["title"]
    code = request_body["code"]

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

        query = "SELECT * FROM Channel WHERE id =%s"
        cursor.execute(query, (channel_id,))
        result = cursor.fetchone()
        if result:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Channel already exists"
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
                query = "INSERT INTO publisher_manage_channel (publisher_username,channel_id) VALUES(%s,%s)"
                cursor.execute(query, (username, channel_id))
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
                release_conn(db_conn)
                return HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=e,
                )


@router.post("/add-publisher-to-channel")
async def join_channel(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user: str = Depends(
        TokenInteraction.get_current_user,
    ),
):
    ## first we check for authentication

    request_body = await request.json()

    username = request_body["username"]
    channel_id = request_body["channel_id"]

    ## second we check for a channel exists
    try:
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
            ## check that the main user operates the channel
            query = "SELECT * FROM publisher_manage_channel WHERE channel_id = %s AND publisher_username = %s"
            cursor.execute(query, (channel_id, user))
            result = cursor.fetchall()
            if not result:
                release_conn(db_conn)
                return HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Main user : {user} Doesn't Operate the channel",
                )
            ## check if the added user  already operates the channel
            query = "SELECT * FROM publisher_manage_channel WHERE channel_id = %s AND publisher_username = %s"
            cursor.execute(query, (channel_id, username))
            result = cursor.fetchall()
            if result:
                release_conn(db_conn)
                return HTTPException(
                    status_code=status.HTTP_204_NO_CONTENT,
                    detail="Already operates the channel",
                )
            query = "INSERT INTO publisher_manage_channel(publisher_username,channel_id) VALUES(%s,%s)"
            cursor.execute(query, (username, channel_id))
            db_conn.commit()
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_202_ACCEPTED,
                detail=f"Publisher : {username} Joined Channel : {channel_id}",
            )

    except Exception as e:
        release_conn(db_conn)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Input"
        )


@router.post("/content/create-article", status_code=status.HTTP_201_CREATED)
async def create_article(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user: str = Depends(TokenInteraction.get_current_user),
):
    request_body = await request.json()

    text = request_body["text"]
    title = request_body["title"]
    channel_id = int(request_body["channel_id"])
    video = request_body["video"]
    photo = request_body["photo"]
    publishedate = datetime.now()

    with db_conn.cursor(dictionary=True) as cursor:
        ## check if the user operates the channel
        query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s and channel_id = %s;"
        cursor.execute(query, (user, channel_id))
        result = cursor.fetchone()

        if not result:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"{user} Doesn't Operate Channel With ID {channel_id}",
            )

        query = "INSERT INTO content (text,title,publishdate,channel_id,publisherusername) VALUES(%s,%s,%s,%s,%s);"
        cursor.execute(
            query,
            (text, title, publishedate, channel_id, user),
        )
        db_conn.commit()
        query = "SELECT LAST_INSERT_ID() as Id"
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
        id = result['Id']

        query = "INSERT INTO article (content_id,video,photo) VALUES(%s,%s,%s)"
        cursor.execute(query, (id, video, photo))
        db_conn.commit()
        release_conn(db_conn)
        return {"message":"Success"}

@router.post("/content/create-question",status_code=status.HTTP_201_CREATED)
async def create_question(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user: str = Depends(TokenInteraction.get_current_user)
):
    request_body = await request.json()

    text = request_body["text"]
    answer = request_body["answer"]
    channel_id = request_body["channel_id"]
    choices = request_body["choices"]



    with db_conn.cursor(dictionary=True) as cursor:
        ## check if the user operates the channel
        query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s and channel_id = %s;"
        cursor.execute(query, (user, channel_id))
        result = cursor.fetchone()

        if not result:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"{user} Doesn't Operate Channel With ID {channel_id}",
            )

        ## create question
        query = "INSERT INTO question(text,answer,channel_id) VALUES(%s,%s,%s)"
        cursor.execute(query,(text,answer,channel_id))

        cursor.execute("select LAST_INSERT_ID() as Id")
        last_question_id = cursor.fetchone()
        last_question_id = last_question_id['Id']

        query = "INSERT INTO question_choices(question_id,choice) VALUES (%s,%s)"

        for choice in choices:
            cursor.execute(query,(last_question_id,choice))
        
        db_conn.commit()
        release_conn(db_conn)
        return {"message":"Success","Question_id":last_question_id}






@router.post("/content/create-quiz",status_code=status.HTTP_201_CREATED)
async def create_quiz(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user: str = Depends(TokenInteraction.get_current_user)
):
    request_body = await request.json()

    text = request_body["text"]
    title = request_body["title"]
    channel_id = request_body["channel_id"]
    questions = request_body["questions"]
    startDate = request_body["start_date"]
    endDate = request_body["end_date"]
    publishDate = datetime.now()


    with db_conn.cursor(dictionary=True) as cursor:
        ## check if the user operates the channel
        query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s and channel_id = %s;"
        cursor.execute(query, (user, channel_id))
        result = cursor.fetchone()

        if not result:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"{user} Doesn't Operate Channel With ID {channel_id}",
            )

        ## create quiz
        query = "INSERT INTO content(text,title,publishDate,channel_id,publisherUsername) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query,(text,title,publishDate,channel_id,user))
        cursor.execute("SELECT LAST_INSERT_ID() as Id")
        last_inserted_id_content = cursor.fetchone()
        last_inserted_id_content = last_inserted_id_content['Id']

        query = "INSERT INTO quiz(content_id,duration,starting_date) VALUES(%s,%s,%s)"
        cursor.execute(query,(last_inserted_id_content,endDate,startDate))

        query = "INSERT INTO quiz_question(question_id,quiz_id) VALUES (%s,%s)"

        for choice in questions:
            cursor.execute(query,(choice,last_inserted_id_content))
        
        db_conn.commit()
        release_conn(db_conn)
        return {"message":"Success","Quiz_id":last_inserted_id_content}








@router.post("/content/create-problemSet",status_code=status.HTTP_201_CREATED)
async def create_problem_set(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user: str = Depends(TokenInteraction.get_current_user)
):
    request_body = await request.json()

    text = request_body["text"]
    title = request_body["title"]
    channel_id = request_body["channel_id"]
    questions = request_body["questions"]
    endDate = request_body["deadline"]
    publishDate = datetime.now()


    with db_conn.cursor(dictionary=True) as cursor:
        ## check if the user operates the channel
        query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s and channel_id = %s;"
        cursor.execute(query, (user, channel_id))
        result = cursor.fetchone()

        if not result:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"{user} Doesn't Operate Channel With ID {channel_id}",
            )

        ## create quiz
        query = "INSERT INTO content(text,title,publishDate,channel_id,publisherUsername) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query,(text,title,publishDate,channel_id,user))
        cursor.execute("SELECT LAST_INSERT_ID() as Id")
        last_inserted_id_content = cursor.fetchone()
        last_inserted_id_content = last_inserted_id_content['Id']

        query = "INSERT INTO problemset(content_id,deadline) VALUES(%s,%s)"
        cursor.execute(query,(last_inserted_id_content,endDate))

        query = "INSERT INTO ps_question(question_id,PS_id) VALUES (%s,%s)"

        for choice in questions:
            cursor.execute(query,(choice,last_inserted_id_content))
        
        db_conn.commit()
        release_conn(db_conn)
        return {"message":"Success","Problem Set_id":last_inserted_id_content}











@router.post("/content/create-homework",status_code=status.HTTP_201_CREATED)
async def create_quiz(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user: str = Depends(TokenInteraction.get_current_user)
):
    request_body = await request.json()

    text = request_body["text"]
    title = request_body["title"]
    channel_id = request_body["channel_id"]
    questions = request_body["questions"]
    publishDate = datetime.now()


    with db_conn.cursor(dictionary=True) as cursor:
        ## check if the user operates the channel
        query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s and channel_id = %s;"
        cursor.execute(query, (user, channel_id))
        result = cursor.fetchone()

        if not result:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"{user} Doesn't Operate Channel With ID {channel_id}",
            )

        ## create quiz
        query = "INSERT INTO content(text,title,publishDate,channel_id,publisherUsername) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query,(text,title,publishDate,channel_id,user))
        cursor.execute("SELECT LAST_INSERT_ID() as Id")
        last_inserted_id_content = cursor.fetchone()
        last_inserted_id_content = last_inserted_id_content['Id']

        query = "INSERT INTO homework(content_id) VALUES(%s)"
        cursor.execute(query,(last_inserted_id_content,))

        query = "INSERT INTO hw_question(question_id,HW_id) VALUES (%s,%s)"

        for choice in questions:
            cursor.execute(query,(choice,last_inserted_id_content))
        
        db_conn.commit()
        release_conn(db_conn)
        return {"message":"Success","Homework_id":last_inserted_id_content}

