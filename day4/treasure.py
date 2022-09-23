import random

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

list = []
for i in position:
    list.append(int(i))

print(list)

map[list[0] - 1][list[1] - 1] = "X "


print(f"{row1}\n{row2}\n{row3}")
