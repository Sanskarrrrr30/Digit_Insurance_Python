user_text1 = 'HelloWorld'
print(type(user_text1))

user_text = "Hello, World!"
print(type(user_text))

# to check the string contains only alphabets, alphanumeric characters, digits, etc.
print(user_text1.isalpha())
print(user_text.isalnum())
print(user_text.isdigit())

# to convert the string to lowercase, uppercase, title case, and to find the length of the string
print(user_text.lower())
print(user_text.upper())
print(user_text.title())
print(len(user_text))

#string slicing
print(user_text[0])
print(user_text[7])
print(user_text[-1])
print(user_text[0:5])
print(user_text[7:])
print(user_text[:5])

# count
print(user_text.count('o'))
print(user_text.count('hello'))
print(user_text.count('Hello'))

# replace
print(user_text.replace('World', 'Python'))




