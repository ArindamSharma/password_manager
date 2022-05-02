from color import Color
from datetime import datetime as dt
from os.path import isdir
from os import mkdir

# from env_handler import *
class Logger:
    def __init__(self,log_filename,env_number=[],bmax=10):
        self.fileName=log_filename
        self.envNumber=env_number
        if (isdir("log")==False):
            mkdir("log")
        # self.filePointer=open(self.fileName,"a")
        # self.filePointer=None
        self.bufferMax=bmax
        self.buffer=""
        self.bufferLen=0
        self.onlylog("===================================================")
        self.__log(0,"Logger  :: Start :: ",dt.now())

    def debug(self,envNumber=0,*arg):
        self.__print(envNumber,"[DEBUG] :: ",Color.fg.BEIGE,arg)
        
    def info(self,envNumber=0,*arg):
        self.__print(envNumber,"[INFO]  :: ",Color.fg.GREEN,arg)

    def error(self,envNumber=0,*arg):
        self.__print(envNumber,"[ERROR] :: ",Color.fg.RED,arg)

    def file(self,*arg):
        self.__print(-1,"[FILE]  :: ",Color.fg.GREEN,arg)
    
    def __log(self,envNumber=0,*arg):
        self.__print(envNumber,"","",arg)

    def onlylog(self,*arg):
        self.__print(-1,"","",arg)

    def __print(self,envNumber,label,labelColor,message):
        colorLabel=Color.style.BOLD+labelColor+label+Color.fg.WHITE+Color.style.RESET_ALL
        strArg="".join([str(i) for i in message])
        if (envNumber in self.envNumber):
            print(colorLabel+strArg)
        self.buffer+=label+strArg+"\n"
        self.bufferLen+=1
        if(self.bufferLen >=self.bufferMax):
            self.__flushBuffer()

    def __flushBuffer(self):
        self.filePointer=open(self.fileName,"a")
        self.filePointer.write(self.buffer)
        self.filePointer.close()
        self.buffer=""
        self.bufferLen=0

    def close(self):
        self.__log(0,"Logger  :: Close :: ",dt.now())
        if(self.bufferLen>0):
            self.filePointer=open(self.fileName,"a")
            self.filePointer.write(self.buffer)
            self.filePointer.close()

    # def __del__(self):
    #     self.__log(0,"Logger  :: Close :: ",dt.now())
    #     if(self.bufferLen>0):
    #         self.filePointer=open(self.fileName,"a")
    #         self.filePointer.write(self.buffer)
    #         self.filePointer.close()


if __name__=="__main__":
    log=Logger("./__pycache__/test_log.log",[0,1,2,3])
    log.debug(0,"hello")
    for i in range(10):
        log.info(3,"my name is khan")
    log.error(0,"my name is not khan")
    log.close()