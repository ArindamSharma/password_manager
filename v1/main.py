def print_debug(*strings):
    if (env in ["debug","onlydebug"]):
        print("[ Debug ]:","".join([str(i) for i in strings]))
        # print("".join([str(i) for i in strings]))
def print_info(*strings):
    if (env in ["info","debug","onlyinfo"]):
        print("[ Info ]:","".join([str(i) for i in strings]))
        # print("".join([str(i) for i in strings]))

def print_master(name,data,indent=4,start_space=""):
    tab=" "*indent
    if (type(data)==type({}) ):
        if(len(data)==0):
            print_debug(start_space,name," : {},")
        else:
            print_debug(start_space,name," : {")
            for i in data:
                print_master(i,data[i],start_space=tab+start_space)
            print_debug(start_space,"},")
    elif (type(data)==type(()) or type(data)==type([]) ):
        if(len(data)==0):
            print_debug(start_space,name," : []")
        else:    
            print_debug(start_space,name," : [")
            for i in data:
                print_master("item",i,start_space=tab+start_space)
            print_debug(start_space,"],")
    else:
        print_debug(start_space,name," : ",data,",")

def update_config(mode="read"):
    status="Not Found"
    if(mode=="read" and os.path.isfile(master["config"]["filename"]) ):
        master["config"]["file"]=open(master["config"]["filename"],"r")
        tmp={}
        # tmp=json.load(master["config"]["file"])
        try:
            tmp=json.load(master["config"]["file"])
        except(json.JSONDecodeError):
            update_config("write")

        print_debug("Checking parameters in Config File")
        for required_key in master["config"]["filedata"].keys():
            if required_key not in tmp.keys():
                print_debug("Keys Mismatch")
                return update_config("write")

        print_debug("Checked Sucessfully")
        master["config"]["filedata"]=tmp
        status="Found"
    else:
        master["config"]["file"]=open(master["config"]["filename"],"w")
        json.dump(master["config"]["filedata"],master["config"]["file"],indent=4,default=lambda e : e.__str__())
        status="updated"

    master["config"]["file"].close()
    print_debug("Config File : ",status)

def window_exit():
    print_info("Have a Nice Day")
    update_config("write")
    master["data"]["database"].csv("store")
    master["root"].destroy()

def canvas_config(e):
    master["view"]["home"]["right_sec"]["canavas"]["root"].config(scrollregion=master["view"]["home"]["right_sec"]["canavas"]["root"].bbox("all"))
    # print_debug(e)
    master["view"]["home"]["right_sec"]["canavas"]["root"].itemconfig(tk.ALL,width=e.width)
    # master["view"]["home"]["right_sec"]["canavas"]["root"].itemconfig(f4_inner_frame_id,x=(e.width-thumb_width)/2)

