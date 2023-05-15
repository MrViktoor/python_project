def correct(str):
    new_char = list(str)
    new_char2 = []
    for i in new_char:
        if i == '1':
            [i] = 'i'
    return new_char

print(correct("Hell0 Mr 5olape. 1 will be with you soon"))
