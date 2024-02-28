from model import Model
from model.user import User
from model.storage.instorage import InStorage
from getpass import getpass
# from 

# Printing Functions 
def printSection(title:str=None,fillchar="=",newline:bool=False):
    x=fillchar*50
    if(title!=None):
        title+=" "
        x=title.ljust(50,fillchar)
    print(("\n" if newline else "")+"+",x,"+")

def printSectionItem(message:str,startchar:str="|"):
    print(startchar,message)

def customInput(_prompt:str,hidden:bool=False,startchar="|",newline:bool=False)->str:
    if(hidden):
        return getpass(("\n" if newline else "")+startchar+" "+_prompt)
    else:
        return input(("\n" if newline else "")+startchar+" "+_prompt)

def printMenu(title:str,itemarray:list[tuple[str,any]],onclosefunction=None):
    itemarray.append(("Close",None))
    while(True):
        printSection(title,newline=True)
        for i in range(len(itemarray)):
            printSectionItem(str(i+1)+". "+itemarray[i][0])
        
        printSection()
        choose=customInput("Choose an Option: ",newline=True,startchar=">")
        try:
            if(int(choose)==len(itemarray)):
                onclosefunction()
                break
            itemarray[int(choose)-1][1]()
        except ValueError as e:
            printSectionItem("Error: Invalid Selection.Please type the number from the menu of your choice")

# User Define Functions
def userLogin():
    while(True):
        try:
            printSection("Login Credentials","-",newline=True)
            AppData.getUser(customInput("Username: ",startchar="|"),customInput("Password: ",hidden=True,startchar="|"))
            printSectionItem("Login Successful..")
            printSection(fillchar="-")
            break
        except Exception as e:
            printSectionItem("Error: "+str(e),startchar="!")
            printSection(fillchar="-")
            x=customInput("Retry...(Y/n): ",startchar=">",newline=True)
            if(x!="Y" and x!="y"):
                return None

    printMenu(AppData.curerntUser.name,[
        # Vault Specific
        "Show Vaults",
        "Use/Select Vault",
        "Add New Vaults",
        "Remove Vault",
        # User Specific
        "Show User Details"
        "Edit Name",
        "Update/Change Password",
        "Logout",
        "Delete Account",
    ])

def userRegister():
    printSection("Register User",fillchar="-",newline=True)
    uname=customInput("Name: ")
    username=customInput("Username: ")
    passwd=customInput("Password: ",hidden=True)
    printSectionItem("Security Question ...")
    for i in range(len(AppData.securityQuestions)):
        printSectionItem(str(i+1)+". "+AppData.securityQuestions[i])
    printSectionItem("-1. Cancel Registration")
    while(True):
        try:
            x=customInput("Select a Security Question Number: ",startchar=">")
            if(x=="-1"):
                print("Registration Canceled.")
                return
            y=customInput(AppData.securityQuestions[int(x)-1]+": ",startchar=">")
            AppData.addUser(uname,username,passwd,x,y)
            printSectionItem("User Added Sucessfully...")
            printSection()
            break
        except Exception as e:
            print(e)
            printSection()
            break

def userForgetPass():
    uname=customInput("Username: ")
    userindex=AppData.checkUsername(uname)
    if(userindex==-1):
        print("User Not Found")
        return
    
    print("Security Question ...")
    x=AppData.getUserSecurityQuestionIndex()
    y=customInput(AppData.securityQuestions[x],": ")
    AppData.getUser(uname,x,y)
    AppData.curerntUser.resetSecurityKey(customInput("New Password: "))
    print("Password Updated Sucessfully. Please login again.")


if(__name__=="__main__"):
    print("Welcome To PassBook")
    global AppData
    AppData=Model()
    printMenu("Menu",[
        ("Login",userLogin),
        ("Register User",userRegister),
        ("Forget Password",userForgetPass)
    ],lambda:print("Have a nice day..."))

