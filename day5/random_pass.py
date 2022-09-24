# Password Generator Project
from operator import le
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_pass = []
for i in range(0, nr_letters):
    letter_pass.append(random.choice(letters))
for i in range(0, nr_symbols):
    letter_pass.append(random.choice(symbols))
for i in range(0, nr_numbers):
    letter_pass.append(random.choice(numbers))
shuffle_pass = random.sample(letter_pass, len(letter_pass))
print(shuffle_pass)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pass_2 = []
all_pass = letters + numbers + symbols
for i in range(0, nr_letters+nr_numbers+nr_symbols):
    pass_2.append(random.choice(all_pass))
print(pass_2)
