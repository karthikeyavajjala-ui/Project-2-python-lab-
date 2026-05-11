#Grades based on marks
def assign_grade(marks):
    if marks<0 or marks>100:
        return "Invalid marks! please enter a value between 0,100."
    elif marks>=90:
        return "Grade:A"
    elif marks>=80:
        return "Grade:B"
    elif marks>=70:
        return "Grade:C"
    elif marks>=60:
        return "Grade:D"
    else:
        return "Grade:F"
marks=int(input("Enter students marks:"))
print(assign_grade(marks))