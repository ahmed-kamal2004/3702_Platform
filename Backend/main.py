from fastapi import FastAPI


program = FastAPI()

@program.get("/program")
def get():
    return {"Message":"Hi"}