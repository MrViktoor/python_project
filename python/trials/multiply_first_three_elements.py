my_nums = [i for i in range(1,11)]
three_vals = my_nums[3:6]
for i in range(len(my_nums)):
    if i > 2 and i < 6:
        my_nums[i] *=2
    # else :
    #     my_nums[i] = my_nums[i]
print(my_nums)