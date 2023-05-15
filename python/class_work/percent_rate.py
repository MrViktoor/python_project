# def percent_of_interest(amt, yrs):
#     rate_of_interest = 0.05
#     for yr in range(1, yrs + 1):
#         roi = amt * rate_of_interest
#         amt += roi
#         print(f"year {yr} return on investment is {roi}, your principal is now {amt}")
#
#
#
# amt = int(input("Enter amount you want to invest: "))
# yrs = int(input("Enter the number of years: "))
# percent_of_interest(amt, yrs)


# def multiplication_table(start,stop):
#     stp = int(input("Enter stop digit: "))
#     for i in range(start, stop+1):
#      for j in range(1,stp+1):
#       print(f"{i} * {j} = {i * j}")
#      print()
#
# start = int(input("Enter the range of numbers. Start: "))
# stop = int(input("Enter the range of numbers. Stop: "))
#
# multiplication_table(start,stop)


# def percent_of_interest(amt, yrs):
#     rate_of_interest = 0.05
#     # for yr in range(1, yrs + 1):
#     yr = 1
#     while (yr < yrs+1):
#         roi = amt * rate_of_interest
#         amt += roi
#         print(f"year {yr} return on investment is {roi}, your principal is now {amt}")
#         yr += 1
#
#
# amt = int(input("Enter amount you want to invest: "))
# yrs = int(input("Enter the number of years: "))
# percent_of_interest(amt, yrs)


# secret_num = 25
# guess_num = int(input("Guess the secret number: "))
# while secret_num != guess_num:
#     guess_num = int(input("Wrong, guess again: "))
# else:
#     pass
#     print()
#     print("Correcto!!!")



# if 80 < score < 101:
#     print("A")
# elif 65 <= score <= 80:
#     print("B")
# elif 50 < score <= 65:
#     print("C")
# elif 41 <= score <= 50:
#     print("D")
# else:
#     if score < 41:
#      print("Chukwuma Adekunle")
#     else:
#         print("Alaye, report to principal office, now!!!")

# if score <= 40:
#     print("You failed this course")
# else:
#     print("You passed, congratulations")

# result = "You fail this course" if score >= 40 else "You passed, congratulations"
# print(result)


# language = input("Enter your choice programming language: ")
# match language.lower():
#     case "java":
#         print(f"You are a hardcore programmer")
#     case "javascript":
#         print("You are a fullstack programmer")
#     case "python":
#         print("You are an amazing programmer")
#     case _:
#         print("You can learn any language of your choice")


# wrd = 'abc'
# for letter in wrd:
