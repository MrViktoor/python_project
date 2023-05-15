celsius = int(input("Enter a temperature in degrees Celsius: "))


def convert_far_to_cel(far):
    c = (far - 32) * 5 / 9
    return c


print(f"{celsius} degrees in C = {convert_far_to_cel(celsius):.2f}")


fahrenheit = int(input("Enter a temperature in degrees Fahrenheit: "))


def convert_cel_to_far(cel):
    f = cel * 9 / 5 + 32
    return f


print(f"{fahrenheit} degrees in F = {convert_cel_to_far(fahrenheit):.2f} C")
