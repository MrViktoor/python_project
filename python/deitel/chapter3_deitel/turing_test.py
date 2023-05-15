question_one = input("What's your problem ")
question_two = input("Have you had this problem before ")
while question_two != 'yes' and question_two != 'no':
    print("Please enter yes or no")
    question_two = input("Have you had it before ")
if question_two == 'yes':
 print("Well, you have it again")
else:
 print('Well, you have it now')
