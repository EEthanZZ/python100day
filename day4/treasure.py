from operator import truediv
import random
from re import M

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

random_x = str(random.randint(0, 2))
random_y = str(random.randint(0, 2))
random_xy = random_x + random_y
print(random_xy)


game = True
while game:
    position = input("Where do you want to put the treasure? ")
    list = []
    for i in position:
        list.append(int(i))

    map[list[0] - 1][list[1] - 1] = "X "

    print(f"{row1}\n{row2}\n{row3}")
    if random_xy == position:
        print("you win")
        map[list[0] - 1][list[1] - 1] = "Y "
        game == False
    else:
        print("try again")
