from numpy.lib.index_tricks import fill_diagonal
from config_handler import json
from config_handler import Configuration
from tk_widget_handler import tk
from tk_widget_handler import WidgetHandler
from tk_widget_handler import print_master
from password_handler import pd
from password_handler import TagedPassbook
from logger import Color
from logger import dt #datatime as dt
from logger import Logger
import sys

# Button Functions >>>>>>>>>>>>>>>>>>

def searchButtonHome():
    log.debug(0,"SearchButton Clicked")
    pass

def newVaultButtonHome():
    passbook.addVault("Vault"+str(len(passbook)))
    log.debug(0,"NewVaultButton Clicked")
    pass

def settingButtonHome():
    log.debug(0,"SettingButton Clicked")
    pass

# Pre Define Functions >>>>>>>>>>>>>>>>>
def canavasConfigHome(e):
    widget.view["home"]["right"]["root"].config(scrollregion=widget.view["home"]["right"]["root"].bbox("all"))
    widget.view["home"]["right"]["root"].itemconfig(tk.ALL,width=e.width)

def window_exit():
    log.info(0,"Have a Nice Day")
    config.save();log.file(config.errorMessage)
    widgetList.data=widget.get_all()
    # widgetList.data=widget.get_root()
    widgetList.save();log.file(widgetList.errorMessage)
    log.close()
    widget.root['root'].destroy()

# Pre Define Variables >>>>>>>>>>>>>>>>.

defaultConfig={
    "filePath":{
        "Log":"./log/main.log",
        "Config":"./config/config.json",
        "Theme":"./config/theme.json",
        "Structure":"./config/structure.json",
        "WidgetList":"./config/widget_list.json",
        "PassBook":"./config/passbook.csv",
    },
    "Theme":{
        0:[],
        1:[],
        2:[],
        3:[],
    },
    "PassBook":{
        "Columns":["title","email","username","password","link","data"],
        "Tags":["College","Comapny","Personal","Intern","Games"],
    }
}
defaultConfig["PassBook"]["filePath"]=defaultConfig["filePath"]["PassBook"]
defaultConfig["Theme"]["filePath"]=defaultConfig["filePath"]["Theme"]
defaultConfig["Theme"]["current"]=defaultConfig["Theme"][0]

# Initilazing widget class
widget=WidgetHandler()

# Initializing main config file
config=Configuration(defaultConfig["filePath"]["Config"],defaultConfig)
# Initializing logger 
eventHandler=[
    # -1, # only shows in log 
    0, # only for debug message 
    1, # only for info message
    2, # only for error message
    3, # only for debug2 message
    4, # only for info2 message
    5, # only for error 2 message
]
log=Logger(config.data["filePath"]["Log"],eventHandler,5)
log.file(config.errorMessage)

# initializing password storage
passbook=TagedPassbook(
    column=config.data["PassBook"]["Columns"],
    filename=config.data["PassBook"]["filePath"],
    tags=config.data["PassBook"]["Tags"],
)

# Initalizing Structure (Optional) 
widgetList=Configuration(defaultConfig["filePath"]["WidgetList"])
log.file(widgetList.errorMessage)

# Initializing Root >>>>>>>>>>>>>>>>>>>>>

widget.set_root("Password Manager",(800,560),(560,360),"../img/icon/logo1.png")

# View Home
widget.root["home"]=widget.set_view("home",widget.root)

widget.view["home"]["left"]=widget.set_frame(widget.view["home"])
widget.view["home"]["left"]["root"].pack(side=tk.LEFT,fill=tk.BOTH)

widget.view["home"]["left"]["brandHead"]=widget.set_frame(widget.view["home"]["left"],"brandHead")
widget.view["home"]["left"]["brandHead"]["root"].pack(side=tk.TOP,fill=tk.X,expand=False,padx=10,pady=10)

widget.frame["brandHead"]["brandLogo"]=widget.set_icon(widget.view["home"]["left"]["brandHead"],"../img/icon/logo1","small")
widget.frame["brandHead"]["brandLogo"]["root"].pack(side=tk.LEFT,fill=tk.Y,expand=True)

