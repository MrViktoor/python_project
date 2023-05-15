import random
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for i in range(10000):
    dice = random.randint(1, 6)
    if dice == 1:
        one += 1
    elif dice == 2:
        two += 1
    elif dice == 3:
        three += 1
    elif dice == 4:
        four += 1
    elif dice == 5:
        five += 1
    else:
        six += 1

print(f"1  -  {one}")
print(f"2  -  {two}")
print(f"3  -  {three}")
print(f"4  -  {four}")
print(f"5  -  {five}")
print(f"6  -  {six}")
