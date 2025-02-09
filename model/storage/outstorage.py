from model.user import User
import pandas as pd 
# from pymongo import MongoClient

class OutStorage:
    def __init__(self) -> None:
        self.username:str=""
        self.password:str=""
        self.url:str=""
        self.serverName:str=""
        self.databaseName:str=""
        self.connection:str=""
        pass

    def Connect(self)->None:
        pass

    def Read(self):
        pass

    def Insert(self):
        pass

    def Update(self):
        pass

    def Delete(self):
        pass