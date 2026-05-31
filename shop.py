def shop(search):
    print("welcome to the shop")
    print("1:fruits")
    print("2:vegetables")
    search = int(input("enter your choice:"))

    basket = 0

    if search == 1:
        while True:
             print("the fruits available are:")
             print("1:apple")
             print("2:mango")
             print("3:bannana")
             print("4:lichi")
             search = int(input("enter your choice:"))
             
             if search == 1:
                 choice1 = int(input("how many kg's are required:"))
                 basket = basket + choice1
                 print(f"basket has collected: {basket}kg's of apple")
                 search = int(input("enter your choice:"))
                 
                   
             elif search == 2:
                 choice2 = int(input("how many kg's are required:"))
                 basket = basket + choice2
                 print(f"basket has collected: {basket}kg's of mango")
                 search = int(input("enter your choice:"))
                 
             elif search == 3:
                 choice3 = int(input("how many kg's are required:"))
                 basket = basket + choice3
                 print(f"basket has collected: {basket}kg's of bannana")
                 search = int(input("enter your choice:"))
                 
             elif search == 4:
                 choice4 = int(input("how many kg's are required:"))
                 basket = basket + choice4
                 print(f"basket has collected: {basket}kg's of lichi")
                 search = int(input("enter your choice:"))
                 
             else:
                 print("invalid input")
                 break
             
           
             
    elif search ==  2:
        while True:
             print("the vegetables available are:")
             print("1:carrot")
             print("2:tomato")
             
             search = int(input("enter your choice:"))
             
              
             if search == 1:
                 choice1 = int(input("how many kg's are required:"))
                 basket = basket + choice1
                 print(f"basket has collected: {basket}kg's of carrot")
                 search = int(input("enter your choice:"))
                   
             elif search == 2:
                 choice2 = int(input("how many kg's are required:"))
                 basket = basket + choice2
                 print(f"basket has collected: {basket}kg's of tomato")
                 search = int(input("enter your choice:"))
                 
             else:
                print("invalid input")
                exit()
                   
             print(f"vegetables total is {basket}")
    
    else:
        print("invalid input ")
        exit()
    
             
             
shop("mall")    