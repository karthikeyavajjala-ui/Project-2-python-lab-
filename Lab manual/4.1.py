#Fibonacci series

def fibonacci(n):
    if n<=0:
       return []
    fib_sequence=[0, 1] if n>1 else[0]
    for i in range(2, n):
       fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    return fib_sequence
n=int(input("Enter the number: "))
result=fibonacci(n)
print(result)