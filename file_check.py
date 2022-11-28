import os 

def check_file(filename,keyword = ""): # check if keyword/string is in a text file.
    matchs = []
    try:
        with open(filename,'r') as txt:
            temp = txt.readlines()
            for each in temp:
                each = each.strip('\n')
                each = each.split(',')

                if each[0] == keyword or each[0] == str(keyword): # If keyword is in txt file. then append line into line
                    matchs.append(each)
                

    except:
        txt.close()
        return False; 
    
    txt.close()

    if not matchs:
        return False; 
    return matchs





def allowed(filename): # check if keyword/string is in a text file.
    allowed = []
    try:
        with open(filename,'r') as txt:
            for each in txt.readlines():
                each = each.strip('\n')
                each = each.split(',')
                each.pop(0)

                try:
                    for ids in each:
                        if int(ids):
                            allowed.append(ids)
                except:
                    continue; 
                
    except:
        txt.close()
        print("error with load and reading file. ")
        return False; 
    
    txt.close()
    if allowed:
        print(allowed) 
        return allowed; 
    
def array_to_string(content):
    text = ''
    for each in content:
        text += ',' +str(each)
    return text




def config_update(ID,content,filename = "config.txt"): # contect is info after the ID in textfile. 
    file_headers = {"config.txt":"ID,channel_ids\n",
                    "message.txt":"ID,Message\n"   }                              
    
    inFile = check_file(filename,ID)
    match = False
    if inFile: # Means there is an entry for the guildID. We need to update it. 
        match = True
    
    try:
        txt =  open(filename,'r')
        temp = open("temp.txt",'w')
        counter = 0 
        state = False
        
        for each in txt.readlines():
                each_formated = each.strip('\n')
                each_formated = each_formated.split(',')
                if counter == 0:
                    counter += 1
                    temp.write(file_headers[filename])
                    continue; 
                
                if each_formated[0] == ID or each_formated[0] == str(ID) :
                    text = str(ID) +array_to_string(content)+'\n'
                    temp.write(text)
                    state = True
                else: 
                    temp.write(each)
    except:
        print("error not sure what happend chief.")
    
    if not state:
        text = text = str(ID) +array_to_string(content)+'\n'
        temp.write(text)
    
    txt.close()
    temp.close()
    os.remove(filename)
    os.rename("temp.txt",filename)
    print("The file has been renamed")



def conversation_decoder(filename,username):
    print(username)
    temp = []
    x = ''
    txt =  open(filename,'r')
    conv = open("conversation.txt",'w')
    for each in txt.readlines():
        x = each
        try:
            each = each.strip('\n')
            each = each.split(',')
            temp = each[1].split(':')
        
            if temp[0].lower().strip(' ') == username.lower():
                conv.write(x)

            temp = temp[1].split('-')


            if temp[0].lower().strip(' ') == f'@{username}'.lower():
                conv.write(x)
        except:
            print("Invalid Line: Codex Error")
            print(each)

    txt.close()
    conv.close()    
    
conversation_decoder('test2_log.txt','Vinay')
