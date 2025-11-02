#WAP to find Factorial using While Loop
try:
    n = int(input("Enter a number: "))
    fact = 1
    i = n
    while i >= 1:
        fact *= i
        i -= 1
    print(f"Factorial of {n} is: {fact}")
except ValueError:
    print("Please enter a valid number.")