import pandas as pd
class Passbook:
    def __init__(self,column,filename="<filename>.csv"):
        self.DB=pd.DataFrame(columns=column)
        self.fileName=filename
        self.index=0
        try:
            self.load()
            self.index=len(self.DB)
        except FileNotFoundError :
            pass
    
    def getDB(self):
        return self.DB
    
    def append(self,itemlist):
        self.DB.loc[self.index]=itemlist
        self.index+=1

    def save(self):
        self.DB.to_csv(self.fileName,index=False)

    def load(self):
        self.DB=pd.read_csv(self.fileName)

if __name__=="__main__":
    print("Testing DataFrame Handler")
    col=["category","subcateogry","microcategory","title","email","username","password","link","data"]
    x=Passbook(col,"test_password.csv")
    x.append([None,None,None,"Google","email","username","passer","dfgdfgdfgf",{"asd":1}])
    print(x.getDB())