try:
    file = open("afile.txt")
    diction = {"key":"value"}
    print(diction["dassa"])
except FileNotFoundError:
    open("afile.txt", mode="w")
except KeyError as error:
    print(f"the key {error} does;t exist")