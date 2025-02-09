from .item import Item

class Vault:
    def __init__(self,_title)->None:
        self.title=_title
        self.__item:list[Item]=[]

    def addItem(self,title:str,uname:str,passwd:str,security_key:str,tag:str=None,**arg)->None:
        _item=Item(title,uname,passwd,security_key,tag,**arg)
        if(_item not in self.__item):
            self.__item.append(_item)
        else:
            raise Exception("similar item already exist in this vault")
        
    def removeItem(self,_item:Item)->None:
        self.__item.remove(_item)

    def renameVault(self,_newname:str)->None:
        self.title=_newname

    def getItem(self,_title:str)->Item: 
        for i in self.__item:
            if(i.title==_title):
                return i
        raise ValueError("mentioned item not found in this vault")

    def __repr__(self) -> str:
        __tmp=""
        for i in self.__dict__:
            if(type(self.__dict__[i])!=list):
                __tmp+=i+": "+str(self.__dict__[i])+", "
            else:
                for x in range(len(self.__dict__[i])):
                    __tmp+="item"+str(x+1)+": "+self.__dict__[i][x].__repr__()+", "

        return "<Vault x"+hex(id(self))+" "+__tmp[:-2]+">"
    
    def __str__(self) -> str:
        return repr(self)
