#Git testing
n = int(input("How many items? "))
items = []

for i in range(n):
    element = int(input(f"Enter item {i+1}: "))
    items.append(element)

print(items)
