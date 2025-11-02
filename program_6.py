# WAP to apply membership operator on a string
text = input("Enter your string: ")
char = input("Enter a character to check: ")
if char in text:
    print(f"'{char}' is present in '{text}'") # can add char.lower() text.lower()(for case - insensitive)
else:
    print(f"'{char}' is not present in '{text}'")