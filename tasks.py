#this file contains the functions related to the tasks they are add,mark complete and delete task
from jsonstorage import load_data,save_data #importing the load and save data functions from jsonstorage.py
from ui import viewtask #importing the viewtask function from ui.py
def checker(data):
    while True:
        try:
            check=input("Do you know the id of task(Yes or No):").capitalize()
            if(check!="Yes" and check!="No"):
                print("Only yes and no are valid")
                continue
            if check == "No":
                print("tasks are")
                viewtask(data)
            break
        except ValueError as e:
            print(e)
def addtask():
    data=load_data()
    while True:
        try:
            title=input("Enter the title of the task:")
            if(title.isspace()):
                raise ValueError("Input is invalid")
            break
        except ValueError as e:
            print(e)
            title.strip()
    while True:
        try:
            status=input("Enter the status of the task(Pending or Done):").capitalize()
            status.strip()
            if(status!="Pending" and status!="Done"):
                raise RuntimeError("Invalid Status")
            break
        except RuntimeError as e:
            print(e)
    if not data:
        taskid=1
    else:
        taskid=max(task["Id"] for task in data) +1
    dic={"Id":taskid,"Title":title,"Status":status}
    data.append(dic)
    save_data(data)
    print("Task Added")
def marktaskcomplete():
    data=load_data()
    if not data:
        print("No tasks available")
        return
    checker(data)
    while True:
        try:
            taskid=int(input("Enter the task id to mark as complete:"))
            if(taskid<=0):
                print("invalid input")
                continue
            break
        except ValueError:
            print("Only numbers are allowed")
    found=False
    for task in data:
        if(task["Id"]==taskid):
            found=True
            if(task["Status"]=="Done"):
                print("Task is completed already,again you are trying to update")
                return
            task["Status"]="Done"
            break
    if not found:
        print("Task Not Found")
    else:
        save_data(data)
        print("task updated")
def deletetask():
    data=load_data()
    if not data:
        print("No tasks available")
        return
    checker(data)
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
    print("Task Deleted")
