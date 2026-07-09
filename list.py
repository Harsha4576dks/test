whatsapp = []

def names():
    print("welcome to whatsapp")

    while True:
        print("1:add contact")
        print("2:view contact")
        print("3:delete contact")
        print("4:quit")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            name = input("enter your contact name:")
            phone = int(input("enter your phone number:"))
            whatsapp.append({"name":name, "phone":phone})
            print(f"contact added succesfully: {name}-{phone}")

        elif choice == 2:
            print("contacts:")
            if not whatsapp:
                print("no contacts found")
            else:
                for i, contact in enumerate(whatsapp, start=1):
                    print(f"{i}.{contact['name']}-{contact['phone']} ")

        elif choice == 3:
            name = input(f"enter conatct name to delete:")
            found = False
            for contact in whatsapp:
                if contact["name"] == name:
                    whatsapp.remove(contact)
                    print(f"deleted contact:{name}")
                    found = True
                    break
                else:
                    print("conatct not found")
          
        elif choice == 4:
            print("exiting whatsapp...")
            exit()

        else:
            print("invalid input")

names()