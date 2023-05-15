def checkParlindrome(my_str):
    return my_str.lower() == my_str[::-1].lower()


str = "Anna"
print(checkParlindrome(str))
