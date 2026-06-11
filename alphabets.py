def search():

    
    choice = input("enter a  character:")
    while True:
       
        if choice.islower() == 1:
             print("it is a small_alphabetical character")
             break

        elif choice.isupper() == 1:
             print("it is a  large_alphabetical character")
             break

        else:
             print("invalid input")
             exit()

search()