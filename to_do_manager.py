import json#handling JSON Files
import os #for the path
import sys#for Exit
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
    title=input("Enter the title of the task:")
    if data:
        taskid=max(task["Id"] for task in data)+1
    else:
        taskid=1
    while True:
        try:
            status=input("Enter the status of the task (Pending or Done):").capitalize()
            if(status!="Pending" and status!="Done"):
                raise RunTimeError("Invalid Status")
            break
        except RunTimeError as e:
            print(e)
    
    dic={"Id":taskid,"Title":title,"Status":status}
    data.append(dic)
    save_data(data)
    print("Task added successfully")
def viewtask():
    data=load_data()
    print("The task list")
    if data:
        for i in data:
            print(i)
    else:
        print("No tasks are added until now")
def marktaskcomplete():
    data=load_data()
    found=False
    task=input("Enter the task title  to mark as complete:")
    for i in data:
        if(i["Title"]==task):
            found=True
            if(i["Status"]=="Pending"):
                i["Status"]="Done"
            else:
                print("Task is already completed not required to mark again")
                return
            break
    if not found:
        print("Task doesnot exist please check the task list by the help of option 2 Thankyou") 
    else:
        save_data(data)
        print("Task got updated")
def deletetask():
    data=load_data()
    if not data:
        print("No tasks are added yet to delete")
        return
    while True:
        try:
            taskid=int(input("Enter the id to delete:"))
            if(taskid<=0):
                print("Invalid input")
                continue
            break
        except ValueError:
            print("Only Numbers are allowed")
    deleteindex=None
    for index,task in enumerate(data):
        if(task["Id"]==taskid):
            deleteindex=index
            break
    
    if deleteindex is None:
        print("Task Not Found")
        return
    del data[deleteindex]
    save_data(data)
    print("Task Deleted successfully")
def Exit():
    print("ThankYou for using")
    print("Exiting............")
    sys.exit(0)
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
            except ValueError:
                print("Intezers are only allowed!")
        if choice==1:
            addtask()
        elif choice==2:
            viewtask()
        elif choice==3:
            marktaskcomplete()
        elif choice==4:
            deletetask()
        elif choice==5:
            Exit()
        else:
            print("Enter the valid option from only 1 to 5")
menu()
