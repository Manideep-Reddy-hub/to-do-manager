import json#handling JSON Files
import os #for the path,rename
import sys#for Exit
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
def load_data():# we are getting the data from the existing json file
    if not os.path.exists("data.json"):
        return []
    try:
        with open("data.json","r") as file:
            data=json.load(file)
        if not isinstance(data,list):
            raise ValueError("Inavlid structure")
        for task in data:
            if not isinstance(task,dict):
                raise ValueError("Invalid Task Format")
            if("Id" not in task or "Title" not in task or "Status" not in task):
                raise ValueError("Missing Fields")
        return data
    except ValueError:
        os.rename("data.json","Data_correpted_Backup.json")
        print("Data File is Correpted and has been reset(backup created)")
        return []
def save_data(data):#this function is used to store the data into the json file if does not exist file will created
    with open("data.json","w") as file:
        json.dump(data,file,indent=4)#overwriting the data by the  added data  the first by erasing the existing one
def addtask():
    data=load_data()
    title=input("Enter the title of the task:")
    while True:
        try:
            status=input("Enter the status of the task(Pending or Done):").capitalize()
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
def viewtask(data):
    if not data:
        print("No data available")
        return
    print("\nId  Title               Status")
    print("................................")
    for task in data:
        print(f"{task['Id']:<4}{task['Title']:<20}{task['Status']}")
    print()
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
                print("Only numbers are allowed!")
        if choice==1:
            addtask()
        elif choice==2:
            data=load_data()
            viewtask(data)
        elif choice==3:
            marktaskcomplete()
        elif choice==4:
            deletetask()
        elif choice==5:
            Exit()
        else:
            print("Enter the valid option from only 1 to 5")
menu()
