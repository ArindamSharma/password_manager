from .__init__ import Vault

if(__name__=="__main__"):
    print("Unit Testing ..."+__file__)
    a=Vault("vault1")
    a.addItem("Google","arindam","password@123","arindam",link="http://arindamsharma.github.io")
    a.addItem("Google1","arindam","password@123","arindam",link="http://arindamsharma.github.io")
    print(a)
    # print(a.getItem("Google3"))