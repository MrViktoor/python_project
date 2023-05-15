with open("student_records.txt", mode='a') as file:
    file.write("Dello 92\n")


with open ("student_records.txt", mode='r') as file:
    print(file.read())

