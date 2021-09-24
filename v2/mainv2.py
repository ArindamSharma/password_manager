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
    config.save();log.onlylog(config.errorMessage)
    themeConfig.save();log.onlylog(themeConfig.errorMessage)
    widgetList.data=widget.get_all()
    widgetList.save();log.onlylog(widgetList.errorMessage)
    log.close()
    widget.root.destroy()

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

    "db_col":["category","subcateogry","microcategory","title","email","username","password","link","data"]
}
# Initilazing widget class
widget=WidgetHandler()

# Initializing main config file
config=Configuration(default_config["config_filename"],default_config)
# Initializing logger 
log=Logger(config.data["log_filename"],[0,1,2,3,4,5],5)
log.onlylog(config.errorMessage)

# Initializing theme config
themeConfig=Configuration(default_config["theme_filename"],theme)
log.onlylog(themeConfig.errorMessage)
# initializing password storage
passbook=Passbook(config.data["db_col"],config.data["passbook_filename"])

# initializing Root
widget.set_root("Password Manager",(800,560),(560,360),widget.set_img("../img/icon/logo1.png","small"))

#Initalizing Structure (Optional) 
widgetList=Configuration(default_config["widgetList_filename"],widget.get_all())
log.onlylog(widgetList.errorMessage)


widget.set_view("home",widget.root)
widget.view["home"]["head"]=widget.set_frame(widget.view["home"]["root"])
widget.view["home"]["body"]=widget.set_frame(widget.view["home"]["root"])
widget.set_view("setting",widget.root)


# Things to do at last
# print_master("master",widget.get_all())
widget.root.protocol("WM_DELETE_WINDOW", window_exit)
widget.root.mainloop()