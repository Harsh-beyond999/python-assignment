#WAP to concatenate and Formatted the String and Integer
try:
    name= input("Enter your name: ")
    age= int(input("Enter your age:"))
    print(f"Your name is {name}\nYour age is {age}")
except ValueError:
    print("Enter valid details")    