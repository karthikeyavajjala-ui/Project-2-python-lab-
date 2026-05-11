def evaluate_exponential(a,b):
    return a**b
a=float(input("Enter the base(a):"))
b=float(input("Enter the exponent(b):"))
result=evaluate_exponential(a,b)
print(f"The value of {a}raised to the power of {b}is:{result}")