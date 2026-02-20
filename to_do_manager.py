import json
import os
class RunTimeError(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
def load_data():# we are getting the data from the json existing file
    if not os.path.exists("data.json"):
        return []
    with open("data.json","r") as file:
        try:
            data=json.load(file)
            if isinstance(data,dict):#it will check the data type first one will be dict
                return [data]
            else:
                return data
        except:
            return []
def save_data(data):#this function is used to store the data into the json file if does not exist file will created
    with open("data.json","w") as file:
        json.dump(data,file,indent=4)#overwriting the data by the  added data  the first by erasing the existing one
def addtask():
    data=load_data()
    while True:
        try:
            taskid=int(input("Enter the id:"))
            break
        except(TypeError):
            print("Enter the integer for the id")
    title=input("Enter the title of the task:")
    while True:
        try:
            status=input("Enter the status of the task (Pending or Done):")
            status=status.capitalize()
            if(status!="Pending" and status!="Done"):
                raise RunTimeError("Invalid Status")
            break
        except RunTimeError as e:
            print(e)
    dic={"Id":taskid,"Title":title,"Status":status}
    data.append(dic)
    save_data(data)     
def viewtask():
    data=load_data()
    for i in data:
        print(i)
def marktaskcomplete():
    data=load_data
    task=input("Enter the task title  to mark as complete:")
    if task in data:
        for i in data:
            if(i[Title]==task):
                i[Status]="Done"
                break
    else:
        print("Task Doesnot exis please check the existing tasks by clicking option 2 Thankyou")
def deletetask():
    pass
def Exit():
    pass
def menu():
    while True:
        print("1.add Task")
        print("2.View Tasks")
        print("3.Mark Task Complete")
        print("4.Delete Task")
        print("5.Exit")
        while True:
            try:
                choice=int(input("Enter the choice:"))
                break
            except TypeError:
                print("Intezers are only allowed!")
        if choice==1:
            addtask()
        elif choice==2:
            viewtask()
        elif choice==3:
            marktaskcomplte()
        elif choice==4:
            deletetask()
        elif choice==5:
            Exit()
        else:
            print("Enter the valid option from only 1 to 5")
menu()
