from fastapi import FastAPI
# from . import models
# from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)

origins=["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# while True:

#   try:
#     conn = psycopg2.connect(
#       host="127.0.0.1",
#       database="fastapi",
#       user="dmitrij",
#       password="postgres",
#       cursor_factory=RealDictCursor
#     )
#     cursor = conn.cursor()
#     print("Database connection was succesfull")
#     break

#   except Exception as error:
#     print("Connecting to database failed")
#     print("Error: ", error)
#     time.sleep(10)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
  return {"message": "welcone to my api"}
