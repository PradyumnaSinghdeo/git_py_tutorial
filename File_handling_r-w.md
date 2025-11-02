Example 1: Basic File Reading and Writing

with open('output.txt', 'w' , encoding = 'utf-8') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.\n')
    
with open("output.txt", 'r', encoding = 'utf-8')as file:
    content = file.read()
    print(content)


Example 2: Reading Large Files Line by Line

with open('output.txt', "r")as file:
    for line in file:
        print(line)

Example 3: Appending to a File

with open("output.txt", 'a')as file:
    file.write("Append Line.\n")

Example 4: Binary File Operations

data = b'\x00\xFF\x7F'
with open('binary_file.bin', "wb") as file:
    file.write(data)
    
with open('binary_file.bin', 'rb') as file:
    read_data = file.read()
    print(read_data)

Explanation: Binary mode ( 'wb' and 'rb' ) is used for non-text files, such as images or executables.

Example 5: Random Access with seek() and tell()

with open("output.txt", 'r+', encoding='utf-8') as file:
    file.seek(6)
    file.write('Python')
    file.seek(0)
    print(file.read())

Example 6: Handling File Not Found and Permissions

try:
    with open("nonexist.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print('File Does Not exists')
except PermissionError:
    print("Insufficinent Permission to read the file")


Example 1: Reading and Writing CSV Files
# Writing to a CSV file
import csv

with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'London'])

Explanation: The csv.writer writes rows to the file, while csv.reader reads them back as lists.

