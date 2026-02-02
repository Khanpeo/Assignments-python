while True:
    inches = float(input("Enter inches (negative number to quit): "))
    if inches < 0:
        break
    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters} cm")
