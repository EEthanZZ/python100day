
from operator import truediv
import random
# create the word list and guess the letter from the selected word.
word_list = ["apple", "banana", "orange"]

select_word = random.choice(word_list)
word_len = len(select_word)
print(f"the word chosen is {select_word}")

show = []
for a in range(word_len):
    show += "_"

a = 0
game = True
while game:
    guess_letter = input("guess the letter: ").lower()
    for x in range(word_len):
        letter = select_word[x]
        if letter == guess_letter:
            show[x] = letter
    a += 1
    print(show)
    if "_" not in show:
        game = False
        print("you win")
    if a > 4:
        game = False
        print("lose")
