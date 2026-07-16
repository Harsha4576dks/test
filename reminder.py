Tasks = [
    {"task":"bike_service", "deadline":"2026-7-20", "done":False},
    {"task":"groceries", "deadline":"2026-7-10", "done":True}
]

class Remainder():
    def __init__(self, tasks):
        self.tasks = tasks

    def add_task(self, task, deadline, done):
        for t in self.tasks:
            if t["task"].lower() == task.lower():
                print("This task is already scheduled")
                return
            else:
                self.tasks.append({"task":task, "deadline":deadline, "done":done})
                print(f"Task '{task} added successfully")   

status = Remainder(Tasks)
task = input("add new task:")
deadline = input("add deadline(YYYY-MM-DD):")
done = input("enter status:")

status.add_task(task, deadline, done)

print("current Tasks:")
for t in Tasks:
    print(t)