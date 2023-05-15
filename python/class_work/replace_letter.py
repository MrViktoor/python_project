name = input("Enter your name: ")
print(f"3{name[1:]}")


def get_age(year_of_birth) -> str:
    import datetime
    curr_yr = datetime.datetime.now()
    return f"Hello {name}, you are {curr_yr.year - year_of_birth} years old today!!!"


print(get_age(2000))


def currency_convert(dollar) -> str:
    return f"${dollar} = #{dollar * 750:,.2f} naira"


print(currency_convert(100))
