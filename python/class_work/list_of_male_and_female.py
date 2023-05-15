def count_male_and_female(my_list):
    cnt_male = 0
    cnt_female = 0
    new_list = []
    male = ()
    female = ()
    for i in my_list:
        if i.lower() == "male":
            cnt_male += 1
        if i.lower() == "female":
            cnt_female += 1
    male = ("male", cnt_male)
    female = ("female", cnt_female)
    new_list.append(male)
    new_list.append(female)
    return new_list


arr = ["Male", "male", "Female"]
print(count_male_and_female(arr))
