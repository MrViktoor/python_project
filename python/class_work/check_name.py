names = []
for i in range(10):
    name = input("Enter a name: ")
    if len(name) > 1 and len(name) < 11:
        names.append(name)
print(names)
