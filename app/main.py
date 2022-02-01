from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.param_functions import Body
from httpx import post
from typing import List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from .database import get_db, engine
from sqlalchemy.orm import Session

from starlette.status import HTTP_404_NOT_FOUND

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:

  try:
    conn = psycopg2.connect(
      host="127.0.0.1",
      database="fastapi",
      user="dmitrij",
      password="postgres",
      cursor_factory=RealDictCursor
    )
    cursor = conn.cursor()
    print("Database connection was succesfull")
    break

  except Exception as error:
    print("Connecting to database failed")
    print("Error: ", error)
    time.sleep(10)

@app.get("/")
async def root():
  return {"message": "welcone to my api"}


@app.get("/posts", response_model=List[schemas.Post])
async def get_posts(db: Session = Depends(get_db)):

  return db.query(models.Post).all()


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

  new_post = models.Post(**post.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)

  return new_post


@app.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):

  post = db.query(models.Post).filter(models.Post.id == id).first()

  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with id: {id} was not found")
  return post


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

  post = db.query(models.Post).filter(models.Post.id == id)

  if post.first() is None:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

  post.delete(synchronize_session=False)
  db.commit()

  return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):

  updated_post = db.query(models.Post).filter(models.Post.id == id)


  if updated_post.first() is None:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
  
  updated_post.update(post.dict(), synchronize_session=False)
  db.commit()

  return updated_post.first()
