# # # File Handling in Python

# # # Reading data from a file

# # #read() method is used to read the entire content of the file as a string.
# # with open("hdfc_loan_sample_20_rows.json", "r") as file:
# #     data = file.read()
# #     print(data)

# # # readline() method is used to read a single line from the file. Each time you call readline(), it reads the next line.
# # with open("hdfc_loan_sample_20_rows.json", "r") as file:
# #     line=file.readline()
# #     while line:
# #         print(line)
# #         line=file.readline()


# # # iterating over the file object directly using a for loop.
# # with open("hdfc_loan_sample_20_rows.json", "r") as file:
# #     for line in file:
# #         print(line)

# # Writing data to a file

# # write() method is used to write a string to a file. If the file does not exist, it will be created. If the file already exists, it will be overwritten.

# with open("output.txt", "w") as file:
#     file.write("Hello, this is a sample output file.\n")
#     file.write("This file is created using Python's file handling.\n")
#     file.write("We can write multiple lines to the file.\n")

#     #writelines() method is used to write a list of strings to a file. Each string in the list will be written as a separate line in the file.

# lines = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]
# with open("output.txt", "w") as file:
#     file.writelines(lines)

# # writing Formatted data to a file using f-strings

# name = "Alice"
# age = 30
# with open("output.txt", "w") as file:
#     file.write(f"Name: {name}\n")
#     file.write(f"Age: {age}\n")