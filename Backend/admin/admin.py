from fastapi import APIRouter,Depends,Request,Response,HTTPException,status
from DatabaseConnection import release_conn,get_conn,PooledMySQLConnection
from .constants import TokenInteraction,EmailInteraction
from auth.auth import PasswordInteraction



router = APIRouter(prefix="/adm",tags = ["Admin"])

############################################################### First Making a new admin
@router.post('/make-new-admin',status_code=status.HTTP_201_CREATED)
async def make_new_admin(request :Request, admin_user :str = Depends(TokenInteraction.get_current_user),
                         db_conn : PooledMySQLConnection = Depends(get_conn)):
    request_body = await request.json()

    current_username = request_body["current_username"]
    username = request_body["username"]
    email = request_body["email"]
    password = request_body["password"]
    DOB = request_body["DOB"]
    phonenumber = request_body["phonenumber"]

    ## check that the current admin is the logged one  Error -> 401 unAuthorized
    ## check that the username  exists   Error -> 409 Conflict
    ## check that the email  exists    Error -> 409 Conflict

    ## add the new admin to Database
    ## Send an Email to the new admin contaning Info and Password
    print(admin_user,current_username)
    if current_username != admin_user:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Login First"
        )
    
    ## Here we must check and return UnprocessAble Entity

    with db_conn.cursor(dictionary = True) as cursor:
        
        query = "SELECT * FROM admin WHERE username = %s OR email = %s"
        cursor.execute(query,(username,email))
        result = cursor.fetchone()
        if result:
            release_conn(db_conn)
            return HTTPException(status_code=status.HTTP_409_CONFLICT,detail = "Username Or Email is Already in Use")
        try:
            query = "INSERT INTO admin (username, email,password,DOB,phonenumber) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(query , (username,email,PasswordInteraction.hash_password(password),DOB,phonenumber))
            db_conn.commit()

        except Exception as e:
            release_conn(db_conn)
            return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail =e)
        else:
            release_conn(db_conn)
            EmailInteraction.send(message=f"""you are added to 3702_Platform as an admin
                                  Your Username is : "{username}"  , Your Password is : "{password}"
                                    Congratulations! """,receiver=email)
            return {"Message":"Success"}