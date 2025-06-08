with open("hallo_world", "w") as file:
    file.write("Hallo Word")


with open("hallo_world", "r") as file:
    print(file.read())
    