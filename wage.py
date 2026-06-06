salary = []

def income():
    print("welcome to income tracker")
    print("1:enter your daily wage")
    print("2:calculate your weekly wage")
    print("3:calculate your momthly wage")
    print("4:calculate your total package")

    choice  = int(input("enter your choice:"))

    while True:
         if choice == 1:
              daily_wage = float(input("enter your daily wage:"))
              salary.append(daily_wage)
              print("added succesfully")
              choice  = int(input("enter your choice:"))

         elif choice == 2:
              weekly_wage = sum(salary) * 7
              print(f"your weekly wage is {weekly_wage} ")
              choice  = int(input("enter your choice:"))

         elif choice == 3:
              monthly_wage = sum(salary) * 30
              print(f"your monthly_wage is {monthly_wage}")
              choice  = int(input("enter your choice:"))

         elif choice == 4:
              total_package = sum(salary) * 365
              print(f"your total package is {total_package}")
              choice  = int(input("enter your choice:"))
              

         else:
              print("invalid input")
              print("Thankyou for using income tracker")
              exit()

income()