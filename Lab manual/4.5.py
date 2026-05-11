#Reverse number
def reverse_number(n):
    reversed_num=0
    is_negative=n<0
    n=abs(n)
    while n>0:
        reversed_num=reversed_num*10+(n%10)
        n//=10
    return-reversed_num if is_negative else reversed_num
num=int(input("Enter the number: "))
print(reverse_number(num))