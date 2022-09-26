import random
# create the word list and guess the letter from the selected word.
word_list = ["apple", "banana", "orange"]
x = input("guess the letter")
select_word = word_list[random.randint(0, len(word_list))]
