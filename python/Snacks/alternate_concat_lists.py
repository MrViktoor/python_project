def concat_lists(list1, list2):
    list3 = []
    for index in range(len(list1)):
        list3.append(list1[index])
        list3.append(list2[index])
    return list3


val1 = ['a', 'b', 'c']
val2 = [1, 2, 3]
print(concat_lists(val1, val2))
