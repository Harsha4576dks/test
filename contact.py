names = []
numbers = []

def contact():
    print("welcome to contact's")
    print("1:add contact:")
    print("2:view contact's")
    print("3:delete contact")
    print("4:exit")

    choice = int(input("enter your choice:"))

    while True:
        if choice == 1:
            name = input("enter your name:")
            names.append(name)
            print("name added successfully")
            number = input("enter your number:")
            numbers.append(number)  
            print("number added successfully")
            choice = int(input("enter your choice:"))

        elif choice  == 2:
            print(f"name:{names}")
            print(f"number:{numbers}")
            choice = int(input("enter your choice:"))

        elif choice == 3:
            delete = input("enter a contact name to delete:")
            index = names.index(delete)
            names.pop(index)
            numbers.pop(index)
            print("contact deleted successfully")
            choice = int(input("enter your choice:"))

        elif choice == 4:
            print("invalid input")
            exit()

        else:
            exit()

contact()