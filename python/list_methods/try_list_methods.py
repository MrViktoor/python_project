# insert(index, value)
# color_names = ["red", "blue", "black"]
# color_names.insert(3, "white")
# print(color_names)
# # print(list(enumerate(color_names)))
# for index, value in enumerate(color_names):
#     print(f"{index} {value}")




# del
# The del keyword can be used to remove elements from a list and delete variables
# car_names = ["Volvo", "Mercedes", "Mazda"]
# del car_names[1:2]
# print(car_names)

# car_names = ["Volvo", "Mercedes", "Mazda"]
# del car_names[1:2]
# print(car_names)


# sort() and sort(reverse = True)
# numbers = [4,6,2,8]
# ref_num = []
# ref_num.append(numbers)
# numbers.sort()
# ref_num.sort(reverse = True)
# print(ref_num == numbers)

# sorted() sorted(reverse = True) returns a new list containing the sorted elements of it's arguments while the originla list is unmodified
# numbers = [4, 6, 2, 8]
# ref_nums_asc = numbers.sorted()
# print(ref_nums_asc)



# search sequence
# index(value)
# # returns the first index value of the element specified and an error if not found
# names = ["Victor", "Joy", "Kc", "HitSquad Baby", 3]
# get_name = names.index('HitSquad Baby')
# print(get_name)

# index(value, bgnSearch(index))
# numbers = ['jey', 'hey', 'bey', 'pey', '', 5]
# numbers *= 2
# new_numbers = numbers.index('pey', 7)
# print(new_numbers)

# index(value, bgnSearch(index), stopSearch(index))
# numbers = ['jey', 'hey', 'bey', 'pey', '', 5]
# numbers *= 3
# new_numbers = numbers.index('pey', 6, len(numbers))
# print(new_numbers)

# in and not in
# checks whether a value is in a list
# numbers = ['jey', 'hey', 'bey', 'pey', '', 5]
# check_num = 5 in numbers
# print(check_num)
#
# numbers = ['jey', 'hey', 'bey', 'pey', '', 5]
# check_num = 6 not in numbers
# print(check_num)

#
# places = ["United Kingdom","USA", "Nigeria", "Ghana", "Jamaica"]
#
# if 'Nigeria' in places:
#     print(f"Found Nigeria at index {places.index('Nigeria')} of places")
# else:
#     print(f"Didn't find Nigeria in places")

# insert(index, value)
# adds a new item at a specified index
# places = ["UK", "USA", "Jamaica"]
# places.insert(0, "Nigeria")
# places.insert(2, "Uganda")
# print(places)

#
# append(value)
# adds an element at the end of a list
# places = ["UK", "USA", "Jamaica"]
# places.append("Tokyo")
# print(places)
# places.reverse()
# places.remove("Tokyo")
# print(places)



# extend([])
# adds all the elements of a sequence to the end of a list
# numbers = [5, 10]
# numbers.extend([15, 20])
# print(numbers)
#
# names = ["Victor", "HitSquad"]
# new_names = ["Joy", "Junior"]
# names.extend(new_names)
# print(names)


# remove(value)
# deletes the first element of a specified value

# numbers = [2, 4, 6, 3, 8, 10]
# numbers.remove(3)
# print(numbers)
# for i in numbers.copy():
#     if i % 2 == 0:
#         numbers.remove(i)


# new_numbers = [i for i in numbers if i % 2 == 0 numbers.remove(i)]
# print(new_numbers)


# clear()
# empties the content of a string

# numbers = [2, 4, 6, 3, 8, 10]
# numbers.clear()
# print(numbers)


# reverse()
# reverses the content of a list in place instead of creating a reversed copy
#
# names = ["Caleb", "John", "Joshua"]
# names.reverse()
# print(names)



# cop()
# returns a new list containing a shallow copy of the original one

# names = ["John", "Joshua", "Caleb"]
# copied_names = names.copy()
# print(copied_names)
