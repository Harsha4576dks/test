def palindrome():
    print("Welcome")
    
    while True:
        choice = input("Enter a string or number: ")

        if choice == choice[::-1]:
            print("It is a palindrome sequence")
        else:
            print("This input is not a palindrome sequence")
            break

palindrome()