from fastapi import FastAPI
from users.publisher import publisher

program = FastAPI(debug=True)


program.include_router(publisher.router)
