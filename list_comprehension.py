numbers = [1, 2, 3, 4, 5, 6]
new_list = []
for i in numbers:
    add_1 = i + 1
    new_list.append(add_1)
print(new_list)

new_2 = [i + 1 for i in numbers]
print(new_2)

name = ["mike", "Joe"]
new_name = [list(i) for i in name]
print(new_name)

range_1 = range(1,5)
range_2 = [n*2 for n in range_1]
print(range_2)