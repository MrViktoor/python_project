

def fib():
    num1 = 0
    num2 = 1
    print(f"{num1}")
    print(f"{num2}")
    for i in range(5):
        num3 = num1 + num2
        print(f"{num3} \n", end='')
        num1 = num2
        num2 = num3


print(fib())
