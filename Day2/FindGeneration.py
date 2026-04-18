# PROG 04 : Find Generation

# Get User's Birth Year

birth_year = int(input("Enter Birth Year: "))

# Identify Generation Using Birth Year

if birth_year >= 1946 and birth_year <= 1964:
    print("You are a Baby Boomer.")
elif birth_year >= 1965 and birth_year <= 1980:
    print("You are a Generation X.")
elif birth_year >= 1981 and birth_year <= 1996:
    print("You are a Millennial.")
elif birth_year >= 1997 and birth_year <= 2012:
    print("You are a Generation Z.")
else:
    print("You are from an unknown generation.")

