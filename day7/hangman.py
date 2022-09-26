import random
from turtle import pen
# create the word list and guess the letter from the selected word.
word_list = ["apple", "banana", "orange"]
guess_letter = input("guess the letter")
select_word = word_list[random.randint(0, len(word_list)-1)]

print(f"the word chosen is {select_word}")

word_into_leeter = list(select_word)
print(word_into_leeter)
# for i in range(len(z)):
#     z[i] = '_'
# print(z)
a = 0
for word in word_into_leeter:
    if guess_letter == word:
        word_into_leeter[a] = guess_letter
    else:
        word_into_leeter[a] = "_"
    a += 1
print(word_into_leeter)
