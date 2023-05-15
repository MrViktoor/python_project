num_of_eggs = 28
num_of_boxes_needed = round(num_of_eggs/6)
remainder_eggs = num_of_eggs % 6
num_of_eggs_needed = 0

for i in range(6):
    if remainder_eggs + i == 6:
        num_of_eggs_needed = i

print(f"The farmer needs {num_of_boxes_needed} crates to store {num_of_eggs} number of eggs")
print(f"There are {remainder_eggs} eggs placed in the last uncompleted box")
print(f"The farmer needs {num_of_eggs_needed} more eggs to fill the last uncompleted box!!!")
