def get_sum_of_nums(my_nums):
    sum = 0
    for index in my_nums:
        sum += index
    return sum


def get_sum_of_nums_in_list(my_nums):
    sum = 0
    index = 0
    while index < len(my_nums):
        sum += my_nums[index]
        index += 1
    return sum

numbers = [2, 8, 10, 20, 30, 40]
print(get_sum_of_nums(numbers))
print(get_sum_of_nums_in_list(numbers))
