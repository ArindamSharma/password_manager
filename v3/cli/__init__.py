from model import Model
from .display import *

class CLI():
    def __init__(self) -> None:
        self.AppData=Model()
        pass

    def mainloop(self):
        print("Welcome To PassBook")
        singleInputMenu("Menu",[
            ("Login",self.userLogin),
            ("Register User",self.userRegister),
            ("Forget Password",self.userForgetPass)
        ],lambda:print("Have a nice day..."))

    def userRegister(self):
        printSection("Register User",fillchar="-",newline=True)
        uname=customInput("Name: ")
        username=customInput("Username: ")
        if(self.AppData.checkUsername(username)!=-1):
            printSectionItem("username",username,"already exist")
            printSection(fillchar="-")
            return
        passwd=customInput("Password: ",hidden=True)

        printSectionItem("Security Question ...")
        for i in range(len(self.AppData.securityQuestions)):
            printSectionItem(str(i+1)+". "+self.AppData.securityQuestions[i])
        
        while(True):
            try:
                x=customInput("Select a Security Question Number: ",startchar=">")
                y=customInput(self.AppData.securityQuestions[int(x)-1]+": ",startchar=">")
                self.AppData.addUser(uname,username,passwd,x,y)
                printSectionItem("User Added Sucessfully...")
                printSection(fillchar="-")
                break
            except Exception as e:
                print(e)
                printSectionItem("Registration Failed")
                printSection(fillchar="-")
                break

    def userForgetPass(self):
        uname=customInput("Username: ")
        userindex=self.AppData.checkUsername(uname)
        if(userindex==-1):
            print("User Not Found")
            return
        
        print("Security Question ...")
        x=self.AppData.getUserSecurityQuestionIndex()
        y=customInput(self.AppData.securityQuestions[x],": ")
        self.AppData.getUser(uname,x,y)
        self.AppData.curerntUser.resetSecurityKey(customInput("New Password: "))
        print("Password Updated Sucessfully. Please login again.")
    
    def userLogin(self):
        while(True):
            try:
                printSection("Login Credentials","-",newline=True)
                self.AppData.getUser(customInput("Username: ",startchar="|"),customInput("Password: ",hidden=True,startchar="|"))
                printSectionItem("Login Successful..")
                printSection(fillchar="-")
                break
            except Exception as e:
                printSectionItem("Error: "+str(e),startchar="!")
                printSection(fillchar="-")
                x=customInput("Retry...(Y/n): ",startchar=">",newline=True)
                if(x!="Y" and x!="y"):
                    return None

        singleInputMenu("Welcome "+self.AppData.curerntUser.name,[
            # Vault Specific
            ("Show Vaults",self.showVault),
            ("Use/Select Vault",self.showVault),
            ("Add New Vaults",self.showVault),
            ("Remove Vault",self.showVault),
            # User Specific
            ("Show User Details",self.showVault),
            ("Edit Name",self.showVault),
            ("Update/Change Password",self.showVault),
            ("Logout",self.showVault),
            ("Delete Account",self.showVault),
        ],lambda:print("Logging off User",self.AppData.curerntUser.name))

    def showVault(self):
        print("Hello")
