# wrd = "the_stealth-warrior"
# remove_char = ["_", "-"]
# for char in remove_char:
#     wrd = wrd.replace(char, "")
# print(wrd)


# letters = list("Hello C16")
# print(letters)
# for index, letter in enumerate(letters):
#     print(index, letter)

# wrds = "Hello world"
# arr = []
# for index, i in enumerate(wrds):
#     arr.append(i)
#     print(index, i)
#
# print(arr)


# letters1 = ['a','b','c','d']
# letters2 = list("abcd")
# print(letters2)


letters = ['a','b','c','f']

letters.insert(-1,'d')
letters.remove('f')
del letters[:-1]
print(letters)
