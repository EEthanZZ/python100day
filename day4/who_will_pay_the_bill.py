import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

random_person = random.randint(0, len(names) - 1)
pay = names[random_person]
print(pay)
