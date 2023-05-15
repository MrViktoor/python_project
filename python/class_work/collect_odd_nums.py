# numbers = []
# odd_nums = []
# first_seven_nums = []
# for i in range(0, 21):
#     numbers.append(i)
# print(numbers)
#
# for i in numbers:
#     # if i % 2 != 0:
#     #     odd_nums.append(i)
#     if i > 4 and i < 11:
#         numbers[i] = 0
#
# print(numbers)
# print(odd_nums)
#
# for i in range(0,len(numbers)):
#     if i < 8:
#         first_seven_nums.append(numbers[i])
# print(first_seven_nums)
#
# numbers = []
# print(numbers)

numbers = list(range(1,21))
print(numbers)
odd_numbers = numbers[::2]
print(odd_numbers)
numbers[4:10] = [0] * 5
print(numbers)
first_seven_nums = numbers[:7]
print(first_seven_nums)
numbers.clear()
print(numbers)