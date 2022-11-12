try:
    file = open("./afile.txt")
    diction = {"key": "value"}
    print(diction["key"])
except FileNotFoundError:
    file = open("./afile.txt", mode="a")
    file.write("hi")
except KeyError as error:
    print(f"the key {error} does;t exist")
else:
    x = file.read()
    print(x)
finally:
    file.close()