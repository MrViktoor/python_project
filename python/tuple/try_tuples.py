letters = ('a', 'b', 'b', 'c')
letters2 = ['a', 'b', 'c']
print(letters)
print(type(letters))
print()
print(letters2)
print(type(letters2))

numbers = 1,2,3
alphs_nums = letters + numbers
print(type(numbers))
print(len(numbers))
print(alphs_nums + ('d',))

print(alphs_nums[1:3])
print(alphs_nums.count("b"))

