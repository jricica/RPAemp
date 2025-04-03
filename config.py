import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    UPLOAD_FOLDER = "uploads/"
    ALLOWED_EXTENSIONS = {'pdf'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    TESTING = os.getenv("TESTING", "False").lower() in ("true", "1", "t")
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "False").lower() in ("true", "1", "t")
    SQLALCHEMY_POOL_SIZE = int(os.getenv("SQLALCHEMY_POOL_SIZE", 5))
    SQLALCHEMY_POOL_TIMEOUT = int(os.getenv("SQLALCHEMY_POOL_TIMEOUT", 10))
    SQLALCHEMY_POOL_RECYCLE = int(os.getenv("SQLALCHEMY_POOL_RECYCLE", 1800))
    SQLALCHEMY_MAX_OVERFLOW = int(os.getenv("SQLALCHEMY_MAX_OVERFLOW", 10))
    SQLALCHEMY_COMMIT_ON_TEARDOWN = os.getenv("SQLALCHEMY_COMMIT_ON_TEARDOWN", "False").lower() in ("true", "1", "t")
    