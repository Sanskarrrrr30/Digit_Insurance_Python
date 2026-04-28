# # # # # # File Handling in Python

# # # # # # Reading data from a file

# # # # # #read() method is used to read the entire content of the file as a string.
# # # # # with open("hdfc_loan_sample_20_rows.json", "r") as file:
# # # # #     data = file.read()
# # # # #     print(data)

# # # # # # readline() method is used to read a single line from the file. Each time you call readline(), it reads the next line.
# # # # # with open("hdfc_loan_sample_20_rows.json", "r") as file:
# # # # #     line=file.readline()
# # # # #     while line:
# # # # #         print(line)
# # # # #         line=file.readline()


# # # # # # iterating over the file object directly using a for loop.
# # # # # with open("hdfc_loan_sample_20_rows.json", "r") as file:
# # # # #     for line in file:
# # # # #         print(line)

# # # # # Writing data to a file

# # # # # write() method is used to write a string to a file. If the file does not exist, it will be created. If the file already exists, it will be overwritten.

# # # # with open("output.txt", "w") as file:
# # # #     file.write("Hello, this is a sample output file.\n")
# # # #     file.write("This file is created using Python's file handling.\n")
# # # #     file.write("We can write multiple lines to the file.\n")

# # # #     #writelines() method is used to write a list of strings to a file. Each string in the list will be written as a separate line in the file.

# # # # lines = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]
# # # # with open("output.txt", "w") as file:
# # # #     file.writelines(lines)

# # # # # writing Formatted data to a file using f-strings

# # # # name = "Alice"
# # # # age = 30
# # # # with open("output.txt", "w") as file:
# # # #     file.write(f"Name: {name}\n")
# # # #     file.write(f"Age: {age}\n")

# # # # Appending data to a file
# # # # append mode ("a") is used to add new content to the end of the file without overwriting the existing content. If the file does not exist, it will be created.

# # # with open("output.txt", "a") as file:
# # #     file.write("This line is appended to the file.\n")
# # #     file.write("We can append multiple lines to the file.\n")

# # # working with file pointers

# # # tell() method is used to get the current position of the file pointer, which is the location in the file where the next read or write operation will occur. The position is returned as the number of bytes from the beginning of the file.

# # # with open("output.txt", "r") as file:
# # #     position = file.tell()
# # #     print("Current file pointer position:", position)

# # # seek() method is used to move the file pointer to a specific position in the file. The seek() method takes two arguments: the offset (number of bytes to move) and the whence (reference point for the offset). The whence can be set to 0 (beginning of the file), 1 (current position), or 2 (end of the file).

# # with open("output.txt", "r") as file:
# #     # Move the file pointer to the 10th byte from the beginning of the file
# #     file.seek(10, 0)
# #     print("File pointer moved to the 10th byte from the beginning of the file.")
# #     print("Current file pointer position:", file.tell())
# #     print(file.read())

# # # finding the size of the file using seek() and tell() methods

# # with open("output.txt", "r") as file:
# #     file.seek(0, 2)  # Move the file pointer to the end of the file
# #     print("File pointer moved to the end of the file.")
# #     print(f"File size: {file.tell()} bytes")

# # # renameing and deleting a file using os module
# import os
# # os.rename("output.txt", "renamed_output.txt")

# # os.rename("renamed_output.txt", "output.txt")

# os.remove("output.txt")

# organizing files and directories using os module

import os
# creating a new directory
# os.mkdir("new_directory")

# os.chdir("new_directory")  # Change the current working directory to the new directory

# os.chdir("File_handling")  # Change to the File_handling directory

# os.chdir("..")  # Change back to the parent directory
# os.listdir()  # List the contents of the current directory
# for file in os.listdir():
#     print(file)

# Exception Handling while working with files

try:
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file does not exist. Please check the file name and try again.")
except PermissionError:
    print("You do not have permission to access this file.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
    