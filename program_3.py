# WAP to add two numbers and print their sum
try:
     x = float(input("Enter first number: "))
     y = float(input("Enter second number: "))
     print("Your sum is: ",(x + y))

except ValueError:
    print("Error: Enter valid numbers only")