# my_numbers = []
#
# for i in range(0, 20):
#     my_numbers.append(i + 1)
# print(my_numbers)
# reverse_num = my_numbers[::-1]
# get_last_five_digits = reverse_num[0:5]
# get_last_five_digits.reverse()
# last_five_digits = get_last_five_digits[::-1]
# print(get_last_five_digits)

# get average and sum
my_nums = [2, 4, 5, 6]
sum = 0
for i in my_nums:
    sum += i
average = sum // len(my_nums)
print(f"The total sum of the numbers is {sum}")
print(f"The average of the numbers is {average}")
