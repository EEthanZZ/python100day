import random
from turtle import pen
# create the word list and guess the letter from the selected word.
word_list = ["apple", "banana", "orange"]
x = input("guess the letter")
select_word = word_list[random.randint(0, len(word_list)-1)]

print(f"the word chosen is {select_word}")

z = list(select_word)
print(z)
# for i in range(len(z)):
#     z[i] = '_'
# print(z)
a = 0
for i in z:
    if x == i:
        z[a] = x
    else:
        z[a] = "_"
    a += 1
print(z)
