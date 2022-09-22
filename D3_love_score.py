# 🚨 Don't change the code below 👇
from tkinter import E


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

name = name1 + name2

t_count = int(name.lower().count('t'))
r_count = int(name.lower().count('r'))
u_count = int(name.lower().count('u'))
e_count = int(name.lower().count('e'))

true_count = (t_count+r_count+u_count+e_count) * 10

l_count = int(name.lower().count('l'))
o_count = int(name.lower().count('o'))
v_count = int(name.lower().count('v'))
e_count_2 = int(name.lower().count('e'))

love_count = (l_count+o_count+v_count+e_count_2)

true_love_count = true_count + love_count
