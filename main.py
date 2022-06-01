from fastapi import FastAPI
from server import *

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_filename/{filename}")
async def filename(filename):
    return {get_filename(filename)}