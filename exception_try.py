# try:
#     file = open("./afile.txt")
#     diction = {"key": "value"}
#     print(diction["key"])
# except FileNotFoundError:
#     file = open("./afile.txt", mode="a")
#     file.write("hi")
# except KeyError as error:
#     print(f"the key {error} does;t exist")
# else:
#     x = file.read()
#     print(x)
# finally:
#     file.close()
#     raise KeyError("my error")

#
# height = float(input("Height:"))
# weight = float(input("Weight:"))
#
# if height > 3:
#     raise ValueError("not a true value")
# bmi = height / weight ** 2
#

# practise 1
fruits = ["Apple", "Pear", "Orange"]


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError as error:
#         print("fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(2)
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError as error:
        total_likes += 0

print(total_likes)