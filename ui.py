def viewtask(data):
    if not data:
        print("No data available")
        return
    print("\nId  Title               Status")
    print("................................")
    for task in data:
        print(f"{task['Id']:<4}{task['Title']:<20}{task['Status']}")
    print()