import json #for handling JSON Files
import os
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