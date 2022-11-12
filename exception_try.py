try:
    file = open("afile.txt")
    diction = {"key":"value"}
    print(diction["dassa"])
except FileNotFoundError:
    open("afile.txt", mode="w")
except KeyError:
    print("the key does;t exist")