import re

def search_digits_in_string(input_string):
    match1=re.findall(r'\d',input_string)
    if not match1:
        print("No digits found in the string.")
    else:
        print("Digits in the string: ", match1)

str1=input("Enter a string: ")
search_digits_in_string(str1)