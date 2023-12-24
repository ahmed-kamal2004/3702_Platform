from fastapi import APIRouter, Depends, Request, HTTPException, status
import DatabaseConnection
from DatabaseConnection import get_conn, release_conn
from typing import List
from schema import ChannelBaseModel, PublisherOperatorModel
from pydantic import TypeAdapter

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
        ta = TypeAdapter(List[ChannelBaseModel])
        release_conn(db_conn)
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
):
    request_body = await request.json()

    channel_id = request_body["channel_id"]

    with db_conn.cursor(dictionary=True) as cursor:
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
