# simple calculator program

def calculate(num1,operator,num2):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        if num2 == "0":
            return "the number is not divisble by 0"
        return num1/num2
    else:
        return "enter a valid operator +,-,*,/"

def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+,-,*,/): ")
            print(calculate(num1,operator,num2))
        except ValueError:  
            print("Error: Enter valid numbers only")
        again = (input("Do you wan to print again : (y/n) ")) 
        if again.lower() != "y":
            print("Goodbye :)" )
            break

if __name__ == "__main__":
	main()        
        
            

