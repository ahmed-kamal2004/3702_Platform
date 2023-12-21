from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..DatabaseConnection import get_conn, PooledMySQLConnection, release_conn
from passlib.context import CryptContext


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

        first_query = "SELECT username FROM publisher WHERE username = %s"
        cursor.execute(first_query, (username,))
        result = cursor.fetchone()
        if result:
            second_query = "SELECT password FROM publisher WHERE username = %s"
            cursor.execute(second_query, (username,))
            result = cursor.fetchone()
            if PasswordInteraction.verify_password(
                password=password, hashed_password=result
            ):
                ## need to generate Token
                pass
            else:
                return HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Wrong Password",
                )

        else:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Username doesn't exist",
            )
        ## at end return close all connections
        release_conn(db_conn)
