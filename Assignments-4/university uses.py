def course_code(code):
    if len(code) != 6:
        return False
    for i in range(3):
        if not ('A' <= code[i] <= 'Z'):
            return False
    for i in range(3, 6):
        if not code[i].isdigit():
            return False
    return True
code = input("Enter course code: ")
print(course_code(code))