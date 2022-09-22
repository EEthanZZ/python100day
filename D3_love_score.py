# 🚨 Don't change the code below 👇
from tkinter import E


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

t_count = int(name1.lower().count('t'))
r_count = int(name1.lower().count('r'))
u_count = int(name1.lower().count('u'))
e_count = int(name1.lower().count('e'))

true_count = (t_count+r_count+u_count+e_count) * 10
