from fastapi import APIRouter, Depends, Request, HTTPException, status
import DatabaseConnection
from DatabaseConnection import get_conn, release_conn
from typing import List
from schema import ChannelBaseModel, PublisherOperatorModel
from pydantic import TypeAdapter
from users.publisher.constants import TokenInteraction
import datetime

router = APIRouter(prefix="/chn", tags=["Channels"])


### Get Publishers


### Get Quizes

### GEt Grades For a Specific Quiz

### GEt Posts

##3


## First Get All Active Channels
@router.get("/get_channels", response_model=List[ChannelBaseModel])
async def get_all_active_channels(
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
):
    with db_conn.cursor(dictionary=True) as cursor:
        query = "SELECT id,type,description,creationdate,rating,title FROM channel where is_active=1;"
        cursor.execute(query)
        result = cursor.fetchall()

        print(result)
        release_conn(db_conn)
        ta = TypeAdapter(List[ChannelBaseModel])
        return ta.validate_python(result)


## Get Channel By id
@router.get(
    "/channel/{channel_id}",
    response_model=List[ChannelBaseModel],
    status_code=status.HTTP_200_OK,
)
async def get_channel_by_id(
    channel_id: int,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
):
    with db_conn.cursor(dictionary=True) as cursor:
        query = "SELECT id,type,description,creationdate,rating,title FROM channel where is_active=1;"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        ta = TypeAdapter(List[ChannelBaseModel])
        release_conn(db_conn)
        return ta.validate_python(result)


## Get Operators of a Channel



@router.get(
    "/get_publishers/",
    status_code=status.HTTP_200_OK,
    response_model=List[PublisherOperatorModel],
)
async def get_publishers_of_channel(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)
):
    request_body = await request.json()

    channel_id = request_body["channel_id"]

    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        

        query = """SELECT user.nickname, user.username
                FROM publisher_manage_channel
                LEFT JOIN publisher ON publisher_manage_channel.publisher_username = publisher.username
                LEFT JOIN user ON publisher.username = user.username
                WHERE publisher_manage_channel.channel_id =%s """
        cursor.execute(query, (channel_id,))
        result = cursor.fetchall()

        ta = TypeAdapter(List[PublisherOperatorModel])
        release_conn(db_conn)
        return ta.validate_python(result)



## to get all articles in articles list
@router.get('/content/articles')
async def get_artciles(
     request:Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)   
):
    

    request_body = await request.json()

    channel_id = request_body["channel_id"]

    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        
        query = """SELECT content.id,content.text,content.title,content.publishdate,
        content.publisherUsername,article.video,article.photo
        FROM content,article WHERE article.content_id  = content.id AND content.channel_id = %s ;
"""
        cursor.execute(query, (channel_id,))
        result = cursor.fetchall()
        return result


## to get all articles in articles list
@router.get('/content/article/{id}')
async def get_artcile(
    id:int,
    request:Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)  
):

        

    request_body = await request.json()

    channel_id = request_body["channel_id"]

    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        
        query = """SELECT content.id,content.text,content.title,content.publishdate,
        content.publisherUsername,article.video,article.photo
        FROM content,article WHERE article.content_id  = content.id AND content.channel_id = %s AND content.id = %s ;
"""
        cursor.execute(query, (channel_id,id))
        result = cursor.fetchall()
        return result


    pass


## to get all articles in articles list
@router.get('/content/questions',status_code=status.HTTP_200_OK)
async def get_questions(
    request:Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)  
):
    request_body = await request.json()

    channel_id = request_body["channel_id"]

    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        query = "SELECT id FROM question WHERE channel_id = %s"
        cursor.execute(query,(channel_id))
        result = cursor.fetchall()
        release_conn(db_conn)
        return result


## to get all articles in articles list
@router.get('/content/question/{id}',status_code=status.HTTP_200_OK)
async def get_question(
    id:int,
    request:Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)  
):
    request_body = await request.json()

    channel_id = request_body["channel_id"]

    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        query = "SELECT id FROM question WHERE channel_id = %s WHERE id = %s"
        cursor.execute(query,(channel_id,id))
        result = cursor.fetchall()

        query = "SELECT choice FROM question_choices WHERE question_id = %s"
        cursor.execute(query,(id))
        result_choice = cursor.fetchall()
        return {"Question":result,"Question_Choices":result_choice}


    pass


## to get all articles in articles list
@router.get('/content/homeworks',status_code=status.HTTP_200_OK)
async def get_homeworks(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)
):
        
    request_body = await request.json()

    channel_id = request_body["channel_id"]


        
    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        

        current_date = datetime.datetime.now()
        query = "SELECT content.id,content.text,content.title,content.publisherUsername FROM content INNER JOIN homework ON content.id = homework.content_id WHERE content.publishdate < %s AND content.channel_id = %s "
        cursor.execute(query,(current_date,channel_id))
        result = cursor.fetchall()
        release_conn(db_conn)
        return result


