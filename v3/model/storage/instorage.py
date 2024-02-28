from model.user import User
import pandas as pd 
import pickle as pk

class InStorage:
    def __init__(self) -> None:
        self.data:list[User]=pd.DataFrame()
        self._backupName="backup.plk"
        self._backupLocation="../backups/"
        pass
    
    def load(self,)->None:
        pass

    def save(self,)->None:
        pass

    def exportAsCSV(self)->None:
        pass

    def importCSV(self)->None:
        pass

    def backup(self,_path:str=None)->None:
        pk.dump(self.data,_path if _path!=None else self._backupLocation+self._backupName)

    def restore(self,_path:str=None)->None:
        self.data=pk.load(_path if _path!=None else self._backupLocation+self._backupName)

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def __del__(self)->None:
        pass