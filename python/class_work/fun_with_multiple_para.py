# def multiply(*lst):
#     product = 1
#     for num in lst:
#         product *= num
#     return product
#
# print(multiply(3,10,5))
def my_function():
    global add
    for nums in range(10):
        add = 0
        add += nums
    return add

print(my_function())


