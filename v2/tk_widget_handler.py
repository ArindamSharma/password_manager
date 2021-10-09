import tkinter as tk
from basic_func import print_master
class WidgetHandler:
    def __init__(self,):
        self.root={}
        self.view={"count":0}
        self.img={"count":0}
        self.icon={"count":0}

        self.canavas={"count":0}
        self.frame={"count":0}
        self.label={"count":0}
        self.button={"count":0}
        self.icon_button={"count":0}

    def set_root(self,title,size=(800,590),min_size=(560,360),favicon_path=None)->None:
        if(self.root!={}):
            raise Exception("Root can only be assigned once")
        self.root["widgetType"]="Root"
        self.root["root"]=tk.Tk()
        self.root["root"].title(title)
        self.root["root"].geometry("x".join([str(i) for i in size]))
        self.root["root"].grid_columnconfigure(0, weight=1)
        self.root["root"].grid_rowconfigure(0, weight=1)
        self.root["root"].minsize(*min_size)
        if (favicon_path!=None):
            self.root["root"].iconphoto(False, self.set_img(favicon_path,"small"))
            # self.root["root"].iconbitmap( dir_path+"logo1.png")
    
    def set_canavas(self,parent,canavas_id=None,**arg)->dict:
        self.__id_exist_check(self.canavas,canavas_id)
        if (canavas_id==None):canavas_id="canavas"+str(self.canavas["count"])
        self.canavas[canavas_id]={}
        self.canavas[canavas_id]["widgetType"]="Canavas"
        self.canavas[canavas_id]["root"]=tk.Canvas(parent["root"],**arg)
        self.canavas["count"]+=1
        return self.canavas[canavas_id]

    def set_view(self,view_id,parent,**arg)->dict:
        self.__id_exist_check(self.view,view_id)
        self.view[view_id]={}
        self.view[view_id]["widgetType"]="View"
        self.view[view_id]["root"]=tk.Frame(parent["root"],**arg)
        self.view[view_id]["root"].grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)
        self.view["count"]+=1
        return self.view[view_id]

    def set_frame(self,parent,frame_id=None,**arg)->dict:
        self.__id_exist_check(self.frame,frame_id)
        if (frame_id==None):frame_id="frame"+str(self.frame["count"])
        self.frame[frame_id]={}
        self.frame[frame_id]["widgetType"]="Frame"
        self.frame[frame_id]["root"]=tk.Frame(parent["root"],**arg)
        self.frame["count"]+=1
        return self.frame[frame_id]
 
    def set_img(self,file_path,size="medium")->tk.PhotoImage:
        """set_img(file_path,size=["root","small","medium","large","custom"]"""
        image_name=file_path.split("/")[-1].split(".")[0]
        try:
            tmp=self.img[image_name]
            try:
                return tmp[size]
            except (KeyError):
                if(size=="small"):
                    self.img[image_name]["small"]=self.img[image_name]["root"].subsample(4)
                elif(size=="medium"):
                    self.img[image_name]["medium"]=self.img[image_name]["root"].subsample(2)
                elif(size=="large"):
                    self.img[image_name]["large"]=self.img[image_name]["root"].zoom(3).subsample(4)
                elif(size=="root"):
                    return self.img[image_name]["root"]
                elif(size=="custom"):
                    try:
                        return self.img[image_name]["custom"]
                    except KeyError:
                        raise ValueError(size,"size needs to assigned manually")
                else:
                    raise ValueError(size," not a valid key ,Key must be from [root,small,medium,large]")
                return self.img[image_name][size]

        except (KeyError):
            self.img[image_name]={}
            self.img[image_name]["widgetType"]="PhotoImage"
            self.img[image_name]["root"]=tk.PhotoImage(file=file_path)
            self.img[image_name]["path"]=file_path
            self.img["count"]+=1
            return self.set_img(file_path,size)

    def set_icon(self,parent,icon_path,size="small",icon_id=None,**arg)->dict:
        self.__id_exist_check(self.icon,icon_id)
        if(icon_id==None):icon_id="icon"+str(self.icon["count"])
        self.icon[icon_id]={}
        self.icon[icon_id]["widgetType"]="Icon"
        self.icon[icon_id]["root"]=tk.Label(parent["root"],image=self.set_img(icon_path,size),**arg)
        self.icon[icon_id]["imgKey"]=icon_path.split("/")[-1].split(".")[0]
        self.icon["count"]+=1
        return self.icon[icon_id]

    def set_label(self,parent,label_message,label_id=None,**arg)->dict:
        self.__id_exist_check(self.label,label_id)
        if(label_id==None):label_id="label"+str(self.label["count"])
        self.label[label_id]={}
        self.label[label_id]["widgetType"]="Label"
        self.label[label_id]["labelText"]=tk.StringVar(parent["root"],label_message,label_message)
        self.label[label_id]["root"]=tk.Label(parent["root"],textvariable=self.label[label_id]["labelText"],**arg)
        self.label["count"]+=1
        return self.label[label_id]
 
    def set_button(self,parent,text,button_id=None,**arg)->dict:
        self.__id_exist_check(self.button,button_id)
        if(button_id==None):button_id="button"+str(self.button["count"])
        self.button[button_id]={}
        self.button[button_id]["widgetType"]="Button"
        self.button[button_id]["buttonText"]=tk.StringVar(parent["root"],text,button_id)
        self.button[button_id]["root"]=tk.Button(parent["root"],textvariable=self.button[button_id]["buttonText"],**arg)
        self.button["count"]+=1
        return self.button[button_id]

    def set_icon_button(self,parent,button_text,icon_path,button_id=None,icon_size="small",icon_side=tk.LEFT,space_btw=0,**arg)->dict:
        self.__id_exist_check(self.icon_button,button_id)
        button_text=space_btw*" "+button_text
        if(button_id==None):button_id="icon_button"+str(self.icon_button["count"])
        self.icon_button[button_id]={}
        self.icon_button[button_id]["widgetType"]="IconButton"
        self.icon_button[button_id]["buttonText"]=tk.StringVar(parent["root"],button_text,button_text)
        self.icon_button[button_id]["root"]=tk.Button(
            parent["root"],
            textvariable=self.icon_button[button_id]["buttonText"],
            image=self.set_img(icon_path,icon_size),
            compound=icon_side,
            **arg
        )
        self.icon_button["count"]+=1
        return self.icon_button[button_id]
    
    def __id_exist_check(self,variable,id)->bool:
        try:
            variable[id]
            raise Exception(id ," id already exist(id must be unique)")
        except KeyError:
            # "Not Exist"
            return True 

    def get_root(self)->dict:
        return self.root
    
    def get_view(self)->dict:
        return self.view
    
    def get_frame(self)->dict:
        return self.frame

    def get_canavas(self)->dict:
        return self.canavas
    
    def get_label(self)->dict:
        return self.label
    
    def get_icon(self)->dict:
        return self.icon
    
    def get_img(self)->dict:
        return self.img
    
    def get_icon_button(self)->dict:
        return self.icon_button
    
    def get_button(self,)->dict:
        return self.button

    def get_all(self)->dict:
        return {
            "root":self.get_root(),
            "view":self.get_view(),
            "frame":self.get_frame(),
            "canavas":self.get_canavas(),
            "icon":self.get_icon(),
            "img":self.get_img(),
            "label":self.get_label(),
            "button":self.get_button(),
            "icon_button":self.get_icon_button(),
        }
        
if __name__=="__main__":
    master=WidgetHandler()
    master.set_root("Testing",(800,560),(560,360),master.set_img("../img/icon/logo1.png","small"))
    master.root.mainloop()