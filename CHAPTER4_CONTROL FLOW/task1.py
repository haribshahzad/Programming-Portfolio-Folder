import os
os.system("cls")

student_name = input("Enter the student's name:")
marks = int(input("Enter the marks (out of 100):"))

if marks > 100:
    print("invalid Marks, Total marks are 100")
elif marks >= 90:
    print("Your grade is A")
elif marks >= 80:
    print("Your grade is B")
elif marks >= 70:
    print("Your grade is C")
else:
    print("Your grade is D")