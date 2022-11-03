# numbers = [1, 2, 3, 4, 5, 6]
# new_list = []
# for i in numbers:
#     add_1 = i + 1
#     new_list.append(add_1)
# print(new_list)
#
# new_2 = [i + 1 for i in numbers]
# print(new_2)
#
# name = ["mike", "Joe"]
# new_name = [list(i) for i in name]
# print(new_name)
#
# range_1 = range(1,5)
# range_2 = [n*2 for n in range_1]
# print(range_2)
#
# name_list = ["Joseph", "Michael", "Manning", "joe", "an"]
# new_name_list = [i[:3]for i in name_list]
# new_name_list2 = [i.upper() for i in name_list if len(i) < 4]
# print(new_name_list)
# print(new_name_list2)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_num = [i * i for i in numbers]
print(square_num)
even_num = [i for i in numbers if i % 2 == 0]
print(even_num)

with open('/Users/ethan/Desktop/python100day/list_comprehension/file1.txt', mode="r") as file1:
    a = file1.readlines()
    new_a = [int(i.strip("\n")) for i in a]
with open('/Users/ethan/Desktop/python100day/list_comprehension/file2.txt', mode="r") as file1:
    b = file1.readlines()
    new_b = [int(i.strip("\n")) for i in b]

print(new_a)
print(new_b)
new_list = [i for i in new_a if i in new_b]
print(new_list)


