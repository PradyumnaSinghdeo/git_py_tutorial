try:
    with open("nonexist.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print('File Does Not exists')
except PermissionError:
    print("Insufficinent Permission to read the file")