def color_change(color_list,color_index):
    def button_color(widget,bg_color,bg_on_hover,fg_color,fg_color_on_hover,cfont=("Arial",12)):
        widget.config(
            bd=0,font=cfont,
            bg=bg_color,
            activebackground=bg_color,
            fg=fg_color
        )
        widget.config(anchor=tk.W)
        widget.bind("<Enter>",func=lambda e: widget.config(fg=fg_color_on_hover))
        widget.bind("<Leave>",func=lambda e: widget.config(fg=fg_color))

    def button_type1(widget):
        bg_color=color_list[color_index][1]
        bg_color_on_hover=None
        fg_color=color_list[color_index][-1]
        fg_color_on_hover=color_list[color_index][-3]
        button_color(widget,bg_color,bg_color_on_hover,fg_color,fg_color_on_hover)

    def button_type2(widget):
        bg_color=color_list[color_index][3]
        bg_color_on_hover=None
        fg_color=color_list[color_index][0]
        fg_color_on_hover=color_list[color_index][-3]
        button_color(widget,bg_color,bg_color_on_hover,fg_color,fg_color_on_hover)
        
    def button_type3(widget):
        bg_color=color_list[color_index][-3]
        bg_color_on_hover=None
        fg_color=color_list[color_index][1]
        fg_color_on_hover=color_list[color_index][3]
        button_color(widget,bg_color,bg_color_on_hover,fg_color,fg_color_on_hover)

    def button_type4(widget):
        bg_color=color_list[color_index][-3]
        bg_color_on_hover=None
        fg_color="black"
        fg_color_on_hover=color_list[color_index][3]
        button_color(widget,bg_color,bg_color_on_hover,fg_color,fg_color_on_hover,("Arial",20))
        
    # Root
    master["root"].configure(bg=color_list[color_index][0])
    
    # F1 Root
    master["view"]["home"]["root"].config(bg=color_list[color_index][0])
    
    # F1 Root Left 
    master["view"]["home"]["left_sec"]["root"].config(bg=color_list[color_index][0])
    master["view"]["home"]["left_sec"]["head"]["root"].config(bg=color_list[color_index][0])
    master["view"]["home"]["left_sec"]["head"]["icon"].config(bg=color_list[color_index][0])
    master["view"]["home"]["left_sec"]["head"]["label"]["root"].config(bg=color_list[color_index][0],fg=color_list[color_index][-1])
    master["view"]["home"]["left_sec"]["menu"]["root"].config(bg=color_list[color_index][1])
    
    for button_widget in [master["view"]["home"]["left_sec"]["menu"]["button"][i]["root"] for i in master["view"]["home"]["left_sec"]["menu"]["button"].keys()]:
        button_widget.config(bg=color_list[color_index][1])
        button_type1(button_widget)

    # F1 Root Right
    master["view"]["home"]["right_sec"]["root"].config(bg=color_list[color_index][-4])
    master["view"]["home"]["right_sec"]["canavas"]["root"].config(bg=color_list[color_index][-4])
    master["view"]["home"]["right_sec"]["head"]["root"].config(bg=color_list[color_index][3])

    master["view"]["home"]["right_sec"]["head"]["search_box"]["root"].config(bg=color_list[color_index][3])
    button_type2(master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["close_button"]["root"])
    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["close_button"]["root"].config(bg="white",activebackground="white")
    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["root"].config(bg="white")
    button_type2(master["view"]["home"]["right_sec"]["head"]["search_box"]["search_button"]["root"])

    master["view"]["home"]["right_sec"]["head"]["user_button"]["root"].config(bg=color_list[color_index][3])
    button_type2(master["view"]["home"]["right_sec"]["head"]["user_button"]["root"])

    for frame_name in list(master["view"]["home"]["right_sec"]["canavas"].keys())[1:]:    
        for button_widget in [master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"][button_name]["root"] for button_name in list(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"].keys())[1:]]:
            button_widget.config(bg=color_list[color_index][1])
            button_type3(button_widget)
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["root"].config(bg=color_list[color_index][-3])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]["root"].config(bg=color_list[color_index][-3])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]["icon"]["label"].config(bg=color_list[color_index][-3])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["root"].config(bg=color_list[color_index][-3])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"]["root"].config(bg=color_list[color_index][-3])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["root"].config(bg=color_list[color_index][-3])
        button_type4(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["vault_button"]["root"])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["entry_number"]["root"].config(bg=color_list[color_index][-3])

