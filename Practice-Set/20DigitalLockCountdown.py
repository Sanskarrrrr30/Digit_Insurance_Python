"""
20. Digital Lock Countdown 
Problem Statement 
Given a number, repeatedly subtract sum of its digits until result is a single digit. 
Input 
number 
Output 
final_digit 
Sample Input 
987 
Sample Output 
6 
Hint: 
Nested loops: digit sum inside reduction loop.
"""

number = int(input())

while number >= 10:
    digit_sum = 0
    temp = number
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    number -= digit_sum

print(number)