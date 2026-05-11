#largest among three
def find_largest(a,b,c):
    return max(a,b,c)
num1,num2,num3=map(int,input("Enter three numbers separated by spaces: ").split())
print("The largest number is :",find_largest (num1,num2,num3))