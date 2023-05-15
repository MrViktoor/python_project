def check_element(my_list,value):
    check_val_exist = False
    for i in my_list:
        if my_list.__contains__(value):
            check_val_exist = True
        else:
            check_val_exist = False
    return check_val_exist


arr = [1, 2, 3, 4]
print(check_element(arr, 3))