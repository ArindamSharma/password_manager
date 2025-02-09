from .sensitive import Sensitive

class Tag:
    PERSONAL="PERSONAL"
    COLLEGE="COLLEGE"
    PRIVATE="PRIVATE"
    EDUCATIONAL="EDUCATION"

    def __init__(self) -> None:
        self.TagList=[]

    def getTag(self,name):
        pass

    def addTag(self,name):
        pass

    def removeTag(self,name):
        pass

class Item:
    def __init__(self,title:str,uname:str,passwd:str,security_key:str,tag:str=None,**arg)->None:
        self.hide=True
        self.title=title
        self.uname=uname
        self.passwd=Sensitive(passwd,security_key)
        self.tag=tag
        self.arg={}
        for i in arg:
            self.arg[i]=arg[i]
    
    def _updateParam(self):
        pass

    def _addParam(self):
        pass

    def __eq__(self, __value: object) -> bool:
        if(self.title==__value.title):
            return True
        return False

    def __repr__(self) -> str:
        __tmp=""
        for i in self.__dict__:
            if(type(self.__dict__[i])!=dict):
                __tmp+=i+": '"+str(self.__dict__[i])+"'; "
            else:
                for x in self.__dict__[i]:
                    __tmp+=x+": '"+str(self.__dict__[i][x])+"'; "

        return "<Item x"+hex(id(self))+" "+__tmp[:-2]+"> "

    def __str__(self) -> str:
        return repr(self)
        
if(__name__=="__main__"):
    print("Unit Testing ..."+__file__)
    i=Item("Google","arindmasharma1998@gmail.com","password@123","arindam",link="http://arindamsharma.github.io")
    j=Item("Google","arindmasharma1998@gmail.com","password123","arindam",link="http://arindamsharma.github.io")
    print(i)
    print(j)
