from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from . import schemas, database, models
from jose import JWTError, jwt
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')


# SECRET_KEY
# Algorithm
# Expriation time

SECRET_KEY = "xsw15rofdeiwzwaketqlkcmig8mmb7rz1h9u35coovexktd4j6rw7oasi0fxbocew13hcsgomkhjxwnyfxrwadrxvn"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
  to_encode = data.copy()

  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode["exp"] = expire

  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str, credentials_exception):

  try:

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    _id: str = payload.get("user_id")

    if _id is None:
      raise credentials_exception

    token_data = schemas.TokenData(id = _id)

  except JWTError as e:
    raise credentials_exception from e

  return token_data
  

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
  credentials_exception = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = 'Could not validate credentials',
    headers = {"WWW-Authenticate": 'Bearer'}
  )

  token = verify_access_token(token, credentials_exception)

  user = db.query(models.User).filter(models.User.id == token.id).first()

  return user