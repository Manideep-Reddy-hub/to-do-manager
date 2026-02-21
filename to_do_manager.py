import sys #for Exit
from ui import viewtask #importing the viewtask function from ui.py
from jsonstorage import load_data,save_data #importing the load and save data functions from jsonstorage.py
from tasks import addtask,marktaskcomplete,deletetask #importing the add,mark complete and delete task functions from tasks.py
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
            print("ThankYou for using")
            print("Exiting...")
            sys.exit(0)
        else:
            print("Enter the valid option from only 1 to 5")
menu()
