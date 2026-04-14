def count_lines(file):
    f = open(file, "r")
    count = 0
    for line in f:
        if line.strip() != "":
            count += 1
    f.close()
    return count

print(count_lines("input.txt"))