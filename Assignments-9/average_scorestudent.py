def average_score(file):
    f = open(file, "r")
    total = 0
    count = 0

    for line in f:
        if line.strip() != "":
            name, score = line.strip().split(",")
            total += float(score)
            count += 1

    f.close()
    return total / count if count != 0 else 0

print(average_score("scores.txt"))