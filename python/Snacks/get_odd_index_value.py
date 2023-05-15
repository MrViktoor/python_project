def get_odd_index_val(my_list):
    odd_index_vals = []
    for index in range(len(my_list)):
        if index % 2 == 0:
            odd_index_vals.append(my_list[index])
    return odd_index_vals


arr = [2, 3, 4, 5, 6, 2, 5, 10, 33]
print(get_odd_index_val(arr))