@router.get('/content/homework/{id}',status_code=status.HTTP_200_OK)
async def get_homework(
    id:int,
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)
):
        
    request_body = await request.json()

    channel_id = request_body["channel_id"]


        
    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        

        current_date = datetime.datetime.now()
        query = "SELECT content.id,content.text,content.title,content.publisherUsername FROM content INNER JOIN homework ON content.id = homework.content_id WHERE content.publishdate < %s AND content.id = %s AND content.channel_id = %s"
        cursor.execute(query,(current_date,id,channel_id))
        result = cursor.fetchall()


        query = "SELECT question_id from hw_question WHERE HW_id = %s"
        cursor.execute(query,(id,))
        result_id = cursor.fetchall()
        release_conn(db_conn)
        return {"Homework":result,"Questions":result_id}


@router.get('/content/problemsets',status_code=status.HTTP_200_OK)
async def get_problemsets(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)
):
        
    request_body = await request.json()

    channel_id = request_body["channel_id"]


        
    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        

        current_date = datetime.datetime.now()
        query = """
                    SELECT content.id,
                        content.text,
                        content.title,
                        content.publisherUsername
                    FROM content
                            INNER JOIN problemset ON content.id = problemset.content_id
                    WHERE content.publishdate < %s
                            AND problemset.deadline > %s,
                            AND content.channel_id = %s;
"""
        cursor.execute(query,(current_date,current_date,channel_id))
        result = cursor.fetchall()
        release_conn(db_conn)
        return result
    

@router.get('/content/problemset/{id}',status_code=status.HTTP_200_OK)
async def get_problemset(
    id:int,
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)
):
        
    request_body = await request.json()

    channel_id = request_body["channel_id"]


        
    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        

        current_date = datetime.datetime.now()
        query = """
                    SELECT content.id,
                        content.text,
                        content.title,
                        content.publisherUsername
                    FROM content
                            INNER JOIN problemset ON content.id = problemset.content_id
                    WHERE content.publishdate < %s
                            AND problemset.deadline > %s
                            AND content.id = %s,
                            AND content.channel_id = %s;
"""
        cursor.execute(query,(current_date,current_date,id,channel_id))
        result = cursor.fetchall()


        query = "SELECT question_id from ps_question WHERE PS_id = %s"
        cursor.execute(query,(id,))
        result_id = cursor.fetchall()
        release_conn(db_conn)
        return {"Problem Set":result,"Questions":result_id}
    

@router.get('/content/quizes',status_code=status.HTTP_200_OK)
async def get_quizes(
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)
):
        
    request_body = await request.json()

    channel_id = request_body["channel_id"]


        
    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        

        current_date = datetime.datetime.now()
        query = """
                    SELECT content.id,
                        content.text,
                        content.title,
                        content.publisherUsername
                    FROM content
                            INNER JOIN quiz ON content.id = quiz.content_id
                    WHERE content.publishdate < %s 
                            AND quiz.starting_date < %s 
                            AND quiz.duration > %s,
                            AND content.channel_id = %s;
"""
        cursor.execute(query,(current_date,current_date,current_date,channel_id))
        result = cursor.fetchall()
        return result
    
@router.get('/content/quiz/{id}',status_code=status.HTTP_200_OK)
async def get_quiz(
    id:int,
    request: Request,
    db_conn: DatabaseConnection.PooledMySQLConnection = Depends(get_conn),
    user :str = Depends(TokenInteraction.get_current_user)
):
        
    request_body = await request.json()

    channel_id = request_body["channel_id"]


        
    ## returns List of PublisherOperators with HTTP status code ok 200
    ## if the user is not part of the channel and the channel is private > Error is 401 unauthorized

    with db_conn.cursor(dictionary=True) as cursor:
        ## first check if the channel is private and the user is part of it
        query = "SELECT * FROM channel WHERE id = %s AND type = %s"
        cursor.execute(query,(channel_id,"private"))
        result = cursor.fetchone()
        if result:
            ## Second check if the user is in the channel as operator or student
            query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
            cursor.execute(query,(user,channel_id))
            result = cursor.fetchone()
            if not result:
                query = "SELECT * FROM publisher_manage_channel WHERE publisher_username = %s AND channel_id = %s"
                cursor.execute(query,(user,channel_id))
                result = cursor.fetchone()
                if not result:
                    query = "SELECT * FROM join_channel WHERE studentUsername = %s AND channel_id = %s AND requestStatus = True"
                    cursor.execute(query,(user,channel_id))
                    result = cursor.fetchone()
                    if not result:
                        release_conn(db_conn)
                        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "This is Private Channel")
        

        current_date = datetime.datetime.now()
        query = """
                    SELECT content.id,
                        content.text,
                        content.title,
                        content.publisherUsername
                    FROM content
                            INNER JOIN quiz ON content.id = quiz.content_id
                    WHERE content.publishdate < %s 
                            AND quiz.starting_date < %s 
                            AND quiz.duration > %s
                            AND content.id = %s
                            AND content.channel_id = %s;
"""
        cursor.execute(query,(current_date,current_date,current_date,id,channel_id))
        result = cursor.fetchall()


        
        query = "SELECT question_id from quiz_question WHERE quiz_id = %s"
        cursor.execute(query,(id,))
        result_id = cursor.fetchall()
        release_conn(db_conn)
        return {"Quiz":result,"Questions":result_id}
    