from fastapi import FastAPI
from server import *
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    # allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_filename/{filename:path}")
def filename(filename):
    return json.loads(get_filename(filename))

@app.get("/get_trending")
def trending():
    return get_trending()

@app.get("/sys_info/{path2:path}")
def sys_info(path2):
    print(path2)
    Server_path = path2
    Server_info = System_info(path2)
    return json.loads(Server_info.home_page())

@app.gt("get_movie_details/{id:id}")
def full_movie_details(id):
    full_movie_json = server_info.get_movie_details(id)
    return full_movie_json
