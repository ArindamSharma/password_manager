from model.vault import Vault
import cryptocode


class User:
    def __init__(self,_uname,_username,_passwd,_securityQuestionIndex,_securityAnswer)->None:
        self.name:str=_uname
        self._username:str=_username
        self.__passwd=hash(_passwd)
        self._securityQuestionIndex:str=_securityQuestionIndex
        self.__securityAnswer:str=_securityAnswer
        self.__vault:list[Vault]=[]
    
    def authenticate(self,_securitykey:str,_securityQuestionIndex:str=None)->bool:
        """
        Authenticate User with either password or with Security Question with answer
        Input :(_password) or (_securityAnswer,_securityQuestionIndex)\n
        Return :None 
        """
        _authPassword=hash(_securitykey)==self.__passwd
        _authSecurityQuestion=(_securityQuestionIndex==self._securityQuestionIndex and _securitykey==self.__securityAnswer)
        if(_authPassword or _authSecurityQuestion):
            return True
        return False

    def resetSecurityKey(self,_newPass:str)->None:
        '''
        reset password/securityKey with a new one
        '''
        self.__passwd=hash(_newPass)

    def updateSecurityKey(self,_oldPass:str,_newPass:str)->None:
        '''
        Updates password with old password check
        '''
        if(hash(_oldPass)==self.__passwd):
            self.resetSecurityKey(_newPass)
        else:
            raise Exception("Incorrect Old Password")

    def addVault(self,_vaultname:str)->bool:
        for i in self.__vault:
            if(i.title==_vaultname):
                raise Exception("Vault with \""+_vaultname+"\" title already exist.")
        self.__vault.append(Vault(_vaultname))
        return True

    def removeVault(self,_vaultname:str)->bool:
        for i in self.__vault:
            if(i.title==_vaultname):
                self.__vault.remove(i)
                return True
        return False
    
    def getVault(self,_vaultname:str)->Vault:
        for i in self.__vault:
            if(i.title==_vaultname):
                return i
        raise Exception("No Vault Found with \""+_vaultname+"\" title")
    
    def getAllVault(self)->list[Vault]:
        return self.__vault

    def getUsername(self):
        return self._username

if(__name__=="__main__"):
    print("Unit Testing ..."+__file__)
    