"""

Q1: Extract all incoming email addresses as a list from the email_exchange_big.txt file.

"""

"""

import re

def extract_emails(file_path):
    emails = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("From "):  # incoming emails
                match = re.search(r'\S+@\S+', line)
                if match:
                    emails.append(match.group())
    
    return emails


# Example usage
emails = extract_emails('./data/email_exchanges_big.txt')
print(list(set(emails)))
print(len(set(emails)))

"""

"""

Q2: Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]

"""

"""

def most_common_words(text, n):
    from collections import Counter
    import re
    
    if isinstance(text, str):
        with open(text, 'r', encoding='utf-8') as f:
            text = f.read()
    
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    
    return [(count, word) for word, count in word_counts.most_common(n)]


print(most_common_words('./data/donald_speech.txt', 10))
print(most_common_words('./data/donald_speech.txt', 5))

"""

"""

Q3: Use the function, find_most_frequent_words to find:
The ten most frequent words used in Obama's speech
The ten most frequent words used in Michelle's speech
The ten most frequent words used in Trump's speech
The ten most frequent words used in Melina's speech

"""

"""

def most_common_words(text, n):
    from collections import Counter
    import re
    
    if isinstance(text, str):
        with open(text, 'r', encoding='utf-8') as f:
            text = f.read()
    
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    
    return [(count, word) for word, count in word_counts.most_common(n)]

print("Obama's speech:")
print(most_common_words('./data/obama_speech.txt', 10))
print("\nMichelle's speech:")
print(most_common_words('./data/michelle_obama_speech.txt', 10))
print("\nTrump's speech:")
print(most_common_words('./data/donald_speech.txt', 10))
print("\nMelina's speech:")
print(most_common_words('./data/melina_trump_speech.txt', 10))

"""

"""

Q4: Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

"""

"""

import re
import os
from collections import Counter
from math import sqrt

# import stop words list from your file
from data.stop_words import stop_words


def clean_text(text):
    if isinstance(text, str) and os.path.isfile(text):
        with open(text, 'r', encoding='utf-8') as f:
            text = f.read()
    
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    
    return words


def remove_stop_words(words):
    return [word for word in words if word not in stop_words]


def cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    
    numerator = sum(vec1[x] * vec2[x] for x in intersection)
    
    sum1 = sum(v**2 for v in vec1.values())
    sum2 = sum(v**2 for v in vec2.values())
    
    denominator = sqrt(sum1) * sqrt(sum2)
    
    return numerator / denominator if denominator != 0 else 0


def check_text_similarity(text1, text2):
    words1 = remove_stop_words(clean_text(text1))
    words2 = remove_stop_words(clean_text(text2))
    
    vec1 = Counter(words1)
    vec2 = Counter(words2)
    
    similarity = cosine_similarity(vec1, vec2)
    
    return similarity


# Example usage
sim = check_text_similarity(
    './data/michelle_obama_speech.txt',
    './data/melina_trump_speech.txt'
)

print(f"Similarity: {sim:.4f}")

"""

"""

Q5: Find the 10 most repeated words in the romeo_and_juliet.txt

"""

"""

def most_common_words(text, n):
    from collections import Counter
    import re
    
    if isinstance(text, str):
        with open(text, 'r', encoding='utf-8') as f:
            text = f.read()
    
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    
    return [(count, word) for word, count in word_counts.most_common(n)]

print(most_common_words('./data/romeo_and_juliet.txt', 10))

"""

"""

Q6: Read the hacker news csv file and find out:
Count the number of lines containing python or Python
Count the number lines containing JavaScript, javascript or Javascript
Count the number lines containing Java and not JavaScript

"""

import csv

def analyze_hacker_news(file_path):
    python_count = 0
    javascript_count = 0
    java_count = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        for row in reader:
            row_text = " ".join(row).lower()
            
            # Count Python
            if 'python' in row_text:
                python_count += 1
            
            # Count JavaScript (all variations handled by lower())
            if 'javascript' in row_text:
                javascript_count += 1
            
            # Count Java but NOT JavaScript
            if 'java' in row_text and 'javascript' not in row_text:
                java_count += 1

    return python_count, javascript_count, java_count


# Example usage
file_path = './data/hacker_news.csv'
python_c, js_c, java_c = analyze_hacker_news(file_path)

print("Python:", python_c)
print("JavaScript:", js_c)
print("Java (not JavaScript):", java_c)

