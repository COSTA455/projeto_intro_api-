import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "leiac@1")
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL","postgresql://postgres:SECRET_KEY@127.0.0.1:5433/tarefas_3a")
    SQLALCHEMY_TRACK_MODIFICATIONS = False