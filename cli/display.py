from getpass import getpass

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

def singleInputMenu(title:str,itemArray:list[tuple[str,any]],onSucessClose=lambda:None,onErrorClose=None):
    """
    title:str,
    itemArray:tuple:[
        label:str,
        function:function(),
        ],
    onSucessClose:any,
    onErrorClose:any(if None its same as onSucessClose Function)
    """
    if onErrorClose==None:
        onErrorClose=onSucessClose

    itemArray.append(("Close",onSucessClose))
    try:
        while(True):
            printSection(title,newline=True)
            for i in range(len(itemArray)):
                printSectionItem(str(i+1)+". "+itemArray[i][0])
            printSection()
            
            choose=customInput("Choose an Option: ",newline=True,startchar=">")
            if(choose.isnumeric() and int(choose)<=len(itemArray)):
                itemArray[int(choose)-1][1]()
                if int(choose)==len(itemArray):
                    break
            else:
                printSectionItem("Error: Invalid Selection.Please type the number from the menu of your choice")
    
    except KeyboardInterrupt as e:
        print()
        onErrorClose()

def multiInputMenu(title:str,itemArray:list[tuple[str,bool,any,str]],onSucessClose=lambda:None,onErrorClose=None):
    """
    title:str,
    itemArray:tuple:[
        label:str,
        visibleInput:bool,
        validationFunction:function(1 parameter)=>bool,
        errorMessage:str
        ],
    onSucessClose:any,
    onErrorClose:any(if None its same as onSucessClose Function)

    """
    if onErrorClose==None:
        onErrorClose=onSucessClose

    printSection(title,"-",newline=True)

    try:
        for i in range(len(itemArray)):
            while(True):
                x=customInput(str(i+1)+". "+itemArray[i][0]+": ",not itemArray[i][1],">")
                #validation input
                if(itemArray[i][2](x)):
                    break
                else:
                    printSectionItem("Error: "+itemArray[i][3])
        
        printSection(fillchar="-")
        onSucessClose()

    except KeyboardInterrupt:
        print()
        onErrorClose()


if (__name__=="__main__"):
    multiInputMenu("Hello World",[
        ("Username",True,lambda e: True if e!="arindam" else False,"User Already Exisit"),
        ("Password",False,lambda e: True,"Incorrect Password"),
    ],lambda:print("Thankyou"),lambda:print("Unsucessfull Try"))

