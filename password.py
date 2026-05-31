import random
def password():
    print("welcome")
    print("1:generate password")
    print("2:show password")
    choice = int(input("enter your choice:"))

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    characters = "!@#$%^&*"
    password  = "your current password is: "

    while True:
        if choice  == 1:
            password = password + random.choice(alphabets) + random.choice(numbers) + random.choice(characters)
            print("password generated successfully")
            choice = int(input("enter your choice:"))

        elif choice == 2:
            print(f" {password}")
            break

        else:
            print("invalid input")
            exit()

password()