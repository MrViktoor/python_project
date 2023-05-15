my_list = [2, 2, 3, 4]
my_set = set(my_list)
print(my_set)

# set1 = {48, 98, 78, 100, 42, 2, 3, 1}
# print(type(set1))
# print(set1)
# set2 = {1, 4, 5, 6, 7, 9}

# Check for values in both sets
# print(set1 & set2)

# Check for values that are not in both sets
# print(set1 - set2)

# Check for values not common in both sets
# print(set1 ^ set2)


# Check if number is in a set
#
# set1 = {1, 4, 6, 8, 2}
# if 6 in set1:
#     print(True)
# else:
#     print(False)


set1 = {5,8,15,20}
set2 =  set1.copy()
set3 = set2.add(0)
set2.add(0)
print(set2)
print(set3)