#Functiions to add
def add(a,b):
    return (a+b)
def subtract(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def divide(a,b):
    if b!=0:
       return a/b
    else:
        return "Division by zero is not allowed."
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
print(f"The addition of {num1}and{num2}is:{add(num1,num2)}")
print(f"The subtraction of {num1}and{num2}is:{subtract(num1,num2)}")
print(f"The multiply of {num1}and{num2}is:{multiply(num1,num2)}")
print(f"The division of {num1}and{num2}is:{divide(num1,num2)}")