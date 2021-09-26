from config_handler import os
from config_handler import json
from config_handler import Configuration
from tk_widget_handler import tk
from tk_widget_handler import WidgetHandler
from tk_widget_handler import print_master
from password_handler import pd
from password_handler import Passbook
from logger import Color
from logger import dt #datatime as dt
from logger import Logger
import sys
    
def window_exit():
    log.info(0,"Have a Nice Day")
    config.save();log.file(config.errorMessage)
    themeConfig.save();log.file(themeConfig.errorMessage)
    # widgetList.data=widget.get_all()
    widgetList.data=widget.get_root()
    widgetList.save();log.file(widgetList.errorMessage)
    log.close()
    widget.root['root'].destroy()

theme={
    0:[],
    1:[],
    2:[],
    3:[],
}
default_config={
    "theme":0,

    "log_filename":"./log/main.log",
    "config_filename":"./config/config.json",
    "theme_filename":"./config/theme.json",
    "structure_filename":"./config/structure.json",
    "widgetList_filename":"./config/widget_list.json",
    "passbook_filename":"./config/passbook.csv",

    "db_col":[
        "category",
        "subcateogry",
        "microcategory",
        "title",
        "email",
        "username",
        "password",
        "link",
        "data",
    ],
}
# Initilazing widget class
widget=WidgetHandler()

# Initializing main config file
config=Configuration(default_config["config_filename"],default_config)
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
log=Logger(config.data["log_filename"],eventHandler,5)
log.file(config.errorMessage)

# Initializing theme config
themeConfig=Configuration(default_config["theme_filename"],theme)
log.file(themeConfig.errorMessage)
# initializing password storage
passbook=Passbook(config.data["db_col"],config.data["passbook_filename"])

# initializing Root
widget.set_root("Password Manager",(800,560),(560,360),"../img/icon/logo1.png")

#Initalizing Structure (Optional) 
widgetList=Configuration(default_config["widgetList_filename"])
log.file(widgetList.errorMessage)

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

for widgetName,buttonText,iconPath in [
        ("searchButton","Search","../img/icon/home.png"),
        ("newVaultButton","New Vault","../img/icon/plus.png"),
        ("importButton","Import Vault","../img/icon/import.png"),
        ("exportButton","Export Vault","../img/icon/export.png"),
        ("settingButton","Setting","../img/icon/setting.png"),
    ]:
    widget.frame["homeMenuList"][widgetName]=widget.set_icon_button(widget.frame["homeMenuList"],buttonText,iconPath,anchor=tk.W,space_btw=2)
    widget.frame["homeMenuList"][widgetName]["root"].pack(side=tk.TOP,fill=tk.X,pady=10,padx=10)
widget.frame["homeMenuList"]["settingButton"]["root"].pack(side=tk.BOTTOM)

widget.view["home"]["right"]=widget.set_frame(widget.view["home"])
widget.view["home"]["right"]["root"].pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

# View Settings
widget.root["setting"]=widget.set_view("setting",widget.root)


# Things to do at last
# Raising View
widget.view["home"]["root"].tkraise()
# widget.view["setting"]["root"].tkraise()

# Debug
# print_master("master",widget.get_all())
widget.root["root"].protocol("WM_DELETE_WINDOW", window_exit)
widget.root["root"].mainloop()