widget.frame["brandHead"]["brandLabel"]=widget.set_label(widget.view["home"]["left"]["brandHead"],"AceVault",font=("Sans",22,"italic"))
widget.frame["brandHead"]["brandLabel"]["root"].pack(side=tk.LEFT,fill=tk.Y,expand=True)

widget.view["home"]["left"]["menuList"]=widget.set_frame(widget.view["home"]["left"],"homeMenuList")
widget.view["home"]["left"]["menuList"]["root"].pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

for widgetName,buttonText,iconPath,function in [
        ("searchButton","Search","../img/icon/home.png",searchButtonHome),
        ("newVaultButton","New Vault","../img/icon/plus.png",newVaultButtonHome),
        # ("importButton","Import Vault","../img/icon/import.png",importButtonHome),
        # ("exportButton","Export Vault","../img/icon/export.png",exportButtonHome),
        ("settingButton","Setting","../img/icon/setting.png",settingButtonHome),
    ]:
    widget.frame["homeMenuList"][widgetName]=widget.set_icon_button(widget.frame["homeMenuList"],buttonText,iconPath,anchor=tk.W,space_btw=2,command=function)
    widget.frame["homeMenuList"][widgetName]["root"].pack(side=tk.TOP,fill=tk.X,pady=10,padx=10)
widget.frame["homeMenuList"]["settingButton"]["root"].pack(side=tk.BOTTOM)

widget.view["home"]["right"]=widget.set_canavas(widget.view["home"],bg="green",canavas_id="homeCanavas",highlightthickness=0)
widget.view["home"]["right"]["root"].pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=5)

for vaultName,vaultCount in [
    ("vault_1",32),
    ("vault_2",13),
    ("vault_3",30),
    ]:
    widget.canavas["homeCanavas"]["frame_"+vaultName]=widget.set_canavas_custom_frame1(widget.canavas["homeCanavas"],frame_id="frame_"+vaultName,height=150)
    
    widget.frame["frame_"+vaultName]["head"]=widget.set_frame(widget.frame["frame_"+vaultName])
    widget.frame["frame_"+vaultName]["head"]["root"].pack(side=tk.TOP,fill=tk.X)

    for buttonName,buttonText in [
        ("exportVaultButton","Export"),
        ("deleteVaultButton","Delete"),
        ("editButton","Edit"),
        ]:
        widget.frame["frame_"+vaultName]["head"][buttonName]=widget.set_button(widget.frame["frame_"+vaultName]["head"],buttonText)
        widget.frame["frame_"+vaultName]["head"][buttonName]["root"].pack(side=tk.RIGHT,padx=5)

    widget.frame["frame_"+vaultName]["body"]=widget.set_frame(widget.frame["frame_"+vaultName],bg="pink")
    widget.frame["frame_"+vaultName]["body"]["root"].pack(side=tk.BOTTOM,fill=tk.BOTH)

    widget.frame["frame_"+vaultName]["body"]["vaultName"]=widget.set_label(widget.frame["frame_"+vaultName]["body"],vaultName)
    widget.frame["frame_"+vaultName]["body"]["vaultName"]["root"].pack(side=tk.BOTTOM,fill=tk.BOTH)


widget.view["home"]["right"]["root"].bind("<Configure>",func=canavasConfigHome)
widget.view["home"]["right"]["root"].bind_all("<MouseWheel>",lambda e: widget.view["home"]["right"]["root"].yview_scroll(int(-1*e.delta/120),tk.UNITS))

# log.debug(0,passbook.getVaultCount())

# View Settings
widget.root["setting"]=widget.set_view("setting",widget.root)


# Things to do at last >>>>>>>>>>>>>>>>>>>>>>>>

# Raising View
widget.view["home"]["root"].tkraise()
# widget.view["setting"]["root"].tkraise()

# Debug
# print_master("master",widget.get_all())

# Running Main Loop >>>>>>>>>>>>>>>>>>>>>>>>>

widget.root["root"].protocol("WM_DELETE_WINDOW", window_exit)
widget.root["root"].mainloop()