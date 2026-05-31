def student_grade(marks):
    
   print("Enter the marks of the student:")
   marks1 = int(input("subject 1:"))
   marks2 = int(input("subject 2:"))
   marks3 = int(input("subject 3:"))
   marks4 = int(input("subject 4:"))
   marks5 = int(input("subject 5:"))
   marks6 = int(input("subject 6:"))

   marks = marks1 + marks2 + marks3 + marks4 + marks5 + marks6

   while True:
        if marks >= 540:
            print("grade: A+")
            break

        elif marks >= 480:
            print("grade: A")
            break

        elif marks >= 420:
            print("grade : B+")
            break

        elif marks >= 360:
            print("grade : B")
            break

        elif marks >= 300:
            print("grade : C")
            break

        else:
            print("grade : F")
            break

student_grade("result")
print("thank you for using our service")