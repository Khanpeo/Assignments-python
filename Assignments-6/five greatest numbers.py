numbers = []
while True:
    value = input("Enter a number (quit by empty): ")
    if value == "":
        break
    numbers.append(float(value))
numbers.sort(reverse=True)
print("5 greatest numbers:")
for num in numbers[:5]:
    print(num)