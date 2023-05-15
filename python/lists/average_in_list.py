my_nums = [10,15,20,25,30]
# a,b,c,d,e = my_nums
# print(a)

def get_average(my_arr):
    sum = 0
    if len(my_arr) == 0:
        return 0
    for i in my_arr:
        sum += i
    average = sum /len(my_arr)
    return average

print(get_average([10,15,20,25,30]))

