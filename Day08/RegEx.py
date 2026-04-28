# regex introduction
# https://colab.research.google.com/drive/1GrwhUu5LZlk068js0PklFdLqDOqVGc6e?usp=classroom_web

import re

# quote = "I scream, you scream, we all scream for ice cream."

# print(re.search(r"scream", quote).group())
# print(re.findall(r"scream", quote))
# print(re.split(r",", quote))

# \d matches any digit character (0-9)
# text1= "I have 2 apples and 3 oranges."
# matches=re.findall(r"\d+", text1)
# print(matches)

# text2="the year is 2026"
# matches=re.findall(r"\d{4}", text2)
# print(matches)
# matches=re.findall(r"\d{3}", text2)
# print(matches)
# matches=re.findall(r"\d{2}", text2)
# print(matches)
# matches=re.findall(r"\d{1}", text2)
# print(matches)


# \D matches any non-digit character
# text3="I have 2 apples and 3 oranges."
# matches=re.findall(r"\D+", text3)
# print(matches)
# matches=re.findall(r"\D{3}", text3)
# print(matches)

# \s matches any whitespace character (space, tab, newline)
# text4="Hello World! Welcome to Python programming."
# matches=re.findall(r"\s+", text4)
# print(matches)
# matches=re.findall(r"\s{2}", text4) 
# print(matches)

# \S matches any non-whitespace character
# text5="Hello World! Welcome to Python programming."
# matches=re.findall(r"\S+", text5)
# print(matches)
# matches=re.findall(r"\S{5}", text5)
# print(matches)

# \w matches any alphanumeric character (letters, digits, and underscores)
# text6="Hello_World123 Welcome to Python programming."
# matches=re.findall(r"\w+", text6)
# print(matches)
# matches=re.findall(r"\w{5}", text6)
# print(matches)

# \W matches any non-alphanumeric character
text7="Hello_World123 Welcome to Python programming. @#$%"
matches=re.findall(r"\W+", text7)
print(matches)
matches=re.findall(r"\W{5}", text7)
print(matches)