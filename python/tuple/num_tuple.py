nums = tuple(range(1, 501))
print(nums)
even_nums = nums[1::2]
print(even_nums)
odd_nums = nums[::2]
print(odd_nums)
concat_nums = even_nums + odd_nums
print(concat_nums)

numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
x, y, z, *others = numbers
print(x, y, z, others)