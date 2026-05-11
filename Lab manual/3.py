Student_marks={}
n=int(input("Enter number of students:"))
for _ in range(n):
 name=input("Enter student name:")
 marks=int(input("Enter marks:"))
 Student_marks[name]=marks
 print("\n Students scoring above 75:")
for name,marks in Student_marks.items():
    if marks>75:
        print(f"{name}:{marks}")