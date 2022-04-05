from pydantic import BaseSettings


class Settings(BaseSettings):
  database_host: str = "localhost"
  database_port: str = "5432"
  database_password: str  = ""
  database_name: str = "postgres"
  database_username: str = "postgres"
  secret_key: str = "xsw15rofdeiwzwaketqlkcmig8mmb7rz1h9u35coovexktd4j6rw7oasi0fxbocew13hcsgomkhjxwnyfxrwadrxvn"
  algorithm: str = "HS256"
  access_token_expire_minutes: int = 60

  class Config:
    env_file = ".env"


settings = Settings()