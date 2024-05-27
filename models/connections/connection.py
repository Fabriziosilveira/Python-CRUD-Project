from pymongo import MongoClient
from .mongodbConfig import mongodbConfig

class managerDbConnection:
    def __init__(self) -> None:
        self.__connectionString = 'mongodb://{}:{}/'.format(
            mongodbConfig["HOST"],
            mongodbConfig["PORT"]
        )
        self.__dataBaseName = mongodbConfig["DB_NAME"]