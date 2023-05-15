rainbow = ["green", "orange", "violet"]
print(rainbow)
index_of_violet = rainbow.index("violet")
print(index_of_violet)

rainbow.insert(index_of_violet, "red")
print(rainbow)

rainbow.append("yellow")
print(rainbow)

rainbow.reverse()
print(rainbow)

if "orange" in rainbow == True:
    rainbow.remove("orange")
    print(rainbow)
