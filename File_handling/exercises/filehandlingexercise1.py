"""
#Q1: Write a function which count number of lines and number of words in a text. All the files are in the data the folder:

Read obama_speech.txt file and count number of lines and words
Read michelle_obama_speech.txt file and count number of lines and words
Read donald_speech.txt file and count number of lines and words
Read melina_trump_speech.txt file and count number of lines and words

"""
"""
def count_lines_and_words(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            return num_lines, num_words
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None, None
    
result={}
    
files = [ "data/obama_speech.txt", "data/michelle_obama_speech.txt", "data/donald_speech.txt", "data/melina_trump_speech.txt"]

for file in files:
    lines, words = count_lines_and_words(file)
    if lines is not None and words is not None:
        result[file] = {"lines": lines, "words": words}

print(result)
"""

"""
Q2: Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]

"""
"""
import json
from collections import Counter

def most_spoken_languages(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    language_count = Counter()
    
    for country in data:
        language_count.update(country.get("languages", []))
    
    return [(count, lang) for lang, count in language_count.most_common(n)]


print(most_spoken_languages('./data/countries_data.json', 10))
print("\n")
print(most_spoken_languages('./data/countries_data.json', 3))

"""

"""
Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

# Your output should look like this
print(most_populated_countries(filename='./data/countries_data.json', 10))

[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000},
{'country': 'Indonesia', 'population': 258705000},
{'country': 'Brazil', 'population': 206135893},
{'country': 'Pakistan', 'population': 194125062},
{'country': 'Nigeria', 'population': 186988000},
{'country': 'Bangladesh', 'population': 161006790},
{'country': 'Russian Federation', 'population': 146599183},
{'country': 'Japan', 'population': 126960000}
]

# Your output should look like this

print(most_populated_countries(filename='./data/countries_data.json', 3))
[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000}
]

"""
import json

def most_populated_countries(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    sorted_countries = sorted(data, key=lambda x: x.get('population', 0), reverse=True)
    return [{'country': country['name'], 'population': country['population']} for country in sorted_countries[:n]]

print(most_populated_countries('./data/countries_data.json', 10))
print("\n")
print(most_populated_countries('./data/countries_data.json', 3))