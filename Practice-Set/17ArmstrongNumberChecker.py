"""
17. Armstrong Number Checker 
Problem Statement 
Check if a number equals sum of cubes of its digits. 
Input 
number 
 
Output 
YES / NO 
 
Sample Input 
153 
 
Sample Output 
YES 
 
Hint: 
Extract digits using modulo and division. 
"""

number = int(input("Enter a number: "))
original_number = number
armstrong_sum = 0
while number > 0:
    digit = number % 10
    armstrong_sum += digit ** 3
    number //= 10
if armstrong_sum == original_number:
    print("YES")
else:    print("NO")

