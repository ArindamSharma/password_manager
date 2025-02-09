import json
from os.path import isfile
class Configuration:
    def __init__(self,filename,default_configuration={}):
        if(filename.split(".")[-1]!="json"):
            raise ValueError (filename.split(".")[-1]," is not acceptable extension ,it have to be .json")
        self.data=default_configuration
        self.fileName=filename
        self.errorMessage=self.fileName
        self.__load()

    def __load(self) ->bool:
        if(isfile(self.fileName)):
            filePointer=open(self.fileName,"r")
            try:
                readData=json.load(filePointer)
            except(json.JSONDecodeError):
                self.errorMessage="Error :: Json File Wrong Formating"
                return False
            filePointer.close()
            if(self.validation_check(readData)):
                self.copy(readData)
        self.errorMessage=self.fileName+" :: Not Found"
        return False

    def save(self) -> bool:
        filePointer=open(self.fileName,"w")
        json.dump(self.data,filePointer,indent=4,default=lambda e : e.__str__())
        filePointer.close()
        self.errorMessage=self.fileName+" :: Saved Sucessfully"
        return False
    
    def validation_check(self,data) -> bool:
        for key in self.data:
            if key not in data:
                self.errorMessage=self.fileName+" :: PreDefined Parameter Changed"
                return False
        self.errorMessage=self.fileName+" :: PreDefined Parameter Found"
        return True
    
    def copy(self,data:dict)->None:
        # if(type(data)==dict):
        #     pass
        for key in self.data:
            self.data[key]=data[key]
            
    # def __del__(self):
    #     self.save()

if __name__=="__main__":
    print("Testing :: Configuration Class")
    default={
        "hello":[12,3,4,5],
        "val":{},
        "env":True,
    }
    config=Configuration("./__pycache__/test_config_handler.json",default)
    print(config.data)
    config.save()
    # print(config.errorMessage)