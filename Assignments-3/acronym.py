def acronym(text):
    result = ""
    for word in text.split():
        result = result + word[0].upper()
    return result
print(acronym("unidentified foreign object"))
