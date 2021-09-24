import tkinter as tk
from basic_func import print_master
class WidgetHandler:
    def __init__(self,):
        self.root=tk.Tk()
        self.view={}
        self.img_obj={}
        self.img={}
        self.frame={}
        self.label={}
        self.button={}
        self.icon_button={}

    def set_img(self,file_path,size="medium"):
        """set_img(file_path,size=["small","medium","large"]"""
        image_name=file_path.split("/")[-1].split(".")[0]
        try:
            if(size=="small"):
                self.img[image_name]["small"]=self.img[image_name]["root"].subsample(4)
            elif(size=="medium"):
                self.img[image_name]["medium"]=self.img[image_name]["root"].subsample(2)
            elif(size=="large"):
                self.img[image_name]["large"]=self.img[image_name]["root"].zoom(3).subsample(4)
            else:
                raise ValueError(size," not a valid key ,Key must be from [small ,medium ,large]")
            return self.img[image_name][size]
        except (KeyError):
            self.img_obj[image_name]={}
            self.img_obj[image_name]["widgetType"]="PhotoImage"
            self.img_obj[image_name]["root"]=tk.PhotoImage(file=file_path)
            self.img_obj[image_name]["path"]=file_path
            self.img[image_name]={}
            self.img[image_name]["widgetType"]="PhotoImage"
            self.img[image_name]["root"]=self.img_obj[image_name]["root"]
            return self.set_img(self.img_obj[image_name]["path"],size)

    def set_label(self,parent,label_message):
        tmp={}
        tmp["name"]=tk.StringVar(parent,label_message,"label"+str(len(self.label)))
        tmp["root"]=tk.Label(parent,textvariable=tmp["name"],)
        self.label["label"+len(self.label)]=tmp
        return tmp

    def set_frame(self,parent,bg="white"):
        frame_number=str(len(self.frame))
        self.frame["frame"+frame_number]={}
        self.frame["frame"+frame_number]["widgetType"]="Frame"
        self.frame["frame"+frame_number]["root"]=tk.Frame(parent,bg=bg)
        return self.frame["frame"+frame_number]
    
    def set_view(self,view_name,parent,bg="white"):
        self.view[view_name]={}
        self.view[view_name]["widgetType"]="View"
        self.view[view_name]["root"]=tk.Frame(parent,bg=bg)
        self.view[view_name]["root"].grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)
        return self.view[view_name]

    def set_root(self,title,size=(800,590),min_size=(560,360),favicon=None):
        self.root.title(title)
        self.root.geometry("x".join([str(i) for i in size]))
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.minsize(*min_size)
        if (favicon!=None):
            self.root.iconphoto(False, favicon)
            # self.root.iconbitmap( dir_path+"logo1.png")
    
    def set_button(self,parent,text,button_name=None):
        if(button_name==None):
            button_name="button"+str(len(self.button))
        tmp={}
        tmp["name"]=tk.StringVar(parent,text,button_name)
        tmp["root"]=tk.Button(parent,textvariable=tmp["name"],)
        self.button[button_name]=tmp
        return tmp

    def set_icon_button(self,parent,button_text,button_name,icon_path,icon_size="small"):
        if(button_name==None):
            button_name="icon_button"+len(self.icon_button)
        tmp={}
        tmp["name"]=tk.StringVar(parent,button_text,button_name)
        tmp["root"]=tk.Button(parent,textvariable=tmp["name"],)
        self.icon_button[button_name]=tmp
        return tmp

    def get_all(self):
        return {
            "view":self.view,
            "img":self.img,
            "img_obj":self.img_obj,
            "frame":self.frame,
            "label":self.label,
            "button":self.button,
            "icon_button":self.icon_button,
        }
if __name__=="__main__":
    master=WidgetHandler()
    master.set_root("Testing",(800,560),(560,360),master.set_img("../img/icon/logo1.png","small"))
    master.root.mainloop()