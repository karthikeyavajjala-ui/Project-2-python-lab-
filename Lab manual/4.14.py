#sum of even numbers
def sum_of_evens(numbers):
    return sum(num for num in numbers if num%2==0)
print(sum_of_evens([1,2,3,4,5,6]))
print(sum_of_evens([7,9,11,13]))