def main():
    global master
    # Master Data
    master={
        "root":None,
        "view":{},
        "icon":{},
        "data":{
            "database":passbook(["category","subcateogry","microcategory","title","email","username","password","link","data"],"password_db.csv"),    
            "category":["Company","Personal","College"],
            "subcategory":["Intern/Job","Education","SocialMedia","Coding","Other","Software","Mobile","Shopping","Banking","Licenced","OTP Based","Gaming"],
            "microcategory":[],
        },
        "theme":{
            # Dark to Light
            "theme1":["#03071E", "#370617", "#6A040F", "#9D0208", "#D00000", "#DC2F02", "#E85D04", "#F48C06", "#FAA307", "#FFBA08"],
            "theme2":["#212529", "#343A40", "#495057", "#6C757D", "#ADB5BD", "#CED4DA", "#DEE2E6", "#E9ECEF", "#F8F9FA"],
            "theme3":["#583101", "#603808", "#6F4518", "#8B5E34", "#A47148", "#BC8A5F", "#D4A276", "#E7BC91", "#F3D5B5", "#FFEDD8"],
            "theme4":["#10002B", "#240046", "#3C096C", "#5A189A", "#7B2CBF", "#9D4EDD", "#C77DFF", "#E0AAFF"],
            "theme5":["#036666", "#14746F", "#248277", "#358F80", "#469D89", "#56AB91", "#67B99A", "#78C6A3", "#88D4AB", "#99E2B4"],
            "theme6":["#03045E", "#0077B6", "#00B4D8", "#90E0EF", "#CAF0F8"], 
            "theme7":["#47126B", "#571089", "#6411AD", "#6D23B6", "#822FAF", "#973AA8", "#AC46A1", "#C05299", "#D55D92", "#EA698B"],
        },
        "config":{
            "file":None,
            "filename":__file__.split(".")[0]+"_config.json",
            "filedata":{
                "config_theme":"theme3",
                "structure":None,
                "vault_count":3,
            },
        },
    }
    # Loading Configration Files
    update_config("read")
    master["data"]["database"].csv("load")
    
    master["root"] = tk.Tk()
    master["root"].title("Password Manager")
    master["root"].geometry("800x580")
    
    # icons Defination
    dir_path= "../img/icon/"
    for icon_path in os.listdir(dir_path):
        master["icon"][icon_path[:-4]]={}
        master["icon"][icon_path[:-4]]["location"]= dir_path+icon_path
        master["icon"][icon_path[:-4]]["small"]=tk.PhotoImage(file = dir_path+icon_path).subsample(4)
        master["icon"][icon_path[:-4]]["medium"]=tk.PhotoImage(file = dir_path+icon_path).subsample(2)
        master["icon"][icon_path[:-4]]["large"]=tk.PhotoImage(file = dir_path+icon_path).zoom(3).subsample(4)

    master["root"].iconphoto(False, master["icon"]["logo1"]["small"])
    # master["root"].iconbitmap( dir_path+"logo1.png")
    master["root"].grid_columnconfigure(0, weight=1)
    master["root"].grid_rowconfigure(0, weight=1)
    master["root"].minsize(560, 360)

    # |Root Frame 1
    master["view"]["home"]={}

    master["view"]["home"]["root"]=tk.Frame(master["root"],)
    master["view"]["home"]["root"].grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)

    # ||F1 Left Side
    master["view"]["home"]["left_sec"]={}
    master["view"]["home"]["left_sec"]["root"]=tk.Frame(master["view"]["home"]["root"])
    master["view"]["home"]["left_sec"]["root"].pack(side=tk.LEFT,fill=tk.BOTH)

    # |||F1 Left Side Head
    master["view"]["home"]["left_sec"]["head"]={}
    master["view"]["home"]["left_sec"]["head"]["root"]=tk.Frame(master["view"]["home"]["left_sec"]["root"])
    master["view"]["home"]["left_sec"]["head"]["root"].pack(side=tk.TOP,fill=tk.X,padx=20)

    master["view"]["home"]["left_sec"]["head"]["icon"]=tk.Label(master["view"]["home"]["left_sec"]["head"]["root"],image=master["icon"]["logo1"]["small"])
    master["view"]["home"]["left_sec"]["head"]["icon"].pack(side=tk.LEFT,fill=tk.X,pady=10)

    master["view"]["home"]["left_sec"]["head"]["label"]={}
    master["view"]["home"]["left_sec"]["head"]["label"]["name"]=tk.StringVar(master["view"]["home"]["left_sec"]["head"]["root"],"AceVault","AceVault",)
    master["view"]["home"]["left_sec"]["head"]["label"]["root"]=tk.Label(master["view"]["home"]["left_sec"]["head"]["root"],textvariable=master["view"]["home"]["left_sec"]["head"]["label"]["name"],font=("Sans",22,"italic"))
    master["view"]["home"]["left_sec"]["head"]["label"]["root"].pack(side=tk.LEFT,fill=tk.BOTH,padx=5)

    # |||F1 Left Side Menu
    master["view"]["home"]["left_sec"]["menu"]={}
    master["view"]["home"]["left_sec"]["menu"]["root"]=tk.Frame(master["view"]["home"]["left_sec"]["root"])
    master["view"]["home"]["left_sec"]["menu"]["root"].pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

    # # ||||F1 Left Side Menu Buttons
    master["view"]["home"]["left_sec"]["menu"]["button"]={}
    for button,button_name,button_icon in [
            # ("dashboard_button","Dashboard",master["icon"]["vault"]["small"]),
            ("search_vault_button","Search",master["icon"]["home"]["small"]),
            ("new_vault_button","New Vault",master["icon"]["plus"]["small"]),
            ("export_vault_button","Export Vault",master["icon"]["export"]["small"]),
            # ("export_all_vault_button","Export All Vault",master["icon"]["export"]["small"]),
            # ("export_selective_vault_button","Export Selected Vault",master["icon"]["export"]["small"]),
            # ("delete_all_vault_button","Delete All Vault",master["icon"]["export"]["small"]),
            # ("delete_selective_vault_button","Delete Selected Vault",master["icon"]["export"]["small"]),
            ("import_vault_button","Import Vault",master["icon"]["import"]["small"]),
            ("setting_button","Setting",master["icon"]["setting"]["small"]),
        ]:
        master["view"]["home"]["left_sec"]["menu"]["button"][button]={}
        master["view"]["home"]["left_sec"]["menu"]["button"][button]["name"]=tk.StringVar(master["view"]["home"]["left_sec"]["menu"]["root"],"  "+button_name,button_name)
        master["view"]["home"]["left_sec"]["menu"]["button"][button]["root"]=tk.Button(master["view"]["home"]["left_sec"]["menu"]["root"],textvariable=master["view"]["home"]["left_sec"]["menu"]["button"][button]["name"],image=button_icon)

    for button_widget in [master["view"]["home"]["left_sec"]["menu"]["button"][i]["root"] for i in master["view"]["home"]["left_sec"]["menu"]["button"].keys()]:    
        button_widget.config(compound=tk.LEFT)
        button_widget.pack(fill=tk.BOTH,padx=20,pady=10)

    master["view"]["home"]["left_sec"]["menu"]["button"]["setting_button"]["root"].pack(side=tk.BOTTOM,pady=20)

    # ||F1 Right Side
    master["view"]["home"]["right_sec"]={}
    master["view"]["home"]["right_sec"]["root"]=tk.Frame(master["view"]["home"]["root"],)
    master["view"]["home"]["right_sec"]["root"].pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

    # ||| F1 Right Side Head
    master["view"]["home"]["right_sec"]["head"]={}
    master["view"]["home"]["right_sec"]["head"]["root"]=tk.Frame(master["view"]["home"]["right_sec"]["root"])
    master["view"]["home"]["right_sec"]["head"]["root"].pack(side=tk.TOP,fill=tk.X)

    # ||| F1 Right Side Head Search Frame
    master["view"]["home"]["right_sec"]["head"]["search_box"]={}
    master["view"]["home"]["right_sec"]["head"]["search_box"]["root"]=tk.Frame(master["view"]["home"]["right_sec"]["head"]["root"])
    master["view"]["home"]["right_sec"]["head"]["search_box"]["root"].pack(side=tk.LEFT,fill=tk.X,pady=10,padx=10)

    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]={}
    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["root"]=tk.Frame(master["view"]["home"]["right_sec"]["head"]["search_box"]["root"])
    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["root"].pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["entry"]=tk.Entry(master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["root"],border=5,relief=tk.FLAT)
    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["entry"].pack(fill=tk.X,side=tk.LEFT)

    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["close_button"]={}
    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["close_button"]["name"]=tk.StringVar(master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["root"],None,"close_button")
    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["close_button"]["root"]=tk.Button(master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["root"],image=master["icon"]["close"]["small"])
    master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["close_button"]["root"].pack(fill=tk.BOTH,side=tk.RIGHT,expand=True,padx=5)
    # master["view"]["home"]["right_sec"]["head"]["search_box"]["input"]["close_button"]["root"]["state"]=tk.DISABLED

    master["view"]["home"]["right_sec"]["head"]["search_box"]["search_button"]={}
    master["view"]["home"]["right_sec"]["head"]["search_box"]["search_button"]["name"]=tk.StringVar(master["view"]["home"]["right_sec"]["head"]["search_box"]["root"],None,"search_button")
    master["view"]["home"]["right_sec"]["head"]["search_box"]["search_button"]["root"]=tk.Button(master["view"]["home"]["right_sec"]["head"]["search_box"]["root"],image=master["icon"]["search2"]["small"])
    master["view"]["home"]["right_sec"]["head"]["search_box"]["search_button"]["root"].pack(fill=tk.X,side=tk.RIGHT)
    # master["view"]["home"]["right_sec"]["head"]["search_box"]["search_button"]["root"]["state"]=tk.DISABLED

    # ||| F1 Right Side Head User
    master["view"]["home"]["right_sec"]["head"]["user_button"]={}
    master["view"]["home"]["right_sec"]["head"]["user_button"]["name"]=tk.StringVar(master["view"]["home"]["right_sec"]["head"]["root"],"  User 1","  User 1")
    master["view"]["home"]["right_sec"]["head"]["user_button"]["root"]=tk.Button(master["view"]["home"]["right_sec"]["head"]["root"],textvariable=master["view"]["home"]["right_sec"]["head"]["user_button"]["name"],image=master["icon"]["user"]["small"],compound=tk.LEFT)
    master["view"]["home"]["right_sec"]["head"]["user_button"]["root"].pack(side=tk.RIGHT,padx=10)
    
    # ||| F1 Right Side Body
    master["view"]["home"]["right_sec"]["canavas"]={}
    master["view"]["home"]["right_sec"]["canavas"]["root"]=tk.Canvas(master["view"]["home"]["right_sec"]["root"],highlightthickness=0)
    master["view"]["home"]["right_sec"]["canavas"]["root"].pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True,padx=10,pady=10)

    for entry in range(master["config"]["filedata"]["vault_count"]):
        frame_name="frame"+str(entry)
        master["view"]["home"]["right_sec"]["canavas"][frame_name]={}
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["root"]=tk.Frame(master["view"]["home"]["right_sec"]["canavas"]["root"],bg="green")
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["index"]=entry
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["height"]=150
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["width"]=0
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["spacing"]=10
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["xy"]=(0,entry*(master["view"]["home"]["right_sec"]["canavas"][frame_name]["height"]+master["view"]["home"]["right_sec"]["canavas"][frame_name]["spacing"]))
        master["view"]["home"]["right_sec"]["canavas"]["root"].create_window(master["view"]["home"]["right_sec"]["canavas"][frame_name]["xy"],window=master["view"]["home"]["right_sec"]["canavas"][frame_name]["root"],anchor=tk.NW,width=master["view"]["home"]["right_sec"]["canavas"][frame_name]["width"],height=master["view"]["home"]["right_sec"]["canavas"][frame_name]["height"])
        
        # Inner Structure
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]={}
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]["root"]=tk.Frame(master["view"]["home"]["right_sec"]["canavas"][frame_name]["root"])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]["root"].pack(side=tk.LEFT,fill=tk.Y)

        master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]["icon"]={}
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]["icon"]["location"]=None
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]["icon"]["label"]=tk.Label(master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]["root"],image=master["icon"]["vault"]["large"])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["left_sec"]["icon"]["label"].pack(fill=tk.BOTH,expand=True,padx=20)
        
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]={}
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["root"]=tk.Frame(master["view"]["home"]["right_sec"]["canavas"][frame_name]["root"])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["root"].pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)
        
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"]={}
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"]["root"]=tk.Frame(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["root"])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"]["root"].pack(side=tk.TOP,fill=tk.X)

        for head_button,button_name in [
                ("saveas_button","Save As"),
                ("export_button","Export"),
                ("delete_button","Delete"),
                ("edit_button","Edit"),
            ]:    
            master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"][head_button]={}
            master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"][head_button]["name"]=tk.StringVar(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"]["root"],button_name,head_button)
            master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"][head_button]["root"]=tk.Button(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"]["root"],textvariable=master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"][head_button]["name"],anchor=tk.W)
            master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["head"][head_button]["root"].pack(side=tk.RIGHT,padx=5)

        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]={}
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["root"]=tk.Frame(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["root"],bg="blue")
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["root"].pack(side=tk.BOTTOM,fill=tk.X,expand=True)

        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["vault_button"]={}
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["vault_button"]["name"]=tk.StringVar(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["root"],"Vault "+frame_name[5:],"Vault "+frame_name[5:])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["vault_button"]["root"]=tk.Button(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["root"],textvariable=master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["vault_button"]["name"],anchor=tk.W,font=("Arial",20))
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["vault_button"]["root"].pack(fill=tk.X)

        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["entry_number"]={}
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["entry_number"]["name"]=tk.StringVar(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["root"],"Entry : 10","Entry Number"+frame_name[5:])
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["entry_number"]["root"]=tk.Label(master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["root"],textvariable=master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["entry_number"]["name"],anchor=tk.W)
        master["view"]["home"]["right_sec"]["canavas"][frame_name]["right_sec"]["body"]["entry_number"]["root"].pack(fill=tk.X)

    master["view"]["home"]["right_sec"]["canavas"]["root"].bind("<Configure>",func=canvas_config)
    master["view"]["home"]["right_sec"]["canavas"]["root"].bind_all("<MouseWheel>",lambda e: master["view"]["home"]["right_sec"]["canavas"]["root"].yview_scroll(int(-1*e.delta/120),tk.UNITS))
    
    # |F2 Root Setting
    master["view"]["view_2"]={}
    master["view"]["view_2"]["root"]=tk.Frame(master["root"],bg="green")
    master["view"]["view_2"]["root"].grid(row=0,column=0,)

    master["view"]["view_2"]["head"]={}
    master["view"]["view_2"]["head"]["root"]=tk.Frame(master["view"]["view_2"]["root"],bg="blue")
    master["view"]["view_2"]["head"]["root"].pack(side=tk.TOP,fill=tk.X,expand=True)

    master["view"]["view_2"]["head"]["title"]={}
    master["view"]["view_2"]["head"]["title"]["name"]=tk.StringVar(master["view"]["view_2"]["head"]["root"],"Message Box","Message Box")
    master["view"]["view_2"]["head"]["title"]["root"]=tk.Label(master["view"]["view_2"]["head"]["root"],textvariable=master["view"]["view_2"]["head"]["title"]["name"])
    master["view"]["view_2"]["head"]["title"]["root"].pack(side=tk.LEFT,fill=tk.X,expand=True)
    
    master["view"]["view_2"]["head"]["close_button"]={}
    master["view"]["view_2"]["head"]["close_button"]["name"]=tk.StringVar(master["view"]["view_2"]["head"]["root"],"close_button","close_button")
    master["view"]["view_2"]["head"]["close_button"]["root"]=tk.Button(master["view"]["view_2"]["head"]["root"],image=master["icon"]["close"]["small"])
    master["view"]["view_2"]["head"]["close_button"]["root"].pack(side=tk.RIGHT,fill=tk.Y)

    master["view"]["view_2"]["container"]={} 
    master["view"]["view_2"]["container"]["root"]=tk.Frame(master["view"]["view_2"]["root"],bg="red")
    master["view"]["view_2"]["container"]["root"].pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

    master["view"]["view_2"]["container"]["message_body"]=tk.Label(master["view"]["view_2"]["container"]["root"],text="Hello this is a test message kindly ignore")
    master["view"]["view_2"]["container"]["message_body"].pack(expand=True,padx=80,pady=100)

    # Root Frame 3
    # import vault_view
    master["view"]["vault_view"]={}
    master["view"]["vault_view"]["root"]=tk.Frame(master["root"],)
    master["view"]["vault_view"]["root"].grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)

    master["view"]["vault_view"]["head"]={}
    master["view"]["vault_view"]["head"]["root"]=tk.Frame(master["view"]["vault_view"]["root"],bg="blue")
    master["view"]["vault_view"]["head"]["root"].pack(side=tk.TOP,fill=tk.X)
    
    master["view"]["vault_view"]["body"]={} 
    master["view"]["vault_view"]["body"]["root"]=tk.Frame(master["view"]["vault_view"]["root"],bg="red")
    master["view"]["vault_view"]["body"]["root"].pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    
    # Raise Frame
    # master["view"]["home"]["root"].tkraise()
    # master["view"]["home"]["root"].configure(state=tk.DISABLED)
    # master["view"]["view_2"]["root"].tkraise()
    master["view"]["vault_view"]["root"].tkraise()
    
    # Color Setting
    color_change(master["theme"],master["config"]["filedata"]["config_theme"])

    master["root"].protocol("WM_DELETE_WINDOW", window_exit)
    # master["root"].overrideredirect(1)
    
    master["config"]["filedata"]["structure"]=master["view"]
    master["config"]["filedata"]["icon"]=master["icon"]
    # Printing
    print_info("AcePass : Password Manger")
    # print_debug(master)
    # print_master("master",master)
    # print_master("View",master["view"])
    # print_master("Config",master["config"])
    # print_master("Icons",master["icon"])
    # print_debug(master["data"]["database"].show())

    master["root"].mainloop()

