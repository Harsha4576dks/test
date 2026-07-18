subjects = []
marks = []

class grade():
    def __init__(self):
      self.subjects = subjects
      self.marks = marks

    def add_subject(self):
       subject = input("enter subject name:")
       mark = int(input("Enter marks for 100:"))
       self.subjects.append(subject)
       self.marks.append(mark)

    def show_grades(self):
       for s, m in zip(self.subjects, self.marks):
          print(f"{s} -> {m}")

    def calculate_grades(self):
       total_marks = sum(self.marks)
       max_marks =len(self.subjects) * 100
       result = (total_marks/max_marks) * 100
       print(f"Result = {result:.2f}%")


c1 = grade()
c1.add_subject()
c1.add_subject()
c1.add_subject()
c1.add_subject()
c1.add_subject()
c1.add_subject()
c1.show_grades()
c1.calculate_grades()