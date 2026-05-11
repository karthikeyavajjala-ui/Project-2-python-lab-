def palindrome(s):
    """Check if string is palindrome"""
    return s == s[::-1]


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()


def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"


def menu():
    print("\n===== MENU =====")
    print("1. Factorial")
    print("2. Prime Check")
    print("3. Fibonacci")
    print("4. Even/Odd")
    print("5. Palindrome")
    print("6. Exit")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        n = int(input("Enter number: "))
        print("Factorial:", fact(n))

    elif choice == '2':
        n = int(input("Enter number: "))
        print("Prime" if prime(n) else "Not Prime")

    elif choice == '3':
        n = int(input("Enter number of terms: "))
        fib(n)

    elif choice == '4':
        n = int(input("Enter number: "))
        print(even_odd(n))

    elif choice == '5':
        text = input("Enter text: ")
        print("Palindrome" if palindrome(text) else "Not Palindrome")

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")