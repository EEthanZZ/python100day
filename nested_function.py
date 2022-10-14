def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculation(a, b, xxx):
    return xxx(a, b)


c = calculation(3, 4, addition)
print(c)
d = calculation(5, 6, multiply)
print(d)