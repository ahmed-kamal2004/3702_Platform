from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from DatabaseConnection import get_conn, PooledMySQLConnection, release_conn
from passlib.context import CryptContext
import users.publisher.constants as upc
import users.student.constants as usc


router = APIRouter(prefix="/login", tags=["Login"])


class PasswordInteraction:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash_password(password: str) -> str:
        return PasswordInteraction.pwd_context.hash(password)

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return PasswordInteraction.pwd_context.verify(password, hashed_password)


@router.post("/pub")
def publisher_login(
    data: OAuth2PasswordRequestForm = Depends(),
    db_conn: PooledMySQLConnection = Depends(get_conn),
):
    with db_conn.cursor() as cursor:
        username = data.username
        password = data.password

        first_query = "SELECT username FROM user WHERE username = %s"
        cursor.execute(first_query, (username,))
        result = cursor.fetchone()
        if result:
            second_query = "SELECT password FROM user WHERE username = %s"
            cursor.execute(second_query, (username,))
            result = cursor.fetchone()
            release_conn(db_conn)
            print(result)
            if PasswordInteraction.verify_password(
                password=password, hashed_password=result[0]
            ):
                ## need to generate Token

                token_data = {"username": username}
                token = upc.TokenInteraction.create_token(token_data)
                return token
            else:
                return HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Wrong Password",
                )

        else:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Username doesn't exist",
            )
        ## at end return close all connections


@router.post("/stu")
def student_login(
    data: OAuth2PasswordRequestForm = Depends(),
    db_conn: PooledMySQLConnection = Depends(get_conn),
):
    with db_conn.cursor() as cursor:
        username = data.username
        password = data.password

        first_query = "SELECT username FROM user WHERE username = %s"
        cursor.execute(first_query, (username,))
        result = cursor.fetchone()
        if result:
            second_query = "SELECT password FROM user WHERE username = %s"
            cursor.execute(second_query, (username,))
            result = cursor.fetchone()
            release_conn(db_conn)
            print(result)
            if PasswordInteraction.verify_password(
                password=password, hashed_password=result[0]
            ):
                ## need to generate Token

                token_data = {"username": username}
                token = usc.TokenInteraction.create_token(token_data)
                return token
            else:
                return HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Wrong Password",
                )

        else:
            release_conn(db_conn)
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Publisher Username doesn't exist",
            )
        ## at end return close all connections
