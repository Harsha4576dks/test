schedule = []
date = []

class Task():
    def __init__(self, schedule, date):
        self.schedule = schedule
        self.date = date

    def tasks(self):
        print("1:sunday")
        print("2:monday")
        print("3:tuesday")
        print("4:wednesday")
        print("5:thursday")
        print("6:friday")
        print("7:saturday")

        choice = int(input("enter your choice: "))

        if choice == 1:
            schedule_text = input("enter your schedule on sunday: ")
            date_text = input("enter date: ")
            self.schedule.append(schedule_text)
            self.date.append(date_text)
            print("added successfully")
            

        elif choice == 2:
            schedule_text = input("enter your schedule on monday: ")
            date_text = input("enter date: ")
            self.schedule.append(schedule_text)
            self.date.append(date_text)
            print("added successfully")

        elif choice == 3:
            schedule_text = input("enter your schedule on tuesday: ")
            date_text = input("enter date: ")
            self.schedule.append(schedule_text)
            self.date.append(date_text)
            print("added successfully")

        elif choice == 4:
            schedule_text = input("enter your schedule on wednesday: ")
            date_text = input("enter date: ")
            self.schedule.append(schedule_text)
            self.date.append(date_text)
            print("added successfully")

        elif choice == 5:
            schedule_text = input("enter your schedule on thursday: ")
            date_text = input("enter date: ")
            self.schedule.append(schedule_text)
            self.date.append(date_text)
            print("added successfully")

        elif choice == 6:
            schedule_text = input("enter your schedule on friday: ")
            date_text = input("enter date: ")
            self.schedule.append(schedule_text)
            self.date.append(date_text)
            print("added successfully")

        elif choice == 7:
            schedule_text = input("enter your schedule on saturday: ")
            date_text = input("enter date: ")
            self.schedule.append(schedule_text)
            self.date.append(date_text)
            print("added successfully")

        else:
            print("invalid input")
            exit()

sunday = Task(schedule, date)
monday = Task(schedule, date)
tuesday = Task(schedule, date)
wednesday = Task(schedule, date)
thursday = Task(schedule, date)
friday = Task(schedule, date)
saturday = Task(schedule, date)

c1 = Task(schedule, date)
c1.tasks()

print(schedule)
print(date)