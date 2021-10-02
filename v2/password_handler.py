from typing import Any, List
import pandas as pd
from pandas._config.config import reset_option
from pandas.core.frame import DataFrame

class TagedPassbook:
    def __init__(self,column:list[str],tags:list=[],filename:"str"= "filename.csv"):
        self.tagColName="Tags"
        self.DB=pd.DataFrame(columns=column+[self.tagColName])
        self.tagList=[i.capitalize() for i in tags]
        self.fileName=filename
        self.index=0
        try:
            self.load()
            self.index=len(self.DB)
        except FileNotFoundError :
            pass

    def __len__(self):
        return self.index

    def getDB(self)->list:
        return self.DB.values

    def getDataFrame(self)->pd.DataFrame:
        return self.DB

    def getTagForRow(self,index:int)->list:
        return self.DB.loc[index,self.tagColName]
    
    def setTagInRow(self,index:int,*tag:str)->None:
        tag=self.__capitalizeTags(tag)
        self.__tagCheck(*tag)
        self.DB.loc[index,self.tagColName]=list(tag)

    def appendTagInRow(self,index:int,*tag:str)->None:
        tag=self.__capitalizeTags(tag)
        self.__tagCheck(*tag)
        self.DB.loc[index,self.tagColName]+=list(tag)
    
    def removeTagInRow(self,index:int,tag:str)->str:
        tag=tag.capitalize()
        self.__tagCheck(tag)
        self.getTagForRow(index).remove(tag)
        pass

    def getRowIndexWithTags(self,*tags:str)->list:
        tags=self.__capitalizeTags(tags)
        self.__tagCheck(*tags)
        tmp=[]
        for index in [self.DB.iloc[i].name for i in range(self.index)]:
            if(set(tags).issubset(set(self.DB.loc[index,self.tagColName]))):
                tmp.append(index)
        return tmp

    def getRowWithTag(self,*tags:str)->list:
        tags=self.__capitalizeTags(tags)
        self.__tagCheck(*tags)
        return self.DB.loc[self.getRowIndexWithTags(*tags)].values

    def updateRow(self,**columnData):
        print(columnData)

    def appendRow(self,itemlist:list,tag:list[str])->None:
        tag=self.__capitalizeTags(tag)
        self.__tagCheck(*tag)
        self.DB.loc[self.index]=itemlist+[tag]
        self.index+=1
    
    def dropAllRowWithTags(self,*tag:str):
        tag=self.__capitalizeTags(tag)
        self.__tagCheck(*tag)
        for i in self.getRowIndexWithTags(*self.__capitalizeTags(tag)):
            self.dropRowWithIndex(i)

    def dropRowWithIndex(self,index:int):
        self.DB.drop(index=index,inplace=True)
        # self.DB.reset_index(drop=True,inplace=True)
        self.index-=1
    
    def getRowsWithKeyWord(self,keyword)->list:
        pass

    def __tagCheck(self,*tag:str):
        for label in tag:
            if label not in self.tagList:
                raise ValueError(label,"not there in the tagList:",self.tagList)

    def __capitalizeTags(self,tagArray:"list[str]|tuple[str] |...")->"list[str]|tuple[str] |...":
        return [i.capitalize() for i in tagArray]

    def addTag(self,*tag:str):
        self.__capitalizeTags(tag)
        for i in tag:
            self.tagList.append(i)

    def save(self):
        self.DB.to_csv(self.fileName,index=False)

    def load(self):
        self.DB=pd.read_csv(self.fileName)

if __name__=="__main__":
    print("Testing DataFrame Handler")
    col=["Vaults","Title","Email","Username","Password","Link","Data"]
    tags=["Company","Personal","Intern","Game"]
    x=TagedPassbook(col,tags,"test_password.csv")
    x.appendRow(["vault_2","Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["Personal","Intern"])
    x.appendRow(["vault_1","Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["Personal","Intern"])
    x.addTag("Other","College")
    x.appendRow(["vault_2","Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["College","Intern"])
    x.appendRow(["vault_1","Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["Company","Other"])
    x.appendRow(["vault_1","Google","email","username","passer","dfgdfgdfgf",{"asd":1}],["Personal"])
    # print(x.getRowWithTag("Intern","Personal"))
    # print(x.getRowWithTag("Intern"))
    x.removeTagInRow(1,"Personal")
    x.appendTagInRow(1,"Game","personal","company")
    # print(x.getTagForRow(1))
    x.dropAllRowWithTags("personal")
    # x.dropRowWithTag("indern")
    # print(x.getDataFrame())
    # print(x.getRowWithTag("company"))
    # print(x.getDB())
    print(x.getDataFrame())
    # print(len(x))