if __name__=="__main__":
    import tkinter as tk
    import pandas as pd
    import sys,os
    from PIL import Image
        
    import json 
    class passbook:
        def __init__(self,column,filename):
            self.database=pd.DataFrame(columns=column)
            self.db_filename=filename
            self.index=0
        
        def show(self):
            return self.database
        
        def save(self):
            self.database.to_csv(self.db_filename)
            print_debug("Database Saved")
        
        def append(self,itemlist):
            self.database.loc[self.index]=itemlist
            self.index+=1

        def csv(self,mode="load"):
            status="Found DB"
            if(mode=="load" and os.path.isfile("./"+self.db_filename)):
                self.database=pd.read_csv("./"+self.db_filename)
            else:
                self.database.to_csv("./"+self.db_filename,index=False)
                status="Updated DB"
            print_debug("Database Updation : ",status)

    # class node:
    #     def __init__(self,node_type,parent=None,):
    #         self.type=node_type
    #         self.name=node_type
    #         self.parent=None
    #         self.child={}
    #         if(self.type=="main"):
    #             self.root=tk.Tk()
    #             self.parent=None
    #         if(self.type=="view"):
    #             self.root=tk.Frame(parent)
    #     def create_view(self,view_name,sticky=tk.N+tk.E+tk.W+tk.S,):
    #         self.child[self.name]=node("view",self)
    #         self.child[self.name].grid(row=0,column=0,sticky=sticky)
    #         return self.child[self.name]
    #     def grid(self,row,column,sticky):
    #         self.root.grid(row=row,column=column,sticky=sticky)
    
    env=None
    if(len(sys.argv)>1):
        env=sys.argv[1]
    main()