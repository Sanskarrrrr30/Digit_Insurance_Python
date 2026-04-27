# check email address using Regular Expression

import re

def check_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

email = input("Enter an email address: ")
check_email(email)