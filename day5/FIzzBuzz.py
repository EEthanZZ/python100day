game = True
a = 0
while game:
    a += 1
    x = input('a number')
    if a % 15 == 0:
        if x != 'fz':
            print('wrong')
            game = False
    elif a % 3 == 0:
        if x != 'f':
            print("wrong")
            game = False
    elif a % 5 == 0:
        if x != 'b':
            print('wrong')
            game = False
