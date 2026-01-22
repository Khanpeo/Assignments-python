def check_zander_size():
    length = float(input("Enter the length of the zander (cm): "))
    size_limit = 42

    if length < size_limit:
        difference = size_limit - length
        print(f"The zander is too small. Release the fish back into the lake.")
        print(f"It is {difference:.1f} cm below the size limit.")
    else:
        print("The zander meets the size limit.")

check_zander_size()
