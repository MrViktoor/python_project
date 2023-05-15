def generate_username(gmail: str):
    get_letter = gmail.index('@')
    return gmail[0:get_letter]


my_gmail = input("Enter your gmail ")
print(f"Your generated username is {generate_username(my_gmail)}")
