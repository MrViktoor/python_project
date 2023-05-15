bacteria = 200
num_of_bacteria = 1
print(f"Hour     Number of Bacteria")
for i in range(0, 16, 5):
    print(f"{i}        {bacteria *(2 ** i): <10.2f}")
