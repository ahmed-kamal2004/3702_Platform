from fastapi import FastAPI
from users.publisher import publisher
from auth import auth

program = FastAPI(debug=True)


program.include_router(publisher.router)
program.include_router(auth.router)
