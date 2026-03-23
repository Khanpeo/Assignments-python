def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

user_input = input("Enter numbers separated by space: ")
my_list = [int(x) for x in user_input.split()]
result = sum_list(my_list)
print("Sum:", result)