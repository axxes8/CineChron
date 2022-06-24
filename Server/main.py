from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from server import *

app=FastAPI()

# app.mount('/filename', app=StaticFiles(directory='Z:/'), name="filename")

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
    server_info = System_info(path2)
    return json.loads(server_info.home_page())
