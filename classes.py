import os
import re
class entry:
    def __init__(self,name,completed=False,description=""):
        self.name=name
        self.completed=completed
        self.description=description

class database:
    users={}
    def __init__(self,name):
        self.users[name] = self
        self.name= name
        self.entries = {}
    
    def add(self, task):
        self.entries[task.name] = task
        return
    
    def remove(self, task):
        self.entries[task.name] = None
        del task
        return
    def change_status(self, task):
        task.completed = not task.completed
        
def string_to_boolean(text):
    return text.lower == "true"

def save_databses():
    data_folder = "data"
    users = database.users

    for username, user in users.items():
        with open(os.path.join(data_folder,username+".txt"),"w") as f:
            f.truncate(0)
            for v in user.entries.values():
                if isinstance(v,entry):
                    f.write(f"{v.name}|{str(v.completed)}|{v.description}\n")
    return
    
def load_databases():
    data_folder = "data"
    for filename in os.listdir(data_folder):
        # Add to database
        user = database(re.sub(r'\.[^.]*$','',filename))
        # open file
        with open(os.path.join(data_folder,filename),"r") as f:
            if os.path.getsize("data\\"+filename): # check for values
                for line in f:
                    name,completed,des = line.strip().split("|")
                    user.add(entry(name,string_to_boolean(completed),des))
    return

def select_user():
    # select your user
    print("Who are you?")
    user = None
    temp_arr=[]
    i = 1
    for v in database.users.keys():
        temp_arr.append(v)
        print(f"[{i}] {re.sub(r'\.[^.]*$','',v)}")
        i+=1
    print(f"[{i}] Create A New User")
    
    index = None
    try:
        index = int(input("Your Choice: "))
        print()
    except:
        print("ERROR: Invalid Input\n")
        return select_user()
    while True:
        if index == 0 or index > len(temp_arr)+1:
            print("ERROR: Invalid Input\n")
            return select_user()
        elif index == len(temp_arr)+1:
            #create new user
            user = database(input("Enter your username: "))
            print()
            break
        else:
            user = database.users[temp_arr[index-1]]
            break
    return user, user.entries

def find_task(entries,name):
    for i,v in entries.items():
        if i == name:
            return v
            break
    return None
