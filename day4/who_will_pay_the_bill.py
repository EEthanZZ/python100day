import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

# random_person = random.randint(0, len(names) - 1)
person = random.choice(names)
print(person)
