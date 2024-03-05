from .user import User
from .storage import Storage

class Model:
    def __init__(self) -> None:
        
        self.__users:list[User]=[]
        self.securityQuestions:tuple[str]=(
            "Whats your Pet name",
            "Whats your House name",
            "Who is your Bestfriend",
            "Who your favoriate hobbie"
        )
        self.currentUser:User=None

    def getUser(self,_username:str,_password:str=None,_securityQ1:int=None,_securityAnswer:str=None)->None:
        '''Gets User Object from Users List\n
            based on either username and password or on username, securityQuestion and securityAnswer\n
            Input: (_username ,_password) or (_username,_securityQuestionIndex,_securityAnswer)\n
            Return: None (updates "currentUser" variable with User() Object)'''
        tmp=self.checkUsername(_username)
        if(tmp==-1):
            raise ValueError("username \""+_username+"\" Not Found")

        if(self.__users[tmp].authenticate(_password) or self.__users[tmp].authenticate(_securityAnswer,_securityQ1)):
            self.curerntUser=self.__users[tmp]
            
        else:
            raise Exception("Authintication Failed")

    def addUser(self,_uname:str,_username:str,_password:str,_securityQI:str,_securityAnswer:str)->bool:
        '''Add User to the User List '''
        if(self.checkUsername(_username)!=-1):
            raise ValueError("username \""+_username+"\" already exist, Use other username")
        if(_securityQI not in [str(i+1) for i in range(len(self.securityQuestions)) ]):
            raise ValueError("Invalid Security Question Selected.")
        self.__users.append(User(_uname,_username,_password,_securityQI,_securityAnswer))

    def checkUsername(self,_username:str)->bool:
        '''Checks if the username already exist in the Users List
        return index of user if found else return -1
        '''
        for i in range(len(self.__users)):
            if(self.__users[i].getUsername()==_username):
                return i
        return -1    

    def getUserSecurityQuestionIndex(self,_username:str)->str:
        '''Checks if the username already exist in the Users List
        return : securityQuestion :str
        '''
        tmp=self.checkUsername(_username)
        if(tmp!=-1):
            return self.__users[tmp]._securityQuestionIndex
        return None