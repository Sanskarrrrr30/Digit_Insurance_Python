"""
3. Password Strength Evaluator 
Problem Statement 
Given a password string: 
● Must contain at least 1 digit 
● Must contain at least 1 uppercase 
● Length ≥ 8 
Print STRONG or WEAK.
Input: 
password 
Output: 
STRONG 
Sample Input: 
Pass1234 
Sample Output: 
STRONG 
Hint: 
Loop through characters and count conditions manually.
"""

password = input("Enter your password: ")
if len(password)<8 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
    print("WEAK")
else:
    print("STRONG")
