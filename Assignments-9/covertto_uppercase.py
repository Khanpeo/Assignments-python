def to_upper(file):
    f = open(file, "r")
    text = f.read()
    f.close()

    f = open("output.txt", "w")
    f.write(text.upper())
    f.close()

to_upper("input.txt")