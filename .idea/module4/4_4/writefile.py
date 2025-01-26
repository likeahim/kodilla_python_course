new_name = '\n' + input("Enter new name fo write in file:\n")

with open("names.txt", "a") as write_file:
    write_file.write(new_name)