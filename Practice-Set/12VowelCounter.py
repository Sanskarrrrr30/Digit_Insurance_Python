"""
12. Vowel Frequency Analyzer 
Problem Statement 
Count total vowels in a given sentence (case-insensitive). 
Input 
sentence 
Output 
vowel_count 
Sample Input 
I Love Python 
Sample Output 
4 
Hint: 
Normalize case before comparison.
"""

sen=input("Enter sentence :  ")
count=0
sen_lower=sen.lower()
print(sen_lower)
for char in sen_lower:
    if (char=='a' or char=='i' or char=='e' or char=='o' or char=='u'):
        count+=1
print(count)