# **args used when working wiith keyword arguments in a function
# def multiply(*lst):
#     product = 0
#     for num in lst:
#         product += num
#     return product
#
#
# print(multiply(2, 2, 2))
#
#
# def multiply(x: int, y: int) -> int:
#     return x * y
#
#
# print(multiply(2, "me"))
#
#
# def get_user(**user):
#     print(user)
#
#
# get_user(id=1, fname="Micheal", lname="Friday")


wrd = 'abcc'
new_wrd = len(wrd)%2 +1
check = wrd[ : new_wrd]
print(check)