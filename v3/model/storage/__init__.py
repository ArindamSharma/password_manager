from .instorage import InStorage
from .outstorage import OutStorage

class Storage:
    def __init__(self,internalStorage:bool=True) -> None:
        self.data=InStorage() if internalStorage else OutStorage()

    def Load(self)->None:
        # self.data.load()
        pass

    def Save(self):
        # self.data.save()
        pass

    def Insert(self):
        # self.data.insert()
        pass

    def Update(self):
        # self.data.update()
        pass

    def Delete(self):
        # self.data.delete()
        pass