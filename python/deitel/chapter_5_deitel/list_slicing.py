nums = []
for i in range(1, 21):
    nums.append(i)
third_num = nums[2:3]
print(third_num)
first_five_num = nums[0:5]
print(first_five_num)
first_half = nums[0:len(nums)//2]
print(first_half)
last_five = nums[::-1]
last_five = last_five[0:5]
last_five = last_five[::-1]
print(last_five)
every_other_num = nums
print(every_other_num)
reverse_nums = nums[::-1]
print(reverse_nums)
last_three_digits = last_five[0:3]
print(last_three_digits)