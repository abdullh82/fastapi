from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post,user,auth,vote
from .config import settings
# models.Base.metadata.create_all(bind=engine)
from fastapi import FastAPI, File, UploadFile
import os
from os import walk


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

        
@app.get("/")
async def root():
    path=os.getcwd()
    dir_list = os.listdir(path)
    return {"message": dir_list}


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


def save_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

import os
@app.post("/uploadfile/")
async def upload(files: List[UploadFile] = File(...)):
     
    # in case you need the files saved, once they are uploaded
    for file in files:
        contents = await file.read()
        save_file(file.filename, contents)

    return {"Uploaded Filenames": [file.filename for file in files]}

