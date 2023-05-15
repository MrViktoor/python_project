num_1 = input("Enter a number ")
num_2 = input("Enter a number ")
difference = float(num_1) - float(num_2)
if difference.is_integer():
    print(f"The difference between {num_1} and {num_2} is an Integer? True!")
else:
    print(f"The difference between {num_1} and {num_2} is an Integer? False!")
