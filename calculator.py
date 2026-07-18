def calculator():
    print("Welcome to calculator:")

    while True:
        print("1:addition:")
        print("2:subtraction:")
        print("3:multiplication:")
        print("4:division:")
        print("5:percentage:")
        print("6:exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            number1 = float(input("Enter number-1:"))
            number2 = float(input("Enter Number-2:"))
            result = number1 + number2
            print(f"result = {result}")
            
        elif choice == 2:
            number1 = float(input("Enter number-1:"))
            number2 = float(input("Enter Number-2:"))
            result = number1 - number2 
            print(f"result = {result}")
            
        elif choice == 3:
            number1 = float(input("Enter number-1:"))
            number2 = float(input("Enter Number-2:"))
            result = number1 * number2
            print(f"result = {result}")
            
        elif choice  == 4:
            number1 = float(input("Enter number-1:"))
            number2 = float(input("Enter Number-2:"))
            result = number1/number2
            print(f"result = {result}")
            
        elif choice == 5:
            x = float(input("Enter the percentage value:"))
            number = float(input("Enter the total_value:"))
            result = number * (x/100)
            print(f"result = {result}")
            
        elif choice == 6:
            print("Invalid choice")
            exit()

calculator()