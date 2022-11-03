numbers = [1, 2, 3, 4, 5, 6]
new_list = []
for i in numbers:
    add_1 = i + 1
    new_list.append(add_1)
print(new_list)

new_2 = [i + 1 for i in numbers]
print(new_2)