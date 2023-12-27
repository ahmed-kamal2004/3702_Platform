from fastapi import FastAPI
from users.publisher import publisher
from users.student import student
from channel import channel
from auth import auth
from admin import admin
from fastapi.middleware.cors import CORSMiddleware

program = FastAPI(debug=True)

# Allow all origins
origins = ["*"]

program.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


program.include_router(publisher.router)
program.include_router(student.router)
program.include_router(auth.router)
program.include_router(channel.router)
program.include_router(admin.router)
