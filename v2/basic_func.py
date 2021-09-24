# def print_debug(env,*strings):
#     if (env in ["debug","onlydebug"]):
#         print("[ Debug ]:","".join([str(i) for i in strings]))
#         # print("".join([str(i) for i in strings]))
        
# def print_info(env,*strings):
#     if (env in ["info","debug","onlyinfo"]):
#         print("[ Info ] :","".join([str(i) for i in strings]))
#         # print("".join([str(i) for i in strings]))

def print_master(name,data,indent=4,start_space=" ",space_filler=" "):
    tab=space_filler*indent
    if (type(data)==type({}) ):
        if(len(data)==0):
            print(start_space,name," : {},")
        else:
            print(start_space,name," : {")
            for i in data:
                print_master(i,data[i],start_space=tab+start_space,space_filler=space_filler)
            print(start_space,"},")
    elif (type(data)==type(()) or type(data)==type([]) ):
        if(len(data)==0):
            print(start_space,name," : []")
        else:    
            print(start_space,name," : [")
            for i in data:
                print_master("item",i,start_space=tab+start_space,space_filler=space_filler)
            print(start_space,"],")
    else:
        print(start_space,name," : ",data,",")

if __name__=="__main__":
    print_master("Dict",{"arindam":{1:2,3:4},"amritesh":{1:2,5:6}},space_filler="-")