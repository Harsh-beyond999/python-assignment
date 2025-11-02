# WAP to Print the Series and miss the number entered by user using break Statement

try:
    stop_num = int(input("Enter a number to stop at: "))

    i = 1
    while i <= 10:
        if i == stop_num:
            break   # exits the loop completely
        print(i)
        i += 1

    print(f"\nLoop stopped when it reached {stop_num}")

except ValueError:
    print("Please enter a valid integer.")
