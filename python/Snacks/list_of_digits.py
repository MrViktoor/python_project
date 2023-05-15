def list_of_digits(number):
    my_arr = []
    num_to_str = str(number)
    for i in num_to_str:
        my_arr.append(int(i))
    return my_arr


my_number = 2345
print(my_number)
print(list_of_digits(my_number))
