import json
import os
class Configuration:
    def __init__(self,filename,default_configuration={}):
        if(filename.split(".")[-1]!="json"):
            raise ValueError (filename.split(".")[-1]," is not acceptable extension ,it have to be .json")
        self.data=default_configuration
        self.fileName=filename
        self.filePointer=None
        self.errorMessage="File :: "+self.fileName
        self.__load()

    def __load(self) ->bool:
        if(os.path.isfile(self.fileName)):
            self.filePointer=open(self.fileName,"r")
            readData=None
            try:
                readData=json.load(self.filePointer)
            except(json.JSONDecodeError):
                self.errorMessage="Json File Error"
                return False
            self.filePointer.close()
            return self.validation_check(readData)
        self.errorMessage="File Not Found"
        return False

    def save(self) -> bool:
        self.filePointer=open(self.fileName,"w")
        json.dump(self.data,self.filePointer,indent=4,default=lambda e : e.__str__())
        self.filePointer.close()
        self.errorMessage="File "+self.fileName+" :: Saved Sucessfully"
        return False
    
    def validation_check(self,data) -> bool:
        for key in self.data:
            if key not in data:
                self.errorMessage="File :: "+self.fileName+" :: PreDefined Parameter Changed"
                return False
        self.data=data
        self.errorMessage="File :: "+self.fileName+" :: PreDefined Parameter Found"
        return True

if __name__=="__main__":
    print("Testing :: Configuration Class")
    default={
        "hello":[12,3,4,5],
        "val":{},
        "env":True,
    }
    config=Configuration("test_config_handler",default)
    # print(config.errorMessage)
    config.load()
    # print(config.errorMessage)
    print(config.data)
    config.save()
    # print(config.errorMessage)