import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

DB_USER = os.environ.get("DB_USER")
DB_HOST = os.environ.get("DB_HOST")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")
DB_PORT = os.environ.get("DB_PORT")

FILES_PATH = os.environ.get("FILES_PATH")
LOG_PATH = os.environ.get("LOG_PATH")
