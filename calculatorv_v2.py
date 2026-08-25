def calculate(first_number, second_number, operator):
	if operator == '+':
		return first_number + second_number
	elif operator == '-':
		return first_number - second_number
	elif operator == '*':
		return first_number * second_number
	elif operator == '/':
		if second_number == 0:
			return "Error: Division by zero is not allowed."
		return first_number / second_number
	return "Error: Invalid operator. Please use +,-,*,/."


def main():
	while True:
		try:
			first_number = float(input("Enter first number: "))
			second_number = float(input("Enter second number: "))
			operator = input("Enter operator (+,-,*,/): ")
			print(calculate(first_number, second_number, operator))
		except ValueError:
			print("Error: Enter valid numbers only")

		again = input("Do you want to calculate again? (y/n): ")
		if again.lower() != 'y':
			print("Goodbye!")
			break


if __name__ == "__main__":
	main()
