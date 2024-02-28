import cryptocode

class Sensitive:
    def __init__(self,value:str,key:str) -> None:
        self.value=self.encrypt(value,key)

    def encrypt(self,value,key)->str:
        return cryptocode.encrypt(value,key)

    def decrypt(self,key)->str:
        return cryptocode.decrypt(self.value,key)
    
    def getValue(self,key)->str:
        x=self.decrypt(key)
        if(x):
            return x
        raise Exception("Incorrect Password")
    
    def __repr__(self) -> str:
        return "<Sensitive x"+hex(id(self))+">"

    def __str__(self) -> str:
        return repr(self)

if(__name__=="__main__"):
    print("Unit Testing ..."+__file__)
    a=Sensitive("passsdfsdfgsdfgword@123","arindam")
    print(a.value)
    print(a.getValue("arindam"))