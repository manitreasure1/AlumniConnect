

from datetime import timedelta
from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    REDIS_URL = os.getenv('REDIS_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES: timedelta = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES: timedelta = timedelta(days=30)
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    CACHE_TYPE = os.getenv('CACHE_TYPE')
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL')

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        if self.CACHE_REDIS_URL is None:
            self.CACHE_REDIS_URL = self.REDIS_URL