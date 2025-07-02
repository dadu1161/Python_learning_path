with open("iwrite.txt", "w") as file:

    file.write("omg u can read this \nhave a nice python\n123\nYEYYYYYS \nwhatsss uppp \nmy name is jeff")

with open(r"C:\Users\dagi\Desktop\Python\iwrite.txt", "r") as file:
    file.seek(0)
    print(file.read())