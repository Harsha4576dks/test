class student():
    def __init__(self):
        self.name = []
        self.section = ["A","B"]
        self.status = ["present" , "absent"]

        choice1= input("enter student name:")
        self.name.append(choice1)
        print("student name added  succesfully")
        
        choice2= input("enter student section:")
        if choice2 in self.section:
           self.section.append(choice2)
           print("section added succesfully")
        else:
            print("section not found")
            exit()

        choice3= input("enter student status:")
        if choice3 in self.status:
            self.status.append(choice3)
            print("status added succesfully")
        else:
            print("status not found")
            exit()


        print(f"dear parent's the student name {choice1}, of section {choice2} is {choice3}")
c1 = student()

