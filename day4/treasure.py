import random

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


put_x = random.randint(0, 2)
put_y = random.randint(0, 2)
map[put_x][put_y] = "X"

print(f"{row1}\n{row2}\n{row3}")
