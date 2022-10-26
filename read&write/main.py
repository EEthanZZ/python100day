with open("my_file.txt", mode="a") as file:
    file.write("this is a test")


with open("new_file", mode="w") as file2:
    file2.write("this is a tset for writing")