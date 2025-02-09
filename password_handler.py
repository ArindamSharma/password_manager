import pandas as pd

class TagedPassbook:
    def __init__(self,column:list[str],tags:list[str]=[],vaults:list[str]=[],filename:"str"= "filename.csv"):
        self.__tagColName="Tags"
        self.__vaultColName="Vault"
        self.__columns=column
        self.DB=pd.DataFrame(columns=[self.__vaultColName]+self.__columns+[self.__tagColName])
        
        self.__tagList=tags
        self.__capitalizeTags(self.__tagList)
        self.__vaultList=vaults
        
        self.__fileName=filename
        self.__currentVault=None
        self.__index=0
        try:
            self.load()
            self.__index=len(self.DB)
            self.initTags()
            self.initVaults()
        except FileNotFoundError :
            pass

    # Magic Functions >>>>>>>>>>.

    def __getitem__(self,i):
        return list(self.DB.loc[i])

    def __len__(self):
        return self.__index

    def __repr__(self)->pd.DataFrame:
        return str(self.DB)

    # def __del__(self):
    #     self.save()

    # Private Methods >>>>>>>>>>

    def __vaultCheck(self,vaultName:str):
        if(vaultName not in self.__vaultList):
            raise ValueError(vaultName," no matching vault found")

    def __tagCheck(self,*tag:str):
        for label in tag:
            if label not in self.__tagList:
                raise ValueError(label,"not there in the __tagList:",self.__tagList)

    def __capitalizeTags(self,tagArray:"list[str]|tuple[str] |...")->None:
        for i in tagArray:
            i.capitalize()

    # Tags Functions >>>>>>>>>>

    def initTags(self)->None:
        for filetag in set(self.DB[self.__tagColName].values):
            if(filetag not in self.__tagList):
                self.__tagList.append(filetag)
    def getTags(self)->list:
        return self.__tagList

    def getTagForRow(self,__index:int)->list:
        return self.DB.loc[__index,self.__tagColName]
    
    def setTagInRow(self,__index:int,*tag:str)->None:
        self.__capitalizeTags(tag)
        self.__tagCheck(*tag)
        self.DB.loc[__index,self.__tagColName]=list(tag)

    def appendTagInRow(self,__index:int,*tag:str)->None:
        self.__capitalizeTags(tag)
        self.__tagCheck(*tag)
        self.DB.loc[__index,self.__tagColName]=list(set(self.DB.loc[__index,self.__tagColName]+list(tag)))
    
    def removeTagInRow(self,__index:int,tag:str)->str:
        tag=tag.capitalize()
        self.__tagCheck(tag)
        self.getTagForRow(__index).remove(tag)
        pass

    def addTag(self,*tags:str):
        self.__capitalizeTags(tags)
        for tag in tags:
            if(tag not in self.__tagList):
                self.__tagList.append(tag)

    # Vault Function >>>>>>>>>
    def initVaults(self)->None:
        for filevault in set(self.DB[self.__vaultColName].values):
            if(filevault not in self.__vaultList):
                self.__vaultList.append(filevault)
    
    def addVault(self,*vaults:tuple[str])->None:
        for vault in vaults:
            if(vault not in self.__vaultList):
                self.__vaultList.append(vault)

    def setCurrentVault(self,vaultName:str,)->None:
        self.__vaultCheck(vaultName)
        self.__currentVault=vaultName

    def getVaultData(self,vaultName:str)->list:
        self.__vaultCheck(vaultName)
        return self.DB[self.DB[self.__vaultColName]==vaultName].values 

    def removeVault(self,vaultName:str)->None:
        self.__vaultCheck(vaultName)
        self.DB.drop(self.DB[self.DB[self.__vaultColName]==vaultName],inplace=True)

    def getVaultCount(self,)->list:
        return list(self.DB[self.__vaultColName].value_counts().items())

    # Row Functions >>>>>>

    def getRowIndexWithTags(self,*tags:str)->list:
        self.__capitalizeTags(tags)
        self.__tagCheck(*tags)
        tmp=[]
        for __index in [self.DB.iloc[i].name for i in range(self.__index)]:
            if(set(tags).issubset(set(self.DB.loc[__index,self.__tagColName]))):
                tmp.append(__index)
        return tmp

    def getRowWithTag(self,*tags:str)->list:
        self.__capitalizeTags(tags)
        self.__tagCheck(*tags)
        return self.DB.loc[self.getRowIndexWithTags(*tags)].values

    def updateRow(self,**columnData):
        print(columnData)

    def appendRow(self,itemlist:list,tag:list[str])->None:
        self.__capitalizeTags(tag)
        self.__tagCheck(*tag)
        self.DB.loc[self.__index]=[self.__currentVault]+itemlist+[tag]
        self.__index+=1
    
    def dropAllRowWithTags(self,*tag:str):
        self.__capitalizeTags(tag)
        self.__tagCheck(*tag)
        for i in self.getRowIndexWithTags(tag):
            self.dropRowWithIndex(i)

    def dropRowWithIndex(self,__index:int):
        self.DB.drop(__index=__index,inplace=True)
        # self.DB.reset___index(drop=True,inplace=True)
        self.__index-=1

    # Search Functions >>>>>>>>>

    def getRowsWithKeyWord(self,keyword)->list:
        pass

    # Other Functions >>>>>>>.

    def getDB(self)->list:
        return self.DB.values

    def save(self)->None:
        self.DB.to_csv(self.__fileName,__index=False)

    def load(self)->None:
        self.DB=pd.read_csv(self.__fileName)

if __name__=="__main__":
    print("Testing DataFrame Handler")
    col=["Title","Email","Username","Password","Link","Data"]
    tags=["Company","Personal","Intern","Game"]
    x=TagedPassbook(col,tags,"test_password.csv")
    x.addVault("vault_1","vault_2")
    x.setCurrentVault("vault_1")
    x.appendRow(["Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["Personal","Intern"])
    x.appendRow(["Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["Personal","Intern"])
    x.addTag("Other","College")
    x.setCurrentVault("vault_2")
    x.appendRow(["Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["College","Intern"])
    x.appendRow(["Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["Company","Other"])
    x.appendRow(["Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["Personal"])
    # print(x.getRowWithTag("Intern","Personal"))
    # print(x.getRowWithTag("Intern"))
    # x.removeTagInRow(1,"Personal")
    print(x)
    x.appendTagInRow(1,"Game","personal","company")
    # print(x.getTagForRow(1))
    # x.dropAllRowWithTags("personal")
    # x.dropRowWithTag("indern")
    # print(x.getDataFrame())
    # print(x.getRowWithTag("company"))
    # print(x.getDB())
    # print(x[0])
    print(x)
    print(x.getVaultCount())
    # p=x["Vaults"].value_counts().items()
    # print(list(p))
    # print(len(x))