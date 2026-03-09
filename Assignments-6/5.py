def odd_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 1:
            result.append(n)
    return result
def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    new_list = odd_numbers(numbers)
    print("Original list:", numbers)
    print("Odd numbers:", new_list)
main()