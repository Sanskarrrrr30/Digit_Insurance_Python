"""
19. Number Mirror Validator 
Problem Statement 
Reverse a number and check if original equals reversed. 
Input 
number 
Output 
PALINDROME / NOT PALINDROME 
Sample Input 
1221 
Sample Output 
PALINDROME 
Hint: 
Build reverse using arithmetic.
"""

number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
if original_number == reversed_number:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
    