def find_keyword(file, keyword):
    f = open(file, "r")
    result = []
    i = 1
    for line in f:
        if keyword in line:
            result.append(i)
        i += 1
    f.close()
    return result

print(find_keyword("input.txt", "hello"))