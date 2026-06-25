def remove_duplicates(items):
    return list(dict.fromkeys(items))

print(remove_duplicates([1, 2, 2, "привет", 3, "привет", 1]))
print(remove_duplicates(["Go", "Python", "Go", "Go"]))
